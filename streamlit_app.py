import streamlit as st
import pandas as pd
import time

st.set_page_config(page_title="Monitor for Guidelines", page_icon=":guardsman:", layout="wide")

# Set up background Color 
st.markdown(  
    """
    <style>
        body {
            background-color: #ffffff ;
        }
        .stApp {
            background-color: #CDCACA0E ;
        }
    </style>
    """,
    unsafe_allow_html=True
)

custom_css = """
<style>
    table th, table td {
        text-align: center !important;
        vertical-align: middle !important;
    }
    table th {
        background-color: #CDCACA53 !important;  /* Blue header */
        color: #000000FF !important;                /* White text */
    }
</style>
"""

custom_Redispatch = """
<style>
    table th {
        text-align: center !important;
        vertical-align: middle !important;
        background-color: #CDCACA53 !important;
        color: #000000FF !important;
    }
    table td:nth-child(1) {
        text-align: center !important;
        vertical-align: middle !important;
    }
    table td:nth-child(2) {
        text-align: left !important;
        vertical-align: middle !important;
    }
</style>
"""


table_A_ICV_1 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 ],
            "Region": [ "Bus01", "Bus02", "Bus03", "Bus04", "Bus05", "Bus06", "Bus07", "Bus08", "Bus09", "Bus10", 
                        "Bus11", "Bus12", "Bus13", "Bus14", "Bus15", "Bus16", "Bus17", "Bus18", "Bus19", "Bus20", 
                        "Bus21", "Bus22", "Bus23", "Bus24", "Bus25", "Bus26", "Bus27", "Bus28", "Bus29", "Bus30" ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0.07317, 1.55581, 0.84427, 0.10711, 0.21682, 0, 0, 0, 0 ] ,
            "Heatmap Color": [ ' ' ] * 30
        })

table_A_ICV_2 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 ],
            "Region": [ "Bus01", "Bus02", "Bus03", "Bus04", "Bus05", "Bus06", "Bus07", "Bus08", "Bus09", "Bus10", 
                        "Bus11", "Bus12", "Bus13", "Bus14", "Bus15", "Bus16", "Bus17", "Bus18", "Bus19", "Bus20", 
                        "Bus21", "Bus22", "Bus23", "Bus24", "Bus25", "Bus26", "Bus27", "Bus28", "Bus29", "Bus30" ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0.18634, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ,
            "Heatmap Color": [ ' ' ] * 30
        })

table_A_ICV_3 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 ],
            "Region": [ "Bus01", "Bus02", "Bus03", "Bus04", "Bus05", "Bus06", "Bus07", "Bus08", "Bus09", "Bus10", 
                        "Bus11", "Bus12", "Bus13", "Bus14", "Bus15", "Bus16", "Bus17", "Bus18", "Bus19", "Bus20", 
                        "Bus21", "Bus22", "Bus23", "Bus24", "Bus25", "Bus26", "Bus27", "Bus28", "Bus29", "Bus30" ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 1.8027, 5.09223, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ,
            "Heatmap Color": [ ' ' ] * 30
        })

table_A_ICV_4 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 ],
            "Region": [ "Bus01", "Bus02", "Bus03", "Bus04", "Bus05", "Bus06", "Bus07", "Bus08", "Bus09", "Bus10", 
                        "Bus11", "Bus12", "Bus13", "Bus14", "Bus15", "Bus16", "Bus17", "Bus18", "Bus19", "Bus20", 
                        "Bus21", "Bus22", "Bus23", "Bus24", "Bus25", "Bus26", "Bus27", "Bus28", "Bus29", "Bus30" ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        601.66667, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ,
            "Heatmap Color": [ ' ' ] * 30
        })

table_A_ICV_5 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 ],
            "Region": [ "Bus01", "Bus02", "Bus03", "Bus04", "Bus05", "Bus06", "Bus07", "Bus08", "Bus09", "Bus10", 
                        "Bus11", "Bus12", "Bus13", "Bus14", "Bus15", "Bus16", "Bus17", "Bus18", "Bus19", "Bus20", 
                        "Bus21", "Bus22", "Bus23", "Bus24", "Bus25", "Bus26", "Bus27", "Bus28", "Bus29", "Bus30" ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 601.66667, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ,
            "Heatmap Color": [ ' ' ] * 30
        })

table_A_ICV_6 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 ],
            "Region": [ "Bus01", "Bus02", "Bus03", "Bus04", "Bus05", "Bus06", "Bus07", "Bus08", "Bus09", "Bus10", 
                        "Bus11", "Bus12", "Bus13", "Bus14", "Bus15", "Bus16", "Bus17", "Bus18", "Bus19", "Bus20", 
                        "Bus21", "Bus22", "Bus23", "Bus24", "Bus25", "Bus26", "Bus27", "Bus28", "Bus29", "Bus30" ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ,
            "Heatmap Color": [ ' ' ] * 30
        })

table_A_ICV_7 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 ],
            "Region": [ "Bus01", "Bus02", "Bus03", "Bus04", "Bus05", "Bus06", "Bus07", "Bus08", "Bus09", "Bus10", 
                        "Bus11", "Bus12", "Bus13", "Bus14", "Bus15", "Bus16", "Bus17", "Bus18", "Bus19", "Bus20", 
                        "Bus21", "Bus22", "Bus23", "Bus24", "Bus25", "Bus26", "Bus27", "Bus28", "Bus29", "Bus30" ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 7.13469, 0.73996, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ,
            "Heatmap Color": [ ' ' ] * 30
        })

table_A_ICV_8 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 ],
            "Region": [ "Bus01", "Bus02", "Bus03", "Bus04", "Bus05", "Bus06", "Bus07", "Bus08", "Bus09", "Bus10", 
                        "Bus11", "Bus12", "Bus13", "Bus14", "Bus15", "Bus16", "Bus17", "Bus18", "Bus19", "Bus20", 
                        "Bus21", "Bus22", "Bus23", "Bus24", "Bus25", "Bus26", "Bus27", "Bus28", "Bus29", "Bus30" ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 601.66667, 0, 0, 0, 0, 0, 0, 0 ] ,
            "Heatmap Color": [ ' ' ] * 30
        })

table_A_ICV_9 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 ],
            "Region": [ "Bus01", "Bus02", "Bus03", "Bus04", "Bus05", "Bus06", "Bus07", "Bus08", "Bus09", "Bus10", 
                        "Bus11", "Bus12", "Bus13", "Bus14", "Bus15", "Bus16", "Bus17", "Bus18", "Bus19", "Bus20", 
                        "Bus21", "Bus22", "Bus23", "Bus24", "Bus25", "Bus26", "Bus27", "Bus28", "Bus29", "Bus30" ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ,
            "Heatmap Color": [ ' ' ] * 30
        })

