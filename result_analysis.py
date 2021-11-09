#RESULT ANALYSIS
import tkinter as tk
from tkinter import messagebox

class ResultAnalysis():
    
    analysis_colour = {"Low" : "#00FFFF", "Normal" : "#32CD32", "Good" : "#138808",
                 "Fair" : "#FFFF00", "Borderline" : "#FF4500", "At Risk" : "#FF4500",
                 "High" : "#FF0000", "Very High" : "#8B0000", "Underweight" : "#00FFFF" ,
                 "Overweight" : "#FF0000", "Obese" : "#8B0000", "Neutral" : "#D5D5D5"}
    
    def __init__(self, test_details_list):
        self.test_details_list = []
        if len(test_details_list) >= 6: # FAMILY HISTORY IS INCLUDED CURRENTLY, MAKING THE VARIABLES 7, ORDINARILY 6 VARIABLES ARE ONLY NEEDED, WHICH WOULD BE ANALYSED
            self.test_details_list = test_details_list
            
        else:
            tk.messagebox.showerror(title="Blank Box", message="All Test Details are required for detection!")
            quit()  # OR exit() -- same function
        
        self.glucose_colour = None
        self.cholesterol_colour = None
        self.blood_pressure_colour = None
        self.hdl_colour = None
        self.triglyceride_colour = None
        self.bmi_colour = None

    ############################## GLUCOSE ##########################
    def glucose_analysis(self):         # Normal 70 mg/dL (3.9 mmol/L) - 100 mg/dL (5.6 mmol/L)
        glucose_level = int(self.test_details_list[1])
        
        if glucose_level in range(70, 101):    
            g_level = "Normal"
            
        elif glucose_level in range(101, 126):  # Mediun 100mg/dL (6.9 mmol/L) to 125 mg/dL (5.6mmol/L)
            g_level = "At Risk"
            
        elif glucose_level >= 126:      #If fasting blood glucose is 126 mg/dL (7 mmol/L) or higher on two separate tests, diabetes is diagnosed. 
            g_level = "High"
            
        else:
            g_level = "Neutral"

        self.glucose_colour = ResultAnalysis.analysis_colour[g_level]
        
        return g_level

    #####################################################################
    

    ############################## CHOLESTEROL ##########################
    def cholesterol_analysis(self):
        cholesterol_level = int(self.test_details_list[2])
        
        if cholesterol_level <= 200:    
            ch_level = "Normal"
            
        elif cholesterol_level in range(200, 240):
            ch_level = "Borderline"
            
        elif cholesterol_level >= 240: 
            ch_level = "High"
            
        else:
            ch_level = "Neutral"

        self.cholesterol_colour = ResultAnalysis.analysis_colour[ch_level]
        
        return ch_level

    #####################################################################
    
    
    ############################## BLOOD PRESSURE ##########################
    def blood_pressure_analysis(self):
        blood_pressure_level = int(self.test_details_list[3])
        
        if blood_pressure_level < 150:
            bp_level = "Low"
        
        elif blood_pressure_level <= 200:   
            bp_level = "Normal"
            
        elif blood_pressure_level in range(201, 229):
            bp_level = "At Risk"
            
        elif blood_pressure_level >= 230: 
            bp_level = "High"
            
        else:
            bp_level = "Neutral"
            
        self.blood_pressure_colour = ResultAnalysis.analysis_colour[bp_level]
        
        return bp_level

    #############################################################################
    
    
    ############################## HIGH DENSITY LIPROPROTEIN ##########################
    def hdl_analysis(self, gender):
        hdl_level = int(self.test_details_list[4])
        
        if gender == "Male":
            if hdl_level > 40:
                HDL_level = "Good"
            
            elif hdl_level <= 40:   
                HDL_level = "Fair"
                
            else:
                HDL_level = "Neutral"
                
        elif gender == "Female":
            if hdl_level > 50:
                HDL_level = "Good"
            
            elif hdl_level <= 40:   
                HDL_level = "Fair"
                
            else:
                HDL_level = "Neutral"
        else:
            HDL_level = "Neutral"
            
        self.hdl_colour = ResultAnalysis.analysis_colour[HDL_level]
        
        return HDL_level
    
    #############################################################################
    

    #####################################################################
    def triglyceride_analysis(self):
        triglyceride_level = int(self.test_details_list[5])
         
        if triglyceride_level < 150:
            tg_level = "Normal"
        
        elif triglyceride_level in range(150, 200):   
            tg_level = "Borderline"
            
        elif triglyceride_level in range(200, 500):
            tg_level = "High"
            
        elif triglyceride_level >= 500: 
            tg_level = "Very High"
            
        else:
            tg_level = "Neutral"

        self.triglyceride_colour = ResultAnalysis.analysis_colour[tg_level]
        
        return tg_level
   

    #####################################################################
    

    ########################## BODY MASS INDEX ############################
    def bmi_analysis(self):
        body_mass_index_level = eval(self.test_details_list[6])
        
        if body_mass_index_level < 18.5:
            bmi_level = "Underweight"
        
        elif 18.5 <= body_mass_index_level <= 24.9:         #in range(18.5, 25):   
            bmi_level = "Normal"
            
        elif 25 <= body_mass_index_level <= 30:             #in range(25, 30):
            bmi_level = "Overweight"
            
        elif body_mass_index_level >= 30: 
            bmi_level = "Obese"
            
        else:
            bmi_level = "Neutral"

        self.bmi_colour = ResultAnalysis.analysis_colour[bmi_level]
        
        return bmi_level

    #####################################################################

'''
bb=[1, 281, 135, 312, 56, 234, 56]
test = ResultAnalysis(bb)
print(test.glucose_analysis())
print(test.glucose_colour)

'''
