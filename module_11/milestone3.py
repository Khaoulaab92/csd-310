#Group 1
#Khaoula Azdoud
#Tanner Agnew
#07/13/2023
#Module 11.1 Assignment: Milestone 3
#Case Study: Outland Adventures

import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "outlandAdventures_user",
    "password": "casestudy",
    "host": "127.0.0.1",
    "database": "outlandAdventures",
    "raise_on_warnings": True
}

try:
    db = mysql.connector.connect(**config)

    print("\n database user {} connected to MYSQL on host {} with database {}".format(config["user"], config["host"], config["database"]))

    input("\n\n  Press any key to continue...\n")

except mysql.connector.Error as err:
    if err.errno == errorcode.Er_ACCES_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

# Display Equipment Sales Report 
cursor = db.cursor()
cursor.execute("SELECT equipment_name, COUNT(*) AS 'Equipment Sales Count' FROM sale, equipment WHERE sale.equipment_id = equipment.equipment_id AND sale_type = 'purchased' GROUP BY equipment_name")
sales = cursor.fetchall()
print("-- DISPLAYING Equipment Sales Report --\n")
for sale in sales:
    print("Equipment Name: {}\nEquipment Sales Count: {}\n".format(sale[0], sale[1]))

# Display Equipment Sales Report details
cursor = db.cursor()
cursor.execute("SELECT equipment_name, sale_id, sale_type, customer_name, customer_address FROM equipment, sale, customer WHERE sale.equipment_id = equipment.equipment_id AND sale.customer_id = customer.customer_id AND sale_type = 'purchased'")
sales = cursor.fetchall()
print("-- DISPLAYING Equipment Sales Report Details --\n")
for sale in sales:
    print("Equipment Name: {}\nSale ID: {}\nSale Type: {}\nCustomer Name: {}\nCustomer Address: {}\n".format(sale[0], sale[1], sale[2], sale[3], sale[4]))

# Display Booking Trend Report 
cursor = db.cursor()
cursor.execute("SELECT trip_destination, COUNT(*) AS 'Booking Count' FROM booking  JOIN trip  ON booking.trip_id = trip.trip_id WHERE trip_destination IN ('Africa', 'Asia', 'Southern Europe') GROUP BY trip_destination")
bookings = cursor.fetchall()
print("-- DISPLAYING Booking Trend Report --\n")
for booking in bookings:
    print("Destination: {}\nBooking Count: {}\n".format(booking[0], booking[1]))

# Display Inventory Aging Report
cursor = db.cursor()
cursor.execute("SELECT equipment_id, equipment_name, equipment_type, purchase_date FROM equipment WHERE purchase_date <= DATE_SUB(NOW(), INTERVAL 5 YEAR)")
equipments = cursor.fetchall()
print("-- DISPLAYING Inventory Aging Report --\n")
for equipment in equipments:
    print("Equipment ID: {}\nEquipment Name: {}\nEquipment Type: {}\nPurchase Date: {}\n".format(equipment[0], equipment[1], equipment[2], equipment[3]))
    
cursor.close()
db.close()