table_A_ICV_10 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 ],
            "Region": [ "Bus01", "Bus02", "Bus03", "Bus04", "Bus05", "Bus06", "Bus07", "Bus08", "Bus09", "Bus10", 
                        "Bus11", "Bus12", "Bus13", "Bus14", "Bus15", "Bus16", "Bus17", "Bus18", "Bus19", "Bus20", 
                        "Bus21", "Bus22", "Bus23", "Bus24", "Bus25", "Bus26", "Bus27", "Bus28", "Bus29", "Bus30" ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 601.66667, 0, 0, 0, 0 ] ,
            "Heatmap Color": [ ' ' ] * 30
        })

table_A_ICV_11 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 ],
            "Region": [ "Bus01", "Bus02", "Bus03", "Bus04", "Bus05", "Bus06", "Bus07", "Bus08", "Bus09", "Bus10", 
                        "Bus11", "Bus12", "Bus13", "Bus14", "Bus15", "Bus16", "Bus17", "Bus18", "Bus19", "Bus20", 
                        "Bus21", "Bus22", "Bus23", "Bus24", "Bus25", "Bus26", "Bus27", "Bus28", "Bus29", "Bus30" ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 1.04667, 0.23877, 0.83202, 1.29422, 0, 0, 0, 0 ] ,
            "Heatmap Color": [ ' ' ] * 30
        })

table_A_ICV_12 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 ],
            "Region": [ "Bus01", "Bus02", "Bus03", "Bus04", "Bus05", "Bus06", "Bus07", "Bus08", "Bus09", "Bus10", 
                        "Bus11", "Bus12", "Bus13", "Bus14", "Bus15", "Bus16", "Bus17", "Bus18", "Bus19", "Bus20", 
                        "Bus21", "Bus22", "Bus23", "Bus24", "Bus25", "Bus26", "Bus27", "Bus28", "Bus29", "Bus30" ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 10.36685, 12.33775, 6.41837, 1.42192, 6.24718, 1.25983, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ,
            "Heatmap Color": [ ' ' ] * 30
        })

table_A_ICV_13 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4 , 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30 ],
            "Region": [ "Bus01", "Bus02", "Bus03", "Bus04", "Bus05", "Bus06", "Bus07", "Bus08", "Bus09", "Bus10", 
                        "Bus11", "Bus12", "Bus13", "Bus14", "Bus15", "Bus16", "Bus17", "Bus18", "Bus19", "Bus20", 
                        "Bus21", "Bus22", "Bus23", "Bus24", "Bus25", "Bus26", "Bus27", "Bus28", "Bus29", "Bus30" ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0 ] ,
            "Heatmap Color": [ ' ' ] * 30
        })

## Set table_A_ICV "Heatmap Color" based on "Value"

def gradient_color_A_ICV(x, min_val=0, max_val=14):
    if x == 0:
        return '<span style="color:#FFFFFFFF">██████</span>'  # White
    elif x == 100:
        return '<span style="color:#FF0000">██████</span>'    # Red
    else:
        # Normalize x between 0 and 1
        ratio = min(max((x - min_val) / (max_val - min_val), 0), 1)
        # Interpolate each channel
        r = int(255)  # stays 255
        g = int(255 * (1 - ratio) + 137 * ratio)
        b = int(153 * (1 - ratio) + 137 * ratio)
        hex_color = f'#{r:02X}{g:02X}{b:02X}'
        return f'<span style="color:{hex_color}">██████</span>'

table_A_ICV_1["Heatmap Color"] = table_A_ICV_1["Value"].apply(gradient_color_A_ICV)
table_A_ICV_2["Heatmap Color"] = table_A_ICV_2["Value"].apply(gradient_color_A_ICV)
table_A_ICV_3["Heatmap Color"] = table_A_ICV_3["Value"].apply(gradient_color_A_ICV)
table_A_ICV_4["Heatmap Color"] = table_A_ICV_4["Value"].apply(gradient_color_A_ICV)
table_A_ICV_5["Heatmap Color"] = table_A_ICV_5["Value"].apply(gradient_color_A_ICV)
table_A_ICV_6["Heatmap Color"] = table_A_ICV_6["Value"].apply(gradient_color_A_ICV)
table_A_ICV_7["Heatmap Color"] = table_A_ICV_7["Value"].apply(gradient_color_A_ICV)
table_A_ICV_8["Heatmap Color"] = table_A_ICV_8["Value"].apply(gradient_color_A_ICV)
table_A_ICV_9["Heatmap Color"] = table_A_ICV_9["Value"].apply(gradient_color_A_ICV)
table_A_ICV_10["Heatmap Color"] = table_A_ICV_10["Value"].apply(gradient_color_A_ICV)
table_A_ICV_11["Heatmap Color"] = table_A_ICV_11["Value"].apply(gradient_color_A_ICV)
table_A_ICV_12["Heatmap Color"] = table_A_ICV_12["Value"].apply(gradient_color_A_ICV)
table_A_ICV_13["Heatmap Color"] = table_A_ICV_13["Value"].apply(gradient_color_A_ICV)


table_A_ICI_1 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                       11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                       21, 22, 23, 24, 25, 26, 27, 28, 29, 30,  
                       31, 32, 33, 34, 35, 36, 37, 38 ] ,
                                           
            "Region": [ 'Line 01-03', 'Line 02-04', 'Line 03-04', 'Line 04-06', 'Line 05-30', 'Line 06-02', 'Line 06-08', 'Line 08-28', 'Line 09-10', 'Line 09-11', 'Line 10-17', 
                        'Line 10-20', 'Line 10-21', 'Line 10-22', 'Line 12-13', 'Line 12-14', 'Line 12-16', 'Line 14-15', 'Line 15-18', 'Line 16-17', 'Line 18-19', 'Line 19-20', 
                        'Line 22-24', 'Line 23-24', 'Line 24-25', 'Line 25-26', 'Line 25-27', 'Line 27-29', 'Line 29-30', 'Trf B04-B12', 'Trf B06-B09', 'Trf B06-B10', 'Trf B27-28',
                        'Trf G1-B01', 'Trf G2-B02', 'Trf G3-B08', 'Trf G4-B11', 'TrfG5-B18' ],
            "Value": [  0, 0, 0, 0, 0, 0, -1, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  
                        0, 0, 0, 0, 12.21361, 0, 30.80531, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, 0, 0 ],
            "Heatmap Color": [ " " ] * 38
        })

table_A_ICI_2 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                       11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                       21, 22, 23, 24, 25, 26, 27, 28, 29, 30,  
                       31, 32, 33, 34, 35, 36, 37, 38 ] ,
                                           
            "Region": [ 'Line 01-03', 'Line 02-04', 'Line 03-04', 'Line 04-06', 'Line 05-30', 'Line 06-02', 'Line 06-08', 'Line 08-28', 'Line 09-10', 'Line 09-11', 'Line 10-17', 
                        'Line 10-20', 'Line 10-21', 'Line 10-22', 'Line 12-13', 'Line 12-14', 'Line 12-16', 'Line 14-15', 'Line 15-18', 'Line 16-17', 'Line 18-19', 'Line 19-20', 
                        'Line 22-24', 'Line 23-24', 'Line 24-25', 'Line 25-26', 'Line 25-27', 'Line 27-29', 'Line 29-30', 'Trf B04-B12', 'Trf B06-B09', 'Trf B06-B10', 'Trf B27-28',
                        'Trf G1-B01', 'Trf G2-B02', 'Trf G3-B08', 'Trf G4-B11', 'TrfG5-B18' ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        -1, 0, 0, 0, 0, 0, 0, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, 0, 0 ],
            "Heatmap Color": [ " " ] * 38
        })

