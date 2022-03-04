from mcculw import ul
from mcculw.enums import DigitalIODirection as diod
from mcculw.device_info import DaqDeviceInfo as ddi
from mcculw.enums import DigitalPortType as dpt

# Configure the A set of ports (0-7) as inputs
ul.d_config_port(0, dpt.FIRSTPORTA, diod.IN)
# Configure the B set of ports (8-15) as outputs
ul.d_config_port(0, dpt.FIRSTPORTB, diod.OUT)

# Output a 0 on port 8
ul.d_bit_out(0, dpt.FIRSTPORTA, 8, 0)


value = ul.d_bit_in(0, dpt.FIRSTPORTA, 0)