# import json

# # Open the original JSON file for reading
# with open("work.json", "r") as json_file:
#     # Load the entire JSON data
#     match_data = json.load(json_file)

# # Calculate the length of the data and divide it into three roughly equal parts
# total_length = len(match_data)
# part_size = total_length // 3

# # Split the data into three parts
# part1 = match_data[:part_size]
# part2 = match_data[part_size:2*part_size]
# part3 = match_data[2*part_size:]

# # Save each part to a different file
# with open("part1.json", "w") as part1_file:
#     json.dump(part1, part1_file, indent=4)

# with open("part2.json", "w") as part2_file:
#     json.dump(part2, part2_file, indent=4)

# with open("part3.json", "w") as part3_file:
#     json.dump(part3, part3_file, indent=4)

# print("JSON data divided into three parts and saved in different files: part1.json, part2.json, part3.json.")

# import json
# from geopy.geocoders import Photon

# # Create a geocoder object
# geolocator = Photon(user_agent="myGeocoder")

# # Function to add latitude and longitude to a match
# def add_lat_long_to_match(match):
#     location = geolocator.geocode(f"{match['city']}, {match['country']}")

#     if location:
#         match['city_latitude'] = location.latitude
#         match['city_longitude'] = location.longitude

# # Load the JSON data from "work.json"
# with open("part3.json", "r") as json_file:
#     match_data = json.load(json_file)

# # Process each match in the data
# for match in match_data:
#     add_lat_long_to_match(match)

# # Serialize the updated data to JSON
# json_data = json.dumps(match_data, indent=4)

# # Write the updated data back to "output.json"
# with open("output.json", "w") as output_file:
#     output_file.write(json_data)

# print("Latitude and longitude added to the JSON data and saved in 'output.json'.")
import json

# Open the original JSON file for reading
with open("work.json", "r") as json_file:
    # Load the entire JSON data
    match_data = json.load(json_file)

# Calculate the length of the data and divide it into 20 roughly equal parts
total_length = len(match_data)
part_size = total_length // 20

# Create 20 parts and save them to different files
for i in range(40):
    start_index = i * part_size
    end_index = (i + 1) * part_size
    part_data = match_data[start_index:end_index]
    
    # Save each part to a different file
    part_filename = f"part{i+1}.json"
    with open(part_filename, "w") as part_file:
        json.dump(part_data, part_file, indent=4)

print("JSON data divided into 20 parts and saved in different files: part1.json, part2.json, ..., part20.json.")
