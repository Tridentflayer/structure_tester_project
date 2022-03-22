from mcculw import ul
from mcculw.enums import DigitalIODirection as Diod
from mcculw.enums import DigitalPortType as Dpt
from mcculw.enums import ULRange
# Import libraries

# Configure the A set of ports on DIO Board (0-7) as inputs
ul.d_config_port(0, Dpt.FIRSTPORTA, Diod.IN)

# Configure the B set of ports on DIO Board (8-15) as outputs        Config Stuff
ul.d_config_port(0, Dpt.FIRSTPORTB, Diod.OUT)

# Configure DIO Ports on A/D Converter. Set as Outputs
ul.d_config_port(1, Dpt.AUXPORT, Diod.OUT)

LoadCell1Raw = ul.a_in(1, 1, ULRange.BIP10VOLTS)
LoadCell2Raw = ul.a_in(1, 2, ULRange.BIP10VOLTS)
LoadCell3Raw = ul.a_in(1, 4, ULRange.BIP10VOLTS)
LoadCell4Raw = ul.a_in(1, 5, ULRange.BIP10VOLTS)

print(LoadCell1Raw)
print(LoadCell2Raw)
print(LoadCell3Raw)
print(LoadCell4Raw)