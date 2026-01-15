import requests
from pprint import pprint

products = requests.get("https://fakestoreapi.com/products").json()

print(f"There are {len(products)} products in the 'YoungFolks' store.")

for p in products:
    print("Title:", p["title"])
    print("Category:", p["category"])
    print("Rate:", p["rating"]["rate"])
    print("Price:", p["price"])
    print("Image:", p["image"])
    print()

#TODO: include the rate (not the count) of the product (Done)
#TODO: include the price (Done)
#TODO: include the picture of the product (Done)