from tkinter import *

from tkinter import ttk
from tkinter import filedialog

window = Tk()

window.title("ArcJSON")  # Cosmetic window title

simple_point_names = ['Style', 'Size', 'Fill-R', 'Fill-G', 'Fill-B', 'Fill-T', 'Line-R', 'Line-G',
                      'Line-B', 'Line-T', 'OL-Width']

simple_line_names = ['Style', 'Width', 'Line-R', 'Line-G', 'Line-B', 'Line-T']

simple_polygon_names = ['Fill Style', 'Fill-R', 'Fill-G', 'Fill-B', 'Fill-T', 'Line Style', 'Line-R', 'Line-G', 'Line-B',
                        'Line-T']


def simple_point():
    tab1.filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("txt", "*.txt"), ("all files",
                                                                                                        "*.*")))
    tab1_file = open(tab1.filename, 'w')
    tab1_file.write('''{{
    "renderer": {{
        "type": "simple",
            "symbol": {{
                "type": "esriSMS",
                "color": [
                 {0},
                 {1},
                 {2},
                 {3}
                ],
                "angle": 0,
                "xoffset": 0,
                "yoffset": 0,
                "size": {4},
                "style": "{5}",
                "outline": {{
                  "type": "esriSLS",
                  "color": [
                    {6},
                    {7},
                    {8},
                    {9}
                   ],
                   "width": {10},
                   "style": "esriSLSSolid"
                    }}
            }}
    }}
}}'''.format(s3.get(), s4.get(), s5.get(), s6.get(), s2.get(), s1.get(), s7.get(), s8.get(), s9.get(), s10.get(),
             s11.get()))
    tab1_file.close()


def simple_line():
    tab2.filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("txt", "*.txt"), ("all files",
                                                                                                        "*.*")))
    tab2_file = open(tab2.filename, 'w')
    tab2_file.write('''{{
  "renderer": {{
    "type": "simple",
    "symbol": {{
      "type": "esriSLS",
      "color": [
        {0},
        {1},
        {2},
        {3}
      ],
      "width": {4},
      "style": "{5}"
    }}
  }}
}}'''.format(u3.get(), u4.get(), u5.get(), u6.get(), u2.get(), u1.get(), ))
    tab2_file.close()


def simple_polygon():
    pass


# =====Create Tab Structure=====
tab_control = ttk.Notebook(window)

# Define tabs
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

# Add defined tabs to window
tab_control.add(tab1, text='Point')
tab_control.add(tab2, text='Line')
tab_control.add(tab3, text='Polygon')


# ===========Point=============
for i in simple_point_names:
    Label(tab1, text=i).grid(row=simple_point_names.index(i))

s1 = Entry(tab1)
s2 = Entry(tab1)
s3 = Entry(tab1)
s4 = Entry(tab1)
s5 = Entry(tab1)
s6 = Entry(tab1)
s7 = Entry(tab1)
s8 = Entry(tab1)
s9 = Entry(tab1)
s10 = Entry(tab1)
s11 = Entry(tab1)

s1.grid(row=0, column=1, sticky=W + E)
s2.grid(row=1, column=1, sticky=W + E)
s3.grid(row=2, column=1, sticky=W + E)
s4.grid(row=3, column=1, sticky=W + E)
s5.grid(row=4, column=1, sticky=W + E)
s6.grid(row=5, column=1, sticky=W + E)
s7.grid(row=6, column=1, sticky=W + E)
s8.grid(row=7, column=1, sticky=W + E)
s9.grid(row=8, column=1, sticky=W + E)
s10.grid(row=9, column=1, sticky=W + E)
s11.grid(row=10, column=1, sticky=W + E)

Button(tab1, text='Save', command=simple_point).grid(row=11, column=1, sticky=W, pady=4)

# ===========Line===========
for i in simple_line_names:
    Label(tab2, text=i).grid(row=simple_line_names.index(i))

u1 = Entry(tab2)
u2 = Entry(tab2)
u3 = Entry(tab2)
u4 = Entry(tab2)
u5 = Entry(tab2)
u6 = Entry(tab2)

u1.grid(row=0, column=1, sticky=W + E)
u2.grid(row=1, column=1, sticky=W + E)
u3.grid(row=2, column=1, sticky=W + E)
u4.grid(row=3, column=1, sticky=W + E)
u5.grid(row=4, column=1, sticky=W + E)
u6.grid(row=5, column=1, sticky=W + E)

Button(tab2, text='Save', command=simple_line).grid(row=6, column=1, sticky=W, pady=4)

# ===========Polygon===========
for i in simple_polygon_names:
    Label(tab3, text=i).grid(row=simple_polygon_names.index(i))

p1 = Entry(tab3)
p2 = Entry(tab3)
p3 = Entry(tab3)
p4 = Entry(tab3)
p5 = Entry(tab3)
p6 = Entry(tab3)
p7 = Entry(tab3)
p8 = Entry(tab3)
p9 = Entry(tab3)
p10 = Entry(tab3)

p1.grid(row=0, column=1, sticky=W + E)
p2.grid(row=1, column=1, sticky=W + E)
p3.grid(row=2, column=1, sticky=W + E)
p4.grid(row=3, column=1, sticky=W + E)
p5.grid(row=4, column=1, sticky=W + E)
p6.grid(row=5, column=1, sticky=W + E)
p7.grid(row=6, column=1, sticky=W + E)
p8.grid(row=7, column=1, sticky=W + E)
p9.grid(row=8, column=1, sticky=W + E)
p10.grid(row=9, column=1, sticky=W + E)

Button(tab3, text='Save', command=simple_polygon).grid(row=20, column=1, sticky=W, pady=4)

tab_control.pack(expand=1, fill='both')

window.mainloop()
