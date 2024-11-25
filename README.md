# Bird Image Dataset
This dataset was developed to tackle the ecological issues caused by starlings, an invasive bird species that poses a threat to native birds by taking over food and nesting resources. This dataset offers high-quality labeled images of starlings and similar-looking birds, such as grackles, blackbirds, and cowbirds. The goal of this dataset is to aid in creating AI models for species recognition. These models could be integrated into smart bird feeder systems or conservation tools to help deter invasive species while supporting native birds.
  
## Data Included
This project contains scripts to web scrape images of specific bird species (e.g., starlings, grackles, blackbirds, cowbirds) from various websites. Each script scrapes bird images from a designated URL and saves them into corresponding folders for each bird species.

**Data Details:**  
The dataset contains images of starlings, grackles, blackbirds, and cowbirds.  
Total Images: #  
Image Format: jpg images, categorized into subfolders by species  

Link to dataset [here](https://www.kaggle.com/datasets/mariamkhan13/starling-grackle-cowbird-and-blackbird-dataset/data)
  
## Installation
1. Install Python 3.7 or higher
2. Install dependencies in ```requirements.txt```
  
## Usage
1. Paste the desired urls to webscrape in ```urls.txt```
2. Ensure you are in the ```web_scrape``` directory. Run the correct web scraper file depending on the website  
3. Manually confirm that the images are correct. Delete any incorrect, blurry, or unrelated images
4. Switch to the ```bird_dataset``` directory and run ```rename.py``` to correct the names of the images

Optional: Convert desired URL to HTML using ```url_to_html.py``` for easier readability

## Power Analysis

  
## Exploratory Data Analysis

  
## Ethics Statement
This dataset was developed with careful consideration of ethical standards to ensure responsible collection and use of data. All images included were sourced from publicly accessible platforms. The dataset is intended exclusively for conservation, research, and educational purposes, with a focus on deterring invasive bird species to support native bird populations and ecological balance.
  
## Open Source License

Copyright 2024 Mariam Khan  
  
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at
  
    http://www.apache.org/licenses/LICENSE-2.0
  
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
