from mcculw import ul
from mcculw.enums import DigitalIODirection as Diod
from mcculw.enums import DigitalPortType as Dpt
from mcculw.enums import ULRange
from mcculw.enums import AnalogInputMode
# Import libraries

ul.d_config_port(0, Dpt.FIRSTPORTA, Diod.IN)       # Config Stuff
ul.d_config_port(0, Dpt.FIRSTPORTB, Diod.OUT)
ul.d_config_port(1, Dpt.AUXPORT, Diod.OUT)
ul.a_input_mode(1, AnalogInputMode.SINGLE_ENDED)

LoadCell1Raw = ul.a_in(1, 1, ULRange.BIP10VOLTS)    # Channel 1, Port 4
LoadCell2Raw = ul.a_in(1, 9, ULRange.BIP10VOLTS)    # Channel 9, Port 5    Need AGND on ports 3, 6, and 9
LoadCell3Raw = ul.a_in(1, 2, ULRange.BIP10VOLTS)    # Channel 2, Port 7
LoadCell4Raw = ul.a_in(1, 10, ULRange.BIP10VOLTS)   # Channel 10, Port 8

print(LoadCell1Raw)
print(LoadCell2Raw)
print(LoadCell3Raw)
print(LoadCell4Raw)