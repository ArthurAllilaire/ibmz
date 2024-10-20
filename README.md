LSOA Area Ranking Project
This project calculates and ranks different Lower Layer Super Output Areas (LSOAs) based on various factors such as rent, commute times, green spaces, schools, and safety. It allows users to assign weights to these factors and obtain a ranking based on the final weighted score for each LSOA.

Features
Weighted Ranking: Customize the weightings of different factors to compute a final score for each LSOA.
Data Normalization: Automatically normalizes key metrics (e.g., rent per square meter) to a 0-1 scale.
Data Merging: Merges multiple data sources (e.g., commute, rent, schools) for each LSOA.
Postcode and Language Filtering: Support for filtering data by frequent postcodes and language demographics.
Prerequisites
Ensure you have the following installed:

Python 3.x
Pandas (pip install pandas)
Project Structure
bash
Copy code
.
├── languages/
│   └── langcensus.csv        # Language census data
├── data/
│   └── lsoa_stats.csv        # LSOA statistics data
├── lsoa_lat_long.py          # Contains functions for data handling and normalization
├── README.md                 # Project documentation
└── main.py                   # Main script to run the ranking process
Installation
Clone the repository:

bash
Copy code
git clone https://github.com/your-repo/lsoa-ranking-project.git
cd lsoa-ranking-project
Install the required dependencies:

bash
Copy code
pip install -r requirements.txt
Place your data files in the appropriate directories:

langcensus.csv should be in the languages/ folder.
lsoa_stats.csv should be in the data/ folder.
Usage
Calculating LSOA Rankings
Define the weightings in the AreaWeightings dataclass:

python
Copy code
from lsoa_lat_long import AreaWeightings

weights = AreaWeightings(
    commute_weighting=0.1,
    rent_per_m2=0.3,
    culture_weight=0.2,
    green_space=0.15,
    crime=0.1,
    schools=0.15
)
Use the get_ranking_from_weights function to calculate the ranking:

python
Copy code
from lsoa_lat_long import get_ranking_from_weights

df_ranked = get_ranking_from_weights(freq_post_code="E01000405", language="English", weights=weights)
print(df_ranked)
Save the output:

python
Copy code
df_ranked.to_csv('ranked_lsoa.csv', index=False)
Running the Project
Run the main script to generate the ranking:
bash
Copy code
python main.py
Example Output
The output will be a CSV file (ranked_lsoa.csv) containing LSOAs sorted by their weighted final score:

Copy code
lsoa,final_score
E01000406,0.85
E01000405,0.78
E01000407,0.73
Customization
You can modify the weights in AreaWeightings to adjust the importance of each factor in the final ranking. Adjust the weights based on your criteria (e.g., higher weight for rent or green space).

File Path Configuration
To access the langcensus.csv file correctly, the file path is constructed dynamically using os:

python
Copy code
import os

# Construct the file path for the language census data
working_dir = os.getcwd()
file_path = os.path.join(working_dir, 'languages', 'langcensus.csv')
License
This project is licensed under the MIT License.

This README.md file provides a concise overview of the project, installation steps, usage examples, and customization options. You can further expand or adjust the details based on specific project needs.
