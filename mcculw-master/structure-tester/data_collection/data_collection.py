from mcculw import ul
from mcculw.enums import ULRange
from mcculw.ul import ULError
from mcculw.enums import DigitalIODirection as Diod  # Import interfacing libraries
from mcculw.device_info import DaqDeviceInfo as Ddi
from mcculw.enums import DigitalPortType as Dpt
# Import interfacing libraries

# set range from -10v > +10v
ai_range = ULRange.BIP10VOLTS
# create memory buffer
mem = ul.win_buf_alloc(1000)
# scan channel 0 > 1
ul.a_in_scan(0, 1, 2, 100, 100, ai_range, mem, 0)
print(mem)

