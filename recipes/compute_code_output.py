# -*- coding: utf-8 -*-
import dataiku
import pandas as pd, numpy as np
from dataiku import pandasutils as pdu

# Read recipe inputs
t_shirt_data_distinct = dataiku.Dataset("t_shirt_data_distinct")
t_shirt_data_distinct_df = t_shirt_data_distinct.get_dataframe()


# Compute recipe outputs from inputs
# TODO: Replace this part by your actual code that computes the output, as a Pandas dataframe
# NB: DSS also supports other kinds of APIs for reading and writing data. Please see doc.

code_output_df = t_shirt_data_distinct_df # For this sample code, simply copy input to output


# Write recipe outputs
code_output = dataiku.Dataset("code_output")
code_output.write_with_schema(code_output_df)
