# access-db-with-py
Accessing Databases using Python Script
## Objectives:
1. Create a database using Python.
2. Load the data from a CSV file as a table to a database.
3. Run basic "queries" on the database to access the information in the table.

## Scenario:
Consider a dataset of employee records available with an HR team in a CSV file. You are required to create a database called STAFF and load the contents of the CSV file as a table called INSTRUCTORS.
The headers of the available data are :
| Header | Description               |
| ------ | ------------------------- |
| ID     | Employee ID               |
| FNAME  | Content Cell              |
| LNAME  | Last Name                 |
| CITY   | City of residence         |
| CCODE  | Country code (2 letters)  |

## Set Up:
This project is done as a part of IBM Data Engineering Certification Course. It is developed and executed in a Cloud IDE. In this project, the database is created on a dummy server using SQLite3 Library.
To download the csv file needed for the project the following code is run in the terminal: wget https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/INSTRUCTOR.csv
To interact with the csv using python, pandas library is needed. The following command is run in the terminal to install it: python3.11 -m pip install pandas

## Code:
- The required libraries pandas and sqlite3 are imported.
- Connection is established to the database.
- A dataframe is generated from the csv file.
- The data in the dataframe is loaded into a table in the database using pandas.
- The table is queried.
- A dictionary is created with data to insert into the table.
- The dictionary is converted into a dataframe.
- The data in this dataframe is appended to the table.
- The table is queried.
- Finally, the database connection is closed. 

## Acknowledgement
[IBM - Python Project for Data Engineering]([https://www.mesquite.com/](https://www.coursera.org/programs/computer-science-comps-alternatives-zphna/learn/python-project-for-data-engineering?authProvider=ttu)https://www.coursera.org/programs/computer-science-comps-alternatives-zphna/learn/python-project-for-data-engineering?authProvider=ttu)

