import streamlit as st
import pickle
import numpy as np

# Importing the model
pipe = pickle.load(open('pipe.pkl', 'rb'))
df = pickle.load(open('df.pkl', 'rb'))

st.title('Laptop Price Predictor')

# Selecting brand
company = st.selectbox('Brand', df['Company'].unique())

# type of laptop

type = st.selectbox('Type', df['TypeName'].unique())

# selecting RAM
RAM = st.selectbox('RAM(in GB', df['Ram'].unique())

# Weight of the laptop
weight = st.number_input('Weight of the Laptop')

# TouchScreen option
touchscreen = st.selectbox('TouchScreen', ['Yes', 'No'])

# IPS Display
ips_display = st.selectbox('IPS Display', ['Yes', 'No'])

# screen size
screen_size = st.number_input('Screen Size', value=13.0)

# resolution
resolution = st.selectbox('Screen Resolution',
                          ['1920x1080', '1366x768', '1600x900', '3840x2160', '3200x1800', '2880x1800', '2560x1600',
                           '2560x1440', '2304x1440'])

# cpu
cpu = st.selectbox('CPU', df['Cpu Brand'].unique())

# ssd and hdd

hdd = st.selectbox('HDD(in GB)', [0, 128, 256, 512, 1024, 2048])

ssd = st.selectbox('SSD(in GB)', [0, 128, 256, 512, 1024])

# gpu
gpu = st.selectbox('GPU', df['Gpu Brand'].unique())

# OS
os = st.selectbox('OS', df['OS'].unique())

if st.button('Predict Price'):
    # taking query to pass to the pipeline
    ppi = None

    if touchscreen == 'Yes':
        touchscreen = 1
    else:
        touchscreen = 0

    if ips_display == 'Yes':
        ips_display = 1
    else:
        ips = 0

    X_res = int(resolution.split('x')[0])
    Y_res = int(resolution.split('x')[1])
    ppi = ((X_res ** 2) + (Y_res ** 2)) ** 0.5 / screen_size
    query = np.array([company, type, RAM, weight, touchscreen, ips_display, ppi, cpu, hdd, ssd, gpu, os])

    query = query.reshape(1, 12)

    st.title("The predicted price of this configuration is: " + str(int(np.exp(pipe.predict(query)[0]))))
