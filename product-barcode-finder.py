import requests

url = input("Paste the url of the product")
req = requests.get(url, 'html.parser')

split_text = req.text.split('barcode":"')
barcode = split_text[1].split('"')
print(barcode[0])
