'''
Script to web scrape for images of starlings, grackles, blackbirds, and cowbirds from On The Wing Photography
'''
import os
import asyncio
from playwright.async_api import async_playwright
import aiohttp
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

def get_full_img_url(img_url, base_url):
    '''Constructs the full URL of an image by joining a relative URL with the base URL'''
    return urljoin(base_url, img_url)

async def download_image(session, img_url, folder, index):
    '''Function to download bird images from a URL and save them to the specified folder'''
    try:
        async with session.get(img_url) as response:  #Make a request to download the image
            if response.status == 200:
                img_name = f"{index}.jpg" #Number the images in order
                img_path = os.path.join(folder, img_name)
                with open(img_path, 'wb') as f:
                    f.write(await response.read())
                print(f"Saved {img_name} in {folder} folder")
            else:
                print(f"Failed to download {img_url}: HTTP {response.status}")
    except Exception as e:
        print(f"Error downloading image {img_url}: {e}")

async def download_bird_images(url):
    '''Function to navigate to a webpage and download images of specific bird categories'''
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True) #Start browser in headless mode
        page = await browser.new_page()
        
        try:
            await page.goto(url, wait_until="networkidle") #Wait until network activity is idle
            img_elements = await page.query_selector_all("img") #Get all <img> elements on page
            
            async with aiohttp.ClientSession() as session:
                for bird, folder in bird_categories.items():
                    create_folder(folder) #Ensure folder for each bird category exists
                    index = 1
                    for img in img_elements:
                        try:
                            #Get the image source (src) and alternative text (alt)
                            src = await img.get_attribute('src')
                            alt = await img.get_attribute('alt')
                            #Check if the bird name appears in the image source or alt attribute
                            if src and (bird in src.lower() or (alt and bird in alt.lower())):
                                full_img_url = get_full_img_url(src, url)
                                await download_image(session, full_img_url, folder, index)
                                index += 1
                                await asyncio.sleep(1)  #Add a delay between downloads
                        except Exception as e:
                            print(f"Error processing image: {e}")
        
        except Exception as e:
            print(f"Error accessing {url}: {e}")
        finally:
            await browser.close() #Ensure browser is closed

async def process_urls_from_file(file_path):
    '''Function to process each URL from a text file'''
    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file.readlines()] #Read all URLs from file
            for url in urls:
                print(f"Processing URL: {url}")
                await download_bird_images(url) #Process each URL to download images
    except FileNotFoundError:
        print(f"File {file_path} not found!")

if __name__ == "__main__":
    file_path = "./urls.txt"
    asyncio.run(process_urls_from_file(file_path)) #Run the main async function