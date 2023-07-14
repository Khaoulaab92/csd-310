#Group 1
#Khaoula Azdoud
#Tanner Agnew
#07/09/2023
#Module 10.1 Assignment: Milestone 2
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

    input("\n\n  Press any key to continue...")

except mysql.connector.Error as err:
    if err.errno == errorcode.Er_ACCES_DENIED_ERROR:
        print("The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print(" The specified database does not exist")

    else:
        print(err)

# Display Customer Table
cursor = db.cursor()
cursor.execute("SELECT * FROM customer")
customers = cursor.fetchall()
print("-- DISPLAYING Customer Table --\n")
for customer in customers:
    print("Customer ID: {}\nCustomer Name: {}\nCustomer Email: {}\nCustomer Address: {}\n".format(customer[0], customer[1], customer[2], customer[3]))

# Display Trip Table
cursor = db.cursor()
cursor.execute("SELECT trip_id, trip_destination, start_date, end_date, employee_name FROM trip, employee WHERE trip.employee_id = employee.employee_id")
trips = cursor.fetchall()
print("-- DISPLAYING Trip Table --\n")
for trip in trips:
    print("Trip ID: {}\nTrip Destination: {}\nStart Date: {}\nEnd Date: {}\nGuide: {}\n".format(trip[0], trip[1], trip[2], trip[3], trip[4]))

# Display Booking Table
cursor = db.cursor()
cursor.execute("SELECT booking_number, customer_name, trip_destination FROM booking, customer, trip WHERE booking.customer_id = customer.customer_id AND booking.trip_id = trip.trip_id")
bookings = cursor.fetchall()
print("-- DISPLAYING Booking Table --\n")
for booking in bookings:
    print("Booking Number: {}\nCustomer Name: {}\nTrip Destination: {}\n".format(booking[0], booking[1], booking[2]))

# Display Employee Table
cursor = db.cursor()
cursor.execute("SELECT * FROM employee")
employees = cursor.fetchall()
print("-- DISPLAYING Employee Table --\n")
for employee in employees:
    print("Employee ID: {}\nEmployee Name: {}\nEmployee Role: {}\n".format(employee[0], employee[1], employee[2]))

# Display Equipment Table
cursor = db.cursor()
cursor.execute("SELECT * FROM equipment")
equipments = cursor.fetchall()
print("-- DISPLAYING Equipment Table --\n")
for equipment in equipments:
    print("Equipment ID: {}\nEquipment Name: {}\nEquipment Type: {}\nPurchase Date: {}\nEquipment Price: ${}\nEquipment Rental Price: ${}\n".format(equipment[0], equipment[1], equipment[2], equipment[3], equipment[4], equipment[5]))

# Display Sale Table
cursor = db.cursor()
cursor.execute("SELECT sale_id, sale_type, equipment_name, customer_name FROM sale, equipment, customer WHERE sale.equipment_id = equipment.equipment_id AND sale.customer_id = customer.customer_id")
sales = cursor.fetchall()
print("-- DISPLAYING Sale Table --\n")
for sale in sales:
    print("Sale ID: {}\nSale Type: {}\nEquipment Name: {}\nCustomer Name: {}\n".format(sale[0], sale[1], sale[2], sale[3]))
    
cursor.close()
db.close()

