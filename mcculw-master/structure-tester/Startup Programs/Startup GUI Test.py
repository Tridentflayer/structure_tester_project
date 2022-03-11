

import tkinter as tk
window = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()
frame_c = tk.Frame()
frame_d = tk.Frame()
frame_e = tk.Frame()
frame_f = tk.Frame()

label_a = tk.Label(master=frame_a, text="Cylinder Bleed")
label_a.pack()
label_b = tk.Label(master=frame_b, text="Magnetic Sensor")
label_b.pack()
label_c = tk.Label(master=frame_b, text="Pressure Sensor")
label_c.pack()
label_d = tk.Label(master=frame_b, text="Distance Sensor")
label_d.pack()
label_e = tk.Label(master=frame_b, text="Light Bar")
label_e.pack()
label_f = tk.Label(master=frame_b, text="Error State")
label_f.pack()

frame_a.pack()
frame_b.pack()
frame_c.pack()
frame_d.pack()
frame_e.pack()
frame_f.pack()

window.mainloop()