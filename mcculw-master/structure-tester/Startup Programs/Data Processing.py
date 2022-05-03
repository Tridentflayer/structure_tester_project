from mcculw import ul
from mcculw.enums import DigitalIODirection as Diod
from mcculw.enums import DigitalPortType as Dpt
from mcculw.enums import ULRange
from mcculw.enums import AnalogInputMode
from datetime import datetime
import time
# Import libraries

ul.d_config_port(0, Dpt.FIRSTPORTA, Diod.IN)       # Config Stuff
ul.d_config_port(0, Dpt.FIRSTPORTB, Diod.OUT)
ul.d_config_port(1, Dpt.AUXPORT, Diod.OUT)
ul.a_input_mode(1, AnalogInputMode.SINGLE_ENDED)

DataProcessing = 1   # Controls Data processing

                                                    # Get current date and time, create and open a file with that name
x = datetime.now()
file_name = x.strftime('%d-%m-%Y-%H-%M-%S.txt')
with open(file_name, 'w') as file:
    print('created', file_name)     # Open the file, and print column headers
L1 = ["Load Cell 1, ", "Load Cell 2, ", "Load Cell 3, ", "Load Cell 4, ", "Distance Sensor"]

while DataProcessing == 1:      # Loop for processing data while active

    LoadCell1Raw = ul.a_in(1, 1, ULRange.BIP10VOLTS)         # Channel 1, Port 4
    LoadCell2Raw = ul.a_in(1, 9, ULRange.BIP10VOLTS)         # Channel 9, Port 5    Need AGND on ports 3, 6, and 9
    LoadCell3Raw = ul.a_in(1, 2, ULRange.BIP10VOLTS)         # Channel 2, Port 7
    LoadCellBRaw = ul.a_in(1, 10, ULRange.BIP10VOLTS)        # Channel 10, Port 8   Taking raw sensor data
    DistanceSensorRaw = ul.a_in(1, 3, ULRange.BIP10VOLTS)    # Channel 3, Port 10

    LoadCell1Final = LoadCell1Raw * 10.8
    LoadCell2Final = LoadCell2Raw * 12.6     # Multiplying the raw data by the experimentally determined constants
    LoadCell3Final = LoadCell3Raw * 12       # Gives us the actual forces/distances
    LoadCellBFinal = LoadCellBRaw * 113
    DistanceSensorFinal = (DistanceSensorRaw**-1) * 10.52631579  # Using the inverse to calculate the approximate value.
                                                                # Approx. 0.05% error on distance sensor

    L2 = [LoadCell1Final, LoadCell2Final, LoadCell3Final, LoadCellBFinal, DistanceSensorFinal]
    file.writelines(L2)         # Writing the data to the file

    if DistanceSensorFinal == 1:     # If deflection exceed te max, close the file
        file.close()

    time.sleep(0.1)     # Time delay. Can be modified to change the resolution of the data

if DataProcessing != 1:
    file.close()