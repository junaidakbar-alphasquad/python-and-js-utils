import os
import json
import re

# Utility functions
def is_object(value):
    return isinstance(value, dict)

def sort_keys(data):
    if is_object(data):
        sorted_data = {}
        keys = sorted(data.keys(), key=lambda k: (not isinstance(data[k], str), k.lower()))
        for key in keys:
            sorted_data[key] = sort_keys(data[key]) if is_object(data[key]) else data[key]
        return sorted_data
    elif isinstance(data, list):
        return [sort_keys(item) for item in data]
    else:
        return data

# Function to read JSON file
def read_json_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8-sig") as file:
            return json.load(file)
    except Exception as err:
        print(f"Error reading or parsing file at {file_path}: {err}")
        exit(1)

# Function to inject missing keys
def update_keys_values(source, target):
    for key, value in source.items():
        if isinstance(value, dict):
            target[key] = update_keys_values(value, target.get(key, {}))
        else:
            target[key] = value
    return target
def inject_missing_keys(source, target):
    for key, value in source.items():
        if isinstance(value, dict):
            # Recursively inject missing keys for nested dictionaries
            if key in target and isinstance(target[key], dict):
                target[key] = inject_missing_keys(value, target[key])
            else:
                target[key] = inject_missing_keys(value, {})
        else:
            if key not in target:
                target[key] = value
    return target
def delete_non_matching_keys(source, target):
    # Create a list of keys to delete from the target
    keys_to_delete = [key for key in target if key not in source]

    # Delete the keys from the target
    for key in keys_to_delete:
        del target[key]

    for key, value in source.items():
        if isinstance(value, dict):
            if key in target and isinstance(target[key], dict):
                # Recursively delete non-matching keys for nested dictionaries
                target[key] = delete_non_matching_keys(value, target[key])
            else:
                # If the key is missing or not a dictionary in target, create an empty dictionary
                target[key] = delete_non_matching_keys(value, {})
                
    return target
# Function to replace <Link> tags with <a> tags and add target="_blank"
def replace_link_tags(value):
    link_pattern = re.compile(r'<Link([^>]*)>(.*?)<\/Link>', re.IGNORECASE)
    a_pattern = re.compile(r'<a(?![^>]*\btarget\s*=\s*["\'][^"\']*["\'])([^>]*)>', re.IGNORECASE)
    
    def replacement(match):
        p1, p2 = match.groups()
        if 'target="' not in p1 and "target='" not in p1:
            p1 += ' target="_blank"'
        return f"<a{p1}>{p2}</a>"
    
    value = re.sub(link_pattern, replacement, value)
    value = re.sub(a_pattern, r'<a\1 target="_blank">', value)
    return value

def update_json(data):
    if isinstance(data, str):
        return replace_link_tags(data)
    elif isinstance(data, list):
        return [update_json(item) for item in data]
    elif isinstance(data, dict):
        return {key: update_json(value) for key, value in data.items()}
    return data
base_dir = "../monkeytilt/frontend/real_money/app/messages"

source_dir = "./newKeys"

filenames1 = [
    "en-ca.json",
#    'newKeys_ara.json', 
#    'newKeys_fre-CA.json',
#    'newKeys_fre.json', 
#    'newKeys_hin.json',
#    'newKeys_jpn.json',
#    'newKeys_kor.json',
#    'newKeys_por-BR.json',
#    'newKeys_rus.json',
#    'newKeys_spa-M9.json',
#    'newKeys_tgl.json',
#    'newKeys_tur.json',
#    'newKeys_vie.json',
#    'newKeys_zho-CN.json'
]

filenames =['es-mx.json', 
            'ja-jp.json', 
            'vi.json', 
            'tl.json', 
            'en-ca.json', 
            'en.json', 
            'fr.json', 
            'es.json', 
            'en-in.json', 
            'zh.json', 
            'ko.json', 
            'hi-in.json', 
            'tr.json', 
            'ar.json', 
            'en-jp.json', 
            'fr-ca.json', 
            'en-nz.json', 
            'es-ar.json', 
            'ru.json', 
            'en-ie.json', 
            'pt-br.json']

# Process each target file
file_path1 = os.path.join(base_dir, 
            filenames1[0])
file1 = read_json_file(file_path1)
sorted_file1 = sort_keys(file1)
for i, file in enumerate(filenames):
    file_path2 = os.path.join(base_dir, file)
    file2 = read_json_file(file_path2)
    sorted_file2 = sort_keys(file2)    
    # Inject missing keys that are not present in file 2 and added in file 1
    sorted_file2 = inject_missing_keys(sorted_file1, sorted_file2)
    # Update already exiting key
    # sorted_file2 = update_keys_values(sorted_file1, sorted_file2)
    # Delete keys present in file2 and not in file one
    # sorted_file2 = delete_non_matching_keys(sorted_file1, sorted_file2)
    sorted_file2 = sort_keys(sorted_file2)
    
    with open(file_path2, "w", encoding="utf-8") as outfile:
        json.dump(sorted_file2, outfile, ensure_ascii=False, indent=2)
    
    print(f"Missing keys injected, Object Sorted and {file} updated.")
