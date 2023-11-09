# import json
# from geopy.geocoders import Photon
# from geopy.exc import GeocoderTimedOut

# # Create a geocoder object with an increased timeout
# geolocator = Photon(user_agent="myGeocoder", timeout=10)

# # Function to add latitude and longitude to a match
# def add_lat_long_to_match(match, max_retries=3):
#     retries = 0
#     while retries < max_retries:
#         try:
#             location = geolocator.geocode(f"{match['city']}, {match['country']}")
#             if location:
#                 match['city_latitude'] = location.latitude
#                 match['city_longitude'] = location.longitude
#             return
#         except GeocoderTimedOut:
#             retries += 1
#     print(f"Geocoding for match failed after {max_retries} retries: {match}")

# # Open the JSON file for reading
# with open("part1.json", "r") as json_file:
#     match_data = json.load(json_file)

# # Process each match in the data
# for match in match_data:
#     add_lat_long_to_match(match)

# # Serialize the updated data to JSON
# json_data = json.dumps(match_data, indent=4)

# # Write the updated data back to a new JSON file
# with open("updated_data_part2.json", "w") as output_file:
#     output_file.write(json_data)

# print("Latitude and longitude added to the JSON data and saved in 'updated_data.json'.")

import json
from geopy.geocoders import Photon
from geopy.exc import GeocoderTimedOut

# Create a geocoder object with an increased timeout
geolocator = Photon(user_agent="myGeocoder", timeout=10)

# Function to add latitude and longitude to a match
def add_lat_long_to_match(match, max_retries=3):
    retries = 0
    while retries < max_retries:
        try:
            location = geolocator.geocode(f"{match['city']}, {match['country']}")
            if location:
                match['city_latitude'] = location.latitude
                match['city_longitude'] = location.longitude
            return
        except GeocoderTimedOut:
            retries += 1
    print(f"Geocoding for match failed after {max_retries} retries: {match}")

# Process multiple JSON files
for part_num in range(1, 4):  # Assuming you have files part1.json through part20.json
    input_filename = f"part{part_num}.json"
    print(input_filename)
    output_filename = f"updated_data_part{part_num}.json"
    
    # Open the JSON file for reading
    with open(input_filename, "r") as json_file:
        match_data = json.load(json_file)

    # Process each match in the data
    for match in match_data:
        add_lat_long_to_match(match)

    # Serialize the updated data to JSON
    json_data = json.dumps(match_data, indent=4)

    # Write the updated data back to a new JSON file
    with open(output_filename, "w") as output_file:
        output_file.write(json_data)

    print(f"Latitude and longitude added to {input_filename} and saved in {output_filename}.")

print("Processing all JSON files completed.")
