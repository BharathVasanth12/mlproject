from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "supersecretkey"  # needed for flash messages

# Homepage
@app.route("/")
def home():
    return render_template("homepage.html")

# Form page
@app.route("/form", methods=["GET", "POST"])
def form():
    if request.method == "POST":
        # Collect form data
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        age = request.form.get("age")

        # Validation for required fields
        if not first_name or not last_name or not age:
            flash("❌ First Name, Last Name, and Age are required fields!", "error")
            return redirect(url_for("form"))

        # If validation passes → go to confirmation page
        return redirect(url_for("confirmation"))

    return render_template("form.html")

# Confirmation page
@app.route("/confirmation")
def confirmation():
    return render_template("confirmation.html")



if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
