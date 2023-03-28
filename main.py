from fastapi import FastAPI, Request
from schemas import *
import connector
import uvicorn

products = []
establishments = []
prices = []

app = FastAPI()

#Method to create a product
@app.post("/products/")
async def createProduct(product: Product):
    def create(response: Product):
        cursor, connection = connector.mycursor()
        sql = "INSERT INTO products (brand,type,calories,fatPerc,sugarPerc) " \
              "VALUES ('" + product["brand"] + "'," + str(product["type"]) + "" \
            "," + str(product["calories"]) + "," + str(product["fatPerc"]) + "," \
             "'" + str(product["sugarPerc"])  + ")"

        cursor.execute(sql)
        connection.commit()
        return {"message": "A product was created successfully."}

#Method to return all products
@app.get("/products/")
async def getAllProducts():
    cursor, connection = connector.mycursor()
    cursor.execute("SELECT product.brand, product.type, product, FROM product INNER JOIN Prices ON Prices.ProductID=products.ProductID;")
    return cursor.fetchall()

@app.put("/products/{productID}")
async def updateProduct(productID: int, product: Product):
    #SQL command to edit any column of the product. Did not have the time
    return {"message": "A product was updated successfully."}

@app.post("/establishments/")
async def createEstablishment(establishment: Establishment):
    #Here the code will be similar to product creation. Did not have the time
    return {"message": "An establishment was created successfully."}

#Method to add a price
@app.post("/prices/")
async def addPrice(price: Price):
    prices.append(price)
    return {"message": "A new price was added successfully."}



if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)