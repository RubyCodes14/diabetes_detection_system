import numpy as np
from sklearn.externals import joblib

import tkinter as tk
from tkinter import ttk, messagebox
from tkinter import *
from PIL import ImageTk, Image


#ROOT WINDOW
root = tk.Tk()
root.title("Diabetes Detection System")
root.iconbitmap("img/dds1.ico")
root.geometry("900x670+250+15")
root.configure(bg="#A0A0A0")
root.state("zoomed")

homepage_frm = tk.Frame(root, relief=tk.FLAT, border=0, bg="#FFFFFF")
homepage_frm.pack(fill=tk.BOTH)

def load_detection_model(model_name):
    global loaded_detection_model
    loaded_detection_model = joblib.load(model_name)


loaded_detection_model = None   # VARIABLE HOLDING THE MODEL WHENEVER ITS LOADED


mainFrame = tk.Frame(root, relief=tk.FLAT, border=2, bg="#1E90FF") #87CEEB
#mainFrame.pack(fill=tk.BOTH)  #SINCE THE HOMEPAGE WOULD HAVE TO DISPLAY FIRST OR EVEN PACKING IT WOULD STILL GIVE THE SAME RESULT

def return_focus(event=None):
    mainFrame.focus_set()  # ONCE A COMBOBOX IS SELECTED, ENTER KEY WORKS FOR DETECT BUTTON
    #home_btn.bind("<space>", home)
    

def start(event=None):   
    homepage_frm.pack_forget()
    mainFrame.pack(fill=tk.BOTH)
    
    homepage_frm.unbind_all("<space>") # UNBINDS THE start function FROM THE SPACEBAR    
    mainFrame.focus_set()
    mainFrame.bind_all("<Return>", get_user_info)
    home_btn.focus_set()
    #home_btn.bind("<BackSpace>", home)
    
img_index = 0

res_w = 700
res_h = 650

img1 = ImageTk.PhotoImage(Image.open("img/img1.png").resize((res_w, res_h), Image.ANTIALIAS))
img2 = ImageTk.PhotoImage(Image.open("img/img2.png").resize((res_w, res_h), Image.ANTIALIAS))
img3 = ImageTk.PhotoImage(Image.open("img/img3.png").resize((res_w, res_h), Image.ANTIALIAS))
img4 = ImageTk.PhotoImage(Image.open("img/img4.png").resize((res_w, res_h), Image.ANTIALIAS))
img5 = ImageTk.PhotoImage(Image.open("img/img5.png").resize((res_w, res_h), Image.ANTIALIAS))
img6 = ImageTk.PhotoImage(Image.open("img/img6.png").resize((res_w, res_h), Image.ANTIALIAS))
img7 = ImageTk.PhotoImage(Image.open("img/img7.png").resize((res_w, res_h), Image.ANTIALIAS))
img8 = ImageTk.PhotoImage(Image.open("img/img8.png").resize((res_w, res_h), Image.ANTIALIAS))
img9 = ImageTk.PhotoImage(Image.open("img/img9.png").resize((res_w, res_h), Image.ANTIALIAS))
img10 = ImageTk.PhotoImage(Image.open("img/img10.png").resize((res_w, res_h), Image.ANTIALIAS))      

imgs_ = [img1, img2, img3, img4, img5, img6, img7, img8, img9, img10]

#HOMEPAGE FRAME RESPONSIVENESS
homepage_frm.rowconfigure(0, weight = 1, minsize = 650)
homepage_frm.columnconfigure(0, weight = 1, minsize = 450)
homepage_frm.columnconfigure(1, weight = 1, minsize = 450)

#GET SCREEN SIZE
#screenWidth = root.winfo_screenwidth()
#screenHeight = root.winfo_screenheight()

#BACKGROUND IMAGE CONTAINER
#RESIZE IMAGE
image = Image.open("img/img1.png")  #LOAD IMAGE
resizedImage = image.resize((res_w, res_h), Image.ANTIALIAS)
background_image = ImageTk.PhotoImage(resizedImage)