table_A_ICI_3 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                       11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                       21, 22, 23, 24, 25, 26, 27, 28, 29, 30,  
                       31, 32, 33, 34, 35, 36, 37, 38 ] ,
                                           
            "Region": [ 'Line 01-03', 'Line 02-04', 'Line 03-04', 'Line 04-06', 'Line 05-30', 'Line 06-02', 'Line 06-08', 'Line 08-28', 'Line 09-10', 'Line 09-11', 'Line 10-17', 
                        'Line 10-20', 'Line 10-21', 'Line 10-22', 'Line 12-13', 'Line 12-14', 'Line 12-16', 'Line 14-15', 'Line 15-18', 'Line 16-17', 'Line 18-19', 'Line 19-20', 
                        'Line 22-24', 'Line 23-24', 'Line 24-25', 'Line 25-26', 'Line 25-27', 'Line 27-29', 'Line 29-30', 'Trf B04-B12', 'Trf B06-B09', 'Trf B06-B10', 'Trf B27-28',
                        'Trf G1-B01', 'Trf G2-B02', 'Trf G3-B08', 'Trf G4-B11', 'TrfG5-B18' ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, -1, 0, 0, 0, 0, 0, 0, 0, 0,  
                        3.05575, 0, 0, 0, 0, 0, 0, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, 0, 0 ],
            "Heatmap Color": [ " " ] * 38
        })

table_A_ICI_4 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                       11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                       21, 22, 23, 24, 25, 26, 27, 28, 29, 30,  
                       31, 32, 33, 34, 35, 36, 37, 38 ] ,
                                           
            "Region": [ 'Line 01-03', 'Line 02-04', 'Line 03-04', 'Line 04-06', 'Line 05-30', 'Line 06-02', 'Line 06-08', 'Line 08-28', 'Line 09-10', 'Line 09-11', 'Line 10-17', 
                        'Line 10-20', 'Line 10-21', 'Line 10-22', 'Line 12-13', 'Line 12-14', 'Line 12-16', 'Line 14-15', 'Line 15-18', 'Line 16-17', 'Line 18-19', 'Line 19-20', 
                        'Line 22-24', 'Line 23-24', 'Line 24-25', 'Line 25-26', 'Line 25-27', 'Line 27-29', 'Line 29-30', 'Trf B04-B12', 'Trf B06-B09', 'Trf B06-B10', 'Trf B27-28',
                        'Trf G1-B01', 'Trf G2-B02', 'Trf G3-B08', 'Trf G4-B11', 'TrfG5-B18' ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, -1, 0, 0, 0, 0, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, 0, 0 ],
            "Heatmap Color": [ " " ] * 38
        })

table_A_ICI_5 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                       11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                       21, 22, 23, 24, 25, 26, 27, 28, 29, 30,  
                       31, 32, 33, 34, 35, 36, 37, 38 ] ,
                                           
            "Region": [ 'Line 01-03', 'Line 02-04', 'Line 03-04', 'Line 04-06', 'Line 05-30', 'Line 06-02', 'Line 06-08', 'Line 08-28', 'Line 09-10', 'Line 09-11', 'Line 10-17', 
                        'Line 10-20', 'Line 10-21', 'Line 10-22', 'Line 12-13', 'Line 12-14', 'Line 12-16', 'Line 14-15', 'Line 15-18', 'Line 16-17', 'Line 18-19', 'Line 19-20', 
                        'Line 22-24', 'Line 23-24', 'Line 24-25', 'Line 25-26', 'Line 25-27', 'Line 27-29', 'Line 29-30', 'Trf B04-B12', 'Trf B06-B09', 'Trf B06-B10', 'Trf B27-28',
                        'Trf G1-B01', 'Trf G2-B02', 'Trf G3-B08', 'Trf G4-B11', 'TrfG5-B18' ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, -1, 0, 0, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, 0, 0 ],
            "Heatmap Color": [ " " ] * 38
        })

table_A_ICI_6 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                       11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                       21, 22, 23, 24, 25, 26, 27, 28, 29, 30,  
                       31, 32, 33, 34, 35, 36, 37, 38 ] ,
                                           
            "Region": [ 'Line 01-03', 'Line 02-04', 'Line 03-04', 'Line 04-06', 'Line 05-30', 'Line 06-02', 'Line 06-08', 'Line 08-28', 'Line 09-10', 'Line 09-11', 'Line 10-17', 
                        'Line 10-20', 'Line 10-21', 'Line 10-22', 'Line 12-13', 'Line 12-14', 'Line 12-16', 'Line 14-15', 'Line 15-18', 'Line 16-17', 'Line 18-19', 'Line 19-20', 
                        'Line 22-24', 'Line 23-24', 'Line 24-25', 'Line 25-26', 'Line 25-27', 'Line 27-29', 'Line 29-30', 'Trf B04-B12', 'Trf B06-B09', 'Trf B06-B10', 'Trf B27-28',
                        'Trf G1-B01', 'Trf G2-B02', 'Trf G3-B08', 'Trf G4-B11', 'TrfG5-B18' ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, -1, 0, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, 0, 0 ],
            "Heatmap Color": [ " " ] * 38
        })

table_A_ICI_7 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                       11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                       21, 22, 23, 24, 25, 26, 27, 28, 29, 30,  
                       31, 32, 33, 34, 35, 36, 37, 38 ] ,
                                           
            "Region": [ 'Line 01-03', 'Line 02-04', 'Line 03-04', 'Line 04-06', 'Line 05-30', 'Line 06-02', 'Line 06-08', 'Line 08-28', 'Line 09-10', 'Line 09-11', 'Line 10-17', 
                        'Line 10-20', 'Line 10-21', 'Line 10-22', 'Line 12-13', 'Line 12-14', 'Line 12-16', 'Line 14-15', 'Line 15-18', 'Line 16-17', 'Line 18-19', 'Line 19-20', 
                        'Line 22-24', 'Line 23-24', 'Line 24-25', 'Line 25-26', 'Line 25-27', 'Line 27-29', 'Line 29-30', 'Trf B04-B12', 'Trf B06-B09', 'Trf B06-B10', 'Trf B27-28',
                        'Trf G1-B01', 'Trf G2-B02', 'Trf G3-B08', 'Trf G4-B11', 'TrfG5-B18' ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 2.17778, 0, 0, 0, 0, 0, 0, 0, 0,  
                        -1, 0, 0, 0, 0, 0, 0, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, 0, 0 ],
            "Heatmap Color": [ " " ] * 38
        })

