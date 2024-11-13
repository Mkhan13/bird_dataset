# Bird Image Dataset
This project contains scripts to web scrape images of specific bird species (e.g., starlings, grackles, blackbirds, cowbirds) from various websites. Each script scrapes bird images from a designated URL and saves them into corresponding folders for each bird species.

## Features
-**Bird Categories:** This scraper supports the following bird categories by default:  
*Starling  
*Grackle  
*Blackbird  
*Cowbird  
-**Folder Management:** Images are stored in separate folders for each bird type.  
-**Error Handling:** Logs any issues encountered during image download or processing, such as broken image URLs or failed downloads.  

## Usage
1. Paste the desired urls to webscrape in ```urls.txt```
2. Run the correct web scraper file depending on the website  
3. Manually confirm that the images are correct. Delete any incorrect, blurry, or unrelated images
4. Switch to ```bird_dataset``` directory and run ```rename.py``` to correct the names of the images

Optional: Convert desired URL to HTML using ```url_to_html.py``` for easier readability
