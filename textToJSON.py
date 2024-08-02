import json

# Read the raw text from the input file
input_file_path = './Untitled-1.txt'
output_file_path = 'output_jsonfile.json'

with open(input_file_path, 'r', encoding='utf-8') as file:
    raw_text = file.read()

# Split the raw text by double line breaks to separate blocks
blocks = raw_text.strip().split('\n\n')

# Initialize an empty dictionary to store the JSON structure
json_data = {}

# Process each block
for block in blocks:
    lines = block.strip().split('\n')
    if len(lines) >= 3:
        url = lines[1]
        title = lines[2]
        description = lines[3]
        key = url.split('/')[-1] or "home"  # Extract the last segment of the URL
        
        # Add to the dictionary
        json_data[key] = {
            "title": title,
            "description": description
        }

# Convert the dictionary to a JSON string
json_output = json.dumps(json_data, indent=4, ensure_ascii=False)

# Write the JSON output to the output file
with open(output_file_path, 'w', encoding='utf-8') as json_file:
    json_file.write(json_output)

print(f'JSON output has been written to {output_file_path}')
