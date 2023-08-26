from flask import Flask, render_template, request, redirect, url_for, flash, session, send_from_directory, request, g
from data import EBOOKS

app = Flask(__name__)
app.secret_key = 'mysecretkey_32meokfwerewlkewqjoi'

def get_cart():
    return set(session.get('cart', []))

def add_book_to_cart(gtin):
    cart = get_cart()
    cart.add(gtin)
    cart = list(cart)
    session['cart'] = cart

def clear_cart():
    session['cart'] = []

@app.route('/')
def home():
    return render_template('home.html', ebooks=EBOOKS, cart=get_cart())

@app.route('/product/<gtin>')
def product(gtin):
    return render_template('product.html', ebooks=[book for book in EBOOKS if book['gtin'] == gtin], cart=get_cart())

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    add_book_to_cart(request.form['gtin'])
    return redirect(url_for('home'))

@app.route('/cart')
def cart():
    cart = get_cart()
    return render_template('cart.html', ebooks=[book for book in EBOOKS if book['gtin'] in cart], cart=cart)

@app.route('/order')
def order():
    cart = get_cart()
    clear_cart()
    return render_template('order.html', ebooks=[book for book in EBOOKS if book['gtin'] in cart], cart=cart)

if __name__ == '__main__':
    app.run(debug=True)

# TODO: add templates etc
# TODO: release website
# TODO: create MC account

# TODO: log events
# TODO: sitemap
# TODO: advertise in CH only, so it's easier to use
# TODO: ask team to use their advertising budget as well? - attribution may be a problem then
# TODO: product page is needed to upload to MC