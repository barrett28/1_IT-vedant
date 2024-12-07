# import mysql.connector

# cnx = mysql.connector.connect(user='root', password='root',
#                               host='127.0.0.1',
#                               database='gs')

# cursor = cnx.cursor()

# query = "SELECT * FROM products;"

# cursor.execute(query)

# for (product_id, name, uom_id, pice_per_unit) in cursor:
#     print(product_id, name, uom_id, pice_per_unit)

# cnx.close()


import mysql.connector

# Connect to the database
cnx = mysql.connector.connect(
    user='root', 
    password='root',
    host='127.0.0.1',
    database='gs'
)

cursor = cnx.cursor()

# Corrected query
# query = "SELECT * FROM products;"
query = ("SELECT products.product_id, products.name, products.uom_id, products.price_per_unit, uom.uom_name "
        "FROM products INNER JOIN uom ON  products.uom_id=uom.uom_id;")

cursor.execute(query)

# Fetch and print rows
for (product_id, name, uom_id, price_per_unit, uom_name) in cursor:
    print(product_id, name, uom_id, price_per_unit, uom_name)

# Close connection
cnx.close()
