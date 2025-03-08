import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("EDA Projects of Flight In India")
# Load your dataset
data = pd.read_csv('data01.csv')

st.write("### Dataset Preview", data.head(len(data)))
st.write("Dataset shape:",data.shape)
st.write("### Data Summary", data.describe())

options = ["Bombay", "Delhi", "Bengaluru", "Hyderabad", "Kolkata", "Chennai"]
selected_option = st.selectbox("Choose origin of Flight:", options)

options = ["Bombay", "Delhi", "Bengaluru", "Hyderabad","Kolkata","Chennai"]
selected_option1 = st.selectbox("Choose Destination:", options)

options = ["IndiGo", "Vistara", "Go First", "SpiceJet","Air India"]
selected_option2 = st.selectbox("Choose Airline", options)

#bom to del 
if selected_option=="Bombay" and selected_option1=="Delhi" and selected_option2=="IndiGo":
    filtered_rows = data[
    (data["Origin"] == "BOM") & 
    (data["Destination"] == "DEL") & 
    (data["Company"] == "IndiGo ")
]
    
    
    st.write(filtered_rows)
    st.write("### Flight records from Bombay to Bengaluru ")
elif selected_option == "Bombay" and selected_option1 == "Delhi" and selected_option2 == "Vistara":
    filtered_rows = data[
        (data["Origin"] == "BOM") & 
        (data["Destination"] == "DEL") & 
        (data["Company"] == "Vistara ")
    ]
    st.write(filtered_rows)
elif selected_option == "Bombay" and selected_option1 == "Delhi" and selected_option2 == "Go First":
    filtered_rows = data[
        (data["Origin"] == "BOM") & 
        (data["Destination"] == "DEL") & 
        (data["Company"] == "Go First ")
    ]
    st.write(filtered_rows)
    st.write("### Flight records from Bombay to Bengaluru")
elif selected_option == "Bombay" and selected_option1 == "Delhi" and selected_option2 == "SpiceJet":
    filtered_rows = data[
        (data["Origin"] == "BOM") & 
        (data["Destination"] == "DEL") & 
        (data["Company"] == "SpiceJet ")
    ]
    st.write(filtered_rows)
elif selected_option == "Bombay" and selected_option1 == "Delhi" and selected_option2 == "Air India":
    filtered_rows = data[
        (data["Origin"] == "BOM") & 
        (data["Destination"] == "DEL") & 
        (data["Company"] == "Air India ")
    ]
    st.write(filtered_rows)
#bom to bengaluru
elif selected_option == "Bombay" and selected_option1 == "Bengaluru" and selected_option2 == "IndiGo":
    filtered_rows = data[
        (data["Origin"] == "BOM") & 
        (data["Destination"] == "BLR") & 
        (data["Company"] == "IndiGo ")
    ]
    st.write(filtered_rows)
    st.write("### Flight records from Bombay to Bengaluru ")
elif selected_option == "Bombay" and selected_option1 == "Bengaluru" and selected_option2 == "Vistara":
    filtered_rows = data[
        (data["Origin"] == "BOM") & 
        (data["Destination"] == "BLR") & 
        (data["Company"] == "Vistara ")
    ]
    st.write(filtered_rows)
    st.write("### Flight records from Bombay to Bengaluru by Go First")
elif selected_option == "Bombay" and selected_option1 == "Bengaluru" and selected_option2 == "Go First":
    filtered_rows = data[
        (data["Origin"] == "BOM") & 
        (data["Destination"] == "BLR") & 
        (data["Company"] == "Go First ")
    ]
    st.write(filtered_rows)
elif selected_option == "Bombay" and selected_option1 == "Bengaluru" and selected_option2 == "SpiceJet":
    filtered_rows = data[
        (data["Origin"] == "BOM") & 
        (data["Destination"] == "BLR") & 
        (data["Company"] == "SpiceJet ")
    ]
    st.write(filtered_rows)
    st.write("### Flight records from Bombay to Bengaluru ")
    st.write("###No flight from Bombay to Bengaluru")
elif selected_option == "Bombay" and selected_option1 == "Bengaluru" and selected_option2 == "Air India":
    filtered_rows = data[
        (data["Origin"] == "BOM") & 
        (data["Destination"] == "BLR") & 
        (data["Company"] == "Air India ")
    ]
    st.write(filtered_rows)
    st.write("### Flight records from Bombay to Bengaluru ")
#delhi to bombay...
elif selected_option == "Delhi" and selected_option1 == "Bombay" and selected_option2 == "IndiGo":
    filtered_rows = data[
        (data["Origin"] == "DEL") & 
        (data["Destination"] == "BOM") & 
        (data["Company"] == "IndiGo ")
    ]
    st.write(filtered_rows)
