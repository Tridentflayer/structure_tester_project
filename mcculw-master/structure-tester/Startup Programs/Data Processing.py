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
file = open(file_name, 'w')
print('created', file_name)     # Open the file, and print column headers
file.writelines("Load Cell 1, Load Cell 2, Load Cell 3, Load Cell 4, Distance Sensor")
file.writelines("\n")
file.writelines("\n")
while DataProcessing == 1:      # Loop for processing data while active

    LoadCell1Raw = ul.a_in(1, 1, ULRange.BIP10VOLTS)         # Channel 1, Port 4
    LoadCell2Raw = ul.a_in(1, 9, ULRange.BIP10VOLTS)         # Channel 9, Port 5    Need AGND on ports 3, 6, and 9
    LoadCell3Raw = ul.a_in(1, 2, ULRange.BIP10VOLTS)         # Channel 2, Port 7
    LoadCellBRaw = ul.a_in(1, 10, ULRange.BIP10VOLTS)        # Channel 10, Port 8   Taking raw sensor data
    DistanceSensorRaw = ul.a_in(1, 3, ULRange.BIP10VOLTS)    # Channel 3, Port 10

    LoadCell1Mid = int(LoadCell1Raw * 0.000305 * 10.8 * 100)
    LoadCell2Mid = int(LoadCell2Raw * 0.000305 * 12.6 * 100)  # Multiplying the raw data by the constants
    LoadCell3Mid = int(LoadCell3Raw * 0.000305 * 12 * 100)    # Gives us the actual forces/distances
    LoadCellBMid = int(LoadCellBRaw * 0.000305 * 10.8 * 100)
    DistanceSensorMid = int((DistanceSensorRaw**-1) * 10.52631579 * 100)

    LoadCell1Final = str((float(LoadCell1Mid)/100))
    LoadCell2Final = str((float(LoadCell2Mid)/100))
    LoadCell3Final = str((float(LoadCell3Mid)/100))
    LoadCellBFinal = str((float(LoadCellBMid)/100))
    DistanceSensorFinal = str((float(DistanceSensorMid)/100))

    L2 = [LoadCell1Final, "kg   /   ", LoadCell2Final, "kg   /   ", LoadCell3Final, "kg   /   "]
    L3 = [LoadCellBFinal, "kg   /   ", DistanceSensorFinal]
    file.writelines(L2)         # Writing the data to the file
    file.writelines(L3)
    file.writelines("\n")
    time.sleep(0.1)     # Time delay. Can be modified to change the resolution of the data

if DataProcessing != 1:
    file.close()