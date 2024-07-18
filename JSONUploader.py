import os
from pathlib import Path
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

# Directory containing the JSON files
directory_path = "./messages/"

# URL of the upload endpoint
upload_url = "https://sse.monkeytilt.codes/cdn/file-upload/upload"

# Read the directory
try:
    files = os.listdir(directory_path)
except Exception as e:
    print(f"Unable to scan directory: {e}")
else:
    # Filter and process only JSON files
    json_files = [file for file in files if file.lower().endswith('.json')]
    file=json_files[1]
    # for file in json_files:
    file_path = Path(directory_path) / file
    with open(file_path, 'rb') as f:
            form_data = MultipartEncoder(
                fields={'file': (file, f, 'application/json')}
            )

            response = requests.post(
                upload_url,
                data=form_data,
                headers={'Content-Type': form_data.content_type}
            )

            if response.status_code == 200:
                try:
                    response_data = response.json()
                    print(f"Success: {response_data}")
                except requests.exceptions.JSONDecodeError:
                    print(f"Success: {response.text}")
            else:
                print(f"Error uploading file {file}: {response.status_code} - {response.text}")
