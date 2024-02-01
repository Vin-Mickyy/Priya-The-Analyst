from bs4 import BeautifulSoup
import requests
import pandas as pd
url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page=requests.get(url)
soup=BeautifulSoup(page.text,'html')
print(soup)
table=soup.find('table',class_="wikitable sortable")
titles=table.find_all('th')
#print(titles)
titles=[x.text.strip() for x in titles]
print(titles)
#adding scraped data into dataframe using pandas
df = pd.DataFrame(columns = titles)
#df
#getting all data's <td></td> and adding it to dataframe
column_data= table.find_all('tr')
#print(column_data)

#to remove empty list from top start from indexing 1
for x in column_data[1:]:
    row_data = x.find_all('td')
    #print(row_data)
    each_row_data = [x.text.strip() for x in row_data]
    #print(each_row_data )
    #adding extracted data to the dataframe using panda inbuilt loc(length of total column) funtion
    length = len(df)
    #print(length)
    #adding it existing df
    df.loc[length] = each_row_data
df
#importing the data as .csv file

df.to_csv(r"C:\My_DataAnalyst_projects\revenues_of_largest_companies_USA.csv", index=False)