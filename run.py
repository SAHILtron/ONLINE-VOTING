from flask import Flask, render_template,request,session,url_for,redirect,flash
import sqlite3 as sql
import os
from os.path import join, dirname, realpath
from flask_sqlalchemy import SQLAlchemy


UPLOADS_PATH = join(dirname(realpath(__file__)), 'static\\images')

app = Flask(__name__)
app.config['SECRET_KEY'] = 'super secret key'

A

@app.route("/login")
def login():
    return render_template("login.html")


@app.route("/details")
def login():
    return render_template("details.html")



       
@app.route("/sahil", methods = ["GET","POST"])
def regActio():
    msg=None
    if(request.method=="POST"):
        if (request.form["username"]!="" and request.form["email"]!=""and request.form["password"]!="" ):
            name = request.form["username"]
            email = request.form["email"]
            pasword = request.form["password"] 

            with sql.connect("data.db") as con:
                c=con.cursor()
                c.execute("INSERT INTO  sai(username,email,password) VALUES('"+name+"','"+email+"','"+pasword+"')")
                msg = "Register Details submitted successfully"

                con.commit()
        else:
            msg="Someting went wrong"
        flash("DETAILS SAVED SUCCESSFULLY")
        return render_template("details.html", msg=msg)
        
           
        



        

if __name__ == "__main__":
    app.run(debug=True)