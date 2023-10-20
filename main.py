from flask import Flask, render_template, request, flash
from forms import ContactForm

from flask_mail import Mail, Message
app = Flask(__name__)

app.secret_key = '3F14FDD675261'

mail = Mail()
app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 465
app.config["MAIL_USERNAME"] = "example@gmail.com"
app.config["MAIL_PASSWORD"] = "your-password"
app.config["MAIL_USE_SSL"] = True
mail.init_app(app)


@app.route("/")
def home():
    return render_template("home.html", active="home")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    form = ContactForm()

    if request.method == "POST":
        if form.validate() is False:
            flash("All fields are required.")
            return render_template("contact.html", active="contact", form=form)
        else:
            msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
            msg.body = """ 
            From: %s <%s> 
            %s 
            """ % (form.name.data, form.email.data, form.message.data)
            mail.send(msg)
            return render_template('contact.html', success=True)

    return render_template("contact.html", active="contact", form=form)


@app.route("/projects")
def projects():
    return render_template("projects.html", active="projects")


if __name__ == "__main__":
    app.run(debug=True)
