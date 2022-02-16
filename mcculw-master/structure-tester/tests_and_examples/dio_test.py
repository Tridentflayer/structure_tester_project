from __future__ import absolute_import, division, print_function
from builtins import *  # @UnusedWildImport

from mcculw import ul
from mcculw.enums import DigitalIODirection as diod
from mcculw.device_info import DaqDeviceInfo as ddi

# configure board 0, port 10 (a0) to input
ul.d_config_port(0, 10, diod.IN)
# read input and assign it to x
x = ul.d_bit_in(0, 10, 0)
# print x
print(x)

ul.d_config_port(0, 22, diod.OUT)
ul.d_out(0, 22, 1)
