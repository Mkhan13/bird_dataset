'''
Script to web scrape for images of starlings, grackles, blackbirds, and cowbirds from Wikipedia sites
'''
import os
import sys
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

bird_categories = {
    'starling': 'starling',
    'grackle': 'grackle',
    'blackbird': 'blackbird',
    'cowbird': 'cowbird'
}

def create_folder(folder_name):
    '''Function to create a folder if it doesn't exist'''
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)


def download_bird_images(url):
    '''Function to download bird images from a URL and categorize them'''
    
    response = requests.get(url) # Send an HTTP request to the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img') # Find all image tags

    for img in img_tags: # Process each image
        img_url = img.get('src')
        alt_text = img.get('alt', '').lower()
        
        for bird, folder in bird_categories.items(): 
            if bird in img_url.lower() or bird in alt_text: # Determine the bird category based on the alt text or src URL

                create_folder(folder) # Create folder if it doesn't exist
                
                existing_images = len([name for name in os.listdir(folder) if name.startswith(bird)]) # Count how many images are already in the folder
                
                img_url = urljoin(url, img_url) # Ensure the image URL is absolute
                
                img_response = requests.get(img_url) # Fetch the image
                if img_response.status_code == 200:
                    img_name = f"{bird}_{existing_images + 1}.jpg" # Save the image in the correct folder
                    img_path = os.path.join(folder, img_name)
                    with open(img_path, 'wb') as f:
                        f.write(img_response.content)
                    print(f"Saved {img_name} in {folder} folder")
                break


if __name__ == "__main__":
    if len(sys.argv) < 2: # Check if URLs are provided via command line arguments
        print("Usage: python script.py <url1> <url2> ... <urlN>")
        sys.exit(1)
    
    for url in sys.argv[1:]: # Iterate over each URL provided
        print(f"Processing URL: {url}")
        download_bird_images(url)
