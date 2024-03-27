

from sqlalchemy import create_engine,text
connection_string = "mysql+mysqlconnector://vicky:admin123@jovian.mysql.database.azure.com:3306/joviancareer"
engine = create_engine(connection_string, echo=True)


# import urllib
# from sqlalchemy import create_engine, text

# server = "jovian.database.windows.net"
# database = "joviancareer"
# username = "vicky"
# password = "admin123@"



# engine = create_engine("mysql+pymysql://vicky:admin123@@jovian/joviancareer?charset=utf8mb4")
# engine = create_engine("mysql+pymysql://vicky:admin123@jovian.mysql.database.azure.com:3306/joviancareer")


with engine.connect() as conn:
    result = conn.execute(text("SELECT * FROM jobs"))  # Replace & with * to select all columns
    print(result.fetchall())





# from sqlalchemy import create_engine

# # Database connection parameters
# server = "<YOUR_SERVER_NAME>"
# database = "<YOUR_DATABASE_NAME>"
# username = "<YOUR_USERNAME>"
# password = "<YOUR_PASSWORD>"  # Please replace with your actual password

# # Database connection URL
# database_url = f"mysql+mysqlconnector://{username}:{password}@{server}/{database}"

# # Create a SQLAlchemy engine
# engine = create_engine(database_url)

# # Connect to the database
# connection = engine.connect()

# Now you can use `connection` to interact with your database