table_A_ICI_8 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                       11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                       21, 22, 23, 24, 25, 26, 27, 28, 29, 30,  
                       31, 32, 33, 34, 35, 36, 37, 38 ] ,
                                           
            "Region": [ 'Line 01-03', 'Line 02-04', 'Line 03-04', 'Line 04-06', 'Line 05-30', 'Line 06-02', 'Line 06-08', 'Line 08-28', 'Line 09-10', 'Line 09-11', 'Line 10-17', 
                        'Line 10-20', 'Line 10-21', 'Line 10-22', 'Line 12-13', 'Line 12-14', 'Line 12-16', 'Line 14-15', 'Line 15-18', 'Line 16-17', 'Line 18-19', 'Line 19-20', 
                        'Line 22-24', 'Line 23-24', 'Line 24-25', 'Line 25-26', 'Line 25-27', 'Line 27-29', 'Line 29-30', 'Trf B04-B12', 'Trf B06-B09', 'Trf B06-B10', 'Trf B27-28',
                        'Trf G1-B01', 'Trf G2-B02', 'Trf G3-B08', 'Trf G4-B11', 'TrfG5-B18' ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  
                        0, 0, 0, -1, 0, 0, 0, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, 0, 0 ],
            "Heatmap Color": [ " " ] * 38
        })

table_A_ICI_9 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                       11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                       21, 22, 23, 24, 25, 26, 27, 28, 29, 30,  
                       31, 32, 33, 34, 35, 36, 37, 38 ] ,
                                           
            "Region": [ 'Line 01-03', 'Line 02-04', 'Line 03-04', 'Line 04-06', 'Line 05-30', 'Line 06-02', 'Line 06-08', 'Line 08-28', 'Line 09-10', 'Line 09-11', 'Line 10-17', 
                        'Line 10-20', 'Line 10-21', 'Line 10-22', 'Line 12-13', 'Line 12-14', 'Line 12-16', 'Line 14-15', 'Line 15-18', 'Line 16-17', 'Line 18-19', 'Line 19-20', 
                        'Line 22-24', 'Line 23-24', 'Line 24-25', 'Line 25-26', 'Line 25-27', 'Line 27-29', 'Line 29-30', 'Trf B04-B12', 'Trf B06-B09', 'Trf B06-B10', 'Trf B27-28',
                        'Trf G1-B01', 'Trf G2-B02', 'Trf G3-B08', 'Trf G4-B11', 'TrfG5-B18' ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  
                        0, 0, 0, 0, -1, 0, 0, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, 0, 0 ],
            "Heatmap Color": [ " " ] * 38
        })

table_A_ICI_10 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                       11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                       21, 22, 23, 24, 25, 26, 27, 28, 29, 30,  
                       31, 32, 33, 34, 35, 36, 37, 38 ] ,
                                           
            "Region": [ 'Line 01-03', 'Line 02-04', 'Line 03-04', 'Line 04-06', 'Line 05-30', 'Line 06-02', 'Line 06-08', 'Line 08-28', 'Line 09-10', 'Line 09-11', 'Line 10-17', 
                        'Line 10-20', 'Line 10-21', 'Line 10-22', 'Line 12-13', 'Line 12-14', 'Line 12-16', 'Line 14-15', 'Line 15-18', 'Line 16-17', 'Line 18-19', 'Line 19-20', 
                        'Line 22-24', 'Line 23-24', 'Line 24-25', 'Line 25-26', 'Line 25-27', 'Line 27-29', 'Line 29-30', 'Trf B04-B12', 'Trf B06-B09', 'Trf B06-B10', 'Trf B27-28',
                        'Trf G1-B01', 'Trf G2-B02', 'Trf G3-B08', 'Trf G4-B11', 'TrfG5-B18' ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  
                        0, 0, 0, 0, 0, -1, 0, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, 0, 0 ],
            "Heatmap Color": [ " " ] * 38
        })

table_A_ICI_11 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                       11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                       21, 22, 23, 24, 25, 26, 27, 28, 29, 30,  
                       31, 32, 33, 34, 35, 36, 37, 38 ] ,
                                           
            "Region": [ 'Line 01-03', 'Line 02-04', 'Line 03-04', 'Line 04-06', 'Line 05-30', 'Line 06-02', 'Line 06-08', 'Line 08-28', 'Line 09-10', 'Line 09-11', 'Line 10-17', 
                        'Line 10-20', 'Line 10-21', 'Line 10-22', 'Line 12-13', 'Line 12-14', 'Line 12-16', 'Line 14-15', 'Line 15-18', 'Line 16-17', 'Line 18-19', 'Line 19-20', 
                        'Line 22-24', 'Line 23-24', 'Line 24-25', 'Line 25-26', 'Line 25-27', 'Line 27-29', 'Line 29-30', 'Trf B04-B12', 'Trf B06-B09', 'Trf B06-B10', 'Trf B27-28',
                        'Trf G1-B01', 'Trf G2-B02', 'Trf G3-B08', 'Trf G4-B11', 'TrfG5-B18' ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, -1, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, 0, 0 ],
            "Heatmap Color": [ " " ] * 38
        })

table_A_ICI_12 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                       11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                       21, 22, 23, 24, 25, 26, 27, 28, 29, 30,  
                       31, 32, 33, 34, 35, 36, 37, 38 ] ,
                                           
            "Region": [ 'Line 01-03', 'Line 02-04', 'Line 03-04', 'Line 04-06', 'Line 05-30', 'Line 06-02', 'Line 06-08', 'Line 08-28', 'Line 09-10', 'Line 09-11', 'Line 10-17', 
                        'Line 10-20', 'Line 10-21', 'Line 10-22', 'Line 12-13', 'Line 12-14', 'Line 12-16', 'Line 14-15', 'Line 15-18', 'Line 16-17', 'Line 18-19', 'Line 19-20', 
                        'Line 22-24', 'Line 23-24', 'Line 24-25', 'Line 25-26', 'Line 25-27', 'Line 27-29', 'Line 29-30', 'Trf B04-B12', 'Trf B06-B09', 'Trf B06-B10', 'Trf B27-28',
                        'Trf G1-B01', 'Trf G2-B02', 'Trf G3-B08', 'Trf G4-B11', 'TrfG5-B18' ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, 0, 0, 0, -1,  
                        0, 0, 0, 0, 0, 0, 0, 0 ],
            "Heatmap Color": [ " " ] * 38
        })

