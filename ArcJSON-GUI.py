from tkinter import *

from tkinter import ttk
from tkinter import filedialog

# Github example

window = Tk()

window.title("ArcJSON")  # Cosmetic window title

simple_point_names = ['Style', 'Size', 'Fill-R', 'Fill-G', 'Fill-B', 'Fill-T', 'Line-R', 'Line-G',
                      'Line-B', 'Line-T', 'OL-Width']

simple_line_names = ['Style', 'Width', 'Line-R', 'Line-G', 'Line-B', 'Line-T']

simple_polygon_names = ['Fill Style', 'Fill-R', 'Fill-G', 'Fill-B', 'Fill-T', 'Line Style', 'Line Width', 'Line-R',
                        'Line-G', 'Line-B', 'Line-T']


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
                "style": "esriSMS{5}",
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
}}'''.format(point3.get(), point4.get(), point5.get(), point6.get(), point2.get(), point1.get(), point7.get(),
             point8.get(), point9.get(), point10.get(), point11.get()))
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
      "style": "esriSLS{5}"
    }}
  }}
}}'''.format(line3.get(), line4.get(), line5.get(), line6.get(), line2.get(), line1.get()))
    tab2_file.close()


def simple_polygon():
    tab3.filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("txt", "*.txt"), ("all files",
                                                                                                        "*.*")))
    tab3_file = open(tab3.filename, 'w')
    tab3_file.write('''{{
  "renderer": {{
    "type": "simple",
    "symbol": {{
      "type": "esriSFS",
      "color": [
        {0},
        {1},
        {2},
        {3}
      ],
      "outline": {{
        "type": "esriSLS",
        "color": [
          {4},
          {5},
          {6},
          {7}
        ],
        "width": {8},
        "style": "{9}"
      }},
      "style": "esriSFS{10}"
    }}
  }}
}}'''.format(poly2.get(), poly3.get(), poly4.get(), poly5.get(), poly8.get(), poly9.get(), poly10.get(), poly11.get(),
             poly7.get(), poly6.get(), poly1.get()))
    tab3_file.close()


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


# ===========Point===========
for i in simple_point_names:
    Label(tab1, text=i).grid(row=simple_point_names.index(i))

point1_options = ['Circle', 'Cross', 'Diamond', 'Square', 'X']

point1 = ttk.Combobox(tab1, values=point1_options)
point1.set('Circle')
point2 = Entry(tab1)  # Size
point3 = Entry(tab1)  # Fill-R
point4 = Entry(tab1)  # Fill-G
point5 = Entry(tab1)  # Fill-B
point6 = Entry(tab1)  # Fill-T
point7 = Entry(tab1)  # Line-R
point8 = Entry(tab1)  # Line-G
point9 = Entry(tab1)  # Line-B
point10 = Entry(tab1)  # Line-T
point11 = Entry(tab1)  # OL-Width

point_list = [point1, point2, point3, point4, point5, point6, point7, point8, point9, point10, point11]

for i in point_list:
    i.grid(row=point_list.index(i), column=1, sticky=W + E)

Button(tab1, text='Save', command=simple_point).grid(row=11, column=1, sticky=W, pady=4)

# ===========Line===========
for i in simple_line_names:
    Label(tab2, text=i).grid(row=simple_line_names.index(i))

line1_options = ['Solid', 'DashDot', 'DashDotDot', 'Dot', 'LongDash', 'LongDashDot', 'ShortDash', 'ShortDashDot',
                 'ShortDashDot', 'ShortDashDotDot', 'ShortDot']

line1 = ttk.Combobox(tab2, values=line1_options)
line1.set('Solid')
line2 = Entry(tab2)
line3 = Entry(tab2)
line4 = Entry(tab2)
line5 = Entry(tab2)
line6 = Entry(tab2)

line_list = [line1, line2, line3, line4, line5, line6]

for i in line_list:
    i.grid(row=line_list.index(i), column=1, sticky=W + E)

Button(tab2, text='Save', command=simple_line).grid(row=6, column=1, sticky=W, pady=4)

# ===========Polygon===========
for i in simple_polygon_names:
    Label(tab3, text=i).grid(row=simple_polygon_names.index(i))

poly1_options = ['Solid', 'Vertical', 'BackwardDiagonal', 'Cross', 'DiagnolCross', 'ForwardDiagnonal', 'Horizontal',
                 'None']

poly1 = ttk.Combobox(tab3, values=poly1_options)
poly1.set('Solid')
poly2 = Entry(tab3)
poly3 = Entry(tab3)
poly4 = Entry(tab3)
poly5 = Entry(tab3)
poly6 = ttk.Combobox(tab3, values=line1_options)
poly6.set('Solid')
poly7 = Entry(tab3)
poly8 = Entry(tab3)
poly9 = Entry(tab3)
poly10 = Entry(tab3)
poly11 = Entry(tab3)

poly_list = [poly1, poly2, poly3, poly4, poly5, poly6, poly7, poly8, poly9, poly10, poly11]

for i in poly_list:
    i.grid(row=poly_list.index(i), column=1, sticky=W + E)

Button(tab3, text='Save', command=simple_polygon).grid(row=11, column=1, sticky=W, pady=4)

tab_control.pack(expand=1, fill='both')

window.mainloop()
