import requests
import config

Request_Type = "POST"
Host = "api.traveltimeapp.com"
Endpoint = "/v4/time-filter/fast"
Application_Id = config.Application_Id
Api_Key = config.Api_Key
headers = {
    "X-Application-Id": Application_Id,
    "X-Api-Key": Api_Key
}

url = f"https://{Host}{Endpoint}"

request_body = {
    "arrival_searches": {
        "one_to_many": [
            {
                "id": "Example Search",
                "departure_location_id": "Origin",
                "arrival_location_ids": [
                    "Destination 1",
                    "Destination 2",
                    "Destination 3"
                ],
                "transportation": {
                    "type": "driving"
                },
                "travel_time": 10800,  # Time in seconds (3 hours)
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
                "lat": 54.238911,
                "lng": -0.397567
            }
        },
        {
            "id": "Destination 1",
            "coords": {
                "lat": 54.24424722,
                "lng": -0.407544543
            }
        },
        {
            "id": "Destination 2",
            "coords": {
                "lat": 54.35384,
                "lng": -0.434984
            }
        },
        {
            "id": "Destination 3",
            "coords": {
                "lat": 53.99283,
                "lng": -0.519234
            }
        }
    ]
}


response = requests.post(url, headers=headers, json=request_body)

if response.status_code == 200:
    print('Success:', response.json())  # Print the response data (assuming it's JSON)
else:
    print(f"Error: {response.status_code}")

