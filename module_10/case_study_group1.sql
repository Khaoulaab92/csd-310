/*
    Title: case_study_group1.sql
    Author: Khaoula Azdoud, Tanner Agnew
    Date: 07/08/2023
    Description: outlandAdventures database initialization script.
*/

-- Drop database user if it exists 
DROP USER IF EXISTS 'outlandAdventures_user'@'localhost';

-- Create outlandAdventures_user and grant all privileges to the outlandAdventures database 
CREATE USER 'outlandAdventures_user'@'localhost' IDENTIFIED WITH mysql_native_password BY 'casestudy';

-- Grant all privileges to the outlandAdventures database to user outlandAdventures_user on localhost 
GRANT ALL PRIVILEGES ON outlandAdventures.* TO 'outlandAdventures_user'@'localhost';

-- Drop tables if they exist
DROP TABLE IF EXISTS sale;
DROP TABLE IF EXISTS booking;
DROP TABLE IF EXISTS equipment;
DROP TABLE IF EXISTS customer;
DROP TABLE IF EXISTS trip;
DROP TABLE IF EXISTS employee;

-- Create the customer table
CREATE TABLE customer (
    customer_id INT NOT NULL AUTO_INCREMENT,
    customer_name VARCHAR(75) NOT NULL,
    customer_email VARCHAR(90) NOT NULL,
    customer_address VARCHAR(120) NOT NULL,
    PRIMARY KEY (customer_id)
);

-- Create the employee table
CREATE TABLE employee (
    employee_id INT NOT NULL AUTO_INCREMENT,
    employee_name VARCHAR(75) NOT NULL,
    employee_role VARCHAR(90) NOT NULL,
    PRIMARY KEY (employee_id)
);

-- Create the trip table
CREATE TABLE trip (
    trip_id INT NOT NULL AUTO_INCREMENT,
    trip_destination VARCHAR(70) NOT NULL,
    start_date DATE NOT NULL,
    end_date DATE NOT NULL,
    employee_id INT NOT NULL,
    PRIMARY KEY (trip_id),

    FOREIGN KEY(employee_id)
        REFERENCES employee(employee_id)
);

-- Create the booking table
CREATE TABLE booking (
    booking_number INT NOT NULL AUTO_INCREMENT,
    customer_id INT NOT NULL,
    trip_id INT NOT NULL,
    PRIMARY KEY (booking_number),
    FOREIGN KEY (customer_id) REFERENCES customer (customer_id),
    FOREIGN KEY (trip_id) REFERENCES trip (trip_id)
);

-- Create the equipment table
CREATE TABLE equipment (
    equipment_id INT NOT NULL AUTO_INCREMENT,
    equipment_name VARCHAR(100) NOT NULL,
    equipment_type VARCHAR(100) NOT NULL,
    purchase_date DATE NOT NULL,
    equipment_price DECIMAL(10, 2) NOT NULL,
    equipment_rentalPrice DECIMAL(10, 2) NOT NULL,
    PRIMARY KEY (equipment_id)
);

-- Create the sale table
CREATE TABLE sale (
    sale_id INT NOT NULL AUTO_INCREMENT,
    sale_type VARCHAR(80) NOT NULL,
    equipment_id INT NOT NULL,
    customer_id INT NOT NULL,
    PRIMARY KEY (sale_id),
    FOREIGN KEY (equipment_id) REFERENCES equipment (equipment_id),
    FOREIGN KEY (customer_id) REFERENCES customer (customer_id)
);


-- insert customer records
INSERT INTO customer(customer_name, customer_email, customer_address)
    VALUES('Lina Smith', 'linaS@gmail.com', '123 Reems Rd');

INSERT INTO customer(customer_name, customer_email, customer_address)
    VALUES('Ron Brown', 'ronB@gmail.com', '676 boat Rd');

INSERT INTO customer(customer_name, customer_email, customer_address)
    VALUES('Sarah Wilson', 'sarahW@gmail.com', '321 Oak St');

INSERT INTO customer(customer_name, customer_email, customer_address)
    VALUES('Paul Sarron', 'paulS@gmail.com', '909 Court Rd');

INSERT INTO customer(customer_name, customer_email, customer_address)
    VALUES('Sophia Bella', 'sophiaB@gmail.com', '877 Cedar Rd');

INSERT INTO customer(customer_name, customer_email, customer_address)
    VALUES('John Radlen', 'johnR@gmail.com', '777 Pino St');

-- insert employee records
INSERT INTO employee(employee_name, employee_role)
    VALUES('John Mac MacNell', 'Guide');

INSERT INTO employee(employee_name, employee_role)
    VALUES('D.B. Duke Marland', 'Guide');

INSERT INTO employee(employee_name, employee_role)
    VALUES('Anita Gallegos', 'Marketing Personnel');

INSERT INTO employee(employee_name, employee_role)
    VALUES('Dimitrios Stravopolous', 'Supply Manager');

-- insert trip records
INSERT INTO trip(trip_destination, start_date, end_date, employee_id) 
    VALUES('Africa', '2023-08-01', '2023-08-10', 1);

INSERT INTO trip(trip_destination, start_date, end_date, employee_id) 
    VALUES('Asia', '2023-09-15', '2023-09-25', 1);

INSERT INTO trip(trip_destination, start_date, end_date, employee_id) 
    VALUES('Southern Europe', '2023-08-03', '2023-08-12', 2);

INSERT INTO trip(trip_destination, start_date, end_date, employee_id) 
    VALUES('Africa', '2023-09-01', '2023-09-10', 2);

INSERT INTO trip(trip_destination, start_date, end_date, employee_id) 
    VALUES('Southern Europe', '2023-10-02', '2023-10-11', 1);

