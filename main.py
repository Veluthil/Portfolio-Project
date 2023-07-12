from flask import render_template, redirect, url_for, flash, request
from flask_bootstrap import Bootstrap5
from flask import Flask
from flask_mail import Mail, Message
import os
from dotenv import load_dotenv
import bleach

# DOTENV
load_dotenv("D:/Programming/PythonEnV/.env.txt")
MY_EMAIL = os.getenv("EC_YOUR_EMAIL")

app = Flask(__name__)
app.secret_key = os.getenv("SECRET_KEY")
bootstrap = Bootstrap5(app)

app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.getenv("EC_YOUR_EMAIL")
app.config['MAIL_PASSWORD'] = os.getenv("PORTFOLIO_SECRET_KEY")
app.config['MAIL_DEFAULT_SENDER'] = os.getenv("EC_YOUR_EMAIL")

mail = Mail(app)


# SANITIZING HTML
def strip_invalid_html(content):
    allowed_tags = ['a', 'abbr', 'acronym', 'address', 'b', 'br', 'div', 'dl', 'dt',
                    'em', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'hr', 'i', 'img',
                    'li', 'ol', 'p', 'pre', 'q', 's', 'small', 'strike',
                    'span', 'sub', 'sup', 'table', 'tbody', 'td', 'tfoot', 'th',
                    'thead', 'tr', 'tt', 'u', 'ul']
    allowed_attrs = {
        'a': ['href', 'target', 'title'],
        'img': ['src', 'alt', 'width', 'height'],
    }
    cleaned = bleach.clean(content,
                           tags=allowed_tags,
                           attributes=allowed_attrs,
                           strip=True)
    return cleaned


@app.route("/")
def home():
    main_page = True
    return render_template("index.html", main_page=main_page)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/projects")
def projects():
    return render_template("projects.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        if data["name"] and data["email"] and data["message"] != "":
            send_mail(strip_invalid_html(data["name"]),
                      strip_invalid_html(data["email"]),
                      strip_invalid_html(data["phone"]),
                      strip_invalid_html(data["message"]))
        else:
            flash("You can't send a message without filling name, email and message fields.")
            return redirect(url_for("contact", msg_sent=False))
        return render_template("contact.html", msg_sent=True)
    return render_template("contact.html", msg_sent=False)


def send_mail(name, email, phone, message):
    recipients = [MY_EMAIL]
    content = Message('Portfolio Mail', recipients=recipients)
    content.body = f"Name: {name}\nEmail: {email}\nPhone: {phone}\nMessage: {message}"
    mail.send(content)
    return 'Email sent'


if __name__ == "__main__":
    app.run(debug=True)
