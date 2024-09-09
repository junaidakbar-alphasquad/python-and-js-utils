import re
import json

def parse_document_to_html(text):
    terms_and_conditions = {}
    lines = text.splitlines()
    
    for line in lines:
        line = line.strip()
        if line:
            # Match headings like 1. General or 2. My Account
            match_heading = re.match(r'^(\d+)\.\s+(.*)', line)
            if match_heading:
                section_number = match_heading.group(1)
                section_title = match_heading.group(2)
                terms_and_conditions[f'{section_number}'] = {
                    "title": section_title,
                    "description": ""
                }
                current_section = section_number
            
            # Match sub-items like 1.1, 2.1, etc.
            match_sub_item = re.match(r'^(\d+\.\d+)\.\s+(.*)', line)
            if match_sub_item:
                sub_item_number = match_sub_item.group(1)
                sub_item_content = match_sub_item.group(2)
                terms_and_conditions[current_section]["description"] += f"<p class='text-sm font-avenirNext font-normal !text-zinc-400'> {sub_item_number}. {sub_item_content}</p><br/><br/>"

    return terms_and_conditions

def convert_to_final_structure(parsed_data):
    final_output = {}
    
    for key, value in parsed_data.items():
        title_key = f"{value['title']}"
        description_key = f"<div class='w-full pb-6 @5xl/main:pb-10 max-w-[1013px] '>{value['description']}</div>"
        
        final_output["termsAndConditions"] = title_key
        final_output["termsAndConditionsDescription"] = description_key
    
    return final_output
input_file_path = './text.txt'
output_file_path = 'output_jsonfile.json'

with open(input_file_path, 'r', encoding='utf-8') as file:
    raw_text = file.read()

parsed_doc = parse_document_to_html(raw_text)
# final_output = convert_to_final_structure(parsed_doc)
# Convert the dictionary to a JSON string
json_output = json.dumps(parsed_doc, indent=4, ensure_ascii=False)

# Write the JSON output to the output file
with open(output_file_path, 'w', encoding='utf-8') as json_file:
    json_file.write(json_output)

print(f'JSON output has been written to {output_file_path}')
