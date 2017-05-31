# -*- coding: utf-8 -*-
import logging
from threading import Thread
from queue import Queue

from app.client import GMTechWebSocket
from app.utils import retry, _print, QueueFullException
from kiteconnect import KiteConnect

# Dummy Keys
from websocket import WebSocketException, WebSocketConnectionClosedException
#
# api_key = "abcd51hdgns"  # API KEY
# user_id = "DR1234"  # USER ID
# public_token = "asljfldlncnl093nnnzc4"  # PUBLIC TOKEN

api_key = "qxlf7e2xdrtkdbk3"  # API KEY
user_id = "ZT6579"  # USER ID
public_token = "btdtrkgobwbyc70u5l59k2v1rjvzanim"  # PUBLIC TOKEN

API_KEY = ''
kite = KiteConnect(api_key=API_KEY)

o_instr = [738561, 5633]
instruments = [53397255, 53426439, 53427463, 53426951, 53329415, 53405959]

logging.basicConfig(
    level=logging.DEBUG,
    format='(%(threadName)-10s) %(message)s',
)
logging.getLogger('websocket').setLevel(logging.DEBUG)

LOG = logging.getLogger(__name__)


class ZerodhaWorker(Thread):
    """"
    """
    __queue = Queue()
    __client_socket = None
    __run_status = False

    def __init__(self, args=(), kwargs=None):
        """

        :param group:
        :param target:
        :param name:
        :param args:
        :param kwargs:
        :param daemon:
        """
        Thread.__init__(self)
        self.__args = args
        self.__kwargs = kwargs

        if not self.__client_socket:
            self.__run_status = self.__start_connection()

    def add_instruments(self, instrument_list):
        """
        Add a List of Instruments into the Queue
        :param instrument_list:
        :return:
        """
        if not self.__queue.full():
            self.__queue.put(instrument_list)
        else:
            raise QueueFullException

    def clear_instruments(cls):
        """

        :return:
        """
        while not cls.__queue.empty():
            cls.__queue.get()
        # print(cls.__queue.empty())
        return True


    @retry(3, exc_type=WebSocketConnectionClosedException)
    @retry(3, exc_type=Exception)
    def run(self):

        # Callback for tick reception.
        def on_close(ws):
            # logging.debug("closed connection")
            ws.reconnect()

        # Callback for tick reception.
        def on_tick(tick, ws):
            _print(tick)

        # Callback for successful connection.
        def on_connect(ws):
            while self.__queue and not self.__queue.empty():
                _instruments = self.__queue.get()
                _print("Adding Instruments - " + str(_instruments))
                # Subscribe to a list of instrument_tokens (RELIANCE and ACC here).
                ws.subscribe(_instruments)
                # Set instruments to tick in `full` mode.
                ws.set_mode(ws.MODE_LTP, _instruments)

        # Assign the callbacks.
        self.__client_socket.on_close = on_close
        self.__client_socket.on_tick = on_tick
        self.__client_socket.on_connect = on_connect

        # while True:
        self.__client_socket.connect(threaded=True)

    @retry(count=10, exc_type=WebSocketException)
    def __start_connection(self):
        """

        :return:
        """
        # Initialise.
        status = False
        try:
            self.__client_socket = GMTechWebSocket(api_key, public_token, user_id)
            status = True
        except WebSocketException as e:
            LOG.error("start_connection - %s" % str(e))
            raise e

        return status

#
# zc = ZerodhaWorker()
# zc.setName("zc")
# zc.run()