table_A_ICI_13 = pd.DataFrame({
            "Order": [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
                       11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 
                       21, 22, 23, 24, 25, 26, 27, 28, 29, 30,  
                       31, 32, 33, 34, 35, 36, 37, 38 ] ,
                                           
            "Region": [ 'Line 01-03', 'Line 02-04', 'Line 03-04', 'Line 04-06', 'Line 05-30', 'Line 06-02', 'Line 06-08', 'Line 08-28', 'Line 09-10', 'Line 09-11', 'Line 10-17', 
                        'Line 10-20', 'Line 10-21', 'Line 10-22', 'Line 12-13', 'Line 12-14', 'Line 12-16', 'Line 14-15', 'Line 15-18', 'Line 16-17', 'Line 18-19', 'Line 19-20', 
                        'Line 22-24', 'Line 23-24', 'Line 24-25', 'Line 25-26', 'Line 25-27', 'Line 27-29', 'Line 29-30', 'Trf B04-B12', 'Trf B06-B09', 'Trf B06-B10', 'Trf B27-28',
                        'Trf G1-B01', 'Trf G2-B02', 'Trf G3-B08', 'Trf G4-B11', 'TrfG5-B18' ],
            "Value": [  0, 0, 0, 0, 0, 0, 0, 0, 33.34159, 0, 
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  
                        0, 0, 0, 0, 0, 0, 0, 0, 0, 0,  
                        0, -1, 0, 0, 0, 0, 0, 0 ],
            "Heatmap Color": [ " " ] * 38
        })


## Set table_A_ICV "Heatmap Color" based on "Value"

def gradient_color_A_ICI(x, min_val=0, max_val=50):
    if x == 0:
        return '<span style="color:#FFFFFFFF">██████</span>'  # White
    elif x == -1:
        return '<span style="color:#D9D9D9">██████</span>'    # Gray
    else:
        # Normalize x between 0 and 1
        ratio = min(max((x - min_val) / (max_val - min_val), 0), 1)
        # Interpolate each channel between yellow (166,201,236) and red (204,0,153)
        r = int(166 * (1 - ratio) + 204 * ratio)
        g = int(201 * (1 - ratio) + 0 * ratio)
        b = int(236 * (1 - ratio) + 153 * ratio)
        hex_color = f'#{r:02X}{g:02X}{b:02X}'
        return f'<span style="color:{hex_color}">██████</span>'

table_A_ICI_1["Heatmap Color"] = table_A_ICI_1["Value"].apply(gradient_color_A_ICI)
table_A_ICI_2["Heatmap Color"] = table_A_ICI_2["Value"].apply(gradient_color_A_ICI)
table_A_ICI_3["Heatmap Color"] = table_A_ICI_3["Value"].apply(gradient_color_A_ICI)
table_A_ICI_4["Heatmap Color"] = table_A_ICI_4["Value"].apply(gradient_color_A_ICI)
table_A_ICI_5["Heatmap Color"] = table_A_ICI_5["Value"].apply(gradient_color_A_ICI)
table_A_ICI_6["Heatmap Color"] = table_A_ICI_6["Value"].apply(gradient_color_A_ICI)
table_A_ICI_7["Heatmap Color"] = table_A_ICI_7["Value"].apply(gradient_color_A_ICI)
table_A_ICI_8["Heatmap Color"] = table_A_ICI_8["Value"].apply(gradient_color_A_ICI)
table_A_ICI_9["Heatmap Color"] = table_A_ICI_9["Value"].apply(gradient_color_A_ICI)
table_A_ICI_10["Heatmap Color"] = table_A_ICI_10["Value"].apply(gradient_color_A_ICI)
table_A_ICI_11["Heatmap Color"] = table_A_ICI_11["Value"].apply(gradient_color_A_ICI)
table_A_ICI_12["Heatmap Color"] = table_A_ICI_12["Value"].apply(gradient_color_A_ICI)
table_A_ICI_13["Heatmap Color"] = table_A_ICI_13["Value"].apply(gradient_color_A_ICI)

## For Ranking worst case 

Ranking_worst_case_1 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08", "Trf B06-B10" , "Trf G5-B18", "Trf G2-B02" ],
})

Ranking_worst_case_2 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08", "Trf B06-B10" , "Trf G5-B18", "Trf G2-B02" ],
})

Ranking_worst_case_3 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08", "Trf B06-B10" , "Trf G5-B18", "Trf B04 - B12" ],
})

Ranking_worst_case_4 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Trf G3 - B08" , "Line 08 - 28", "Trf B06-B10" , "Trf G5-B18", "Trf B04 - B12" ],
})

Ranking_worst_case_5 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08", "Trf B06-B10" , "Trf G5-B18", "Trf B04 - B12" ],
})

Ranking_worst_case_6 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08", "Trf B06-B10" , "Trf G5-B18", "Trf B04 - B12" ],
})

Ranking_worst_case_7 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Trf G3-B08" , "Trf B06-B10" , "Line 08-28" , "Trf G5-B18", "Trf B04 - B12" ],
})

Ranking_worst_case_8 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18", "Trf B04 - B12" ],
})

Ranking_worst_case_9 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18", "Trf G2-B02" ],
})

Ranking_worst_case_10 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18", "Trf B04-B12" ],
})

Ranking_worst_case_11 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18", "Trf G2-B02" ],
})

Ranking_worst_case_12 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18", "Trf G2-B02" ],
})

Ranking_worst_case_13 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18", "Trf B04-B12" ],
})

Ranking_worst_case_14 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf G5-B18" , "Trf B06-B10", "Trf G2-B02" ],
})

Ranking_worst_case_15 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf G5-B18" , "Trf B06-B10", "Trf G2-B02" ],
})

Ranking_worst_case_16 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18" , "Trf G2-B02" ],
})

Ranking_worst_case_17 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf G5-B18" , "Trf B06-B10" , "Trf G2-B02" ],
})

Ranking_worst_case_18 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18"  , "Trf B04-B12" ],
})

Ranking_worst_case_19 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18"  , "Trf G2-B02" ],
})

Ranking_worst_case_20 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf G5-B18" , "Trf B06-B10"  , "Trf G2-B02" ],
})

Ranking_worst_case_21 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Trf G3-B08" , "Line 08-28" , "Trf B06-B10" , "Trf G5-B18" , "Trf B04-B12" ],
})

Ranking_worst_case_22 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18" , "Trf G1-B01" ],
})

Ranking_worst_case_23 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18" , "Trf B04-B12" ],
})

Ranking_worst_case_24 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf G5-B18" , "Trf B06-B10" , "Trf G2-B02" ],
})

Ranking_worst_case_25 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18" , "Trf G2-B02" ],
})

Ranking_worst_case_26 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18" , "Trf B04-B12" ],
})

Ranking_worst_case_27 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18" , "Trf G1-B01" ],
})

Ranking_worst_case_28 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Trf B06-B10" , "Line 08-28" , "Trf G3-B08" , "Trf G5-B18" , "Trf B04-B12" ],
})

Ranking_worst_case_29 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Trf B06-B10" , "Trf G3-B08" , "Trf B04-B12" , "Line 08-28" , "Trf G5-B18"  ],
})

Ranking_worst_case_30 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Trf B06-B10" , "Trf B04-B12" , "Trf G3-B08"  , "Trf G2-B02" , "Trf G5-B18"  ],
})

Ranking_worst_case_31 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Trf B06-B10" , "Trf G3-B08" , "Trf B04-B12" , "Trf G2-B02" , "Line 10-20"  ],
})

Ranking_worst_case_32 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Trf B06-B10" , "Trf B04-B12" , "Trf G3-B08" , "Line 06-08" , "Line 10-20"  ],
})

