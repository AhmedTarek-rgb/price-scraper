# import requests
# from bs4 import BeautifulSoup
# import csv

# # The website I am scraping
# url = "https://books.toscrape.com/"

# # Sending request to the website and store the response
# response = requests.get(url)
# response.encoding = "utf-8"

# # # Printing the status code to check if it is worked
# # print(response.status_code)

# # Parse the HTML content
# soup = BeautifulSoup(response.text, "html.parser")

# # Find all book containers on the page
# books = soup.find_all("article", class_="product_pod")

# print how many books I have found
# print(len(books))

# # Look at the first book only
# first_book = books[0]

# # Extract the title
# title = first_book.find("h3").find("a")["title"]

# # Extract the price
# price = first_book.find("p", class_="price_color").text

# # Loop through all 20 books
# for book in books:
#     title = book.find("h3").find("a")["title"]
#     price = book.find("p", class_="price_color").text
#     print(title, price)

# Open a CSV file to write into
# with open("books.csv", "w", newline="", encoding="utf-8") as file:
#     writer = csv.writer(file)
#     # Writer the header row
#     writer.writerow(["Title", "Price"])

#     # Loop through all books and write each one
#     for book in books:
#         title = book.find("h3").find("a")["title"]
#         price = book.find("p", class_="price_color").text
#         writer.writerow([title, price])

# print("Done! books.csv has been created.")

import requests
from bs4 import BeautifulSoup
import csv

url = "https://books.toscrape.com/"

response = requests.get(url)
response.encoding = "utf-8"

soup = BeautifulSoup(response.text, "html.parser")
books = soup.find_all("article", class_="product_pod")

with open("books.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Price"])
    
    for book in books:
        title = book.find("h3").find("a")["title"]
        price = book.find("p", class_="price_color").text
        writer.writerow([title, price])

print("Done! books.csv has been created.")