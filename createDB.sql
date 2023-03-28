
CREATE TABLE products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  brand TEXT,
  type TEXT,
  calories REAL,
  fatPerc REAL,
  sugarPerc REAL
);

CREATE TABLE establishments (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE,
  address TEXT,
  openingHours TEXT
);

CREATE TABLE prices (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  productID INTEGER,
  establishmentID INTEGER,
  price REAL,
  FOREIGN KEY (productID) REFERENCES products (id),
  FOREIGN KEY (establishmentID) REFERENCES establishments (id)
);