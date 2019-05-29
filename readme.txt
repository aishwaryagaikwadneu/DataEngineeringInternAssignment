Python version 3.6 required
-Install packages wikipedia, bs4, lxml and csv

The idea behind the scrapper is as follows:
-Listing the required wikipedia page as this scrapper is specifically for the page list of US city by population. 
-Using BeautifulSoup package as it parses the broken HTML and encoding it as UTF_8 format for character encoding
-Finding tables on the page using td and th
-Using colspan to span the columns in one cell
-Finally appending the data as outputrow
-Opening file and storing as csv file
-Writing the output rows in csv and handling exception