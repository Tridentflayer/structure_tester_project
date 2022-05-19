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

x = datetime.now()
file_name = x.strftime('%d-%m-%Y-%H-%M-%S.txt')    # Get current date and time, create and open a file with that name
file = open(file_name, 'w')
print('created', file_name)     # Open the file, and print column headers
file.writelines("Load Cell 1, Load Cell 2, Load Cell 3, Load Cell 4, Total Load, Distance Sensor")
file.writelines("\n")
file.writelines("\n")

DataProcessing = 0
TareAvg = 50
MathController = 0         # Math related variables
Tare1Total = 0
Tare2Total = 0
Tare3Total = 0
TareBTotal = 0
DSTotal = 0
Tare1 = 0
Tare2 = 0
Tare3 = 0                  # More of the same
TareB = 0
DTare = 0

for TareAvg in range(51, 1, -1):   # Main loop for calculating the tare value

    LoadCell1Tare = ul.a_in(1, 1, ULRange.BIP10VOLTS)
    LoadCell2Tare = ul.a_in(1, 9, ULRange.BIP10VOLTS)
    LoadCell3Tare = ul.a_in(1, 2, ULRange.BIP10VOLTS)
    LoadCellBTare = ul.a_in(1, 10, ULRange.BIP10VOLTS)   # Take input every cycle
    DSTareRaw = ul.a_in(1, 3, ULRange.BIP10VOLTS)

    Tare1Total = Tare1Total + LoadCell1Tare
    Tare2Total = Tare2Total + LoadCell2Tare
    Tare3Total = Tare3Total + LoadCell3Tare   # Continuously add inputs
    TareBTotal = TareBTotal + LoadCellBTare
    DSTotal = DSTotal + DSTareRaw
    time.sleep(.1)      # Delay. Change to increase tare resolution.

Tare1 = Tare1Total/50
Tare2 = Tare2Total/50
Tare3 = Tare3Total/50       # Take the total divide by the number of cycles
TareB = TareBTotal/50
DTare = DSTotal/50
print(Tare1, Tare2, Tare3, TareB)
DataProcessing = 1   # Then activate the recording section
print("Tare Found. Collecting data")

while DataProcessing == 1:      # Loop for processing data while active

    LoadCell1Raw = (ul.a_in(1, 1, ULRange.BIP10VOLTS) - Tare1)     # Channel 1, Port 4
    LoadCell2Raw = (ul.a_in(1, 9, ULRange.BIP10VOLTS) - Tare2)     # Channel 9,Port 5. Need AGND ports 3, 6, and 9
    LoadCell3Raw = (ul.a_in(1, 2, ULRange.BIP10VOLTS) - Tare3)     # Channel 2, Port 7
    LoadCellBRaw = (ul.a_in(1, 10, ULRange.BIP10VOLTS) - TareB)   # Channel 10, Port 8   Taking raw sensor data
    DistanceSensorRaw = ul.a_in(1, 3, ULRange.BIP10VOLTS)    # Channel 3, Port 10

    LoadCell1Mid = int(LoadCell1Raw * 0.000305 * 10.8 * 100)  # 1-10.8, 2-12.6, 3-12, B-10.8
    LoadCell2Mid = int(LoadCell2Raw * 0.000305 * 12.6 * 100)  # Multiplying the raw data by the constants
    LoadCell3Mid = int(LoadCell3Raw * 0.000305 * 12 * 100)    # Gives us the actual forces/distances
    LoadCellBMid = int(LoadCellBRaw * 0.000305 * 9.2 * 100)  # Need to change 10.8, 12.6, 12, and 10.8.
    DistanceSensorMid = int((DistanceSensorRaw**-1) * 10.52631579 * 100)

    LoadCell1Final = str((float(LoadCell1Mid)/100))
    LoadCell2Final = str((float(LoadCell2Mid)/100))
    LoadCell3Final = str((float(LoadCell3Mid)/100))      # Continuing the math
    LoadCellBFinal = str((float(LoadCellBMid)/100))
    DistanceSensorFinal = str((float(DistanceSensorMid)/100))
    TotalLoad1 = float((LoadCell1Mid + LoadCell2Mid + LoadCell3Mid + LoadCellBMid)/100)
    TotalLoad2 = str(TotalLoad1)

    L2 = [LoadCell1Final, "kg   /  ", LoadCell2Final, "kg   /  ", LoadCell3Final, "kg   /  "]
    L3 = [LoadCellBFinal, "kg   /  ", TotalLoad2, "kg   /  ", DistanceSensorFinal, "in"]
    file.writelines(L2)         # Writing the data to the file
    file.writelines(L3)
    file.writelines("\n")
    time.sleep(.5)     # Time delay. Can be modified to change the resolution of the data

if DataProcessing != 1:
    file.close()