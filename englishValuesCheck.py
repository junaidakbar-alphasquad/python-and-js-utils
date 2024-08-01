import json
import re

def contains_russian(text):
    """Check if the text contains any Russian (Cyrillic) characters."""
    return re.search(r'[А-Яа-я]', text) is not None

def filter_non_russian(data):
    """Recursively filter the dictionary for keys with values that do not contain Russian characters and remove empty objects."""
    if isinstance(data, dict):
        filtered_dict = {k: filter_non_russian(v) for k, v in data.items() if isinstance(v, (dict, list)) or (isinstance(v, str) and not contains_russian(v))}
        # Remove empty dictionaries
        return {k: v for k, v in filtered_dict.items() if v}
    elif isinstance(data, list):
        filtered_list = [filter_non_russian(item) for item in data]
        # Remove empty lists
        return [item for item in filtered_list if item]
    return data

def main(input_file, output_file):
    with open(input_file, 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    filtered_data = filter_non_russian(data)
    
    with open(output_file, 'w', encoding='utf-8') as f:
        json.dump(filtered_data, f, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    input_file = '../monkeytilt/frontend/real_money/app/messages/ru.json'
    output_file = 'non_russian_output.json'
    main(input_file, output_file)
