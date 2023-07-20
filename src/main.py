import mysql.connector
from mysql.connector import Error
import sys
import time
from unidecode import unidecode
from zeep import Client

import config

class DatabaseManager:
    def __init__(self, user, password, host, database):
        self.cnx, self.cursor = self.connect_to_mysql(user, password, host, database)

    def connect_to_mysql(self, user, password, host, database):
        # Establishes a connection to the MySQL server and returns the connection and a cursor.
        for attempt in range(3):
            try:
                cnx = mysql.connector.connect(user=user, password=password, host=host, database=database)
                cursor = cnx.cursor()
                return cnx, cursor
            except Error as e:
                print(f"Error while connecting to MySQL: {e}")
                print(f"Attempt {attempt+1} of {3} failed. Retrying in {5} seconds...")
                time.sleep(5)
        sys.exit(f"Could not connect to MySQL after {3} attempts.")

    def create_table(self, query):
        # Creates a table in the database using the given query.
        try:
            self.cursor.execute(query)
        except Error as e:
            print(f"Error while creating table: {e}")

    def insert_data(self, data):
        # Inserts the data into the countries table, if it does not exist, otherwise updates it.
        try:
            for country in data:
                query = "REPLACE INTO countries (iso_code, name) VALUES (%s, %s)"
                self.cursor.execute(query, (country['sISOCode'], country['sName']))
        except Error as e:
            print(f"Error while inserting data: {e}")

    def query_db(self):
        # Queries the countries table and prints the results.
        try:
            self.cursor.execute("SELECT * FROM countries")
            for record in self.cursor:
                print(record)
                pass
        except Error as e:
            print(f"Error while querying data: {e}")

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.cnx:
            self.cnx.close()

def get_soap_data(url):
    # Retrieves data from the SOAP service.
    client = Client(url)
    try:
        data = client.service.ListOfCountryNamesByCode()
        return data
    except Exception as e:
        sys.exit(f"Error while getting SOAP data: {e}")

def clean_data(data):
    for country in data:
        country["sName"] = unidecode(country["sName"])

    return data

def main():
    data = get_soap_data(config.URL)
    db_manager = DatabaseManager(config.USER, config.PASSWORD, config.HOST, config.DATABASE)
    db_manager.create_table(config.CREATE_TABLE_QUERY)
    cleaned_data = clean_data(data)
    db_manager.insert_data(cleaned_data)
    db_manager.query_db()
    db_manager.close()

if __name__ == '__main__':
    main()