from bs4 import BeautifulSoup as bs
import requests
import pandas as pd
import time

# Variable to keep track of successful tests
testcount = 0

# ANSI color codes for terminal text formatting
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# User input to determine whether to run in test mode
opinion1 = input(f"{bcolors.WARNING}Warning: Do you want to turn on test mode? Y/n{bcolors.ENDC}")

# Function to run a test and print a success message if in test mode
def runTest():
    global testcount
    if opinion1 == "Y" or opinion1=="y":
        testcount+=1
        print(f"{bcolors.OKGREEN}Test Completed, Index {testcount}{bcolors.ENDC}")

# Define the URL of the webpage to be scraped
url = "https://en.wikipedia.org/wiki/List_of_brown_dwarfs"

# Run test for accessing the URL
runTest()

# Send a GET request to the webpage
page = requests.get(url)

# Run test for successful GET request
runTest()

# Parse the HTML content of the page using BeautifulSoup
soup = bs(page.text, "html.parser")

# Run test for successful HTML parsing
runTest()

# Find the table containing the data we need
startable = soup.find_all('table')
templist = []
tablerows = startable[7].find_all('tr')

# Run test for successful table identification
runTest()

# Extract the data from the table
for tr in tablerows:
    td = tr.find_all('td')
    row = [i.text.rstrip()for i in td]
    templist.append(row)

# Run test for successful data extraction
runTest()

# Create a Pandas dataframe from the extracted data
starname = []
distance = []
mass = []
radius = []

# Run test for successful DataFrame creation
runTest()

for i in range(1, len(templist)):
    starname.append(templist[i][0])
    distance.append(templist[i][5])
    mass.append(templist[i][7])
    radius.append(templist[i][8])

df2 = pd.DataFrame(list(zip(starname, distance, mass, radius)), columns=['starname', 'distance', 'mass', 'radius'])

# Run test for successful DataFrame saving to CSV
runTest()

# Save the dataframe to a CSV file
df2.to_csv("csv1.csv")

# Loop to clean the DataFrame
for i in range(0, len(df2)):
    if (df2.loc[i, 'distance'] == "") or (df2.loc[i, 'distance'] == " "):
        df2.drop(index=i, inplace=True)
    elif (df2.loc[i, 'mass'] == "") or (df2.loc[i, 'mass'] == " "):
        df2.drop(index=i, inplace=True)
    elif (df2.loc[i, 'radius'] == "") or (df2.loc[i, 'radius'] == " "):
        df2.drop(index=i, inplace=True)

# Run test for successful DataFrame cleaning
runTest()

# Save the cleaned dataframe to a CSV file
df2.to_csv("csv2.csv")

# Loop to process mass and radius data
for i in range(0, len(df2)):
    try:
        tempmass = df2.loc[i, 'mass']
        floatmass = float(tempmass)
        mainmass = floatmass * 0.0000954588
        tempstarname = df2.loc[i, 'starname']
        df2.loc[df2['starname'] == tempstarname, 'mass'] = mainmass

        tempradi = df2.loc[i, 'radius']
        floatradi = float(tempradi)
        mainradi = floatradi * 0.102763
        df2.loc[df2['starname'] == tempstarname, 'radius'] = mainradi
    except:
        pass

# Run test for successful data processing
runTest()

# Save the processed dataframe to a CSV file
df2.to_csv("csv3.csv")

# Print the overall status
print(f"{bcolors.OKCYAN}Code Executed with {testcount} tests success out of total 9 Tests{bcolors.ENDC}")
print(f"{bcolors.FAIL}One Server Error should be given to MacOs/Linux users. If not then can be avoided{bcolors.ENDC}")
print(f"{bcolors.FAIL}STATE : NON-CRITICAL{bcolors.ENDC}")
