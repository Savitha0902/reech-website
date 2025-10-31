from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mail import Mail, Message

app = Flask(__name__)
app.secret_key = "reech_secret_key"

# ------------------ Email Config ------------------
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
import os

app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')
app.config['MAIL_DEFAULT_SENDER'] = ('REECH Website', os.environ.get('MAIL_USERNAME'))


mail = Mail(app)

# ------------------ Routes ------------------

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('product.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        msg = Message(
            subject=f"New Message from {name}",
            recipients=['reechsoapworks24@gmail.comm'],  # 🔹 where you’ll receive messages
            body=f"Name: {name}\nEmail: {email}\n\nMessage:\n{message}"
        )
        mail.send(msg)

        flash('Your message has been sent successfully! 💌')
        return redirect(url_for('contact'))

    return render_template('contact.html')


if __name__ == "__main__":
    app.run(debug=True)
