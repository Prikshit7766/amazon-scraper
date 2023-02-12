# amazon-scraper

deployment
https://prikshit7766-amazon-scraper-app-64vo0e.streamlit.app/


```
The aim of this project is to scrape product information from Amazon's website using BeautifulSoup4, Requests, and re (regular expressions) libraries. The project will scrape at least 10 product listing pages, extracting information about the product's URL, name, price, rating, and number of reviews. For each product URL, the project will further scrape product descriptions, ASIN, product descriptions, and the manufacturer's name. The final data will be exported in a CSV format.
Methodology:

Scraping Product Listing Pages:
The first step of the project was to scrape product information from the product listing pages on Amazon's website. Using the Requests library, we made a GET request to the URL of each product listing page. We then parsed the HTML content of the page using BeautifulSoup4.

Extracting Product Information:
Once we had the HTML content, we used regular expressions to extract the product's URL, name, price, rating, and number of reviews. We used re.findall() to find all instances of the desired information in the HTML content.

Scraping Product Pages:
For each product URL, we made a GET request to the URL using Requests. We then parsed the HTML content of the product page using BeautifulSoup4.

Extracting Product Descriptions:
We used regular expressions and BeautifulSoup4 to extract the product description, ASIN, product description, and the manufacturer's name from the HTML content of the product page.

Exporting Data to a CSV File:
Finally, we used the pandas library to create a data frame containing all the product information and exported the data to a CSV file.

Results:
We successfully scraped product information from 200 product pages on Amazon's website, extracting the product's URL, name, price, rating, number of reviews, product description, ASIN, product description, and manufacturer's name. The data was then exported to a CSV file for further analysis.

Conclusion:
This project demonstrates the power of web scraping for extracting valuable information from websites. By using BeautifulSoup4, Requests, and regular expressions, we were able to efficiently scrape a large amount of product information from Amazon's website. This data can now be used for various purposes, such as data analysis and market research.
```