#COLUMN 1 
col1_frm = tk.Frame(homepage_frm, bg="#FFFFFF", relief=tk.GROOVE, bd=2)
col1_frm.grid(row=0, column=0, sticky="nsew")

#RESPONSIVENESS
col1_frm.rowconfigure([0, 2], weight = 1, minsize = 50)
col1_frm.rowconfigure(1, weight = 1, minsize = 550)
col1_frm.columnconfigure([0, 1], weight = 0, minsize = 225)

col1_img = tk.Label(col1_frm, image = background_image, relief=tk.FLAT, bd=0)
col1_img.grid(row=1, column=0, columnspan=2, padx=0, sticky="nsew")

#COLUMN 2 
col2_frm = tk.Frame(homepage_frm, bg="#7777FF", relief=tk.GROOVE, bd=0)
col2_frm.grid(row=0, column=1, sticky="nsew")

#RESPONSIVENESS
col2_frm.rowconfigure(0, weight = 1, minsize = 420)
col2_frm.rowconfigure(1, weight = 1, minsize = 150)
col2_frm.rowconfigure(2, weight = 1, minsize = 20)
col2_frm.rowconfigure(3, weight = 1, minsize = 70)
col2_frm.rowconfigure(4, weight = 1, minsize = 30)
#col2_frm.columnconfigure([0, 1, 2], weight = 1, minsize = 250)
col2_frm.columnconfigure(0, weight = 1, minsize = 450)


txt_ = "Diabetes \nDetection \nSystem"
title_text = tk.Label(col2_frm, text=txt_, relief=tk.GROOVE, bd=0, bg="#1111FF", fg="#FFFFFF", font=("Kartika", 55, "bold"))
title_text.grid(row=0, column=0, sticky="nsew", ipadx=115,)# padx=(0, 0), ipady=0, pady=(0, 0),  columnspan=3,

#Fast and Easy Way \nto \nDetect Diabetes
txt_1 = "Reliable and Accurate \nDiagnosis System."
display_text = tk.Label(col2_frm, text=txt_1, relief=tk.FLAT, bd=3, bg="#FFFFFF", fg="#8B0000", font=("Alex Brush", 30, "normal"))
display_text.grid(row=1, column=0, sticky="nsew")

launch_btn = tk.Button(col2_frm, text="Start", bg="#AAAAFF", relief=tk.GROOVE, bd=2, font=("time", 20, "bold"), command=start)
launch_btn.grid(row=3, column=0, ipadx=10, padx=(0, 0), ipady=2, pady=(0, 20),)# sticky="nsew")
homepage_frm.bind_all("<space>", start)

def img_seq():
    global img_index
    loop = root.after(3000, img_seq)
    if img_index >= len(imgs_):
        img_index = 0
    col1_img["image"] = imgs_[img_index]
    
    if img_index == 900:
        root.after_cancel(loop)
        
    img_index += 1

def justify(text, lenght=30):
    len_txt = len(text)
    size = int(lenght/2) + len_txt
    rj = text.rjust(size, " ")
    lj = rj.ljust(size, " ")
    return text

img_seq()
#THE DETECTION MODEL IS LOADED IMMEDIATELY AFTER THE APPLICATION IS LAUNCHED

load_detection_model("C:\\Users\\DELL\\Desktop\\CSC_400L\\Project\\Model\\detection_model.sav")

#************@@@@@@@@@@@@@@@@@@<<<<<<<<<<<<<********>>>>>>>>>>>>>>>>@@@@@@@@@@@@@@@@@@@************************
#                              MAIN PAGE ---  DETECTION PAGE
#@@@@@@@@@@@@******************>>>>>>>>>>>>>********<<<<<<<<<<<<<<<<*******************@@@@@@@@@@@@@@@@@@@@@@@@

current_result_window = False
continue_detection = True


