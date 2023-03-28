import csv

class Product:
    def __init__(self, brand, type, calories, fatPerc, sugarPerc):
        self.brand = brand
        self.type = type
        self.calories = calories
        self.fatPerc = fatPerc
        self.sugarPerc = sugarPerc

class Establishment:
    def __init__(self, name, address, openingHours):
        self.name = name
        self.address = address
        self.openingHours = openingHours


def createCSV():
    #Create random products
    products = []
    products.append(Product("Pascual", "Milk",400, 10, 20.5))
    products.append(Product("Cocacola", "Softdrink",60, 0.1, 13.5))
    products.append(Product("KitKat","Candy",500,10.0,40.0))

    #Create the csv of the products
    with open("products.csv","w+", newline="") as proFile:
        writer = csv.writer(proFile)
        writer.writerow(["Brand","Type","Calories","Fat Percentage","Sugar Percentage"])
        for product in products:
            writer.writerow([product.brand,product.type,product.calories,product.fatPerc,product.sugarPerc])

    establishments = []
    establishments.append(Establishment("Mercadona","Calle Juan Roig 5", "09:00-21:00"))
    establishments.append(Establishment("7Eleven", "Calle Mayor 4", "00:00-23:59"))

    #Create the csv of the products
    with open("establishments.csv","w+", newline="") as estaFile:
        writer = csv.writer(estaFile)
        writer.writerow(["Name","Address","Opening Hours"])
        for establishment in establishments:
            writer.writerow([establishment.name,establishment.address,establishment.openingHours])


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    createCSV()

