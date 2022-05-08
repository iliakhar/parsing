
import requests
from bs4 import BeautifulSoup as BS

def SearchInCrypt(key, dictionary):
    if key in dictionary:
        if(len(key)<7):
            print(key,'\t\t', dictionary[key][0],'\t',dictionary[key][1])
        else: print(key,'\t', dictionary[key][0],'\t',dictionary[key][1])
    else: print("Invalid name")

response = requests.get("https://coinmarketcap.com/")
soup = BS(response.content, 'html.parser')
Name = (soup.find("table", class_="h7vnx2-2 czTsgW cmc-table")).find_all("p", class_="sc-1eb5slv-0 iworPT")
Market_cap = (soup.find("table", class_="h7vnx2-2 czTsgW cmc-table")).find_all("span", class_="sc-1ow4cwt-1 ieFnWP")
Price = ((soup.find("table", class_="h7vnx2-2 czTsgW cmc-table")).find_all("div", class_="sc-131di3y-0 cLgOOr"))
for elem in Price:
    elem = elem.find("span")
d = dict()

for ind in range(len(Name)):
    l = [Market_cap[ind].text, Price[ind].text]
    d.update({Name[ind].text : l})

print("Name\t\t Market_cap\t\t Price\n")

for key in d.keys():
    SearchInCrypt(key, d)

while(1):
    key = input("\nEnter the name (0 to exit): ")
    print('\n')
    if(key == "0"): break
    SearchInCrypt(key, d)