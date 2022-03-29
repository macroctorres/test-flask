from flask import Blueprint, render_template, request, redirect, url_for, flash

contacts = Blueprint('contacts', __name__)


@contacts.route("/")
def home():
    return render_template("index.html")

# save a contact
@contacts.route("/new")
def add_contact():
    return "save a contact"

#about page
@contacts.route("/about")
def about():
    return render_template("about.html")

#update a contact
@contacts.route("/update")
def update_contact():
    return "update a contact"

#delete a contact
@contacts.route("/delete")
def delete_contact():
    return "delete a contact"