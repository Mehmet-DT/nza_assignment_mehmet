# MySQL configuration
USER = 'gebruiker'
PASSWORD = 'w8woord'
HOST = 'mydb'
DATABASE = 'codetest'

# Create table
CREATE_TABLE_QUERY = """
    CREATE TABLE IF NOT EXISTS countries (
    iso_code CHAR(2) PRIMARY KEY,
    name VARCHAR(64)
    );
    """

# SOAP API Endpoint
URL = 'http://webservices.oorsprong.org/websamples.countryinfo/CountryInfoService.wso?WSDL'