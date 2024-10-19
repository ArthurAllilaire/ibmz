# Main file for the LSOA lat long conversion

# Importing the required libraries
import pandas as pd

# Declaring local files to read from
lsoa_lat_long_file = 'lsoa_lat_long.csv'
lsoa_stats_file = 'lsoa_stats.csv'
rent_col = 'Rent_per_m'

import pandas as pd

def normalise(col_name: str):
    return f'normalized_{col_name}'

def order_and_normalize_by_column(file_name: str, column_name: str, ascending: bool = False) -> pd.DataFrame:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_name)

    # Check if the provided column name exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the DataFrame")

    # Normalize the column values to a range between 0 and 1
    col_min = df[column_name].min()
    col_max = df[column_name].max()
    df[normalise(column_name)] = (df[column_name] - col_min) / (col_max - col_min)

    # Sort the DataFrame by the normalized column in the specified order
    sorted_df = df[['lsoa', normalise(column_name)]].sort_values(by=normalise(column_name), ascending=ascending)

    return sorted_df



def order_by_column(file_name: str, column_name: str, ascending: bool = False) -> pd.DataFrame:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_name)

    # Check if the provided column name exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the DataFrame")

    # Sort the DataFrame by the specified column in ascending order
    sorted_df = df.sort_values(by=column_name, ascending=ascending)    

    return sorted_df


def lsoa_lat_long_dict(file_name: str = lsoa_lat_long_file) -> list[dict]:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_name)

    # Create a list of dictionaries in the desired format
    lsoa_lat_long_list = [
        {
            "id": lsoa,  # Use the LSOA value as the 'id'
            "coords": {
                "lat": avg_lat,  # Latitude
                "lng": avg_long  # Longitude
            }
        }
        for lsoa, avg_lat, avg_long in df.itertuples(index=False, name=None)
    ]

    return lsoa_lat_long_list

def lsoa_lat_long_tuples(file_name: str = lsoa_lat_long_file) -> list[tuple[str, float, float]]:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_name)

    # Create a list of tuples (lsoa, avg_lat, avg_long)
    lsoa_lat_long = list(df.itertuples(index=False, name=None))

    return lsoa_lat_long

def lsoa_to_lat_long(file_name: str, lsoa: str) -> tuple[float, float]:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_name)

    # Filter the DataFrame for the specified LSOA
    filtered_df = df[df['lsoa'] == lsoa]

    # If the LSOA is not found, raise an error or return None
    if filtered_df.empty:
        raise ValueError(f"LSOA '{lsoa}' not found in the file")

    # Get the average latitude and longitude
    avg_lat = filtered_df['avg_lat'].values[0]
    avg_long = filtered_df['avg_long'].values[0]

    # Return the latitude and longitude as a tuple
    return avg_lat, avg_long
