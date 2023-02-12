# Amazon Scraper

## Deployment
The app is deployed at https://prikshit7766-amazon-scraper-app-64vo0e.streamlit.app/

## Introduction
The aim of this project is to scrape product information from Amazon's website using BeautifulSoup4, Requests, and re (regular expressions) libraries. The project will scrape at least 10 product listing pages, extracting information such as the product's URL, name, price, rating, and number of reviews. For each product URL, further information such as the product description, ASIN, product description, and the manufacturer's name will be scraped. The final data will be exported in a CSV format.

## Methodology
### Scraping Product Listing Pages
1. The first step is to scrape product information from product listing pages on Amazon's website.
2. Using the Requests library, a GET request is made to the URL of each product listing page.
3. The HTML content of the page is parsed using BeautifulSoup4.

### Extracting Product Information
1. The HTML content is used to extract the product's URL, name, price, rating, and number of reviews using regular expressions.
2. re.findall() is used to find all instances of the desired information in the HTML content.

### Scraping Product Pages
1. For each product URL, a GET request is made to the URL using Requests.
2. The HTML content of the product page is parsed using BeautifulSoup4.

### Extracting Product Descriptions
1. The product description, ASIN, product description, and the manufacturer's name are extracted from the HTML content of the product page using regular expressions and BeautifulSoup4.

### Exporting Data to a CSV File
1. The pandas library is used to create a data frame containing all the product information.
2. The data is then exported to a CSV file for further analysis.

## Results
The project successfully scraped product information from 200 product pages on Amazon's website, extracting the product's URL, name, price, rating, number of reviews, product description, ASIN, product description, and manufacturer's name. The data was exported to a CSV file for further analysis.
