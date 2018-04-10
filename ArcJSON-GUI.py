from tkinter import *

from tkinter import ttk
from tkinter import filedialog

window = Tk()

window.title("ArcJSON")  # Cosmetic window title


def unique_point():
    tab1.filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("txt", "*.txt"), ("all files",
                                                                                                        "*.*")))
    fill_r = s3.get()
    fill_g = s4.get()
    fill_b = s5.get()
    fill_t = s6.get()
    size = s2.get()
    style = s1.get()
    outline_r = s7.get()
    outline_g = s8.get()
    outline_b = s9.get()
    outline_t = s10.get()
    outline_w = s11.get()
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
}}'''.format(fill_r, fill_g, fill_b, fill_t, size, style, outline_r, outline_g, outline_b, outline_t, outline_w))
    tab1_file.close()


# =====Create Tab Structure=====
tab_control = ttk.Notebook(window)

# Define tabs
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)
tab3 = ttk.Frame(tab_control)

# Add defined tabs to window
tab_control.add(tab1, text='Simple')
tab_control.add(tab2, text='Unique')
tab_control.add(tab3, text='Class Break')


# ===========Simple=============
simple_point_names = ['Style', 'Size', 'Fill-R', 'Fill-G', 'Fill-B', 'Fill-Transp', 'Outline-R', 'Outline-G',
                      'Outline-B', 'OL-Transp', 'OL-Width']
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

Button(tab1, text='Save', command=unique_point).grid(row=11, column=1, sticky=W, pady=4)

# ===========Unique===========
Label(tab2, text="Style").grid(row=0)
Label(tab2, text="Size").grid(row=1)
Label(tab2, text="Fill-R").grid(row=2)
Label(tab2, text="Fill-G").grid(row=3)
Label(tab2, text="Fill-B").grid(row=4)
Label(tab2, text="Fill-Transp").grid(row=5)
Label(tab2, text="Outline-R").grid(row=6)
Label(tab2, text="Outline-G").grid(row=7)
Label(tab2, text="Outline-B").grid(row=8)
Label(tab2, text="OL-Transp").grid(row=9)

u1 = Entry(tab2)
u2 = Entry(tab2)
u3 = Entry(tab2)
u4 = Entry(tab2)
u5 = Entry(tab2)
u6 = Entry(tab2)
u7 = Entry(tab2)
u8 = Entry(tab2)
u9 = Entry(tab2)
u10 = Entry(tab2)

u1.grid(row=0, column=1, sticky=W + E)
u2.grid(row=1, column=1, sticky=W + E)
u3.grid(row=2, column=1, sticky=W + E)
u4.grid(row=3, column=1, sticky=W + E)
u5.grid(row=4, column=1, sticky=W + E)
u6.grid(row=5, column=1, sticky=W + E)
u7.grid(row=6, column=1, sticky=W + E)
u8.grid(row=7, column=1, sticky=W + E)
u9.grid(row=8, column=1, sticky=W + E)
u10.grid(row=9, column=1, sticky=W + E)

tab_control.pack(expand=1, fill='both')

window.mainloop()
