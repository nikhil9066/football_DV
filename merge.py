# import json
# from geopy.geocoders import Photon
# from itertools import islice

# # Define the maximum batch size (you can adjust this as needed)
# batch_size = 2000

# # Create a geocoder object
# geolocator = Photon(user_agent="myGeocoder")

# # Function to add latitude and longitude to a batch of matches
# def add_lat_long_to_batch(batch):
#     for match in batch:
#         # Use the geocoder to obtain the location information
#         location = geolocator.geocode(f"{match['city']}, {match['country']}")

#         if location:
#             # Extract latitude and longitude
#             match['city_latitude'] = location.latitude
#             match['city_longitude'] = location.longitude

# # Process the JSON file in chunks
# with open("work.json", "r") as json_file:
#     while True:
#         chunk = list(islice(json_file, batch_size))
#         if not chunk:
#             break
        
#         match_data = json.loads("".join(chunk))
#         add_lat_long_to_batch(match_data)
        
#         # Serialize and write the updated data back to a separate output file
#         json_data = json.dumps(match_data, indent=4)
#         with open("output.json", "a") as output_file:
#             output_file.write(json_data)
#             output_file.write("\n")

# print("Latitude and longitude added to the JSON data and saved in 'output.json'.")
# import geopandas as gpd

# # Load the GeoJSON file
# geojson_path = "custom.geo.json"  # Replace with the actual path
# gdf = gpd.read_file(geojson_path)

# # Count the number of features (countries)
# print(gdf)
# num_countries = len(gdf)
# print(f"The number of countries is: {num_countries}")

import pandas as pd

# Read the CSV file into a DataFrame
df = pd.read_csv('CSV files/results.csv')

# Convert the 'date' column to datetime format
df['date'] = pd.to_datetime(df['date'])

# Group by date and count the number of matches played on each date
matches_per_date = df.groupby('date').size().reset_index(name='matches_played')

# Convert the 'date' column to the desired format
matches_per_date['date'] = matches_per_date['date'].dt.strftime('%Y-%m-%d')

# Convert 'matches_played' column to integers (optional)
matches_per_date['matches_played'] = matches_per_date['matches_played'].astype(int)

# Convert the DataFrame to JSON in the desired format and save it to a file
matches_per_date.to_json('matches_per_date.json', orient='records', date_format='iso', date_unit='s', default_handler=str)

