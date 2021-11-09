import tkinter as tk
from tkinter import *
import random

#to be called in the model script --- maybe, still thinking though

class ResultDisplay():
    from date_time import Timestamp
    TS = Timestamp()
    stamp = TS.timestamp()
    
    #global current_result_window
    current_result_window = True
    
    def __init__(self, parentWindow, info_dict):
        
        from result_analysis import ResultAnalysis
        test_analysis = ResultAnalysis(info_dict["testDetails"])

        self.result_window = tk.Toplevel(parentWindow)
        self.result_window.title("Result Window")
        self.result_window.iconbitmap("img/dds1.ico")

        self.result_window.lift()#attributes("-topmost", True)
        
        self.result_window.geometry("900x700+240+22")
        self.result_window.configure(bg="#A0A0A0")

        self.result_window.overrideredirect(True)

        self.info_dict = info_dict
        
        #SPLIT THE DICTIONARY INTO PATIENT INFORMATION, TEST DETAILS AND DIAGNOSIS RESULT
        #   structure of info_dict, found in [gui_main module]
        #       {"patientDetails" : pd, "testDetails" : td, "diagnosis" : diag}
        
        self.PD = self.info_dict["patientDetails"]
        self.TD = self.info_dict["testDetails"]
        self.DIAG = self.info_dict["diagnosis"]
        
        self.PNames = ""
        for i in range(len(self.PD) - 2):   # Removes age and gender values from the names
            self.PNames += self.PD[i].capitalize() + "   "

        self.PAge = self.info_dict["patientDetails"][-2]
        self.PGender = self.info_dict["patientDetails"][-1]
        #print(self.PGender)
            

        #####################################################################333
        
        self.bg_lbl = "#D5D5D5"
        self.fg_lbl = "#000000"
        
        self.bd_lbl = 1
        self.font1 = ("times", 14, "bold")
        self.lbl_relief1 = tk.FLAT
        self.lbl_padx = (0, 0)
        self.ent_width1 = 4
        self.ent_bg = "#FFFFFF"
        self.ent_relief = tk.FLAT
        self.ent_padx = (0, 10)
        self.ent_ipadx = 5
        self.ent_sticky = "nsew"
        #self.lbl_ent_pady =
        
        #INDEX IS GOTTEN FROM MODEL
        self.diag_colour = ["#32CD32", "#FF0000"]
        self.diag_col_index = self.DIAG
        
        self.result_frm = tk.Frame(self.result_window, relief=tk.FLAT, bd=2, bg="#AABBCC") #CONTAINER FOR EVERYTHING ON THE WINDOW
        self.result_frm.pack(fill=tk.BOTH)
        
        self.result_frm.rowconfigure(0, weight=1, minsize=30)   #
        self.result_frm.rowconfigure(1, weight=1, minsize=20)
        self.result_frm.rowconfigure(2, weight=1, minsize=582)
        self.result_frm.rowconfigure(3, weight=1, minsize=40)  #  
        #self.result_frm.rowconfigure(4, weight=1, minsize=30) 

        self.result_frm.columnconfigure(0, weight=1, minsize=60)
        self.result_frm.columnconfigure(1, weight=0, minsize=600)
        self.result_frm.columnconfigure(2, weight=1, minsize=60) 
        #self.result_frm.columnconfigure(3, weight=1, minsize=50)
        #self.result_frm.columnconfigure(4, weight=1, minsize=30)

        result_frm_cs = 3   # CS --> columnspan
        #'''

        self.title = tk.Label(self.result_frm, text="Diabetes Detection System", relief=tk.FLAT, bd=0,
                              bg="#000AFF", fg="#FFFFFF", font=("cambria", 20, "bold")) #Alex Brush
        self.title.grid(row=0, column=0, columnspan=result_frm_cs, sticky="nsew")

        self.btns_frm = tk.Frame(self.result_frm, relief=tk.FLAT, bd=2, bg="#AABBCC")    
        self.btns_frm.grid(row=3, column=1, pady=(10, 5), sticky="nsew")

        self.btns_frm.rowconfigure(0, weight=1, minsize=30)
        self.btns_frm.columnconfigure([0, 1, 2, 3, 4, 5], weight=1, minsize=50)

        self.close_btn = tk.Button(self.btns_frm, text="Close", bg="#FFFFFF", relief=tk.GROOVE,
                               bd=2, font=("time", 16, "bold"), command=lambda: self.result_window.destroy())
        self.close_btn.grid(row=0, column=0, ipadx=10, padx=(0, 0), ipady=2, pady=(0, 0), sticky="s")
        
        
        self.print_btn = tk.Button(self.btns_frm, text="Print", bg="#FFFFFF", relief=tk.GROOVE,
                               bd=2, font=("time", 16, "bold"), command=lambda: None)
        self.print_btn.grid(row=0, column=5, ipadx=10, padx=(0, 0), ipady=2, pady=(0, 0), sticky="s")
        

        self.save_btn = tk.Button(self.btns_frm, text="Save", bg="#FFFFFF", relief=tk.GROOVE,
                               bd=2, font=("time", 16, "bold"), command=lambda: None)
        self.save_btn.grid(row=0, column=4, ipadx=10, padx=(0, 0), ipady=2, pady=(0, 0), sticky="s")
        

        #RESULT FORM
        self.result_form = tk.Frame(self.result_frm, relief=tk.FLAT, bd=2, bg="#FFFFFF")    #ROW 2 NOTHING IN ROW 3
        self.result_form.grid(row=2, column=1, sticky="nsew")

        rf_w = 1
        self.result_form.rowconfigure(0, weight=0, minsize=30)  
        self.result_form.rowconfigure(1, weight=rf_w, minsize=60) # FOR self.patient_details_frm
        self.result_form.rowconfigure(2, weight=rf_w, minsize=10)
        self.result_form.rowconfigure(3, weight=rf_w, minsize=300) # self.result_form_inner
        self.result_form.rowconfigure(4, weight=rf_w, minsize=10)
        self.result_form.rowconfigure(5, weight=rf_w, minsize=40) #DIAGNOSIS COMMENT
        self.result_form.rowconfigure(6, weight=0, minsize=30)
        
        self.result_form.columnconfigure(1, weight=rf_w, minsize=400)
        self.result_form.columnconfigure([0, 2], weight=rf_w, minsize=50)

        self.result_heading = tk.Label(self.result_form, text="Diagnosis Result", relief=tk.FLAT, bd=0, bg=self.diag_colour[self.diag_col_index],
                                       fg="#FFFFFF", font=("Alex Brush", 25, "bold"))
        self.result_heading.grid(row=0, column=0, columnspan=3, sticky="nsew")

        #PATIENT PERSONAL DETAILS FRAME
        self.patient_details_frm = tk.Frame(self.result_form, relief=tk.GROOVE, bd=1, bg="#FFFFFF") #ROW 0
        self.patient_details_frm.grid(row=1, column=0, columnspan=3, sticky="nsew") 

        self.patient_details_frm.rowconfigure([0, 1, 2], weight=1, minsize=20)
        self.patient_details_frm.columnconfigure([0, 1, 2, 3, 4, 5], weight=1, minsize=80)

        self.name_relief = tk.FLAT#GROOVE
        self.name_bd = 1
        self.name_bg = "#FFFFFF"
        self.name_fg = "#000000"
        self.name_sticky = "w"
        self.name_font = ("Times", 13, "bold") #Kartika
        font_detail_lbl = ("Times", 12, "normal")  # aller

        # NAME, AGE, GENDER, DATE AND TIME LABELS
        '''self.name_detail_lbl = tk.Label(self.patient_details_frm, text="Name:", relief=tk.SUNKEN, bd=0, bg=self.name_bg, font=font_detail_lbl) #"#9999FF"
        self.name_detail_lbl.grid(row=0, column=1, sticky="e")  '''
        
        full_name = f"Name:  {self.PNames}"
        p_age = f"Age:  {self.PAge}"
        p_gender = f"Gender:  {self.PGender}"
        
        self.full_name_lbl = tk.Label(self.patient_details_frm, text=full_name, relief=self.name_relief,
                                       bd=self.name_bd, bg=self.name_bg, fg=self.name_fg, font=self.name_font, justify="center")
        self.full_name_lbl.grid(row=0, column=1, columnspan=4, ipadx=0, sticky="ew")

        #self.age_detail_lbl = tk.Label(self.patient_details_frm, text="Age:", relief=tk.FLAT,
        #                                  bd=0, bg=self.name_bg, font=font_detail_lbl)  #"#000AFF"
        #self.age_detail_lbl.grid(row=1, column=1, sticky="e")

        self.age_lbl = tk.Label(self.patient_details_frm, text=p_age, relief=tk.FLAT,
                                        bd=self.name_bd, bg=self.name_bg, fg=self.name_fg, font=self.name_font, justify="center")
        self.age_lbl.grid(row=1, column=2, ipadx=10, sticky=self.name_sticky)
        
        #self.gender_detail_lbl = tk.Label(self.patient_details_frm, text="Gender:", relief=tk.FLAT,
        #                                  bd=0, bg=self.name_bg, font=font_detail_lbl)  #"#000AFF"
        #self.gender_detail_lbl.grid(row=1, column=3, sticky="e")

        self.gender_lbl = tk.Label(self.patient_details_frm, text=p_gender, relief=tk.FLAT,
                                        bd=self.name_bd, bg=self.name_bg, fg=self.name_fg, font=self.name_font, justify="center")
        self.gender_lbl.grid(row=1, column=3, ipadx=10, sticky=self.name_sticky)

        #Time and Date
        stamp = ResultDisplay.stamp #Stamp is a class (ResultDisplay) attribute
        time_hr = int(stamp[3])
        
        # ADD AM OR PM TO THE TIME
        if 24 > time_hr >= 13:
            time_hr -= 12
            time = f"Time:  {time_hr} : {stamp[4]} : {stamp[5]} PM"
            
        elif time_hr == 24:
            time_hr -= 12
            time = f"Time:  {time_hr} : {stamp[4]} : {stamp[5]} AM"
        else:
            time = f"Time:  {time_hr} : {stamp[4]} : {stamp[5]} AM"
            
        date = f"Date:  {stamp[2]}/{stamp[1]}/{stamp[0]}"
        
        datetime_relief = tk.FLAT
        datetime_bg = "#FFFFFF"
        
        '''self.date_detail_lbl = tk.Label(self.patient_details_frm, text="Date:", relief=datetime_relief,
                                        bd=2, bg=datetime_bg, font=font_detail_lbl, justify="right")
        self.date_detail_lbl.grid(row=2, column=1, sticky="e")'''

        self.date_lbl = tk.Label(self.patient_details_frm, text=date, relief=datetime_relief,
                                 bd=2, bg=datetime_bg, font=font_detail_lbl, justify="right")
        self.date_lbl.grid(row=2, column=2, columnspan=1, sticky="w")

        '''self.time_detail_lbl = tk.Label(self.patient_details_frm, text="Time:", relief=datetime_relief,
                                        bd=2, bg=datetime_bg, font=font_detail_lbl, justify="right")
        self.time_detail_lbl.grid(row=2, column=3, columnspan=1, sticky="e")'''

        self.time_lbl = tk.Label(self.patient_details_frm, text=time, relief=datetime_relief,
                                 bd=2, bg=datetime_bg, font=font_detail_lbl, justify="right")
        self.time_lbl.grid(row=2, column=3, ipadx=15, sticky="w")        
        
        ###############****************************************####################        
        
        #RESULT DETAILS FRAME
        #Parent Frame [self.result_form] column 1 = 400
        self.result_form_inner = tk.Frame(self.result_form, relief=tk.FLAT, bd=2, bg="#AFAFAF")
        self.result_form_inner.grid(row=3, column=1, sticky="nsew")

        self.result_form_inner.rowconfigure(list(range(7)), weight=1, minsize=20)
        #self.result_form_inner.rowconfigure([0, 1, 3, 5, 7, 9, 11], weight=1, minsize=20) #400
        #self.result_form_inner.rowconfigure([2, 4, 6, 8, 12], weight=1, minsize=20)
        
        self.result_form_inner.columnconfigure(0, weight=1, minsize=120) #600
        self.result_form_inner.columnconfigure(1, weight=1, minsize=120)
        self.result_form_inner.columnconfigure(2, weight=1, minsize=120)

        # rfi_pady -- result_form_inner pady
        rfi_pady = (10, 0)
        self.lbl_sticky = "nsew"

        #******** TEST FEATURE HEADING ********************
        self.test_features_lbl = tk.Label(self.result_form_inner, text="Features", bg="#000AFF", fg="#FFFFFF",
                               relief=self.lbl_relief1, bd=self.bd_lbl, font=self.font1, justify="center")
        self.test_features_lbl.grid(row=0, column=0, padx=(0, 0), pady=(0, 0), sticky="nsew")
        #*********************************************

        self.glucose_lbl = tk.Label(self.result_form_inner, text="Glucose", bg=self.bg_lbl, fg=self.fg_lbl,
                               relief=self.lbl_relief1, bd=self.bd_lbl, font=self.font1, justify="center")
        self.glucose_lbl.grid(row=1, column=0, padx=self.lbl_padx, pady=rfi_pady, sticky=self.lbl_sticky)

        self.cholesterol_lbl = tk.Label(self.result_form_inner, text="Cholesterol", bg=self.bg_lbl, fg=self.fg_lbl,
                                   relief=self.lbl_relief1, bd=self.bd_lbl, font=self.font1, justify="center")
        self.cholesterol_lbl.grid(row=2, column=0, padx=self.lbl_padx, pady=rfi_pady, sticky=self.lbl_sticky)

        self.blood_pressure_lbl = tk.Label(self.result_form_inner, text="Blood Pressure", bg=self.bg_lbl, fg=self.fg_lbl,
                                      relief=self.lbl_relief1, bd=self.bd_lbl, font=self.font1, justify="center")
        self.blood_pressure_lbl.grid(row=3, column=0, padx=self.lbl_padx, pady=rfi_pady, sticky=self.lbl_sticky)

        self.high_density_lipoprotein_lbl = tk.Label(self.result_form_inner, text="High Density Lipoprotein", bg=self.bg_lbl, fg=self.fg_lbl,
                                                relief=self.lbl_relief1, bd=self.bd_lbl, font=self.font1, justify="center")
        self.high_density_lipoprotein_lbl.grid(row=4, column=0, ipadx=4, padx=self.lbl_padx, pady=rfi_pady, sticky=self.lbl_sticky)

        self.triglyceride_lbl = tk.Label(self.result_form_inner, text="Triglyceride", bg=self.bg_lbl, fg=self.fg_lbl,
                                    relief=self.lbl_relief1, bd=self.bd_lbl, font=self.font1, justify="center")
        self.triglyceride_lbl.grid(row=5, column=0, padx=self.lbl_padx, pady=rfi_pady, sticky=self.lbl_sticky)

        self.body_mass_index_lbl = tk.Label(self.result_form_inner, text="Body Mass Index", bg=self.bg_lbl, fg=self.fg_lbl,
                                       relief=self.lbl_relief1, bd=self.bd_lbl, font=self.font1, justify="center")
        self.body_mass_index_lbl.grid(row=6, column=0, padx=self.lbl_padx, pady=rfi_pady, sticky=self.lbl_sticky)

        #******** TEST VALUES HEADING ********************
        self.test_values_lbl = tk.Label(self.result_form_inner, text="Value", bg="#000AFF", fg="#FFFFFF",
                               relief=self.lbl_relief1, bd=self.bd_lbl, font=self.font1, justify="center")
        self.test_values_lbl.grid(row=0, column=1, padx=(0, 0), pady=(0, 0), sticky="nsew")
        #*********************************************
        
        self.glucose_ent = tk.Entry(self.result_form_inner, width=self.ent_width1, bg=self.ent_bg,
                                    relief=self.ent_relief, font=self.font1, justify="center")
        self.glucose_ent.grid(row=1, column=1, padx=self.ent_padx, pady=rfi_pady, sticky=self.ent_sticky)
        self.glucose_ent.insert(0, str(self.TD[1]) + " mg/dL")
        self.glucose_ent.config(state=tk.DISABLED)       

        self.cholesterol_ent = tk.Entry(self.result_form_inner, width=self.ent_width1, bg=self.ent_bg,
                                        relief=self.ent_relief, font=self.font1, justify="center")
        self.cholesterol_ent.grid(row=2, column=1, padx=self.ent_padx, pady=rfi_pady, sticky=self.ent_sticky)
        self.cholesterol_ent.insert(0, str(self.TD[2]) + " mg/dL")
        self.cholesterol_ent.config(state=tk.DISABLED)

        self.blood_pressure_ent = tk.Entry(self.result_form_inner, width=self.ent_width1, bg=self.ent_bg,
                                           relief=self.ent_relief, font=self.font1, justify="center")
        self.blood_pressure_ent.grid(row=3, column=1, padx=self.ent_padx, pady=rfi_pady, sticky=self.ent_sticky)
        self.blood_pressure_ent.insert(0, str(self.TD[3]) + " mmHg")
        self.blood_pressure_ent.config(state=tk.DISABLED)

        self.high_density_lipoprotein_ent = tk.Entry(self.result_form_inner, width=self.ent_width1, bg=self.ent_bg,
                                                     relief=self.ent_relief, font=self.font1, justify="center")
        self.high_density_lipoprotein_ent.grid(row=4, column=1, padx=self.ent_padx, pady=rfi_pady, sticky=self.ent_sticky)
        self.high_density_lipoprotein_ent.insert(0, str(self.TD[4]) + " mg/dL")
        self.high_density_lipoprotein_ent.config(state=tk.DISABLED)

        self.triglyceride_ent = tk.Entry(self.result_form_inner, width=self.ent_width1, bg=self.ent_bg,
                                         relief=self.ent_relief, font=self.font1, justify="center")
        self.triglyceride_ent.grid(row=5, column=1, padx=self.ent_padx, pady=rfi_pady, sticky=self.ent_sticky)
        self.triglyceride_ent.insert(0, str(self.TD[5]) + " mg/dL")
        self.triglyceride_ent.config(state=tk.DISABLED)

        self.body_mass_index_ent = tk.Entry(self.result_form_inner, width=self.ent_width1, bg=self.ent_bg,
                                            relief=self.ent_relief, font=self.font1, justify="center")
        self.body_mass_index_ent.grid(row=6, column=1, padx=self.ent_padx, pady=rfi_pady, sticky=self.ent_sticky)
        self.body_mass_index_ent.insert(0, str(self.TD[6]) + " kg/m2")
        self.body_mass_index_ent.config(state=tk.DISABLED)

        #  FEATURES REMARK
        #       
        
        glucose_remark = test_analysis.glucose_analysis()
        glucose_remark_colour = test_analysis.glucose_colour
        
        cholesterol_remark = test_analysis.cholesterol_analysis()
        cholesterol_remark_colour = test_analysis.cholesterol_colour
        
        bp_remark = test_analysis.blood_pressure_analysis()
        bp_remark_colour = test_analysis.blood_pressure_colour
        
        hdl_remark = test_analysis.hdl_analysis(self.PGender)
        hdl_remark_colour = test_analysis.hdl_colour
        
        triglyceride_remark = test_analysis.triglyceride_analysis()
        triglyceride_remark_colour = test_analysis.triglyceride_colour
        
        bmi_remark = test_analysis.bmi_analysis()
        bmi_remark_colour = test_analysis.bmi_colour
        
        
        self.fr_fg = "#FFFFFF"
        self.rmk_sticky = "nsew"

        #******** REMARK HEADING ********************
        self.remark_lbl = tk.Label(self.result_form_inner, text="Remark", bg="#000AFF", fg="#FFFFFF",
                               relief=self.lbl_relief1, bd=self.bd_lbl, font=self.font1, justify="center")
        self.remark_lbl.grid(row=0, column=2, padx=(0, 0), pady=(0, 0), sticky="nsew")
        #*********************************************
        
        self.glucose_remark_lbl = tk.Label(self.result_form_inner, text=glucose_remark, bg=glucose_remark_colour, fg=self.fr_fg,
                               relief=self.lbl_relief1, bd=self.bd_lbl, font=self.font1, justify="center")
        self.glucose_remark_lbl.grid(row=1, column=2, padx=self.lbl_padx, pady=rfi_pady, sticky=self.rmk_sticky)

        self.cholesterol_remark_lbl = tk.Label(self.result_form_inner, text=cholesterol_remark, bg=cholesterol_remark_colour, fg=self.fr_fg,
                                   relief=self.lbl_relief1, bd=self.bd_lbl, font=self.font1, justify="center")
        self.cholesterol_remark_lbl.grid(row=2, column=2, padx=self.lbl_padx, pady=rfi_pady, sticky=self.rmk_sticky)

        self.blood_pressure_remark_lbl = tk.Label(self.result_form_inner, text=bp_remark, bg=bp_remark_colour, fg=self.fr_fg,
                                      relief=self.lbl_relief1, bd=self.bd_lbl, font=self.font1, justify="center")
        self.blood_pressure_remark_lbl.grid(row=3, column=2, padx=self.lbl_padx, pady=rfi_pady, sticky=self.rmk_sticky)

        self.high_density_lipoprotein_remark_lbl = tk.Label(self.result_form_inner, text=hdl_remark, bg=hdl_remark_colour, fg=self.fr_fg,
                                                relief=self.lbl_relief1, bd=self.bd_lbl, font=self.font1, justify="center")
        self.high_density_lipoprotein_remark_lbl.grid(row=4, column=2, padx=self.lbl_padx, pady=rfi_pady, sticky=self.rmk_sticky)

        self.triglyceride_remark_lbl = tk.Label(self.result_form_inner, text=triglyceride_remark, bg=triglyceride_remark_colour, fg=self.fr_fg,
                                    relief=self.lbl_relief1, bd=self.bd_lbl, font=self.font1, justify="center")
        self.triglyceride_remark_lbl.grid(row=5, column=2, padx=self.lbl_padx, pady=rfi_pady, sticky=self.rmk_sticky)

        self.body_mass_index_remark_lbl = tk.Label(self.result_form_inner, text=bmi_remark, bg=bmi_remark_colour, fg=self.fr_fg,
                                       relief=self.lbl_relief1, bd=self.bd_lbl, font=self.font1, justify="center")
        self.body_mass_index_remark_lbl.grid(row=6, column=2, padx=self.lbl_padx, pady=rfi_pady, sticky=self.rmk_sticky)

        ###############****************************************####################

        ############## DIAGNOSIS COMMENT #################   bg -->  self.diag_colour[self.diag_col_index]
        self.result_status_frm = tk.Frame(self.result_form, bg="#D3D3D3", relief=tk.GROOVE)
        self.result_status_frm.grid(row=5, column=1, sticky="nsew")
        
        self.result_status_frm.rowconfigure(0, weight=1, minsize=40)
        self.result_status_frm.rowconfigure(1, weight=1, minsize=30)
        self.result_status_frm.columnconfigure(0, weight=1, minsize=400)
        
        possible_outcomes = ["Non-Diabetic", "Diabetic"]
        diagnosis_result = possible_outcomes[self.DIAG]
        
        diagnosis_comment = "From the Diagnosis carried out, it has been confirmed that,\nYou are:"#\n{diagnosis_result}."     
        
        self.diagnosis_comment_lbl = tk.Label(self.result_status_frm, text=diagnosis_comment, relief=tk.FLAT, bd=0, bg="#D3D3D3",
                                       fg="#000000", font=("Times", 13, "normal"))
        self.diagnosis_comment_lbl.grid(row=0, column=0, ipady=5, sticky="nsew")
        #fg=self.diag_colour[self.diag_col_index]
        self.diabetics_status_lbl = tk.Label(self.result_status_frm, text=diagnosis_result, relief=tk.GROOVE, bd=1, bg=self.diag_colour[self.diag_col_index],
                                       fg="#FFFFFF", font=("Tahoma", 14, "bold"))
        self.diabetics_status_lbl.grid(row=1, column=0, ipadx=5, ipady=6, pady=(0,10))
        
        ## FOOTER LABEL
        '''
        self.footer_txt = tk.Label(self.result_frm, text = "(c) 2021 - RubyTech Systems Inc.", relief=tk.FLAT, border=2,
                                   bg="#FFFFFF", fg= "#000000", font=("courier new", 12, "normal"))
        self.footer_txt.grid(row=4, column=0, columnspan=result_frm_cs, ipady=0, pady=(5, 0), sticky="sew")

        self.result_window.protocol("WM_DELETE_WINDOW", self.window_closed) # CALLS window_closed() ONCE THIS WINDOW IS CLOSED
        '''
        
    def window_closed(self):  # WOULD BE CALLED WHEN WINDOW IS TO BE CLOSED
        ResultDisplay.current_result_window = False
        self.result_window.destroy()
        
    def justify(self, string, width=29):
        return string.rjust(width, " ")

    
    
# enter here to mark as comment :)'''
######## TEST VARIABLES ##########################
'''
test_window = tk.Tk()
test_window.title("Test Window")
test_window.iconbitmap("trial.ico")
test_window.geometry("900x715+220+10")
test_window.configure(bg="#A0A0A0")
        
aa=["Swashbuckle", "taskman", "Gately", 34, "Male"]
bb=[1, 281, 135, 312, 56, 234, "56"]
cc=random.randint(0, 1)

dit = {"patientDetails" : aa, "testDetails" : bb, "diagnosis" : cc}
res = ResultDisplay(test_window, dit)

##################################################
'''
# 
