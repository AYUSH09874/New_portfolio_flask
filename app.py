from flask import Flask, render_template, request, flash, redirect, url_for
import smtplib
from email.mime.text import MIMEText

app = Flask(__name__)
app.secret_key = 'supersecretkey'

SENDER_EMAIL = "opayush.osm@gmail.com"
SENDER_PASSWORD = "hfly xmls kfsa zxes"  # Use app password here
RECEIVER_EMAIL = "opayush.osm@gmail.com"

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']

        subject = f"Portfolio Contact - {name}"
        body = f"Name: {name}\nEmail: {email}\nMessage:\n{message}"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = SENDER_EMAIL
        msg['To'] = RECEIVER_EMAIL

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(SENDER_EMAIL, SENDER_PASSWORD)
                smtp.send_message(msg)

            flash('Thanks! Your message has been sent.')
        except Exception as e:
            flash('Oops, something went wrong.')
            print("Error sending email:", e)

        return redirect(url_for('index'))

    return render_template('index.html')

# ✅ This part is required to run it
if __name__ == '__main__':
    app.run(debug=True)