Ranking_worst_case_33 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Trf B06-B10" , "Trf G3-B08" , "Trf B04-B12" , "Trf G5-B18" , "Trf G2-B02"  ],
})

Ranking_worst_case_34 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Trf B06-B10" , "Trf G3-B08" , "Trf B04-B12" , "Trf G5-B18" , "Trf G1-B01"  ],
})

Ranking_worst_case_35 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Trf B06-B10" , "Trf G3-B08" , "Trf B04-B12" , "Trf G5-B18" , "Trf G2-B02"  ],
})

Ranking_worst_case_36 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Trf B06-B10" , "Trf G3-B08" , "Trf B04-B12" , "Trf G5-B18" , "Line 08-28"  ],
})

Ranking_worst_case_37 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Trf B06-B10" , "Trf G3-B08" , "Trf B04-B12" , "Trf G5-B18" , "Line 08-28"  ],
})

Ranking_worst_case_38 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18" , "Trf B04-B12"  ],
})

Ranking_worst_case_39 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18" , "Trf B04-B12"  ],
})

Ranking_worst_case_40 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18" , "Trf B04-B12"  ],
})

Ranking_worst_case_41 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf B06-B10" , "Trf G3-B08" , "Trf G5-B18" , "Trf B04-B12"  ],
})

Ranking_worst_case_42 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18" , "Trf B04-B12" ],
})

Ranking_worst_case_43 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18" , "Trf B04-B12" ],
})

Ranking_worst_case_44 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18" , "Trf G1-B01" ],
})

Ranking_worst_case_45 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf G5-B18" , "Trf B06-B10" , "Trf G2-B02" ],
})

Ranking_worst_case_46 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf G3-B08" , "Trf B06-B10" , "Trf G5-B18" , "Trf G2-B02" ],
})

Ranking_worst_case_47 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf B06-B10" , "Trf G3-B08" , "Trf G5-B18" , "Trf B04-B12" ],
})

Ranking_worst_case_48 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Trf B06-B10" , "Trf G3-B08" , "Line 08-28" , "Trf G5-B18" , "Trf B04-B12" ],
})

Ranking_worst_case_49 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Trf B06-B10" , "Trf G3-B08" , "Line 08-28" , "Trf G5-B18" , "Trf B04-B12" ],
})

Ranking_worst_case_50 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Line 08-28" , "Trf B06-B10" ,  "Trf G5-B18" , "Trf G3-B08" , "Trf G2-B02" ],
})

Ranking_worst_case_51 = pd.DataFrame({
    "Ranking No.": [ 1, 2, 3, 4, 5 ],
    "Line Name": [ "Trf B06-B10" , "Trf G3-B08" , "Trf B04-B12" , "Trf G5-B18" , "Trf G2-B02" ],
})


ranking_list = [
    Ranking_worst_case_1, Ranking_worst_case_2, Ranking_worst_case_3, Ranking_worst_case_4,
    Ranking_worst_case_5, Ranking_worst_case_6, Ranking_worst_case_7, Ranking_worst_case_8,
    Ranking_worst_case_9, Ranking_worst_case_10, Ranking_worst_case_11, Ranking_worst_case_12,
    Ranking_worst_case_13, Ranking_worst_case_14, Ranking_worst_case_15, Ranking_worst_case_16,
    Ranking_worst_case_17, Ranking_worst_case_18, Ranking_worst_case_19, Ranking_worst_case_20,
    Ranking_worst_case_21, Ranking_worst_case_22, Ranking_worst_case_23, Ranking_worst_case_24,
    Ranking_worst_case_25, Ranking_worst_case_26, Ranking_worst_case_27, Ranking_worst_case_28,
    Ranking_worst_case_29, Ranking_worst_case_30, Ranking_worst_case_31, Ranking_worst_case_32,
    Ranking_worst_case_33, Ranking_worst_case_34, Ranking_worst_case_35, Ranking_worst_case_36,
    Ranking_worst_case_37, Ranking_worst_case_38, Ranking_worst_case_39, Ranking_worst_case_40,
    Ranking_worst_case_41, Ranking_worst_case_42, Ranking_worst_case_43, Ranking_worst_case_44,
    Ranking_worst_case_45, Ranking_worst_case_46, Ranking_worst_case_47, Ranking_worst_case_48,
    Ranking_worst_case_49, Ranking_worst_case_50, Ranking_worst_case_51
]

## For Redispatch and Switching
Switching_1 = pd.DataFrame({
    "Line Name": [ "Line 08-28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch" ]
})

Switching_2 = pd.DataFrame({
    "Line Name": [ "Line 08-28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch" ]
})

Switching_3 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_4 = pd.DataFrame({
    "Line Name": [ "Line 08-28" , "Trf B06-B10" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch" , "Switching : 'All Breakers <br> No Redispatch" ]
})

Switching_5 = pd.DataFrame({
    "Line Name": [ "Line 08-28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch" ]
})

Switching_6 = pd.DataFrame({
    "Line Name": [ "Line 08-28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch" ]
})

Switching_7 = pd.DataFrame({
    "Line Name": [ "Trf B06 - B10" ],
    "Action": [ "Switching : 'All Breakers' <br> No Redispatch" ]
})

Switching_8 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch" ]
})

Switching_9 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch" ]
})

Switching_10 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch" ]
})

Switching_11 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch" ]
})

Switching_12 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch" ]
})

Switching_13 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch" ]
})

Switching_14 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> Redispatch : Can not Redispatch from Gen No.5 because more Overload in Line. Use other way to reduce overload." ]
})

Switching_15 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> Redispatch : Can not Redispatch from Gen No.5 because more Overload in Line. Use other way to reduce overload." ]
})

Switching_16 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_17 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_18 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_19 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_20 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> Redispatch : Can not Redispatch from Gen No.5 because more Overload in Line. Use other way to reduce overload. " ]
})

Switching_21 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" , "Trf B06 - B10" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " , "Switching : All Breakers <br> No Redispatch " ]
})

Switching_22 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_23 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_24 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_25 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_26 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_27 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28" ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_28 = pd.DataFrame({
    "Line Name": [ "Trf B06 - B10" ],
    "Action": [ "Switching : 'All Breakers ' <br> No Redispatch " ]
})

Switching_29 = pd.DataFrame({
    "Line Name": [ "Trf B06 - B10" ],
    "Action": [ "Switching : 'All Breakers ' <br> No Redispatch " ]
})

Switching_30 = pd.DataFrame({
    "Line Name": [ "Trf B06 - B10" ],
    "Action": [ "Switching : 'All Breakers ' <br> Redispatch : 75%% Full Gen " ]
})

Switching_31 = pd.DataFrame({
    "Line Name": [ "Trf B06 - B10" ],
    "Action": [ "Switching : 'All Breakers ' <br> Redispatch : 75%% Full Gen " ]
})