def activate_user_info_window():
    detect_btn["state"] = "normal"


def get_diagnosis(test_details):
    test_details = list(test_details)
    test_details.insert(0, age_ent.get())
    test_details = np.array(test_details).reshape(1, -1)
    diagnosis = loaded_detection_model.predict(test_details)

    return diagnosis[0]

def detection_result(pre_result):
    global current_result_window, lift_result_window
    from result_window import ResultDisplay   
    ResultDisplay(root, pre_result)

    '''current_result_window = ResultDisplay.current_result_window
    if current_result_window:
        yes_ = tk.messagebox.askyesno(title="Close Window", message="Close current Result Window.") # RETURNS ok
        #print(yes_)
        if yes_:
            ResultDisplay.window_closed
            continue_detection = True
        elif yes_:
            continue_detection = False
    else:
        continue_detection = True '''
        
def values_are_integers(varsList):
    for value in varsList:
        value = str(value)  # TO ENABLE DATA TYPE CHECK AT ALL TIMES -- int TO AVOID 'AttributeError: 'int' object has no attribute 'isdigit'/'isnumeric'' 
        if value.isnumeric() or value.isdigit():
            return_value = True
        else:
            return_value = False
            break
            
    return return_value

def get_user_info(event=None):
    #global continue_detection
    
    if True: 
        pd_provided = False
        td_provided = False
        if first_name_ent.get() and last_name_ent.get() and age_ent.get() and gender_var.get():
            if gender_var.get() in ["Male", "Female"]:
                pd = [first_name_ent.get(), middle_name_ent.get(), last_name_ent.get(), age_ent.get(), gender_var.get()]
                pd_provided = True
            else:
                tk.messagebox.showinfo(title="Select Option", message="Please select valid Gender.")
                pd_provided = False
                gender_combo.focus_set()
                
        else:
            tk.messagebox.showwarning(title="Blank Box", message="All Patients details (except Middle Name) MUST be entered!")
            
           
        if family_history_var.get() and glucose_ent.get() and cholesterol_ent.get() and blood_pressure_ent.get()and high_density_lipoprotein_ent.get() and triglyceride_ent.get() and body_mass_index_ent.get():
            family_history = family_history_options.index(family_history_var.get())
            #print(family_history)
            td = [family_history, glucose_ent.get(), cholesterol_ent.get(),blood_pressure_ent.get(),
                   high_density_lipoprotein_ent.get(), triglyceride_ent.get(), body_mass_index_ent.get()
              ]
                
            if values_are_integers(td):  # TO CHECK IF ALL THE TEST INPUTS ARE CORRECT - NUMBER VALUES
                if family_history > 1:  #TO CHECK WHETHER USER LEFT THE COMBOBOX ON --select--
                    tk.messagebox.showinfo(title="Select Option", message="Please select valid Family History.")
                    td_provided = False
                    family_history_combo.focus_set()
                    
                else:
                    td_provided = True
                 
            else:
                td_provided = False
                tk.messagebox.showerror(title="Wrong Input", message="Only Numerical Values are allowed for test details.")
                   
        else:
            tk.messagebox.showwarning(title="Blank Box", message="All Test Details are required!")
                
        diag = 0
        # DETECTION
        if  pd_provided and td_provided: 
            diag = get_diagnosis(td) #MAIN PREDICTION USING THE PROVIDED TEST DETAILS

            information_dict = {"patientDetails" : pd, "testDetails" : td, "diagnosis" : diag}
            detection_result(information_dict)
            
        else:
            pass

def home(event=None):
    mainFrame.pack_forget()
    homepage_frm.pack(fill=tk.BOTH)
    
    mainFrame.unbind_all("<space>")
    mainFrame.unbind_all("<Return>")       
    homepage_frm.focus_set()
    homepage_frm.bind_all("<space>", start)  # BINDS THE start function TO THE SPACEBAR

    #home_btn.unbind("<BackSpace>")
      


