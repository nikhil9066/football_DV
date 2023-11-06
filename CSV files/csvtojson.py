import geopandas as gpd
import pandas as pd

# Load the CSV files
goalscorers = pd.read_csv('goalscorers.csv')
results = pd.read_csv('results.csv')
shootouts = pd.read_csv('shootouts.csv')

# Assuming you have a 'location' column in your CSV files
# You can create GeoDataFrames using a fictional 'geometry' column for demonstration purposes

goalscorers_gdf = gpd.GeoDataFrame(goalscorers, geometry=gpd.points_from_xy(goalscorers.longitude, goalscorers.latitude))
results_gdf = gpd.GeoDataFrame(results, geometry=gpd.points_from_xy(results.longitude, results.latitude))
shootouts_gdf = gpd.GeoDataFrame(shootouts, geometry=gpd.points_from_xy(shootouts.longitude, shootouts.latitude))

# Convert to GeoJSON and save
goalscorers_gdf.to_file('goalscorers.geojson', driver='GeoJSON')
results_gdf.to_file('results.geojson', driver='GeoJSON')
shootouts_gdf.to_file('shootouts.geojson', driver='GeoJSON')