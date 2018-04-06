# Ask user if point, poly, or line
# Ask user if unique values, break values, or single design

from tkinter import filedialog
from tkinter import *

master = Tk()


def json_point():
    point_red = ''
    point_green = ''
    point_blue = ''
    point_trans = ''
    point_size = ''
    pass


def unique_values():
    field_name = ''
    # Add values - how to handle multiples
    pass


def break_values():
    # Class breaks + min value + max value
    pass


def write_file():


master.filename = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=(("txt", "*.txt"), ("all files", "*.*"
                                                                                                      )))


def json_line():
    pass


def json_poly():
    pass
