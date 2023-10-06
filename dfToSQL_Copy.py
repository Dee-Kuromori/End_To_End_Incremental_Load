import pandas as pd
from sqlalchemy import create_engine
from urllib.parse import quote_plus

DB_USERNAME = 'consultants'
DB_PASSWORD = 'WelcomeItc@2022'
DB_HOST = 'ec2-3-9-191-104.eu-west-2.compute.amazonaws.com'
DB_PORT = '5432'
DB_NAME = 'testdb'

# Construct the connection string
DATABASE_URL = 'postgresql://consultants:%s@ec2-3-9-191-104.eu-west-2.compute.amazonaws.com:5432/testdb' % quote_plus(
    "WelcomeItc@2022")

TABLE_NAME = 'FraudAnalysis_Demetric'

# Read the CSV file into a Pandas DataFrame
csv_file_path = "FraudAnalysis.csv"
data = pd.read_csv(csv_file_path)

print(len(data))

# Create a SQLAlchemy engine and connect to the database
# engine = create_engine(DATABASE_URL)

# # Upload the data to the database table
# data.to_sql(TABLE_NAME, engine, if_exists='append', index=False)

print('CSV data successfully uploaded to the database table.')


