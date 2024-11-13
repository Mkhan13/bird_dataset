'''
Script to web scrape for images of starlings, grackles, blackbirds, and cowbirds from Cornells eBird site
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
    '''Create a folder if it doesn't exist'''
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

async def download_image(session, img_url, folder, existing_images):
    '''Download an image from a URL and save it to a specified folder'''
    try:
        async with session.get(img_url) as response:
            if response.status == 200:
                img_name = f"{existing_images + 1}.jpg"
                img_path = os.path.join(folder, img_name)
                with open(img_path, 'wb') as f:
                    f.write(await response.read())
                print(f"Saved {img_name} in {folder} folder")
            else:
                print(f"Failed to download {img_url}: HTTP {response.status}")
    except Exception as e:
        print(f"Error downloading image {img_url}: {e}")

async def download_bird_images(url):
    '''Navigate to a webpage and download images of specific bird categories'''
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        try:
            await page.goto(url, wait_until="networkidle")
            img_elements = await page.query_selector_all("img") #Get all <img> tags
            async with aiohttp.ClientSession() as session:
                for bird, folder in bird_categories.items():
                    create_folder(folder)
                    existing_images = len([name for name in os.listdir(folder)]) #Count how many images are already in the folder
                    for img in img_elements:
                        try:
                            src = await img.get_attribute('src')
                            if src and 'cdn.download.ams.birds.cornell.edu' in src: #Check for specific domain in the src
                                full_img_url = urljoin(url, src)
                                await download_image(session, full_img_url, folder, existing_images)
                                existing_images += 1
                                await asyncio.sleep(1)
                        except Exception as e:
                            print(f"Error processing image: {e}")
        
        except Exception as e:
            print(f"Error accessing {url}: {e}")
        finally:
            await browser.close()

async def process_urls_from_file(file_path):
    '''Process each URL from a text file'''
    try:
        with open(file_path, 'r') as file:
            urls = [line.strip() for line in file.readlines()]
            for url in urls:
                print(f"Processing URL: {url}")
                await download_bird_images(url)
    except FileNotFoundError:
        print(f"File {file_path} not found!")

if __name__ == "__main__":
    file_path = "./urls.txt"
    asyncio.run(process_urls_from_file(file_path))
