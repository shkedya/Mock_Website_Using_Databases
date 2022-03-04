from flask import Flask, render_template, redirect
from flask_mysqldb import MySQL
from flask import request

# Configuration
app = Flask(__name__)

# database connection - from template
app.config["MYSQL_HOST"] = "classmysql.engr.oregonstate.edu"
app.config["MYSQL_USER"] = "cs340_wiedersp"
app.config["MYSQL_PASSWORD"] = "9567"
app.config["MYSQL_DB"] = "cs340_wiedersp"
app.config["MYSQL_CURSORCLASS"] = "DictCursor"

mysql = MySQL(app)


# Homepage
@app.route('/index.html')
@app.route('/')
def root():
    return render_template("/index.j2")

# Customers Page
@app.route('/customer.html', methods=["POST", "GET"])
def customers():
    """ 
    Read, and Create functionality for Customers page.
    """
    # Add a Customer to the database 
    if request.method == "POST":                    
        if request.form.get("insert_customer_submit"):
            Name = request.form["Name"]
            Phone_number = request.form["Phone_number"]
            Badges = request.form["Badges"]
            Gender = request.form["Gender"]

            #Insert new values into Customer Table
            query = "INSERT INTO Customers (Name, Phone_number, Badges, Gender) VALUES (%s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (Name, Phone_number, Badges, Gender))
            mysql.connection.commit()

            # redirect back to customer page
            return redirect("/customer.html")

    # Get Customer data from Customer Table
    if request.method == "GET":
        # Query to populate table
        query_table = "SELECT * FROM Customers"
        cur = mysql.connection.cursor()
        cur.execute(query_table)
        customer_table = cur.fetchall()

        # Render the Customers page with the fetched data
        return render_template("customers.j2", customer_data = customer_table)
    
# Items table
@app.route('/items.html', methods=["POST", "GET"])
def items():
    """ 
    Read, and Create functionality for Customers page.
    """
    # Add an Item to the database 
    if request.method == "POST":                    
        if request.form.get("insert_item_submit"):
            price = request.form["price"]
            description = request.form["description"]
            badges_req = request.form["badges_req"]

            #Insert new values into Items Table
            query = "INSERT INTO Items (price, description, badges_req) VALUES (%s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (price, description, badges_req))
            mysql.connection.commit()

            # redirect back to items page
            return redirect("/items.html")

    # Get Item data from Items Table
    if request.method == "GET":
        # Query to populate table
        query_table = "SELECT * FROM Items"
        cur = mysql.connection.cursor()
        cur.execute(query_table)
        item_table = cur.fetchall()

        # Render the Products page with the fetched data
        return render_template("items.j2", item_data = item_table)
    
# Orders Page
@app.route('/orders.html', methods=["POST", "GET"])
def customers():
    """ 
    Read, and Create functionality for Orders page.
    """
    # Add a order to the database 
    if request.method == "POST":                    
        if request.form.get("insert_item_submit"):
            customer_id = request.form["customer_id"]
            item_id = request.form["item_id"]
            quantity = request.form["quantity"]
            date = request.form["date"]
            total = request.form["total"]

            #Insert new values into Customer Table
            query = "INSERT INTO Orders (customer_id, item_id, quantity, date, total) VALUES (%s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (customer_id, item_id, quantity, date, total))
            mysql.connection.commit()

            # redirect back to customer page
            return redirect("/items.html")

    # Get Order data from Orders Table
    if request.method == "GET":
        # Query to populate table
        query_table = "SELECT * FROM Items"
        cur = mysql.connection.cursor()
        cur.execute(query_table)
        customer_table = cur.fetchall()

        # Render the Order page with the fetched data
        return render_template("items.j2", item_data = item_table)