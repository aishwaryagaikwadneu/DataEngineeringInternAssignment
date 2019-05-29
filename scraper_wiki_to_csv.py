#Python 3.6 environment
#importing required packages(Install packages wikipedia, bs4 and csv)
import wikipedia
from bs4 import BeautifulSoup
import csv
#listing the required wikipedia page
wikiPage = wikipedia.page("List_of_United_States_cities_by_population")
#beautifulSoup parses broken HTML
soup = BeautifulSoup(wikiPage.html().encode("UTF-8"), 'lxml')

#Finding tables on wikipedia page
tables = soup.find_all('table')

fileCnt =0

for table in tables:

    try:
        rows = []
        for row in table.find_all('tr'):

            outputrow = []
            #Finding tables using table data and table header
            columns = row.find_all(["td","th"])
            for column in columns:
                if len(column)>0:
                    colspan = 0
                    #replacing unrequired fields
                    colData = column.text.replace('\ufeff', '').replace('\xa0', ' ').replace('\n', '')
                    #colData = column.text
                    #print(colData)
                    #print(column)
                    #spanning the columns in one cell
                    try:
                        colspan= column.attrs['colspan']
                    except:
                        pass

                    #appending data
                    if int(colspan)>0 :
                        for i in range(int(colspan)):
                            outputrow.append(f"{colData}_{i}")
                    else:
                        outputrow.append(colData)

            if(len(outputrow)>0):
                rows.append(outputrow)

        #opening file and storing in csvfile
        filename= f'WikiCsv_{fileCnt}.csv'
        with open(filename, 'w', encoding='utf-8') as csvfile:
            # creating a csv writer object
            csvwriter = csv.writer(csvfile)
            # writing the data rows
            csvwriter.writerows(rows)

    #catching exception
    except Exception as ex:

        print(ex)
    finally:
       fileCnt = fileCnt + 1

