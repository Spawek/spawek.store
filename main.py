from flask import Flask, render_template, request, redirect, url_for, session, request
from data import BOOKS
import uuid

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
    return render_template('home.html', books=BOOKS, cart=get_cart())

@app.route('/product/<gtin>')
def product(gtin):
    return render_template('product.html', books=[book for book in BOOKS if book['gtin'] == gtin], cart=get_cart())

@app.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    add_book_to_cart(request.form['gtin'])
    return redirect(url_for('home'))

@app.route('/cart')
def cart():
    cart = get_cart()
    return render_template('cart.html', books=[book for book in BOOKS if book['gtin'] in cart], cart=cart)

@app.route('/order')
def order():
    cart = get_cart()
    clear_cart()
    books = [book for book in BOOKS if book['gtin'] in cart]
    transaction_value = 0
    for book in books:
        transaction_value += book["price_float"]
    return render_template('order.html', books=books, cart=cart, transaction_value=transaction_value, transaction_id=str(uuid.uuid4()))

@app.route('/sitemap.xml')
def sitemap():
    sites = [""]  # home page
    for book in BOOKS:
        sites.append(f"product/{book['gtin']}")
    return render_template('sitemap.xml', sites=sites)

# Google Merchant Center feed
@app.route('/mc_feed.txt')
def mc_feed():
    products = []
    for book in BOOKS:
        p = book # covers "title", "description", "author", "cost_of_goods_sold", "price", "gtin" 
        p.pop("price_float", None)
        p['id'] = p['gtin']
        p['availability'] = 'in_stock'
        p['condition'] = 'new'
        p['google_product_category'] = 'Media > Books'
        p['product_type'] = 'Books'
        p['auto_pricing_min_price'] = p['cost_of_goods_sold']
        p['link'] = "https://spawek.store" + url_for('product', gtin=p['gtin'])
        p['image_link'] = "https://spawek.store" + url_for('static', filename=f'images/{p["gtin"]}.jpg')
        products.append(p)

    columns = products[0].keys()
    feed = "\t".join(columns) + "\n"

    for p in products:
        feed += "\t".join([p[col] for col in columns]) + "\n"

    return render_template('mc_feed.txt', feed=feed)

if __name__ == '__main__':
    app.run(debug=True)

# TODO: google ads

# TODO: configure 3 conversions in AW:
#       - AW
#       - GA4
#       - GTM -> GA

# TODO: support for automated discounts

# TODO: log events is db?