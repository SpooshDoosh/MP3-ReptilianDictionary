import os
from flask import (
    Flask, flash, render_template,
    redirect, request, session, url_for)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from werkzeug.security import generate_password_hash, check_password_hash
if os.path.exists("env.py"):
    import env

app = Flask(__name__)

app.register_error_handler(404, page_not_found)

app.config["MONGO_DBNAME"] = os.environ.get("MONGO_DBNAME")
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")
app.secret_key = os.environ.get("SECRET_KEY")

mongo = PyMongo(app)


@app.route("/")
@app.route("/get_definitions")
def get_definitions():
    definitions = list(mongo.db.definitions.find().sort("word", 1))
    return render_template(
        "definitions.html",
        definitions=definitions,
        )


@app.route("/search", methods=["GET", "POST"])
def search():
    query = request.form.get("query")
    definitions = list(mongo.db.definitions.find(
        {"$text": {"$search": query}}))
    return render_template(
        "definitions.html",
        definitions=definitions
        )


@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        # Checks to see if username is in db already
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            flash("Username taken. Please try again ...")
            return redirect(url_for("register"))

        register = {
            "username": request.form.get("username").lower(),
            "password": generate_password_hash(request.form.get("password"))
        }
        mongo.db.users.insert_one(register)

        # Enters user into new session
        session["user"] = request.form.get("username").lower()
        flash("Successfully registered, welcome to Reptilian Dictionary!")
        return redirect(url_for(
            "profile",
            username=session["user"]
            ))

    return render_template("register.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        # Checks to see if username is in db already
        existing_user = mongo.db.users.find_one(
            {"username": request.form.get("username").lower()})

        if existing_user:
            # Check password hash
            if check_password_hash(
               existing_user["password"], request.form.get("password")):
                session["user"] = request.form.get("username").lower()
                flash("Welcome, {}".format(request.form.get("username")))
                return redirect(url_for(
                    "profile",
                    username=session["user"]
                    ))

            else:
                # Invalid password match
                flash("The username and/or password is incorrect")
                return redirect(url_for("login"))

        else:
            # Username does not exist
            flash("The username and/or password is incorrect")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/profile/<username>", methods=["GET", "POST"])
def profile(username):
    # Grab session user username from database
    username = mongo.db.users.find_one(
        {"username": session["user"]})["username"]
    words = mongo.db.definitions.find_one(
        {"contributor": session["user"]})

    if session["user"]:
        return render_template(
            "profile.html",
            username=username,
            words=words)

    return redirect(url_for("login"))


@app.route("/logout")
def logout():
    # Remove user from session cookies
    flash("You have successfully logged out.")
    session.pop("user")
    return redirect(url_for("login"))


@app.route("/add_word", methods=["GET", "POST"])
def add_word():
    if request.method == "POST":
        definition = {
            "category_name": request.form.get("category_name"),
            "word": request.form.get("word"),
            "word_definition": request.form.get("word_definition"),
            "contributor": session["user"]
        }
        mongo.db.definitions.insert_one(definition)
        flash("Thank you for your conribution! Word successfully added!")
        return redirect(url_for("get_definitions"))

    categories = mongo.db.categories.find().sort("category_name, 1")
    return render_template("add_word.html", categories=categories)


@app.route("/edit_word/<word_id>", methods=["GET", "POST"])
def edit_word(word_id):
    if request.method == "POST":
        definition = {
            "category_name": request.form.get("category_name"),
            "word": request.form.get("word"),
            "word_definition": request.form.get("word_definition"),
            "contributor": session["user"]
        }
        mongo.db.definitions.update_one(
            {"_id": ObjectId(word_id)}, {"$set": definition})
        flash("Word successfully updated!")

    word = mongo.db.definitions.find_one({"_id": ObjectId(word_id)})
    categories = mongo.db.categories.find().sort("category_name, 1")
    return render_template(
        "edit_word.html",
        word=word,
        categories=categories
        )


@app.route("/delete_word/<word_id>")
def delete_word(word_id):
    mongo.db.definitions.remove({"_id": ObjectId(word_id)})
    flash("Word removed successfully")
    return redirect(url_for("get_definitions"))


if __name__ == "__main__":
    app.run(host=os.environ.get("IP"),
            port=int(os.environ.get("PORT")),
            debug=True)
