# -*- coding: utf-8 -*-

import arrow
utc = arrow.utcnow()
print(utc.timestamp)
in_time = utc.to('Asia/Kolkata')
print(in_time)
print(arrow.Arrow.fromtimestamp(utc.float_timestamp).to('Asia/Kolkata'))