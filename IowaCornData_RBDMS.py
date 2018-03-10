'''
run this SQL statement on RDBMS of choice

CREATE TABLE dbo.CornData (County NVARCHAR(150), Value INT)
'''

import csv
import pyodbc

def readinfile(self):
	with open(self,'r') as f:
		reader = csv.reader(f)
		listy = list(reader)
		return listy
		
cnxn = pyodbc.connect('DRIVER={SQL Server};SERVER=YOURSERVER;DATABASE=YOURDATABASE;UID=YOURUSERID;PWD=YOURPASSWORD')
			
corn_Data = readinfile('C://Users//Daniel.Beach//AppData//Local//Programs//Python//Python35-32//Iowa Corn Yields.csv')

for line in corn_Data:
	year = corn_Data[0]
	county = corn_Data[8]
	value = corn_Data[18]

	cursor = cnxn.cursor()
	cursor.execute("INSERT INTO dbo.CornData (Year,County,Value) VALUES (?,?,?)",year,country,value)
	cnxn.commit()

	
cursor.execute("SELECT County,SUM(Value) as Bushels FROM dbo.CornData WHERE Year = 2017 GROUP BY County")
Results = {}
			for row in cursor.fetchall():
				print(row)
				
cnxn.close()