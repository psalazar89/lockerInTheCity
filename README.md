# lockerInTheCity
locker in the city assestment

This assestment contains:

  - createDB.sql. Point 2 in the assestment. This file with the SQL Commands to create a DB with 3 tables.
                      - Establishments
                      - Products
                      - Prices
                      
  - main.py. The server written with FastAPI and the API Rest. Only two functions are completed. I didnt have the time to complete the others.
  - connector.py. This function is used to connect via pymysql to the database
  - schemas.py. File with the DTOS used for the database, products, establishments and Prices.
  
  - generate_data.py. Script to create two csv files with some establishments and products (point 1 in assestment)
  
  - load_data.py. Script to load the data into the database using pymysql. Point 4 of the assestment
  
  
  With these 5 files the 3 first points of the assestments can be done. The code is not yet runable as I didnt want to spend more than 2 hours on it.
  
  
  As well two CSV files are updated as an example for products and Establishments
  
  
  The code is not fully completed and it needs to be tested. I think for the refinement the main file shouldnt contain all the SQL commands. These interaction between API and DB can be done with 2-3 additional files product.py, establishment.py, utils.py where all the requests are given.
  
  I used FastAPI as it is better as the documentation is built-in and it can help the user understand with the help of OpenAPI the methods written.
  