#MAINFRAME RESPONSIVENESS
mainFrame.rowconfigure(0, weight = 1, minsize = 50)
mainFrame.rowconfigure(1, weight = 1, minsize = 35)
mainFrame.rowconfigure(2, weight = 1, minsize = 520)
mainFrame.rowconfigure(3, weight = 2, minsize = 50)
mainFrame.rowconfigure(4, weight = 1, minsize = 20)
mainFrame.rowconfigure(5, weight = 1, minsize = 20)

mainFrame.columnconfigure([0, 6], weight = 1, minsize = 20)
mainFrame.columnconfigure(1, weight = 0, minsize = 100) #STRICTLY FOR HOME BUTTON
mainFrame.columnconfigure(3, weight = 1, minsize = 10)
mainFrame.columnconfigure([2, 4, 5], weight = 0, minsize = 130)
#mainFrame.columnconfigure(3, weight = 1, minsize = 600)


#GENERAL FONT
gen_font = ("Cambria", 20, "bold")

#BACKGROUND COLOUR
bg_lbl = "#C5C5C5"  #FOR INPUT LABELS ONLY
fg_lbl = "#000000"
bg_lbl_heading = "#000AFF" #"#000080" #navy blue

ent_bg = "#FFFFFF"
form_frm_bg = "#DFDFDF"
frm_bg_patient_info = "#FFFFFF"

btn_bg = "#000AFF"
btn_fg = "#FFFFFF"

#TEXT OR FONT COLOUR
fg_lbl_heading = "#FFFFFF"

#FONT
font_patient_info = ("times new roman", 14, "normal")
font_patient_and_test_heading = ("arial", 18, "normal")

#STICKY
ent_sticky = "we"
lbl0_sticky = "w"
lbl_sticky = "we"

#PADDING
ent0_padx = (10, 10)
ent_padx = (0, 10)
lbl0_padx = 10
lbl_padx = (10, 0)

#RELIEF
lbl_relief_patient_info = tk.FLAT
relief_patient_info_frm = tk.SUNKEN
form_frm_relief = tk.FLAT
ent_relief = tk.RAISED

#BORDER - RELIEF
bd_patient_info_frm = 2
form_frm_bd = 1
lbl_bd_patient_info = 1

#WIDTH - ENTRY TEXT
ent_width = 20
ent_width1 = 10

#SYSTEM TITLE LABEL
system_name = tk.Label(mainFrame, text = "DIABETES \tDETECTION\tSYSTEM", relief=tk.GROOVE, border=2, bg="#000AFF", fg= "#FFFFFF", font=gen_font)
system_name.grid(row=0, column=0, columnspan=7, sticky="nsew")

home_btn = tk.Button(mainFrame, text="Home", relief=tk.GROOVE, border=2, bg="#DCDCFF", fg= "#000080", font=("jester", 15, "normal"), command=home)
home_btn.grid(row=1, column=0, ipadx=5, ipady=5, pady=(5, 0), padx=(5, 0), sticky="w")

#PATIENT DETAILS FRAME
patient_details_Frm = tk.Frame(mainFrame, relief=relief_patient_info_frm, bd=bd_patient_info_frm, bg=frm_bg_patient_info)
patient_details_Frm.grid(row=2, column=1, columnspan=2, sticky="nsew")

#responsiveness
patient_details_Frm.rowconfigure(0, weight=1, minsize=25)
patient_details_Frm.rowconfigure(1, weight=1, minsize=400)
patient_details_Frm.rowconfigure(2, weight=1, minsize=25)
patient_details_Frm.columnconfigure(1, weight=1, minsize=300)
patient_details_Frm.columnconfigure([0, 2], weight=1, minsize=20)

patient_form = tk.Label(patient_details_Frm, bg=bg_lbl_heading, fg=fg_lbl_heading, text="Patient's Details", font = font_patient_and_test_heading)
patient_form.grid(row=0, column=0, columnspan=3, ipady=5, sticky="new")