elif selected_option == "Delhi" and selected_option1 == "Bombay" and selected_option2 == "Vistara":
    filtered_rows = data[
        (data["Origin"] == "DEL") & 
        (data["Destination"] == "BOM") & 
        (data["Company"] == "Vistara ")
    ]
    st.write(filtered_rows)
elif selected_option == "Delhi" and selected_option1 == "Bombay" and selected_option2 == "Go First":
    filtered_rows = data[
        (data["Origin"] == "DEL") & 
        (data["Destination"] == "BOM") & 
        (data["Company"] == "Go First ")
    ]
    st.write(filtered_rows)
elif selected_option == "Delhi" and selected_option1 == "Bombay" and selected_option2 == "SpiceJet":
    filtered_rows = data[
        (data["Origin"] == "DEL") & 
        (data["Destination"] == "BOM") & 
        (data["Company"] == "SpiceJet ")
    ]
    st.write(filtered_rows)
elif selected_option == "Delhi" and selected_option1 == "Bombay" and selected_option2 == "Air India":
    filtered_rows = data[
        (data["Origin"] == "DEL") & 
        (data["Destination"] == "BOM") & 
        (data["Company"] == "Air India ")
    ]
    st.write(filtered_rows)
#Bengaluru to hydrabad with all company(empty)
elif selected_option == "Bengaluru" and selected_option1 == "Hyderabad" and selected_option2 == "IndiGo":
    filtered_rows = data[
        (data["Origin"] == "BLR") & 
        (data["Destination"] == "HYD") & 
        (data["Company"] == "IndiGo ")
    ]
    st.write(filtered_rows)
    st.write("### No records found for flights from Bengaluru to other states.")
elif selected_option == "Bengaluru" and selected_option1 == "Hyderabad" and selected_option2 == "Vistara":
    filtered_rows = data[
        (data["Origin"] == "BLR") & 
        (data["Destination"] == "HYD") & 
        (data["Company"] == "Vistara ")
    ]
    st.write(filtered_rows)
    st.write("### No records found for flights from Bengaluru to other states.")
elif selected_option == "Bengaluru" and selected_option1 == "Hyderabad" and selected_option2 == "Go First":
    filtered_rows = data[
        (data["Origin"] == "BLR") & 
        (data["Destination"] == "HYD") & 
        (data["Company"] == "Go First ")
    ]
    st.write(filtered_rows)
    st.write("### No records found for flights from Bengaluru to other states.")
elif selected_option == "Bengaluru" and selected_option1 == "Hyderabad" and selected_option2 == "SpiceJet":
    filtered_rows = data[
        (data["Origin"] == "BLR") & 
        (data["Destination"] == "HYD") & 
        (data["Company"] == "SpiceJet ")
    ]
    st.write(filtered_rows)
    st.write("### No records found for flights from Bengaluru to other states.")
elif selected_option == "Bengaluru" and selected_option1 == "Hyderabad" and selected_option2 == "Air India":
    filtered_rows = data[
        (data["Origin"] == "BLR") & 
        (data["Destination"] == "HYD") & 
        (data["Company"] == "Air India ")
    ]
    st.write(filtered_rows)
    st.write("### No records found for flights from Bengaluru to other states.")
else:
    st.write("No records found")

user_input = st.text_input("Enter your flight id:", "")
st.write("You entered:", user_input)
if user_input == "A1001":
    filtered_row = data[data["Flight Id"]==user_input]
    st.write(filtered_row)
elif user_input == "A1002":
    filtered_row = data[data["Flight Id"]==user_input]
    st.write(filtered_row)
elif user_input == "A1003":
    filtered_row = data[data["Flight Id"]==user_input]
    st.write(filtered_row)
elif user_input == "A1004":
    filtered_row = data[data["Flight Id"]==user_input]
    st.write(filtered_row)
elif user_input == "A1005":
    filtered_row = data[data["Flight Id"]==user_input]
    st.write(filtered_row)
elif user_input == "A2000":
    filtered_row = data[data["Flight Id"]==user_input]
    st.write(filtered_row)
elif user_input == "A2500":
    filtered_row = data[data["Flight Id"]==user_input]
    st.write(filtered_row)
elif user_input == "A3000":
    filtered_row = data[data["Flight Id"]==user_input]
    st.write(filtered_row)
else:
    st.write("Flight Id does not exist.")

st.write("## Flight Distribution By Airline Company")
fig, ax = plt.subplots()
sns.histplot(data['Company'], kde=True, ax=ax)
st.pyplot(fig)

st.write("## Flight Price Distrubution and Density Curve")
fig, ax = plt.subplots()
sns.histplot(data['Flight Price'], kde=True, ax=ax)
st.pyplot(fig)