INSERT INTO trip(trip_destination, start_date, end_date, employee_id) 
    VALUES('Asia', '2023-09-18', '2023-09-26', 2);

INSERT INTO trip(trip_destination, start_date, end_date, employee_id) 
    VALUES('Africa', '2023-10-20', '2023-10-29', 2);

INSERT INTO trip(trip_destination, start_date, end_date, employee_id) 
    VALUES('Southern Europe', '2023-11-02', '2023-11-10', 1);

-- insert booking records
INSERT INTO booking(customer_id, trip_id) 
    VALUES(4, 1);

INSERT INTO booking(customer_id, trip_id) 
    VALUES(1, 1);

INSERT INTO booking(customer_id, trip_id) 
    VALUES(5, 4);

INSERT INTO booking(customer_id, trip_id) 
    VALUES(6, 6);

INSERT INTO booking(customer_id, trip_id) 
    VALUES(3, 1);

INSERT INTO booking(customer_id, trip_id) 
    VALUES(1, 5);

INSERT INTO booking(customer_id, trip_id) 
    VALUES(3, 2);

INSERT INTO booking(customer_id, trip_id) 
    VALUES(2, 1);

INSERT INTO booking(customer_id, trip_id) 
    VALUES(2, 5);

INSERT INTO booking(customer_id, trip_id) 
    VALUES(4, 4);

INSERT INTO booking(customer_id, trip_id) 
    VALUES(4, 7);

INSERT INTO booking(customer_id, trip_id) 
    VALUES(5, 8);

INSERT INTO booking(customer_id, trip_id) 
    VALUES(6, 8);

-- insert equipment records
INSERT INTO equipment(equipment_name, equipment_type, purchase_date, equipment_price, equipment_rentalPrice) 
    VALUES('Hiking Boots', 'Hiking Gear', '2021-05-05', 120, 12);

INSERT INTO equipment(equipment_name, equipment_type, purchase_date, equipment_price, equipment_rentalPrice) 
    VALUES('Tent', 'Camping Gear', '2016-01-01', 120, 15);

INSERT INTO equipment(equipment_name, equipment_type, purchase_date, equipment_price, equipment_rentalPrice) 
    VALUES('Headlamp', 'Lighting', '2023-04-01', 38, 5);

INSERT INTO equipment(equipment_name, equipment_type, purchase_date, equipment_price, equipment_rentalPrice) 
    VALUES('Tent', 'Camping Gear', '2022-12-09', 120, 15);

INSERT INTO equipment(equipment_name, equipment_type, purchase_date, equipment_price, equipment_rentalPrice) 
    VALUES('Backpack', 'Camping Gear', '2017-01-30', 80, 15);

INSERT INTO equipment(equipment_name, equipment_type, purchase_date, equipment_price, equipment_rentalPrice) 
    VALUES('Sleeping Pad', 'Camping Gear', '2023-01-08', 42, 10);

INSERT INTO equipment(equipment_name, equipment_type, purchase_date, equipment_price, equipment_rentalPrice) 
    VALUES('Hiking Hat', 'Hiking Gear', '2023-07-01', 20, 5);

INSERT INTO equipment(equipment_name, equipment_type, purchase_date, equipment_price, equipment_rentalPrice) 
    VALUES('Sleeping Pad', 'Camping Gear', '2017-11-16', 42, 10);

INSERT INTO equipment(equipment_name, equipment_type, purchase_date, equipment_price, equipment_rentalPrice) 
    VALUES('Backpack', 'Camping Gear', '2023-01-10', 80, 15);

INSERT INTO equipment(equipment_name, equipment_type, purchase_date, equipment_price, equipment_rentalPrice) 
    VALUES('Hiking Boots', 'Hiking Gear', '2015-05-09', 120, 12);


-- insert sale records
INSERT INTO sale(sale_type, equipment_id, customer_id) 
    VALUES('rent', 3, 4);

INSERT INTO sale(sale_type, equipment_id, customer_id) 
    VALUES('purchased', 3, 3);

INSERT INTO sale(sale_type, equipment_id, customer_id) 
    VALUES('purchased', 6, 1);

INSERT INTO sale(sale_type, equipment_id, customer_id) 
    VALUES('rent', 3, 1);

INSERT INTO sale(sale_type, equipment_id, customer_id) 
    VALUES('purchased', 4, 2);

INSERT INTO sale(sale_type, equipment_id, customer_id) 
    VALUES('rent', 2, 2);

INSERT INTO sale(sale_type, equipment_id, customer_id) 
    VALUES('purchased', 4, 3);

INSERT INTO sale(sale_type, equipment_id, customer_id) 
    VALUES('purchased', 5, 6);

INSERT INTO sale(sale_type, equipment_id, customer_id) 
    VALUES('purchased', 6, 4);

INSERT INTO sale(sale_type, equipment_id, customer_id) 
    VALUES('purchased', 6, 5);

INSERT INTO sale(sale_type, equipment_id, customer_id) 
    VALUES('purchased', 1, 1);

INSERT INTO sale(sale_type, equipment_id, customer_id) 
    VALUES('rent', 2, 5);

INSERT INTO sale(sale_type, equipment_id, customer_id) 
    VALUES('rent', 1, 5);

INSERT INTO sale(sale_type, equipment_id, customer_id) 
    VALUES('purchased', 2, 1);

INSERT INTO sale(sale_type, equipment_id, customer_id) 
    VALUES('purchased', 6, 2);

INSERT INTO sale(sale_type, equipment_id, customer_id) 
    VALUES('purchased', 3, 6);



