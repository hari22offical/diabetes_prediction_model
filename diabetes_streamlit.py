# -*- coding: utf-8 -*-
"""
Created on Sun Jan 15 19:31:53 2023

@author: harin
"""

import pickle 
import streamlit as st

lod=pickle.load(open("C:/Users/harin/Pictures/diabetes_model.sav","rb"))


def status( vari ):
    vari1=np.asarray(vari)
    vari2=vari1.reshape(1,-1)
    predi=lod.predict(vari2)
    print(predi)
    
    if(predi[0]==1):
        return "HE/SHE WILL  NOT HAVE DIABETES"
    else:
        return "HE/SHE WILL HAVE DIABETES"
    
def main():
     st.title("DIABETES_PREDICTION_MODEL")
     Pregnancies=st.number_input("enter no of Pregnancies")
     Glucose=st.number_input("enter the Glucose level")
     BloodPressure=st.number_input("enter the BloodPressure	level")
     Insulin=st.number_input("enter the Insulin level")
     BMI=st.number_input("enter the BMI level")
     DiabetesPedigreeFunction=st.number_input("enter the DiabetesPedigreeFunction")
     
     vari3=""
     
     if(st.button("predict")):
         vari3=status(["Pregnancies","Glucose","BloodPressure","Insulin","BMI","DiabetesPedigreeFunction"])
         
         
         
     st.success(vari3)
         
         
if __name__=='__main__':
    main()
     
     
     