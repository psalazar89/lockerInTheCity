import csv
import connector

# Open the first CSV file
with open('products.csv', 'r') as proFile:
    cursor, connection = connector.mycursor()
    readerPro = csv.reader(proFile)
    next(readerPro)  # Skit row with the labels
    for row in readerPro:
        cursor = connector.mycursor()
        cursor.execute(
            "INSERT INTO products (name, type, calories, fatPerc, sugarPerc) VALUES (%s, %s, %s, %s, %s)",
            (row[0], row[1], row[2], row[3], row[4])
        )
        connector.commit()

with open('establishments.csv', 'r') as estFile:
    cursor, connection = connector.mycursor()
    readerEst = csv.reader(estFile)
    next(readerEst) #Skit row with the labels
    for row in readerEst:
        cursor = connector.mycursor()
        cursor.execute(
            "INSERT INTO establishments (name, address, openingHours) VALUES (%s, %s, %s)",
            (row[0], row[1], row[2])
        )
        connector.commit()


