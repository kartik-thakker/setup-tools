import pyodbc 

'''
Setup required before this -
1. Download the SQL server - https://www.microsoft.com/en-in/sql-server/sql-server-downloads
2. Downlaod SSMS to manage the server - https://docs.microsoft.com/en-us/sql/ssms/download-sql-server-management-studio-ssms?view=sql-server-ver15
3. Setup a dummy table - https://docs.microsoft.com/en-us/sql/ssms/quickstarts/ssms-connect-query-sql-server?view=sql-server-ver15
'''

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=LAPTOP-FB8O6O54;'
                      'Database=TutorialDB;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM dbo.Customers')

for i in cursor:
    print(i)

