import streamlit as st
import pandas as pd
import logging

class CSVDataProcessor(object):
    def __init__(self,path):
        self.path = path
        self.data = None

    def load_csv(self):
        try:
            df = pd.read_csv(self.path)
            self.data = df
        except FileNotFoundError:
            print(f"\nPath {self.path} is Wrong give correct one")

    def filter_csv(self,condition):
        if isinstance(self.data, pd.DataFrame) and self.data is not None:
            if condition in list(self.data.columns):
                return self.data[condition]
            else:
                logging.error(f"\n[FAILED] Given filter condition: '{condition}' IS NOT A COLUMN" )
                print(f"{self.data.columns}")
        else:
            logging.error(f"\n[FAILED] self.data is not a pandas.DataFrame Object ")
            print(f"INITIALIZE FIRST with load_csv()")
