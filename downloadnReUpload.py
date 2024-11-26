import os
import requests
from pathlib import Path
from requests_toolbelt.multipart.encoder import MultipartEncoder
import json

# The array of countries
countries = [
{
	"name":"cabo verde","code":"CV"
},
{
	"name":"Slovenia","code":"SI"
}
,{
	"name":"c%C3%B4te-d'ivoire","code":"CI"
}
]

# Directory where images will be saved
directory_path = './webp_images1'
os.makedirs(directory_path, exist_ok=True)

# URL pattern for downloading images
base_url = "https://monkeytilt-games.imgix.net/{name}"  # Replace 'link' with the correct base URL

# URL of the upload endpoint
upload_url = "https://sse.monkeytilt.codes/cdn/file-upload/upload"  # Replace with your actual CDN upload URL

# Function to download and save the image
def download_image(country_name,code):
    # Generate the URL for the image based on the country name
    image_name = country_name + ".webp"
    exportName = code + ".webp"
    image_url = base_url.format(name=image_name)
    
    try:
        # Download the image
        response = requests.get(image_url)
        response.raise_for_status()  # Raise an error if the request fails
        
        # Save the image locally
        image_path = Path(directory_path) / exportName
        with open(image_path, 'wb') as file:
            file.write(response.content)
        
        print(f"Downloaded image: {exportName}")
        return image_path

    except requests.exceptions.RequestException as e:
        print(f"Failed to download image for {country_name}: {e}")
        return None

# Function to upload the image to the CDN
def upload_image(image_path, new_name):
    with open(image_path, 'rb') as f:
        form_data = MultipartEncoder(
            fields={'file': (new_name, f, 'image/webp')}
        )

        try:
            # Send the image to the CDN
            response = requests.post(
                upload_url,
                data=form_data,
                headers={'Content-Type': form_data.content_type}
            )

            if response.status_code == 200:
                response_data = response.json()
                print(f"Success: {response_data}")
            else:
                print(f"Error uploading file {new_name}: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Failed to upload {new_name}: {e}")

# Loop through the countries array
for country in countries:
    country_name = country['name']
    country_code = country['code']  # You can use this as the new image name or any other logic

    # Download the image based on the country name
    image_path = download_image(country_name,country_code)
    
    # if image_path:
        # Upload the image with the new name (using country code for example)
        # upload_image(image_path, f"{country_code}.webp")
        # Optionally, you can delete the local file after upload
        # os.remove(image_path)
