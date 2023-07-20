# NZA Code Assignment
## Introduction
This project retrieves data from a SOAP service, cleans the data, and inserts it into a MySQL database.
The following SOAP service is used to retrieve the data: http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL

The goal is to save the country names along with with their respective ISO codes in a locally hosted MySQL database.

## How it works
- `config.py` contains configurations which are used in `main.py`
- `main.py` contains the main code which is being executed. Which works as follows:
  1. Retrieves the raw data from the SOAP service.
  2. It sets up the connection to the MySQL database.
  3. It creates a table called `countries` with `iso_code` and `name` as columns, `iso_code` being the primary key.
  4. It cleans the raw data by replacing any non-ASCII characters with their ASCII counter-part.
  5. It loops over the cleaned data and inserts it into the database.
  6. Finally it performs a `SELECT * FROM countries` query and prints out each record to reveal the data stored in the database.
- Docker is used to containerize the project. Two docker containers are created. One to run the MySQL server and one for the Python project.

## Instructions
1. Make sure to have [Docker Desktop](https://www.docker.com/) installed on your system.

2. Clone the project to your system.

3. In the root directory run the following command to build the Docker images: `docker-compose up -d`

4. To run the script run the following command: `docker-compose run app`