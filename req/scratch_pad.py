# -*- coding: utf-8 -*-

import arrow
utc = arrow.utcnow()
print(utc.float_timestamp)
in_time = utc.to('Asia/Kolkata')
print(in_time)
print(arrow.Arrow.utcfromtimestamp(float(1496381356)).to('Asia/Kolkata'))
print(arrow.Arrow.fromtimestamp(float(1496387203 / in_time.microsecond/1e6)).to('Asia/Kolkata'))
print(arrow.Arrow.fromtimestamp(float(1496387203)).microsecond)