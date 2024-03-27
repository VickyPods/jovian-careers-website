import pyodbc

# Database connection parameters
server = "jovian.database.windows.net"
database = "joviancareer"
username = "vicky"
password = "admin123@"  # Please replace with your actual password

connection_string = f"DRIVER={{MySQL ODBC 8.0 Unicode Driver}};SERVER={server};DATABASE={database};USER={username};PASSWORD={password};"

# Connect to the database
try:
    connection = pyodbc.connect(connection_string)
    print("Connected to the database!")

    # Now you can use the 'connection' object to execute SQL queries
    # For example:
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM jobs")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # Don't forget to close the connection when you're done
    connection.close()
except pyodbc.Error as e:
    print(f"Error connecting to the database: {e}")