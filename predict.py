import streamlit as st 
import pickle 
import numpy as np
import pandas as pd
from streamlit_option_menu import option_menu

def load_model():
    with open("rom_num.pkl", 'rb') as file:
     data = pickle.load(file)
    return data 

data = load_model()
    
regressor = data["model"]


def show_predict_page():

   
   # horizontal menu tab
   selected = option_menu(
      menu_title = None,
      options=["Home", "Predict", "Explore"],
      icons=["house","airplane-engines-fill","bar-chart-steps"],
      menu_icon="cast",
      default_index=0,
      orientation="horizontal",    
      styles ={
         "container":{"padding": "01important", "background-color": "black"},
         "icon":{"color":"white", "Font-size": "25px"},
         "nav-link":{
            "font-size":"25px",
            "text-align":"left",
            "margin":"0px",
            "--hover-color":"#eee",
         },
         "nav-link-selected": {"background-color": "magenta"},
      },
   )
   df=pd.read_csv("datacfd.csv")

   #Different pages

   if selected == "Predict":     
     st.title("Scramjet Engine Simulation")

     st.write("")
     st.write("""### Enter engine's design variables  """)

     st.write("")

     machno = (
        "12",
        "13",
        "14",
        "15",
        "16",
        "17",
        "18",
        "19",
        "20",
        "21",
        "22",
        "23",
        "24",
     )

     
   
     
   
     CH = st.slider("Combustion Chamber Height (m)", 6.8 , 12.8)
     st.write("")
     
        


     mach = st.selectbox( "Strut Wedge Angle (Degree)",machno)
     st.write("")

        
   
     WD = st.slider("Top Wall Displacemnt (m)", 30.2, 90.2)
  


     #FP_activate = st.toggle("Activate to add Fuel Pressure ")
    # FP = st.slider("Freestream Temperature (K)", 200, 350)
    # st.write("")

    # altitiude_activate = st.toggle("Activate to add altitude ")
   #  altitude = st.number_input("Altitude (m)")

     st.write("")
     st.write("")

     ok = st.button("Calculate Outputs") 

     if ok:
        X = np.array([[mach,CH,WD]])

        y_final= regressor.predict(X)

        value1=y_final[0]
        value2=y_final[5]
        value3=y_final[4]
        value4=y_final[6]
        value5=y_final[1]
     
        st.write("The Outlet Mach Number is",value1)
        st.write("The Outlet Temperature is",value2)
        st.write("The Outlet Pressure is",value3)
        st.write("The Engine's Performance Efficiency is",value4)
        st.write("The Produced Oblique Shock Angle is",value5)

   if selected == "Home":
      st.title("Predict --> Optimise Engine Efficiency")
      st.title("Explore --> Analyse Engine CHaracteristics")

   if selected == "Explore":
      st.title(f"Explore Relativity in Predictions")
      st.write()
      st.write()
      
      st.write(
         """

      ### Total Pressure Relative to Intake Length 
      """
      )
      data1=df.groupby(["Top wall distance"])["Total Pressure"].mean().sort_values(ascending=True)
      ax = st.line_chart(data1)

      st.write(
         """

      ### Total Mach Number relative to Combustion Chamber Height 
      """
      )

      data2=df.groupby(["Combustion chamber height"])["Mach at outlet chamber"].mean().sort_values(ascending=True)
      st.scatter_chart(data2)

      st.write(
         """

      ### Total Temperature Relative to Combustion Chamber Height
      """
      )

      data3=df.groupby(["Combustion chamber height"])["Total Temperature"].mean().sort_values(ascending=True)
      st.bar_chart(data3)

      st.write(
         """

      ### Shock Angle Relative to Strut wedge angle
      """
      )

      data4=df.groupby(["Strut wedge angle"])["Shock angle"].mean().sort_values(ascending=True)
      ax = st.scatter_chart(data4)
      

