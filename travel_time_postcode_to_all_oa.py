import requests
import csv

# Define OA List here or import it from somewhere
# List all OA's names and latitude and longitudes 
# so that we can use this to cross check with Time Travel API

OA_List = [
    {
    "id": "oa_1",
    "coords": {
        "lat": 51.50,
        "lng": -0.30,
    }
    },
    {
        "id": "oa_2",
    "coords": {
        "lat": 51.48,
        "lng": 50.0,
    }
    }
        ]

# This uses postcodes.io API to get longtitude and latitude of a postcode
# To use to search in Travel Time API

Api_Key = "cf6f440b8c1a8438f4ca619e015a2d8b"
Application_Id = "da4535ae"
Request_Type = "POST"
Host = "api.traveltimeapp.com"
Endpoint = "/v4/time-filter/fast"
headers = {
    "X-Application-Id": Application_Id,
    "X-Api-Key": Api_Key
}

url = f"https://{Host}{Endpoint}"

# get_search_postcode prompts user input to input their work postcode

def get_search_postcode() :
    search_postcode = input("Enter search postcode: ")
    return search_postcode

# get_lat_and_lng_of_postcode uses the user's search_postcode to get their latitude
# and longitude using another API (postcodes.io)
# this function also includes a guard - return None when postcode is invalid / unfindable

def get_lat_and_lng_of_postcode(search_postcode):

    # Searching for the postcode using the API
    postcode_url = f"https://api.postcodes.io/postcodes/{search_postcode}"
    postcode_response = requests.get(postcode_url)
  
    if postcode_response.status_code == 200: # Success code for postcodes.io API
        postcode_data = postcode_response.json()  # Parse JSON response
        
        # Check if 'result' key exists and is not None
        if 'result' in postcode_data and postcode_data['result'] is not None:
            latitude = postcode_data['result']['latitude']
            longitude = postcode_data['result']['longitude']

            return latitude, longitude

        else:
            print(f"No result found for postcode: {search_postcode}")
            return None  # Return None if there's no result
    else:
        print(f"Error: {postcode_response.status_code} - {postcode_response.text}")
        return None  # Return None for any other error

# find_oa_from_postcode_by_transport uses Time Travel API to return list of OA's
# that are within [minutes] by [transport_method] from [search_postcode]

# transport methods: driving, public_transport, cycling, walking, motorcycling, scooter
# I think we can add walking+public_transport '+' to indicate walking then public transport

def find_oa_from_postcode_by_transport(OA_List, search_postcode, transport_method, minutes) :
    try_get_lat_and_lng = get_lat_and_lng_of_postcode(search_postcode)
    
    if try_get_lat_and_lng is None:
        print("Could not retrieve coordinates.")
        return None
        
    else:
        latitude, longitude = try_get_lat_and_lng
    
    request_body = {
        "arrival_searches": {
            "one_to_many": [
                {
                    "id": "Example Search",
                    "departure_location_id": "Origin",
                    "arrival_location_ids": [oa["id"] for oa in OA_List],
                    "transportation": {
                        "type": transport_method
                    },
                    "travel_time": (minutes * 60),
                    "arrival_time_period": "weekday_morning",
                    "properties": [
                        "travel_time",
                        "distance"
                    ]
                }
            ]
        },
        "locations": [
            {
                "id": "Origin",
                "coords": {
                    "lat": latitude,
                    "lng": longitude
                }
            }
        ] + OA_List
    }
    oa_response = requests.post(url, headers=headers, json=request_body)
    oa_data = oa_response.json() 
    # this takes out the part that we can use
    
    return oa_data

def given_data_return_csv(oa_data):
    
    reachable_oa = oa_data['results'][0]['locations']
    unreachable_oa = oa_data['results'][0]['unreachable']
    
    with open('oa_travel_times.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        field = ["OA", "walking_time", "score"]
        writer.writerow(field)
        
        for oa in reachable_oa:
            oa_id = oa['id']  # Access the 'id' of the OA
            oa_travel_time = oa['properties']['travel_time']  # Access travel time
            oa_score = 1 / (travel_time_limit * 60 - oa_travel_time)  # Calculate score
    
        # Write the data to CSV
            writer.writerow([f"{oa_id} {oa_travel_time} {oa_score}"])
    
        for uoa in unreachable_oa:
            uoa_id = uoa
            uoa_score = 0
            writer.writerow([f"{uoa} NULL {uoa_score}"])

        return file

# Sample usage
search_postcode = get_search_postcode() 
#     - to get postcode from user
oa_data = find_oa_from_postcode_by_transport(OA_List, search_postcode, "walking", 10)
#     - to get full results of OA's reachable and unreachable by walking 10 mins
given_data_return_csv(oa_data)
#     this returns a csv file with all OA's:
#     reachable OA's first with travel_time and score 
#     unreachable OA's with NULL travel_time and 0 score
#     Scoring calculation is yet to be decided
