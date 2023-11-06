# import json

# # Read and parse the GeoJSON file
# with open('world-countries.geojson', 'r') as geojson_file:
#     geojson_data = json.load(geojson_file)

# # Read and parse the result JSON file
# with open('data/results.json', 'r') as result_file:
#     result_data = json.load(result_file)

# # Iterate through result_data and merge it into geojson_data
# for match in result_data:
#     match_country = match['country']
#     for feature in geojson_data['features']:
#         feature_properties = feature['properties']
#         if 'country' in feature_properties and feature_properties['country'] == match_country:
#             feature_properties['match_info'] = {
#                 'date': match['date'],
#                 'home_team': match['home_team'],
#                 'away_team': match['away_team'],
#                 'city': match['city'],
#                 'country': match['country']
#             }

# # Write the merged GeoJSON data back to the file
# with open('merged_word.geojson', 'w') as merged_geojson_file:
#     json.dump(geojson_data, merged_geojson_file)
import json
from geopy.geocoders import Photon

# Define the JSON data
data = {
   "date": "1916-06-25",
   "home_team": "Norway",
   "away_team": "Denmark",
   "home_score": 0,
   "away_score": 2,
   "tournament": "Friendly",
   "city": "Kristiania",
   "country": "Norway",
   "neutral": False
}

# Create a geocoder object
geolocator = Photon(user_agent="myGeocoder")

# Use the geocoder to obtain the location information
location = geolocator.geocode(f"{data['city']}, {data['country']}")

if location:
    # Extract latitude and longitude
    data['city_latitude'] = location.latitude
    data['city_longitude'] = location.longitude

    # Serialize the data to JSON
    json_data = json.dumps(data, indent=4)

    # Write the updated data back to the file
    with open("work.json", "w") as json_file:
        json_file.write(json_data)
    print("Latitude and longitude added to the JSON data.")
else:
    print("Location not found for the given city and country.")
