from mcculw import ul
from mcculw.enums import DigitalIODirection as Diod
from mcculw.enums import DigitalPortType as Dpt
from mcculw.enums import ULRange
from mcculw.enums import AnalogInputMode
from datetime import datetime
import time
# Import libraries

ul.d_config_port(1, Dpt.AUXPORT, Diod.OUT)
ul.a_input_mode(1, AnalogInputMode.SINGLE_ENDED)
Data = 1
while Data == 1:
    LoadCell1 = ul.a_in(1, 1, ULRange.BIP10VOLTS)
    LoadCell2 = ul.a_in(1, 9, ULRange.BIP10VOLTS)
    LoadCell3 = ul.a_in(1, 2, ULRange.BIP10VOLTS)
    LoadCellB = ul.a_in(1, 10, ULRange.BIP10VOLTS)
    print(LoadCell1, LoadCell2, LoadCell3, LoadCellB)
    time.sleep(0.5)