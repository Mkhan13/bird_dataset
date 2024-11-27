# Bird Image Dataset
This dataset was developed to tackle the ecological issues caused by starlings, an invasive bird species that poses a threat to native birds by taking over food and nesting resources. This dataset offers high-quality labeled images of starlings and similar-looking birds, such as grackles, blackbirds, and cowbirds. The goal of this dataset is to aid in creating AI models for species recognition. These models could be integrated into smart bird feeder systems or conservation tools to help deter invasive species while supporting native birds.
  
## Data Included
This project contains scripts to web scrape images of specific bird species (e.g., starlings, grackles, blackbirds, cowbirds) from various websites. Each script scrapes bird images from a designated URL and saves them into corresponding folders for each bird species.

**Data Details:**  
The dataset contains images of starlings, grackles, blackbirds, and cowbirds.  
Total Images: 564  
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
Using the ANOVA model to perform a power analysis, in order for the data to be statistically significant, there needs to be 277 images of each bird species, for a total of 1108 images. This dataset has a total of 564 images, meaning more data needs to be collected of each species for this dataset to be significant.
  
## Exploratory Data Analysis
The dataset requires further data collection to increase the number of images for each species, particularly starlings. Although the dataset is intended to focus on starlings, they currently have the fewest images. This is because other bird types include multiple subspecies, which expands the range of sources available for web scraping, whereas there is only one species of starling.

The existing images in the dataset are of high quality: they are well-focused, similar in size, feature a single bird, and the bird is the central focal point of each image. This consistency ensures that the dataset is suitable for machine learning applications because clear and focused images are important for accurate model training.
  
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
