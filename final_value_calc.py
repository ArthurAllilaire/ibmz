import pandas as pd

# This will take in all the pd dfs.
# This will then calculate final value metric for each lsoa.
from lsoa_lat_long import lsoa_stats_file, order_and_normalize_by_column, rent_col, normalise, green_space_col, safety_col, schools_col


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

# dfs

# Sample data for df1
df_commute = pd.DataFrame({
    'lsoa': [1, 2, 3],
    'commute_score': [0.1, 0.2, 0.3]
})

# Sample data for df2
df_rent = order_and_normalize_by_column(lsoa_stats_file, rent_col)
df_green = order_and_normalize_by_column(lsoa_stats_file, green_space_col)
df_schools = order_and_normalize_by_column(lsoa_stats_file, schools_col)
df_safety = order_and_normalize_by_column(lsoa_stats_file, safety_col)
df_green.to_csv('rent.csv')
# Sample data for df3
df_culture = pd.DataFrame({
    'lsoa': [1, 2, 3],
    'culture_score': [0.4, 0.7, 0.9]
})

# Merge df1, df2, and df3 on the 'key' column
df_merged = df_commute.merge(df_rent, on='lsoa').merge(df_culture, on='lsoa')

# Define a function that takes relevant columns and returns some result
def value_function(row, weights: AreaWeightings):
    total = 0
    total += weights.commute_weighting * row['commute_score'] 
    total += weights.rent_per_m2 * row[normalise(rent_col)]
    total += weights.culture_weight * row['culture_score']
    return total



def get_ranking_from_weights(freq_post_code: str, language: str, weights: AreaWeightings) -> pd.DataFrame:
    pass


df_merged['result'] = df_merged.apply(value_function, axis=1)

