#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 09:55:09 2021

@author: tryfighter
"""
import streamlit as  st
import pandas as pd
import altair as alt
import numpy as np
st.write(st.__version__)
st.write(pd.__version__)
st.write(alt.__version__)
st.write(np.__version__)

def can_be_numeric(col_name):
    try:
        pd.to_numeric(df[col_name])
        return True
    except:
        return False
    

st.title("Powerful Plotting Application")
st.markdown('Shuaijiang Liu: https://github.com/shuaijl')

upload_file = st.file_uploader("Upload the file you want to plot. Only csv\
                               file will be allowed", type = 'csv')
if upload_file is not None:
    df = pd.read_csv(upload_file)
    df = df.applymap(lambda x: np.nan if x == " " else x)
    numeric_cols = [ x for x in df.columns if can_be_numeric(x)]
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, axis = 0)
    x_axis = st.selectbox("Select your x axis.", options = numeric_cols)
    y_axis = st.selectbox("Select your y axis.", options = numeric_cols)
    row = st.slider("Choose the rows you want to plot.", 0,
                    len(df))
    st.write(f"x axis is {x_axis}, y axis is {y_axis}. First {row} are showing.")
    
    my_chart = alt.Chart(df[0:row]).mark_circle().encode(x = x_axis, y = y_axis,
                                                  size = y_axis, color = x_axis)
    st.altair_chart(my_chart)
    
    st.write("Only work for spotify file, the following chart shows the most 20 songs.\
             If it is not working, you will say a massage for sorry.")
    try:
        df_pop = df.sort_values("Popularity", ascending = False)
    
        my_extra_chart = alt.Chart(df_pop[0:20]).mark_bar().encode(x = "Song Name",y = "Popularity",
                                                                   tooltip = ["Artist","Release Date","Chord"])
        st.altair_chart(my_extra_chart)
    except:
         st.write("Sorry the chart is not working for the current file.")
    