patient_details_form_frm = tk.Frame(patient_details_Frm, relief=form_frm_relief, bd=form_frm_bd, bg=form_frm_bg)
patient_details_form_frm.grid(row=1, column=1, sticky="nsew")


patient_details_form_frm.rowconfigure(list(range(15)), weight=1, minsize=20)
patient_details_form_frm.columnconfigure(0, weight=1, minsize=170)
patient_details_form_frm.columnconfigure(1, weight=1, minsize=180)

#details label
first_name_lbl = tk.Label(patient_details_form_frm, text="First Name", bg=bg_lbl, fg=fg_lbl,
                          relief=lbl_relief_patient_info, bd=lbl_bd_patient_info, font=font_patient_info)
first_name_lbl.grid(row=0, column=0, ipadx=lbl0_padx, padx=lbl_padx, sticky=lbl0_sticky)

middle_name_lbl = tk.Label(patient_details_form_frm, text="Middle Name", bg=bg_lbl, fg=fg_lbl,
                           relief=lbl_relief_patient_info, bd=lbl_bd_patient_info, font=font_patient_info)
middle_name_lbl.grid(row=3, column=0, ipadx=lbl0_padx, padx=lbl_padx, sticky=lbl0_sticky)

last_name_lbl = tk.Label(patient_details_form_frm, text="Last Name", bg=bg_lbl, fg=fg_lbl,
                         relief=lbl_relief_patient_info, bd=lbl_bd_patient_info, font=font_patient_info)
last_name_lbl.grid(row=6, column=0, ipadx=lbl0_padx, padx=lbl_padx, sticky=lbl0_sticky)

age_lbl = tk.Label(patient_details_form_frm, text="Age", bg=bg_lbl, fg=fg_lbl,
                   relief=lbl_relief_patient_info, bd=lbl_bd_patient_info, font=font_patient_info)
age_lbl.grid(row=9, column=0, ipadx=lbl0_padx, padx=lbl_padx, sticky=lbl0_sticky)

gender_lbl = tk.Label(patient_details_form_frm, text="Gender", bg=bg_lbl, fg=fg_lbl,
                   relief=lbl_relief_patient_info, bd=lbl_bd_patient_info, font=font_patient_info)
gender_lbl.grid(row=12, column=0, ipadx=lbl0_padx, padx=lbl_padx, sticky=lbl0_sticky)

#details entry
first_name_ent = tk.Entry(patient_details_form_frm, width=ent_width, bg=ent_bg, relief=ent_relief, font=font_patient_info)
first_name_ent.grid(row=1, column=0, columnspan=2, padx=ent0_padx, sticky=ent_sticky)

middle_name_ent = tk.Entry(patient_details_form_frm, width=ent_width, bg=ent_bg, relief=ent_relief, font=font_patient_info)
middle_name_ent.grid(row=4, column=0, columnspan=2, padx=ent0_padx, sticky=ent_sticky)

last_name_ent = tk.Entry(patient_details_form_frm, width=ent_width, bg=ent_bg, relief=ent_relief, font=font_patient_info)
last_name_ent.grid(row=7, column=0, columnspan=2, padx=ent0_padx, sticky=ent_sticky)

age_ent = tk.Entry(patient_details_form_frm, width=ent_width, bg=ent_bg, relief=ent_relief, font=font_patient_info)
age_ent.grid(row=10, column=0, columnspan=2, padx=ent0_padx, sticky=ent_sticky)

'''gender_ent = tk.Entry(patient_details_form_frm, width=ent_width, bg=ent_bg, relief=ent_relief, font=font_patient_info)
gender_ent.grid(row=13, column=0, columnspan=2, padx=ent0_padx, sticky=ent_sticky)'''

gender_var = StringVar()
gender_options = ["Male", "Female", "-select-"]
gender_combo = ttk.Combobox(patient_details_form_frm, width=12, textvariable=gender_var, value=gender_options, state = "readonly", font=font_patient_info)
gender_combo.current(2)
gender_combo.grid(row=13, column=0, columnspan=1, padx=ent0_padx, sticky=ent_sticky)
gender_combo.bind("<<ComboboxSelected>>", return_focus)


