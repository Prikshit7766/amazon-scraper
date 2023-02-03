import streamlit as st 
from bs4 import BeautifulSoup
import requests
import pandas as pd
import numpy as np
import re

# Function to extract Product Title
def get_title(soup):

    try:
        # Outer Tag Object
        title = soup.find("span", attrs={"id":'productTitle'})
        
        # Inner NavigatableString Object
        title_value = title.text

        # Title as a string value
        title_string = title_value.strip()

    except AttributeError:
        title_string = ""

    return title_string

# Function to extract Product Price
def get_price(soup):

    try:
        
        price = soup.find("span", attrs={"class":'a-price aok-align-center'}).find("span", attrs={"class": "a-price-whole"}).get_text()[:-1]

    except AttributeError:

        try:
            # If there is some deal price
            price = soup.find("span", attrs={'id':'priceblock_dealprice'}).string.strip()

        except:
            price = ""

    return price

# Function to extract Product Rating
def get_rating(soup):

    try:
        rating = soup.find("i", attrs={'class':'a-icon a-icon-star a-star-4-5'}).string.strip()
    
    except AttributeError:
        try:
            rating = soup.find("span", attrs={'class':'a-icon-alt'}).string.strip()
        except:
            rating = ""

    return rating

# Function to extract Number of User Reviews
def get_review_count(soup):
    try:
        review_count = soup.find("span", attrs={'id':'acrCustomerReviewText'}).string.strip()

    except AttributeError:
        review_count = ""

    return review_count

# Function to extract Availability Status
def get_availability(soup):
    try:
        available = soup.find("div", attrs={'id':'availability'})
        available = available.find("span").string.strip()

    except AttributeError:
        available = "Not Available"

    return available

def get_asin(href,soup):
    try:
        asin = re.search(r'/[dg]p/([^/]+)', href, flags=re.IGNORECASE)
        if asin:
            asin_number=asin.group(1)
        if asin==None:
                s=soup.find("div", attrs={"id":'detailBullets_feature_div'}).ul.text
                L=s.split()
                for i in range(len(L)):
                    if len(L[i])==10:
                        if L[i].isupper()==True:
                            asin_number=L[i]
                            break

                return asin_number  
        else:
            return asin_number           
    except AttributeError:
            asin_number=""
            return asin_number
            
def get_product_description(soup):
    try:
        product_description=soup.find("div", attrs={"id":'feature-bullets'}).text.strip().split("   ")
    except AttributeError:
            product_description=""
    return product_description
    
    
def get_seller(soup):
    try:
        #seller=soup.find("div", attrs={"id":'merchant-info'}).find(attrs={"id":"sellerProfileTriggerId"}).text
        seller=soup.find("div", attrs={"id":'merchant-info'}).text[9:-28]
        return seller
    except AttributeError: 
        seller=""
        return seller
    
 
def get_manufacturer(soup):
    try:
        manufacturer=soup.find("table", attrs={"id":'productDetails_detailBullets_sections1'}).find_all(attrs={"class":'a-size-base prodDetAttrValue'})[2].text
        return manufacturer
    
    except AttributeError:
        try:
            a=len(soup.find("div", attrs={"id":'detailBulletsWrapper_feature_div'}).find_all("span"))
            correct='Manufacturer'
            for i in range(a):
                w=new_soup.find("div", attrs={"id":'detailBulletsWrapper_feature_div'}).find_all("span")[i].text.replace("                                    ","")[:12]
                if w==correct:
                    manufacturer=new_soup.find("div", attrs={"id":'detailBulletsWrapper_feature_div'}).find_all("span")[i+1].text
                    break
            return manufacturer
        except:
            manufacturer = ""
            return manufacturer
        
@st.experimental_memo
def convert_df(df):
   return df.to_csv(index=False).encode('utf-8')





