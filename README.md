# Accepting Payments with Stripe, Vue.js, and Flask

### Want to learn how to build this?

Check out the [tutorial](https://testdriven.io/blog/accepting-payments-with-stripe-vuejs-and-flask/).

## Want to use this project?

1. Fork/Clone

1. Sign up for [Stripe](https://stripe.com/) (if you don't already have an account).

1. Set the Stripe [keys](https://stripe.com/docs/keys) as environment variables:

    ```sh
    $ cd server
    $ export STRIPE_PUBLISHABLE_KEY=<YOUR_STRIPE_PUBLISHABLE_KEY>
    $ export STRIPE_SECRET_KEY=<YOUR_STRIPE_SECRET_KEY>
    ```

1. Run the server-side Flask app in one terminal window:

    ```sh
    $ cd server
    $ python3 -m venv env
    $ source env/bin/activate
    (env)$ pip install -r requirements.txt
    (env)$ flask run --port=5001 --debug
    ```

    Navigate to [http://localhost:5001/ping](http://localhost:5001/ping)

1. Run the client-side Vue app in a different terminal window:

    ```sh
    $ cd client
    $ npm install
    $ npm run dev
    ```

    Navigate to [http://localhost:5173](http://localhost:5173)
