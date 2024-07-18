import os
from pathlib import Path
import requests
from requests_toolbelt.multipart.encoder import MultipartEncoder

# Directory containing the images
directory_path = './webp_images'
# directory_path = './webp_images'

# URL of the upload endpoint
upload_url = "https://sse.monkeytilt.codes/cdn/file-upload/upload"  # Make sure to include the http:// or https://

# Read the directory
try:
    files = os.listdir(directory_path)
except Exception as e:
    print(f"Unable to scan directory: {e}")
else:
    # Filter and process only webp files
    image_files = [file for file in files if file.lower().endswith('.webp')]

    for file in image_files:
        file_path = Path(directory_path) / file
        with open(file_path, 'rb') as f:
            form_data = MultipartEncoder(
                fields={'file': (file, f, 'image/webp')}
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