Switching_32 = pd.DataFrame({
    "Line Name": [ "Line 06 - 08" , "Line 10 - 20" , "Line 18 - 19" , "Trf B06 - B10" ],
    "Action": [ "Switching : 'All Breakers ' <br> Redispatch : 75%% Full Gen " , "Switching : 'BKR.B21-B22' & 'BKR.B22-B26 ' <br> No Redispatch " , "Switching : 'All Breakers ' <br> No Redispatch" , "Switching : 'All Breakers ' <br> Redispatch : 90%% Full Gen " ]
})

Switching_33 = pd.DataFrame({
    "Line Name": [ "Line 10 - 20" , "Line 18 - 19" , "Trf B06 - B10" ],
    "Action": [ "Switching : 'BKR.B21-B22' & 'BKR.B22-B26 ' <br> No Redispatch " , "Switching : 'All Breakers ' <br> No Redispatch" , "Switching : 'All Breakers ' <br> Redispatch : 90%% Full Gen " ]
})

Switching_34 = pd.DataFrame({
    "Line Name": [ "Trf B06 - B10" ],
    "Action": [ "Switching : 'All Breakers ' <br> Redispatch : 90%% Full Gen " ]
})

Switching_35 = pd.DataFrame({
    "Line Name": [ "Line 18 - 19" , "Trf B06 - B10" ],
    "Action": [ "Switching : 'All Breakers ' <br> No Redispatch" , "Switching : 'All Breakers ' <br> Redispatch : 75%% Full Gen " ]
})

Switching_36 = pd.DataFrame({
    "Line Name": [ "Trf B06 - B10" ],
    "Action": [ "Switching : 'All Breakers ' <br> No Redispatch " ]
})

Switching_37 = pd.DataFrame({
    "Line Name": [ "Trf B06 - B10" ],
    "Action": [ "Switching : 'All Breakers ' <br> No Redispatch " ]
})

Switching_38 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28"  ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_39 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28"  ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_40 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28"  ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_41 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28"  ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_42 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28"  ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_43 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28"  ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_44 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28"  ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_45 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28"  ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_46 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28"  ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_47 = pd.DataFrame({
    "Line Name": [ "Line 08 - 28"  ],
    "Action": [ "Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' <br> No Redispatch " ]
})

Switching_48 = pd.DataFrame({
    "Line Name": [ " "  ],
    "Action": [ "No Switching <br> No Redispatch " ]
})

Switching_49 = pd.DataFrame({
    "Line Name": [ " "  ],
    "Action": [ "No Switching <br> No Redispatch " ]
})

Switching_50 = pd.DataFrame({
    "Line Name": [ " "  ],
    "Action": [ "No Switching <br> No Redispatch " ]
})

Switching_51 = pd.DataFrame({
    "Line Name": [ "Trf B06 - B10"   ],
    "Action": [ "Switching : 'All Breakers' <br> No Redispatch " ]
})

switching_list = [
    Switching_1, Switching_2, Switching_3, Switching_4, Switching_5, Switching_6, Switching_7, Switching_8,
    Switching_9, Switching_10, Switching_11, Switching_12, Switching_13, Switching_14, Switching_15, Switching_16,
    Switching_17, Switching_18, Switching_19, Switching_20, Switching_21, Switching_22, Switching_23, Switching_24,
    Switching_25, Switching_26, Switching_27, Switching_28, Switching_29, Switching_30, Switching_31, Switching_32,
    Switching_33, Switching_34, Switching_35, Switching_36, Switching_37, Switching_38, Switching_39, Switching_40,
    Switching_41, Switching_42, Switching_43, Switching_44, Switching_45, Switching_46, Switching_47, Switching_48,
    Switching_49, Switching_50, Switching_51
]


#Switching_2 = ( { "Line 08-28 Trip": " Switching : 'BKR.B15-B23' & 'BKR.B21-B22' & 'BKR.B22-B26' " } )
#Switching_53 = ( { "Trf B06-B10 Trip": " Switching All Breakers " } )


st.title("Monitor for Guidelines")
#st.snow()

#str = "Date: " + pd.Timestamp.now().strftime("%d-%m-%Y ")

#col1, col2, col3 = st.columns([2, 1, 1])  # col1 is twice as wide as col2 and col3
col1, col2, col3, col4  = st.columns([ 2.1 , 2.48 , 3 , 3.5 ])

#For Select Line Trip
with col1 :
    str = "Date: 28-05-2657" 
    st.code(str)

    if 'n' not in st.session_state:
        st.session_state.n = 0

    #For Show Time for Test
    str2 = f"{st.session_state.n } Sec."
    st.code(str2)

    Selection = st.selectbox("Select Line Trip", ["Line 06-08 Trip", "Line 10-17 Trip", "Line 10-20 Trip", "Line 10-21 Trip", "Line 12-13 Trip", "Line 12-14 Trip", "Line 18-19 Trip", 
                                                "Line 23-24 Trip", "Line 24-25 Trip", "Line 25-26 Trip", "Line 25-27 Trip", "Trf B04-B12 Trip", "Trf B06-B10 Trip"])

# For Set area in col 2
with col2 :
    st.markdown("####  ")
    st.markdown("####  ")
    st.markdown("####  ")

