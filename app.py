from flask import Flask, render_template, redirect, flash
from flask_mysqldb import MySQL
from flask import request
import datetime

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
@app.route('/customers.html', methods=["POST", "GET"])
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

            # Insert new values into Customer Table
            query = "INSERT INTO Customers (Name, Phone_number, Badges, Gender) VALUES (%s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (Name, Phone_number, Badges, Gender))
            mysql.connection.commit()

            # redirect back to customer page
            return redirect("/customers.html")

    # Get Customer data from Customer Table
    if request.method == "GET":
        # Query to populate table
        query_table = "SELECT * FROM Customers"
        cur = mysql.connection.cursor()
        cur.execute(query_table)
        customer_table = cur.fetchall()

        # Render the Customers page with the fetched data
        return render_template("customers.j2", customer_data = customer_table)


# Delete customer based on ID
@app.route('/delete-customer/<int:id>')
def delete_customer(id):
    cur = mysql.connection.cursor()
    query = "DELETE FROM Customers WHERE Customer_id =%s"
    cur.execute(query, (id,))
    mysql.connection.commit()
    flash("User deleted successfully")
    return redirect("/customers.html")


# Delete item based on ID
@app.route('/delete-item/<int:id>')
def delete_item(id):
    cur = mysql.connection.cursor()
    query = "DELETE FROM Items WHERE Item_id =%s"
    cur.execute(query, (id,))
    mysql.connection.commit()
    flash("Item deleted successfully")
    return redirect("/items.html")

    
# Items table
@app.route('/items.html', methods=["POST", "GET"])
def items():
    """ 
    Read, and Create functionality for Customers page.
    """
    # Add an Item to the database 
    if request.method == "POST":                    
        if request.form.get("insert_item_submit"):
            Price = request.form["Price"]
            Description = request.form["Description"]
            Badge_required = request.form["Badge_required"]

            # Insert new values into Items Table
            query = "INSERT INTO Items (Price, Description, Badge_required) VALUES (%s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (Price, Description, Badge_required))
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

        # Render the items page with the fetched data
        return render_template("items.j2", item_data=item_table)


# Orders Page
@app.route('/orders.html', methods=["POST", "GET"])
def orders():
    """ 
    Read, and Create functionality for Orders page.
    """
    # Add a order to the database 
    if request.method == "POST":                    
        if request.form.get("insert_order_submit"):
            Customer_id = request.form["Customer_id"]
            Item_id = request.form["Item_id"]
            Quantity = request.form["Quantity"]
            Date = datetime.datetime.utcnow()
            Total = request.form["Total"]

            # Insert new values into Customer Table
            query = "INSERT INTO Orders (Customer_id, Item_id, Quantity, Date, Total) VALUES (%s, %s, %s, %s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (Customer_id, Item_id, Quantity, Date, Total))
            mysql.connection.commit()

            # redirect back to orders page
            return redirect("/orders.html")

    # Get Order data from Orders Table
    if request.method == "GET":
        # Query to populate table
        query_table = "SELECT * FROM Orders"
        cur = mysql.connection.cursor()
        cur.execute(query_table)
        order_table = cur.fetchall()

        # Render the Order page with the fetched data
        return render_template("orders.j2", order_data=order_table)


# Trades Page
@app.route('/trades.html', methods=["POST", "GET"])
def trades():
    """ 
    Read, and Create functionality for Trades page.
    """
    # Add a order to the database 
    if request.method == "POST":                    
        if request.form.get("insert_trade_submit"):
            Sender = request.form["Sender"]
            Receiver = request.form["Receiver"]

            # Insert new values into Customer Table
            query = "INSERT INTO Trades (Sender, Receiver) VALUES (%s, %s)"
            cur = mysql.connection.cursor()
            cur.execute(query, (Sender, Receiver))
            mysql.connection.commit()

            # redirect back to trades page
            return redirect("/trades.html")

    # Get Order data from Trades Table
    if request.method == "GET":
        # Query to populate table
        query_table = "SELECT * FROM Trades"
        cur = mysql.connection.cursor()
        cur.execute(query_table)
        trade_table = cur.fetchall()

        # Render the Order page with the fetched data
        return render_template("trades.j2", trade_data=trade_table)
    

app.secret_key = 'This is a secret'

# Listener
if __name__ == "__main__":
    app.run(host="flip2.engr.oregonstate.edu", debug=True)
