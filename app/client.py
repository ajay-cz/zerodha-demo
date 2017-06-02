# -*- coding: utf-8 -*-
import datetime as dt
import json

from app.utils import insert_into_ltp_table, print_message
from kiteconnect import WebSocket
import timeit
import threading
import arrow


class GMTechWebSocket(WebSocket):
    """

    """

    def __init__(self, api_key, public_token, user_id, root=None):
        """

        :param api_key:
        :param public_token:
        :param user_id:
        :param root:
        """
        self.__call_time = arrow.utcnow().float_timestamp
        self._gm_name = self.__call_time
        WebSocket.__init__(self, api_key, public_token, user_id, root)


    def _parse_binary(self, bin):
        """Parse binary data to a (list of) ticks structure."""
        packets = self._split_packets(bin)  # split data to individual ticks packet
        data = []
        print_message("_parse_binary ")
        for packet in packets:
            instrument_token = self._unpack_int(packet, 0, 4)
            segment = instrument_token & 0xff  # Retrive segment constant from instrument_token

            divisor = 10000000.0 if segment == self.EXCHANGE_MAP["cds"] else 100.0
            _stream_data = {}
            # Parse index packets.
            if segment in self.INDICES:
                d = {}
                if len(packet) == 8:
                    _stream_data = {
                        "tradeable": False,
                        "mode": self.MODE_LTP,
                        "instrument_token": instrument_token,
                        "last_price": self._unpack_int(packet, 4, 8) / divisor
                    }
                    self.__insert_into_db(self.MODE_LTP, _stream_data)
                    data.append(_stream_data)
                elif len(packet) == 28:
                    _stream_data = {
                        "tradeable": False,
                        "mode": self.MODE_QUOTE,
                        "instrument_token": instrument_token,
                        "last_price": self._unpack_int(packet, 4, 8) / divisor,
                        "ohlc": {
                            "high": self._unpack_int(packet, 8, 12) / divisor,
                            "low": self._unpack_int(packet, 12, 16) / divisor,
                            "open": self._unpack_int(packet, 16, 20) / divisor,
                            "close": self._unpack_int(packet, 20, 24) / divisor
                        },
                        "change": self._unpack_int(packet, 24, 28) / divisor,
                    }
                    self.__insert_into_db(self.MODE_QUOTE, _stream_data)
                    data.append(_stream_data)

                continue

            # Parse non-index packets.
            if len(packet) == 8:
                _stream_data = {
                    "tradeable": True,
                    "mode": self.MODE_LTP,
                    "instrument_token": instrument_token,
                    "last_price": self._unpack_int(packet, 4, 8) / divisor
                }
                self.__insert_into_db(self.MODE_LTP, _stream_data)
                data.append(_stream_data)
            elif len(packet) > 8:
                d = {
                    "tradeable": True,
                    "mode": self.MODE_QUOTE,
                    "instrument_token": instrument_token,
                    "last_price": self._unpack_int(packet, 4, 8) / divisor,
                    "last_quantity": self._unpack_int(packet, 8, 12),
                    "average_price": self._unpack_int(packet, 12, 16) / divisor,
                    "volume": self._unpack_int(packet, 16, 20),
                    "buy_quantity": self._unpack_int(packet, 20, 24),
                    "sell_quantity": self._unpack_int(packet, 24, 28),
                    "ohlc": {
                        "open": self._unpack_int(packet, 28, 32) / divisor,
                        "high": self._unpack_int(packet, 32, 36) / divisor,
                        "low": self._unpack_int(packet, 36, 40) / divisor,
                        "close": self._unpack_int(packet, 40, 44) / divisor
                    }
                }

                # Compute the change price.
                d["change"] = 0
                if (d["ohlc"]["close"] != 0):
                    d["change"] = (d["last_price"] - d["ohlc"]["close"]) * 100 / d["ohlc"]["close"]

                # Market depth entries.
                depth = {
                    "buy": [],
                    "sell": []
                }

                if len(packet) > 44:
                    # Compile the market depth lists.
                    for i, p in enumerate(range(44, len(packet), 12)):
                        depth["sell" if i >= 5 else "buy"].append({
                            "quantity": self._unpack_int(packet, p, p + 4),
                            "price": self._unpack_int(packet, p + 4, p + 8) / divisor,
                            # Byte format is unsigned short for orders field
                            "orders": self._unpack_int(packet, p + 8, p + 10, byte_format="H")
                        })

                d["depth"] = depth
                self.__insert_into_db(self.MODE_QUOTE, d)
                data.append(d)

        return data

    def __insert_into_db(self, mode, data):
        """

        :return:
        """
        if mode == self.MODE_LTP:
            print_message("Received Tick %s - %s at %f" % (mode, data, arrow.utcnow().float_timestamp))
            db_thread = threading.Thread(name='insert_into_ltp_table_thread', target=insert_into_ltp_table, args=(self.__call_time, arrow.utcnow().float_timestamp, data,), daemon=True).start()
            # db_thread.daemon = True
            # db_thread.start()
        else:
            pass