#TEST DETAILS FRAME

test_details_Frm = tk.Frame(mainFrame, relief=relief_patient_info_frm, bd=bd_patient_info_frm, bg=frm_bg_patient_info)
test_details_Frm.grid(row=2, column=4, columnspan=2, sticky="nsew")

#responsiveness
test_details_Frm.rowconfigure(0, weight=1, minsize=25)
test_details_Frm.rowconfigure(1, weight=1, minsize=400)
test_details_Frm.rowconfigure(2, weight=1, minsize=25)
test_details_Frm.columnconfigure(1, weight=1, minsize=300)
test_details_Frm.columnconfigure([0, 2], weight=1, minsize=20)

#test details form
test_form = tk.Label(test_details_Frm, text="Test Details", bg=bg_lbl_heading, fg=fg_lbl_heading, font=font_patient_and_test_heading)
test_form.grid(row=0, column=0, columnspan=3, ipady=5, sticky="new")

test_details_form_frm = tk.Frame(test_details_Frm, relief=form_frm_relief, bd=form_frm_bd, bg=form_frm_bg)
test_details_form_frm.grid(row=1, column=1, sticky="nsew")

test_details_form_frm.rowconfigure([1, 2, 3, 4, 5, 6, 7], weight=1, minsize=30)
test_details_form_frm.columnconfigure(0, weight=1, minsize=250)
test_details_form_frm.columnconfigure(1, weight=1, minsize=100)


#test label
#lbl_padx = (20, 0)
#lbl_sticky = "w"


family_history_lbl = tk.Label(test_details_form_frm, text=justify("Diabetes in Family History"), bg=bg_lbl, fg=fg_lbl,
                              relief=lbl_relief_patient_info, bd=lbl_bd_patient_info, font=font_patient_info)
family_history_lbl.grid(row=1, column=0, padx=lbl_padx, sticky=lbl_sticky)

glucose_lbl = tk.Label(test_details_form_frm, text=justify("Glucose"), bg=bg_lbl, fg=fg_lbl,
                       relief=lbl_relief_patient_info, bd=lbl_bd_patient_info, font=font_patient_info)
glucose_lbl.grid(row=2, column=0, padx=lbl_padx, sticky=lbl_sticky)

cholesterol_lbl = tk.Label(test_details_form_frm, text=justify("Cholesterol"), bg=bg_lbl, fg=fg_lbl,
                           relief=lbl_relief_patient_info, bd=lbl_bd_patient_info, font=font_patient_info)
cholesterol_lbl.grid(row=3, column=0, padx=lbl_padx, sticky=lbl_sticky)

blood_pressure_lbl = tk.Label(test_details_form_frm, text=justify("Blood Pressure"), bg=bg_lbl, fg=fg_lbl,
                              relief=lbl_relief_patient_info, bd=lbl_bd_patient_info, font=font_patient_info)
blood_pressure_lbl.grid(row=4, column=0, padx=lbl_padx, sticky=lbl_sticky)

high_density_lipoprotein_lbl = tk.Label(test_details_form_frm, text=justify("High Density Lipoprotein"), bg=bg_lbl, fg=fg_lbl,
                                        relief=lbl_relief_patient_info, bd=lbl_bd_patient_info, font=font_patient_info)
high_density_lipoprotein_lbl.grid(row=5, column=0, ipadx=4, padx=lbl_padx, sticky=lbl_sticky)

triglyceride_lbl = tk.Label(test_details_form_frm, text=justify("Triglyceride"), bg=bg_lbl, fg=fg_lbl,
                            relief=lbl_relief_patient_info, bd=lbl_bd_patient_info, font=font_patient_info)
triglyceride_lbl.grid(row=6, column=0, padx=lbl_padx, sticky=lbl_sticky)

