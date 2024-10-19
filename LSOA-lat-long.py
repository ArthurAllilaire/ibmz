# Main file for the LSOA lat long conversion

# Importing the required libraries
import pandas as pd

# Declaring local files to read from
lsoa_lat_long = 'lsoa_lat_long.csv'
lsoa_stats = 'lsoa_stats.csv'

def order_by_column(file_name: str, column_name: str, ascending: bool = False) -> pd.DataFrame:
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_name)

    # Check if the provided column name exists in the DataFrame
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' not found in the DataFrame")

    # Sort the DataFrame by the specified column in ascending order
    sorted_df = df.sort_values(by=column_name, ascending=ascending)

    return sorted_df


def lsoa_lat_long_tuples(file_name: str) -> list[tuple[str, float, float]]:
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
