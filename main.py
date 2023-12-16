from bs4 import BeautifulSoup as bs
import requests
import pandas as pd

# Define the URL of the webpage to be scraped
url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Send a GET request to the webpage
page = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = bs(page.text, "html.parser")

# Find the table containing the data we need
startable = soup.find_all('table')
templist = []
tablerows = startable[7].find_all('tr')

# Extract the data from the table
for tr in tablerows:
    td = tr.find_all('td')
    row = [i.text.rstrip()for i in td]
    templist.append(row)

# Create a Pandas dataframe from the extracted data
starname = []
distance = []
mass = []
radius = []
for i in range(1,len(templist)):
    starname.append(templist[i][0])
    distance.append(templist[i][5])
    mass.append(templist[i][7])
    radius.append(templist[i][8])
df2 = pd.DataFrame(list(zip(starname,distance,mass,radius)),columns = ['starname','distance','mass','radius'])

# Save the dataframe to a CSV file
df2.to_csv("dwarfstars.csv")
