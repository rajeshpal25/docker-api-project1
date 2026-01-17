import requests
import json

def get_book():
    response = requests.get('https://potterapi-fedeperin.vercel.app/en/books')
    books = response.json()
    return books

book_list=get_book()
with open("books.json", "w") as json_file:
    json.dump(book_list, json_file, indent=4)  # indent=4 makes it readable   
print("Data saved successfully to data.json")