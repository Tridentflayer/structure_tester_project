from mcculw import ul
from mcculw.enums import DigitalIODirection as Diod
from mcculw.enums import DigitalPortType as Dpt
from mcculw.enums import ULRange
from mcculw.enums import AnalogInputMode
import time
import tkinter as tk

ul.d_config_port(0, Dpt.FIRSTPORTA, Diod.IN)   # 12-20
ul.d_config_port(0, Dpt.FIRSTPORTB, Diod.OUT)  # 2-10
ul.d_config_port(0, Dpt.FIRSTPORTC, Diod.IN)   # 32-40

while 1 == 1:
    ul.d_bit_out(0, Dpt.FIRSTPORTA, 8, 1)
    ul.d_bit_out(0, Dpt.FIRSTPORTA, 9, 1)