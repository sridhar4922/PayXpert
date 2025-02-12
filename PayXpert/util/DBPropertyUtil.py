import pyodbc

class DBPropertyUtil:
    @staticmethod
    def getDBConn():
        # Specify the server name and the database name
        server = r'DESKTOP-CTO9G4R\SQLEXPRESS01'
        database = 'PayXpert'

        # Construct the connection string
        conn_str = f'DRIVER={{SQL Server}};SERVER={server};DATABASE={database};Trusted_Connection=yes;'

        try:
            # Establish the database connection
            conn = pyodbc.connect(conn_str)
            return conn
        except Exception as e:
            # Handle connection errors
            print(f"Error connecting to the database: {str(e)}")
            raise e
