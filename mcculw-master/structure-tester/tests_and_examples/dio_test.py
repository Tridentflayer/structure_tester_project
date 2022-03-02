from __future__ import absolute_import, division, print_function
from builtins import *  # @UnusedWildImport

from mcculw import ul
from mcculw.enums import DigitalIODirection as diod
from mcculw.device_info import DaqDeviceInfo as ddi

def run_example():
    # By default, the example detects and displays all available devices and
    # selects the first device listed. Use the dev_id_list variable to filter
    # detected devices by device ID (see UL documentation for device IDs).
    # If use_device_detection is set to False, the board_num variable needs to
    # match the desired board number configured with Instacal.
    use_device_detection = True
    dev_id_list = []
    board_num = 0

    daq_dev_info = ddi(board_num)
    dio_info = ddi.get_dio_info(daq_dev_info)

    port = next((port for port in dio_info.port_info if port.supports_output),
            None)

    if port.is_port_configurable:
        ul.d_config_port(board_num, port.type, diod.OUT)

    port_value = 0xFF
    print('Setting', port.type.name, 'to', port_value)

    # Output the value to the port
    ul.d_out(board_num, port.type, port_value)

    bit_num = 0
    bit_value = 1
    print('Setting', port.type.name, 'bit', bit_num, 'to', bit_value)

    # Output the value to the bit
    ul.d_bit_out(board_num, port.type, bit_num, bit_value)

    if __name__ == '__main__':
        run_example()