if Selection == 'Line 06-08 Trip':
    with col1:
        st.markdown("###### *Heatmap Organizer for A_ICV* ")

        # Filter rows where Value != 0
        table_A_ICV_1_nonzero = table_A_ICV_1[table_A_ICV_1["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICV_1_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    with col2:
        st.markdown("###### *Heatmap Organizer for A_ICI* ")
        
        # Filter rows where Value != 0
        table_A_ICI_1_nonzero = table_A_ICI_1[table_A_ICI_1["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICI_1_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)       
     
    with col3:
        st.image('Picture/Line 06-08.png')

if Selection == 'Line 10-17 Trip':
    with col1:
        st.markdown("###### *Heatmap Organizer for A_ICV* ")

        # Filter rows where Value != 0
        table_A_ICV_2_nonzero = table_A_ICV_2[table_A_ICV_2["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICV_2_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    with col2:
        st.markdown("###### *Heatmap Organizer for A_ICI* ")
        
        # Filter rows where Value != 0
        table_A_ICI_2_nonzero = table_A_ICI_2[table_A_ICI_2["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICI_2_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)       
     
    with col3:
        st.image('Picture/Line 10-17.png')

if Selection == 'Line 10-20 Trip':
    with col1:
        st.markdown("###### *Heatmap Organizer for A_ICV* ")

        # Filter rows where Value != 0
        table_A_ICV_3_nonzero = table_A_ICV_3[table_A_ICV_3["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICV_3_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    with col2:
        st.markdown("###### *Heatmap Organizer for A_ICI* ")
        
        # Filter rows where Value != 0
        table_A_ICI_3_nonzero = table_A_ICI_3[table_A_ICI_3["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICI_3_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)       
     
    with col3:
        st.image('Picture/Line 10-20.png')

if Selection == 'Line 10-21 Trip':
    with col1:
        st.markdown("###### *Heatmap Organizer for A_ICV* ")

        # Filter rows where Value != 0
        table_A_ICV_4_nonzero = table_A_ICV_4[table_A_ICV_4["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICV_4_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    with col2:
        st.markdown("###### *Heatmap Organizer for A_ICI* ")
        
        # Filter rows where Value != 0
        table_A_ICI_4_nonzero = table_A_ICI_4[table_A_ICI_4["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICI_4_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)       
     
    with col3:
        st.image('Picture/Line 10-21.png')

if Selection == 'Line 12-13 Trip':
    with col1:
        st.markdown("###### *Heatmap Organizer for A_ICV* ")

        # Filter rows where Value != 0
        table_A_ICV_5_nonzero = table_A_ICV_5[table_A_ICV_5["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICV_5_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    with col2:
        st.markdown("###### *Heatmap Organizer for A_ICI* ")
        
        # Filter rows where Value != 0
        table_A_ICI_5_nonzero = table_A_ICI_5[table_A_ICI_5["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICI_5_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)       
     
    with col3:
        st.image('Picture/Line 12-13.png')

if Selection == 'Line 12-14 Trip':
    with col1:
        st.markdown("###### *Heatmap Organizer for A_ICV* ")

        # Filter rows where Value != 0
        table_A_ICV_6_nonzero = table_A_ICV_6[table_A_ICV_6["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICV_6_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    with col2:
        st.markdown("###### *Heatmap Organizer for A_ICI* ")
        
        # Filter rows where Value != 0
        table_A_ICI_6_nonzero = table_A_ICI_6[table_A_ICI_6["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICI_6_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)       
     
    with col3:
        st.image('Picture/Line 12-14.png')

if Selection == 'Line 18-19 Trip':
    with col1:
        st.markdown("###### *Heatmap Organizer for A_ICV* ")

        # Filter rows where Value != 0
        table_A_ICV_7_nonzero = table_A_ICV_7[table_A_ICV_7["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICV_7_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    with col2:
        st.markdown("###### *Heatmap Organizer for A_ICI* ")
        
        # Filter rows where Value != 0
        table_A_ICI_7_nonzero = table_A_ICI_7[table_A_ICI_7["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICI_7_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)       
     
    with col3:
        st.image('Picture/Line 18-19.png')

if Selection == 'Line 23-24 Trip':
    with col1:
        st.markdown("###### *Heatmap Organizer for A_ICV* ")

        # Filter rows where Value != 0
        table_A_ICV_8_nonzero = table_A_ICV_8[table_A_ICV_8["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICV_8_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    with col2:
        st.markdown("###### *Heatmap Organizer for A_ICI* ")
        
        # Filter rows where Value != 0
        table_A_ICI_8_nonzero = table_A_ICI_8[table_A_ICI_8["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICI_8_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)       
     
    with col3:
        st.image('Picture/Line 23-24.png')

if Selection == 'Line 24-25 Trip':
    with col1:
        st.markdown("###### *Heatmap Organizer for A_ICV* ")

        # Filter rows where Value != 0
        table_A_ICV_9_nonzero = table_A_ICV_9[table_A_ICV_9["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICV_9_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    with col2:
        st.markdown("###### *Heatmap Organizer for A_ICI* ")
        
        # Filter rows where Value != 0
        table_A_ICI_9_nonzero = table_A_ICI_9[table_A_ICI_9["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICI_9_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)       
     
    with col3:
        st.image('Picture/Line 24-25.png')

if Selection == 'Line 25-26 Trip':
    with col1:
        st.markdown("###### *Heatmap Organizer for A_ICV* ")

        # Filter rows where Value != 0
        table_A_ICV_10_nonzero = table_A_ICV_10[table_A_ICV_10["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICV_10_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    with col2:
        st.markdown("###### *Heatmap Organizer for A_ICI* ")
        
        # Filter rows where Value != 0
        table_A_ICI_10_nonzero = table_A_ICI_10[table_A_ICI_10["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICI_10_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)       
     
    with col3:
        st.image('Picture/Line 25-26.png')

if Selection == 'Line 25-27 Trip':
    with col1:
        st.markdown("###### *Heatmap Organizer for A_ICV* ")

        # Filter rows where Value != 0
        table_A_ICV_11_nonzero = table_A_ICV_11[table_A_ICV_11["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICV_11_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    with col2:
        st.markdown("###### *Heatmap Organizer for A_ICI* ")
        
        # Filter rows where Value != 0
        table_A_ICI_11_nonzero = table_A_ICI_11[table_A_ICI_11["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICI_11_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)       
     
    with col3:
        st.image('Picture/Line 25-27.png')

if Selection == 'Trf B04-B12 Trip':
    with col1:
        st.markdown("###### *Heatmap Organizer for A_ICV* ")

        # Filter rows where Value != 0
        table_A_ICV_12_nonzero = table_A_ICV_12[table_A_ICV_12["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICV_12_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    with col2:
        st.markdown("###### *Heatmap Organizer for A_ICI* ")
        
        # Filter rows where Value != 0
        table_A_ICI_12_nonzero = table_A_ICI_12[table_A_ICI_12["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICI_12_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)       
     
    with col3:
        st.image('Picture/Trf B04-B12.png')

if Selection == 'Trf B06-B10 Trip':
    with col1:
        st.markdown("###### *Heatmap Organizer for A_ICV* ")

        # Filter rows where Value != 0
        table_A_ICV_13_nonzero = table_A_ICV_13[table_A_ICV_13["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICV_13_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)
    
    with col2:
        st.markdown("###### *Heatmap Organizer for A_ICI* ")
        
        # Filter rows where Value != 0
        table_A_ICI_13_nonzero = table_A_ICI_13[table_A_ICI_13["Value"] != 0]

        # Display only nonzero rows in the HTML table
        st.markdown(custom_css + table_A_ICI_13_nonzero.to_html(escape=False, index=False), unsafe_allow_html=True)       
     
    with col3:
        st.image('Picture/Trf B06-B10.png')
 

# Calculate which set to show every 15 seconds
interval = 15
idx = int(st.session_state.n // interval)
if idx >= len(ranking_list):
    idx = len(ranking_list)  # Prevent index out of range

with col4:
    st.markdown("###### *Ranking worst case* ")
    st.markdown(custom_css + ranking_list[idx].to_html(escape=False, index=False), unsafe_allow_html=True)

    st.markdown("###### *Switching and Redispatch* ")
    st.markdown(custom_Redispatch + switching_list[idx].to_html(escape=False, index=False), unsafe_allow_html=True)



#st.success('This is a success message!', icon="🟧")

st.write(
    " "
)

st.write(
    " "
)

st.write(
    " "
)

st.write(
    " "
)

st.write(
    " "
)

st.success("Let's start building! For help and inspiration, head over to [docs.streamlit.io](https://docs.streamlit.io/).")
st.success("If you want a codes, can download at my Github (https://github.com/pluem34/blank-app.git).")


# For update data every 7.5 sec.
time.sleep(7.5)
st.session_state.n += 7.5
st.rerun()
