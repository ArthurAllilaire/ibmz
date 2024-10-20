import pandas as pd

# This will take in all the pd dfs.
# This will then calculate final value metric for each lsoa.
from lsoa_lat_long import lsoa_stats_file, order_and_normalize_by_column, rent_col, normalise, green_space_col, safety_col, schools_col
from languages.lang import getlsoasbylang
from travel_time_postcode_to_all_oa import given_postcode_return_df
from dataclasses import dataclass

@dataclass
class AreaWeightings:
    commute_weighting: float
    rent_per_m2: float
    culture_weight: float
    green_space: float
    crime: float
    schools: float


MAX_WEIGHT = 1

# How are the weights calculated ? 

v_commute = 0
w_commute = v_commute / MAX_WEIGHT
v_rent = 0
w_rent = v_rent / MAX_WEIGHT
v_culture = 0
w_culture = v_culture / MAX_WEIGHT

# Sample data for df2
df_rent = order_and_normalize_by_column(lsoa_stats_file, rent_col)
df_green = order_and_normalize_by_column(lsoa_stats_file, green_space_col)
df_schools = order_and_normalize_by_column(lsoa_stats_file, schools_col)
df_safety = order_and_normalize_by_column(lsoa_stats_file, safety_col)

# Merge DataFrames on 'lsoa'
df_merged = df_rent.merge(df_green, on='lsoa') \
                      .merge(df_schools, on='lsoa') \
                      .merge(df_safety, on='lsoa')


# Define a function that takes relevant columns and returns some result
def value_function(row, weights: AreaWeightings):
    """Calculates the final score based on provided weights."""
    total = 0
    total += weights.commute_weighting * row['travel_score']
    total += weights.rent_per_m2 * row[normalise(rent_col)]
    total += weights.green_space * row[green_space_col]
    total += weights.schools * row[schools_col]
    total += weights.crime * row[safety_col]
    total += weights.culture_weight * row['lang_score']
    return total

def get_ranking_from_weights(freq_post_code: str, language: str, weights: AreaWeightings) -> pd.DataFrame:
    """Calculates the final score for each LSOA and returns a sorted DataFrame."""
    
    # Filter the DataFrame based on freq_post_code and language if needed (not implemented here)
    # You can add your filtering logic based on the freq_post_code or language
    
    # Assume df_merged is available globally
    global df_merged
    
    # Calculate final scores using the provided weights
    print("Got here!")
    df_culture = getlsoasbylang(language)
    print(freq_post_code)
    df_culture.to_csv('culture.csv', index=False)
    df_time = given_postcode_return_df(freq_post_code)
    df_time.to_csv('travel_times.csv', index=False)
    df_merged = df_merged.merge(df_culture, on='lsoa') \
                         .merge(df_time, on='lsoa')
    df_merged['final_score'] = df_merged.apply(value_function, axis=1, weights=weights)
    df_merged.to_csv('final_scores_full.csv', index=False)
    
    # Sort the DataFrame by final_score in descending order (highest scores first)
    df_sorted = df_merged.sort_values(by='final_score', ascending=False)
    return df_sorted[['lsoa', 'final_score']]


if __name__ == '__main__':
    get_ranking_from_weights('sw72bb', 'English', AreaWeightings(0.2, 0.2, 0.2, 0.2, 0.2, 0.2)).to_csv('final_scores.csv', index=False)