import requests
from bs4 import BeautifulSoup
import pandas as pd

# download the webpage
url = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-PY0220EN-SkillsNetwork/labs/project/netflix_data_webpage.html"
r = requests.get(url)

# parse the html using beautiful_soup
soup = BeautifulSoup(r.content)

# find the table containing the stock data
table = soup.find('table')

# extract the column headers
headers = []
for th in table.find_all('th'):
    headers.append(th.text.strip())

# extract the data rows
data = []
for tr in table.find_all('tr')[1:]:
    row = []
    for td in tr.find_all('td'):
        row.append(td.text.strip())
    data.append(row)

# create a Pandas DataFrame from the extracted data
df = pd.DataFrame(data, columns=headers)

# print the DataFrame
print(df)
