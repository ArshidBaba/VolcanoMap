# import all the important libraries
import requests
from bs4 import BeautifulSoup
from csv import writer
import pandas as pd

#make requests
response = requests.get("http://volcano.oregonstate.edu/volcano_table")

#instantiate BeautifulSoup
soup = BeautifulSoup(response.text, "html.parser")

#find all the tables on the page
table = soup.find_all("table")

#open csv file in write mode
with open("volcano_data.csv", "w") as csv_file:
	csv_writer = writer(csv_file) 
	csv_writer.writerow(["VolcanoName", "Country", "Type", "Latitude", "Longitude", "Elevation"])
	
	#iterate through the elements of the table on the page
	l = []
	for mytable in table:
		table_body = mytable.find('tbody')
		rows = table_body.find_all('tr')
		for tr in rows:
			cols = tr.find_all('td')
			for td in cols:
				a_tag = td.find("a") 	#find the anchor tag present in the column
				if a_tag != None:
					name = a_tag.get_text()		#save the text from the anchor tag
					l.append(name)				#append the name to the list
				else:
					l.append(td.get_text())		#append the rest of the columns to the list
					

	#remove all the extra spaces and escape sequences from the list
	nl = []
	for item in l:
		nl.append(item.strip())

	print(nl)

	#append the existing list to the new list of lists six elements at a time, 
	#which is the length of a single row in the table
	listoflists = []
	i, j = 0, 6
	while j <len(nl):
		listoflists.append(nl[i:j])
		i+=6
		j+=6

	print(listoflists)


	# write the cleaned list of lists to a csv file
	csv_writer.writerows(listoflists)



