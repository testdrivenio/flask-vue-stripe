import json
import os
import uuid

import stripe
from flask import Flask, jsonify, request
from flask_cors import CORS


BOOKS = [
    {
        'id': uuid.uuid4().hex,
        'title': 'On the Road',
        'author': 'Jack Kerouac',
        'read': True,
        'price': '19.99'
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Harry Potter and the Philosopher\'s Stone',
        'author': 'J. K. Rowling',
        'read': False,
        'price': '9.99'
    },
    {
        'id': uuid.uuid4().hex,
        'title': 'Green Eggs and Ham',
        'author': 'Dr. Seuss',
        'read': True,
        'price': '3.99'
    }
]

# instantiate the app
app = Flask(__name__)
app.config.from_object(__name__)

# configure stripe
stripe_keys = {
    'secret_key': os.environ['STRIPE_SECRET_KEY'],
    'publishable_key': os.environ['STRIPE_PUBLISHABLE_KEY'],
}

stripe.api_key = stripe_keys['secret_key']

# enable CORS
CORS(app, resources={r'/*': {'origins': '*'}})


def remove_book(book_id):
    for book in BOOKS:
        if book['id'] == book_id:
            BOOKS.remove(book)
            return True
    return False


# sanity check route
@app.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')


@app.route('/config')
def get_publishable_key():
    stripe_config = {'publicKey': stripe_keys['publishable_key']}
    return jsonify(stripe_config)


@app.route('/create-checkout-session', methods=['POST'])
def create_checkout_session():
    domain_url = 'http://localhost:5173'

    try:
        data = json.loads(request.data)

        # get book
        book_to_purchase = ''
        for book in BOOKS:
            if book['id'] == data['book_id']:
                book_to_purchase = book

        # create new checkout session
        checkout_session = stripe.checkout.Session.create(
            success_url=domain_url +
            '/success?session_id={CHECKOUT_SESSION_ID}',
            cancel_url=domain_url + '/canceled',
            payment_method_types=['card'],
            mode='payment',
            line_items=[
                {
                    'name': book_to_purchase['title'],
                    'quantity': 1,
                    'currency': 'usd',
                    'amount': round(float(book_to_purchase['price']) * 100),
                }
            ]
        )

        return jsonify({'sessionId': checkout_session['id']})
    except Exception as e:
        return jsonify(error=str(e)), 403


@app.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {'status': 'success'}
    if request.method == 'POST':
        post_data = request.get_json()
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read'),
            'price': post_data.get('price')
        })
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = BOOKS
    return jsonify(response_object)


@app.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {'status': 'success'}
    if request.method == 'PUT':
        post_data = request.get_json()
        remove_book(book_id)
        BOOKS.append({
            'id': uuid.uuid4().hex,
            'title': post_data.get('title'),
            'author': post_data.get('author'),
            'read': post_data.get('read'),
            'price': post_data.get('price')
        })
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        remove_book(book_id)
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
