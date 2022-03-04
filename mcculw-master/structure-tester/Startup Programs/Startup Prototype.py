from mcculw import ul
from mcculw.enums import DigitalIODirection as Diod  # Import interfacing libraries
from mcculw.device_info import DaqDeviceInfo as Ddi
from mcculw.enums import DigitalPortType as Dpt
# Import interfacing libraries

# Configure the A set of ports (0-7) as inputs
ul.d_config_port(0, Dpt.FIRSTPORTA, Diod.IN)

# Configure the B set of ports (8-15) as outputs
ul.d_config_port(0, Dpt.FIRSTPORTB, Diod.OUT)

ManualLock = 1  # Create variable to toggle manual control. Lock is true by default

# Port numbers are completely random right now. Will need to change ports to match actual wiring.

# Define Magnetic sensors
MagSensorTop = ul.d_bit_in(0, Dpt.FIRSTPORTA, 0)
MagSensorBottom = ul.d_bit_in(0, Dpt.FIRSTPORTA, 1)  # Read True/False from port, set as variable

def MagSensorTest():

    if MagSensorTop != 1 or 0:
        MagSensorTopStatus = 1  # Test top sensor. If there's an invalid value, record as variable
    else:
        MagSensorTopStatus = 0  # Otherwise, set it as good

    if MagSensorBottom != 1 or 0:
        MagSensorBottomStatus = 1  # Same as above, but with bottom sensor
    else:
        MagSensorBottomStatus = 0

    MagSensorData = MagSensorTopStatus, MagSensorBottomStatus  # Create variable for extracting data

    # return MagSensorData as value of the function
    return MagSensorData

# Split MagSensorData into usable components
MagSensorTop = (MagSensorTest()[0])
MagSensorBottom = (MagSensorTest()[1])




# Temp Data Readout
print("Mag Top")
print(MagSensorTop)
print("Mag Bottom")
print(MagSensorBottom)