def main():
    raw_text = st.text_area("Type your URL here .....")
    int_val = st.slider('end  page', min_value=1, max_value=10, value=5, step=1)
    if st.button("Extract"):


        # add your user agent 
        # Headers for request
        HEADERS = ({'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36', 'Accept-Language': 'en-INR, en;q=0.5'}) 

        # The webpage URL
        amazon_url=raw_text

        # HTTP Request
        webpage = requests.get(amazon_url, headers=HEADERS)

        # Soup Object containing all data
        soup = BeautifulSoup(webpage.content, "html.parser")

        # Fetch links as List of Tag Objects
        links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

        # Store the links
        links_list = []

        # Loop for extracting links from Tag Objects
        for link in links:
                links_list.append(link.get('href'))

        d = {"Product URL":[],"Product Name":[], "Product Price":[], "Rating":[], "Number of reviews":[],"Availability":[],"ASIN":[],"Product Description":[],"Sold by":[],"Manufacturer":[]}
        
        # Loop for extracting product details from each link 
        for link in links_list:
            new_webpage = requests.get("https://www.amazon.in" + link, headers=HEADERS)

            new_soup = BeautifulSoup(new_webpage.content, "html.parser")

            # Function calls to display all necessary product information
            d["Product URL"].append("https://www.amazon.in"+link)
            d['Product Name'].append(get_title(new_soup))
            d['Product Price'].append(get_price(new_soup))
            d['Rating'].append(get_rating(new_soup))
            d['Number of reviews'].append(get_review_count(new_soup))
            d['Availability'].append(get_availability(new_soup))
            d['ASIN'].append(get_asin("https://www.amazon.in" + link,new_soup))
            d['Product Description'].append(get_product_description(new_soup))
            d['Sold by'].append(get_seller(new_soup))
            d['Manufacturer'].append(get_manufacturer(new_soup))
        
            
        for i in range(0,int_val-1):
            if i == 0:
                second_page_url="https://amazon.in" + soup.find_all("a", attrs={'class':'s-pagination-item s-pagination-button'})[0].get("href")
                webpage = requests.get(second_page_url, headers=HEADERS)
                soup=BeautifulSoup(webpage.content,"html.parser")
                # Fetch links as List of Tag Objects
                links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

                # Store the links
                links_list = []

                # Loop for extracting links from Tag Objects
                for link in links:
                    links_list.append(link.get('href')) 
                for link in links_list:
                    new_webpage = requests.get("https://www.amazon.in" + link, headers=HEADERS)

                    new_soup = BeautifulSoup(new_webpage.content, "html.parser")

                    # Function calls to display all necessary product information
                    d["Product URL"].append("https://www.amazon.in"+link)
                    d['Product Name'].append(get_title(new_soup))
                    d['Product Price'].append(get_price(new_soup))
                    d['Rating'].append(get_rating(new_soup))
                    d['Number of reviews'].append(get_review_count(new_soup))
                    d['Availability'].append(get_availability(new_soup))
                    d['ASIN'].append(get_asin("https://www.amazon.in" + link,new_soup))
                    d['Product Description'].append(get_product_description(new_soup))
                    d['Sold by'].append(get_seller(new_soup))
                    d['Manufacturer'].append(get_manufacturer(new_soup))
                
            else :
                next_page_url="https://amazon.in" + soup.find_all("a", attrs={'class':'s-pagination-item s-pagination-button'})[-1].get("href")
                webpage = requests.get(next_page_url, headers=HEADERS)
                soup=BeautifulSoup(webpage.content,"html.parser")
    
                links = soup.find_all("a", attrs={'class':'a-link-normal s-no-outline'})

                # Store the links
                links_list = []

                # Loop for extracting links from Tag Objects
                for link in links:
                    links_list.append(link.get('href')) 
                for link in links_list:
                    new_webpage = requests.get("https://www.amazon.in" + link, headers=HEADERS)

                    new_soup = BeautifulSoup(new_webpage.content, "html.parser")

                    # Function calls to display all necessary product information
                    d["Product URL"].append("https://www.amazon.in"+link)
                    d['Product Name'].append(get_title(new_soup))
                    d['Product Price'].append(get_price(new_soup))
                    d['Rating'].append(get_rating(new_soup))
                    d['Number of reviews'].append(get_review_count(new_soup))
                    d['Availability'].append(get_availability(new_soup))
                    d['ASIN'].append(get_asin("https://www.amazon.in" + link,new_soup))
                    d['Product Description'].append(get_product_description(new_soup))
                    d['Sold by'].append(get_seller(new_soup))
                    d['Manufacturer'].append(get_manufacturer(new_soup))

        
        amazon_df = pd.DataFrame.from_dict(d)
        amazon_df['Product Name'].replace('', np.nan, inplace=True)
        amazon_df = amazon_df.dropna(subset=['Product Name'])
        csv=convert_df(amazon_df)
        st.download_button("Press to Download",csv,"file.csv","text/csv",key='download-csv')





if __name__ == '__main__':
	main()
