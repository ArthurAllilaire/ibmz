import pandas as pd

# This will take in all the pd dfs.
# This will then calculate final value metric for each OA.

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
    'oa': [1, 2, 3],
    'commute_score': [0.1, 0.2, 0.3]
})

# Sample data for df2
df_rent = pd.DataFrame({
    'oa': [1, 2, 3],
    'rent_score': [0.3, 0.5, 0.7]
})

# Sample data for df3
df_culture = pd.DataFrame({
    'oa': [1, 2, 3],
    'culture_score': [0.4, 0.7, 0.9]
})

# Merge df1, df2, and df3 on the 'key' column
df_merged = df_commute.merge(df_rent, on='oa').merge(df_culture, on='oa')

# Define a function that takes relevant columns and returns some result
def value_function(row):
    assert isinstance(row['commute_score'], float), "commute_score is a float"
    assert isinstance(row['rent_score'], float), "rent_score is a float"
    assert isinstance(row['culture_score'], float), "culture_score is a float"

    return w_commute * row['commute_score'] + w_rent * row['rent_score'] + w_culture * row['culture_score']


df_merged['result'] = df_merged.apply(value_function, axis=1)

