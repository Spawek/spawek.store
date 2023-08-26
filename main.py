from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory, request, g
from data import EBOOKS

app = Flask(__name__)
app.secret_key = 'mysecretkey_32meokfwerewlkewqjoi'

@app.route('/')
def home():
    return render_template('home.html')

if __name__ == '__main__':
    app.run(debug=True)


# TODO: log events
# TODO: sitemap
# TODO: advertise in CH only, so it's easier to use