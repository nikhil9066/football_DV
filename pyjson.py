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

# # List of JSON files to process
# file_names = ["part19.json", "part20.json"]

# # Process each JSON file
# for file_name in file_names:
#     with open(file_name, "r") as json_file:
#         print(f"Processing {file_name}")
#         match_data = json.load(json_file)

#     # Process each match in the data
#     for match in match_data:
#         add_lat_long_to_match(match)

#     # Serialize the updated data to JSON
#     json_data = json.dumps(match_data, indent=4)

#     # Write the updated data back to a new JSON file
#     output_file_name = f"updated_{file_name}"
#     with open(output_file_name, "w") as output_file:
#         output_file.write(json_data)

#     print(f"Latitude and longitude added to the JSON data and saved in '{output_file_name}'.")


# -----------------------------------------------------------import json

# # List of updated JSON files
# updated_file_names = ["combined_data.json","combined_data_1.json"]

# # List to store the combined data
# combined_data = []

# # Read and combine data from each updated file
# for updated_file_name in updated_file_names:
#     with open(updated_file_name, "r") as updated_file:
#         updated_data = json.load(updated_file)
#         combined_data.extend(updated_data)

# # Serialize the combined data to JSON
# combined_json_data = json.dumps(combined_data, indent=4)

# # Write the combined data to a new JSON file
# combined_output_file = "combined_data_final.json"
# with open(combined_output_file, "w") as output_file:
#     output_file.write(combined_json_data)

# print(f"Combined data saved in '{combined_output_file}'.")

# -----------------------------------------------------------import json

# # Update the list to include files from updated_part6 to updated_part20
# updated_file_names = [f"updated_part{i}.json" for i in range(6, 21)]

# # List to store the combined data
# combined_data = []

# # Read and combine data from each updated file
# for updated_file_name in updated_file_names:
#     try:
#         with open(updated_file_name, "r") as updated_file:
#             updated_data = json.load(updated_file)
#             if isinstance(updated_data, list):
#                 combined_data.extend(updated_data)
#             else:
#                 print(f"Data in {updated_file_name} is not a list.")
#     except Exception as e:
#         print(f"Error reading {updated_file_name}: {e}")

# # Serialize the combined data to JSON
# combined_json_data = json.dumps(combined_data, indent=4)

# # Write the combined data to a new JSON file
# combined_output_file = "combined_data.json"
# with open(combined_output_file, "w") as output_file:
#     output_file.write(combined_json_data)

# print(f"Combined data saved in '{combined_output_file}'.")

import json

# updated_file_names = ["combined_data.json","combined_data_1.json"]

# Specify the JSON file you want to find the length of
json_file_path = "combined_data_final.json"

# Read the JSON file
with open(json_file_path, "r") as json_file:
    json_data = json.load(json_file)

# Check if the content is a list (array)
if isinstance(json_data, list):
    # Print the length of the list
    print(f"Length of the JSON file '{json_file_path}': {len(json_data)}")
else:
    print(f"The content of '{json_file_path}' is not a list (array).")

