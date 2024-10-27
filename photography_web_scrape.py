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
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)

def get_full_img_url(img_url, base_url):
    return urljoin(base_url, img_url)

async def download_image(session, img_url, folder, index):
    try:
        async with session.get(img_url) as response:
            if response.status == 200:
                img_name = f"{index}.jpg"
                img_path = os.path.join(folder, img_name)
                with open(img_path, 'wb') as f:
                    f.write(await response.read())
                print(f"Saved {img_name} in {folder} folder")
            else:
                print(f"Failed to download {img_url}: HTTP {response.status}")
    except Exception as e:
        print(f"Error downloading image {img_url}: {e}")

async def download_bird_images(url):
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()
        
        try:
            await page.goto(url, wait_until="networkidle")
            img_elements = await page.query_selector_all("img")
            
            async with aiohttp.ClientSession() as session:
                for bird, folder in bird_categories.items():
                    create_folder(folder)
                    index = 1
                    for img in img_elements:
                        try:
                            src = await img.get_attribute('src')
                            alt = await img.get_attribute('alt')
                            if src and (bird in src.lower() or (alt and bird in alt.lower())):
                                full_img_url = get_full_img_url(src, url)
                                await download_image(session, full_img_url, folder, index)
                                index += 1
                                await asyncio.sleep(1)  # Add a delay between downloads
                        except Exception as e:
                            print(f"Error processing image: {e}")
        
        except Exception as e:
            print(f"Error accessing {url}: {e}")
        finally:
            await browser.close()

async def process_urls_from_file(file_path):
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