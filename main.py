import sys
import json
import pandas as pd
import numpy as np
import pyexcel as pe


def separate_sheets(input_filename: str):
    data = pe.get_book(file_name=input_filename)
    for sheetname in data.sheetnames():
        sheet = data[sheetname]
        sheet.save_as(sheetname = ".xls")





if __name__ == "__main__":
    input_filename = sys.argv(0)
    separate_sheets(input_filename)
