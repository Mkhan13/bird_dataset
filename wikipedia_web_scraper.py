'''
Script to web scrape for images of starlings, grackles, blackbirds, and cowbirds from Wikipedia sites.
'''
import os
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

def get_full_img_url(img_url):
    '''Constructs the full URL of an image by joining a relative URL with the base URL'''
    if img_url.startswith('//'):
        return 'https:' + img_url
    elif img_url.startswith('/'):
        return 'https://upload.wikimedia.org' + img_url
    return img_url

def download_bird_images(url):
    '''Function to download bird images from a URL and save them to the specified folder'''
    response = requests.get(url) #Send an HTTP request to the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    img_tags = soup.find_all('img') #Find all image tags

    for img in img_tags:
        img_url = img.get('src') or img.get('srcset')
        alt_text = img.get('alt', '').lower()

        if img_url:
            img_url = get_full_img_url(img_url)

        for bird, folder in bird_categories.items():
            if bird in img_url.lower() or bird in alt_text:  #Check if bird type is in URL or alt text
                create_folder(folder)

                existing_images = len([name for name in os.listdir(folder)])  #Count how many images are already in the folder
                img_response = requests.get(img_url)  #Download the image

                if img_response.status_code == 200:
                    img_name = f"{existing_images + 1}.jpg"
                    img_path = os.path.join(folder, img_name)
                    with open(img_path, 'wb') as f:
                        f.write(img_response.content) #Save the image to the correct folder
                    print(f"Saved {img_name} in {folder} folder")
                break


def process_urls_from_file(file_path):
    '''Function to process each URL from a text file'''
    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file.readlines()]  #Read all lines and strip newlines
            for url in urls:
                print(f"Processing URL: {url}")
                download_bird_images(url)
    except FileNotFoundError:
        print(f"File {file_path} not found!")

if __name__ == "__main__":
    file_path = "./urls.txt"
    process_urls_from_file(file_path)
