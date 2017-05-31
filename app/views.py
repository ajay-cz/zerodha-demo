# -*- coding: utf-8 -*-
from queue import Queue

from app.utils import fetch_ltp_results
from app.zerodha import ZerodhaWorker
from flask import Flask, render_template

DB_HOST = 'ayshar.com'
DB_NAME = 'trading1'
DB_USER = 'tradeuser2'
DB_PWD = 'tradeuser2'

# DB_HOST = 'localhost'
# DB_NAME = 'zerodhaquotesdb'
# DB_USER = 'root'
# DB_PWD = ''

# Flask app
app = Flask(__name__)
app.config.from_object(__name__)
app.debug = True

truthy = frozenset(('t', 'true', 'y', 'yes', 'on', '1'))


q = Queue(maxsize=200)

def asbool(s):
    """ Return the boolean value ``True`` if the case-lowered value of string
    input ``s`` is any of ``t``, ``true``, ``y``, ``on``, or ``1``, otherwise
    return the boolean value ``False``.  If ``s`` is the value ``None``,
    return ``False``.  If ``s`` is already one of the boolean values ``True``
    or ``False``, return it."""
    if s is None:
        return False
    if isinstance(s, bool):
        return s
    s = str(s).strip()
    return s.lower() in truthy


@app.route('/')
def home_page():
    """
    View Controller for the Home Page
    :return:
    """
    return "<h4>Welcome !</h4><br><a href='/fetch'>View Results</a>"


@app.route('/add/<instrument_token>')
def add_instrument(instrument_token):
    """

    :return:
    """
    if instrument_token:
        # q.put()
        zc = ZerodhaWorker()
        zc.add_instruments([int(i) for i in instrument_token.split(',')])
        # zc.setName("zc")
        # zc.setDaemon(False)
        zc.start()
        return "Added the following instruments - %s . <br><a href='/fetch'>View Results</a>" % instrument_token

    return "Invalid"


@app.route('/fetch')
def fetch_data():
    """

    :return:
    """
    return render_template('listing.html', listings=fetch_ltp_results())