body_mass_index_lbl = tk.Label(test_details_form_frm, text=justify("Body Mass Index"), bg=bg_lbl, fg=fg_lbl,
                               relief=lbl_relief_patient_info, bd=lbl_bd_patient_info, font=font_patient_info)
body_mass_index_lbl.grid(row=7, column=0, padx=lbl_padx, sticky=lbl_sticky)



#test entry
#
'''
family_history_ent = tk.Entry(test_details_form_frm, width=ent_width1, bg=ent_bg, relief=ent_relief, font=font_patient_info)
family_history_ent.grid(row=1, column=1, padx=ent_padx, sticky=ent_sticky)
'''

family_history_var = StringVar()
family_history_options = ["No", "Yes", "-select-"]
family_history_combo = ttk.Combobox(test_details_form_frm, width=8, textvariable=family_history_var,
                                    value=family_history_options, state = "readonly", font=font_patient_info)
family_history_combo.grid(row=1, column=1, columnspan=1, padx=(0, 10), sticky=ent_sticky)
family_history_combo.current(2)
family_history_combo.bind("<<ComboboxSelected>>", return_focus)

glucose_ent = tk.Entry(test_details_form_frm, width=ent_width1, bg=ent_bg, relief=ent_relief, font=font_patient_info)
glucose_ent.grid(row=2, column=1, padx=ent_padx, sticky=ent_sticky)

cholesterol_ent = tk.Entry(test_details_form_frm, width=ent_width1, bg=ent_bg, relief=ent_relief, font=font_patient_info)
cholesterol_ent.grid(row=3, column=1, padx=ent_padx, sticky=ent_sticky)

blood_pressure_ent = tk.Entry(test_details_form_frm, width=ent_width1, bg=ent_bg, relief=ent_relief, font=font_patient_info)
blood_pressure_ent.grid(row=4, column=1, padx=ent_padx, sticky=ent_sticky)

high_density_lipoprotein_ent = tk.Entry(test_details_form_frm, width=ent_width1, bg=ent_bg, relief=ent_relief, font=font_patient_info)
high_density_lipoprotein_ent.grid(row=5, column=1, padx=ent_padx, sticky=ent_sticky)

triglyceride_ent = tk.Entry(test_details_form_frm, width=ent_width1, relief=ent_relief, bg=ent_bg, font=font_patient_info)
triglyceride_ent.grid(row=6, column=1, padx=ent_padx, sticky=ent_sticky)

body_mass_index_ent = tk.Entry(test_details_form_frm, width=ent_width1, relief=ent_relief, bg=ent_bg, font=font_patient_info)
body_mass_index_ent.grid(row=7, column=1, padx=ent_padx, sticky=ent_sticky)


#*****FOR TESTING **** 
'''
aa=["Swashbuckle", "taskman", "Gately", 34, "Male"]
bb=[1, 281, 135, 312, 56, 234, "56"]
cc=0

dict_ = {"patientDetails" : aa, "testDetails" : bb, "diagnosis" : cc}
# on detect button replace 'get_user_info' with 'lambda: detection_result(dict_)'

#****************
'''

#DETECT BUTTON

detect_btn = tk.Button(mainFrame, text="Detect", bg=btn_bg, fg=btn_fg, relief=tk.GROOVE, bd=4,
                       font=("garamond", 20, "bold"), command=get_user_info) #lambda: detection_result(dict_)
detect_btn.grid(row=3, column=5, ipadx=5, padx=(0, 10), ipady=2, pady=(10, 0), sticky="e")

#FOOTER TEXT
footer_txt = tk.Label(mainFrame, text = "(c) 2021 - RubyTech Inc.", relief=tk.FLAT, border=2, bg="#FFFFFF", fg= "#000000", font=("courier new", 12, "normal"))
footer_txt.grid(row=5, column=0, columnspan=7, ipady=0, pady=(5, 0), sticky="sew")


root.mainloop()
