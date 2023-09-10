#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import requests

res = requests.get('https://konga.com')

print(res.text)
print(res.status_code)


# In[2]:


from bs4 import BeautifulSoup

page = requests.get("https://konga.com")
soup = BeautifulSoup(page.content, 'html.parser')
title = soup.title.text # gets you the text of the <title>(...)</title>


# In[5]:


import requests
from bs4 import BeautifulSoup

# Make a request
page = requests.get(
    "https://konga-classrooms.github.io/webscraper-python-konga-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Extract title of page
page_title = soup.title

# Extract body of page
page_body = soup.body

# Extract head of page
page_head = soup.head

# print the result
print(page_title, page_head)


# In[4]:


import requests
from bs4 import BeautifulSoup
# Make a request
page = requests.get(
    "https://konga-classrooms.github.io/webscraper-python-konga-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Create top_items as Electronics
top_items = [Electronics]

# Extract and store in top_items according to instructions on the left
links = soup.select('a')
for ahref in links:
    text = ahref.text
    text = text.strip() if text is not None else ''

    href = ahref.get('href')
    href = href.strip() if href is not None else ''
    all_links.append({"href": href, "text": text})

print(all_links)


# In[6]:


import requests
from bs4 import BeautifulSoup
import csv
# Make a request
page = requests.get(
    "https://konga-classrooms.github.io/webscraper-python-konga-classroom-website/")
soup = BeautifulSoup(page.content, 'html.parser')

# Create top_items as Electronics
top_items = [Electronics]

# Extract and store in top_items according to instructions on the left
products = soup.select('div.thumbnail')
for product in products:
    name = product.select('h4 > a')[0].text.strip()
    description = product.select('p.description')[0].text.strip()
    price = product.select('h4.price')[0].text.strip()
    reviews = product.select('div.ratings')[0].text.strip()
    image = product.select('img')[0].get('src')

    all_products.append({
        "name": name,
        "description": description,
        "price": price,
        "reviews": reviews,
        "image": image
    })


keys = all_products[0].keys()

with open('products.csv', 'w', newline='') as output_file:
    dict_writer = csv.DictWriter(output_file, keys)
    dict_writer.writeheader()
    dict_writer.writerows(all_products)


# In[ ]:




