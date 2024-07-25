import json
import re

def is_english(text):
    """Check if the text contains only English letters."""
    return all(re.match(r'[a-zA-Z]', char) for char in text)

def filter_english_only(data):
    """Recursively filter the dictionary for keys with English-only values and remove empty objects."""
    if isinstance(data, dict):
        filtered_dict = {k: filter_english_only(v) for k, v in data.items() if isinstance(v, (dict, list)) or (isinstance(v, str) and is_english(v))}
        # Remove empty dictionaries
        return {k: v for k, v in filtered_dict.items() if v}
    elif isinstance(data, list):
        filtered_list = [filter_english_only(item) for item in data]
        # Remove empty lists
        return [item for item in filtered_list if item]
    return data

def main(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    filtered_data = filter_english_only(data)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    input_file = '../monkeytilt/frontend/real_money/app/messages/ru.json'
    output_file = 'english_only_output.json'
    main(input_file, output_file)
