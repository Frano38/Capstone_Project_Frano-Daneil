import tkinter as tk
from cvd_model import *

class CVD_GUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tk.Tk()
        self.main_window.title("Lung Cancer Predictor")

        # Create two frames to group widgets.
        self.one_frame = tk.Frame()
        self.two_frame = tk.Frame()
        self.three_frame = tk.Frame()
        self.four_frame = tk.Frame()
        self.five_frame = tk.Frame()
        self.six_frame = tk.Frame()
        self.seven_frame = tk.Frame()
        self.eight_frame = tk.Frame()
        self.nine_frame = tk.Frame()
        self.ten_frame = tk.Frame()
        self.eleven_frame = tk.Frame()
        self.twelve_frame = tk.Frame()
        self.thirteen_frame = tk.Frame()
        self.fourteen_frame = tk.Frame()
        self.fifteen_frame = tk.Frame()
        self.sixteen_frame = tk.Frame()
        self.seventeen_frame = tk.Frame()

        # Create the widgets for one frame. (title display)
        self.title_label = tk.Label(self.one_frame, text='LUNG CANCER PREDICTOR',fg="Blue", font=("Helvetica", 18))
        self.title_label.pack()

        # Create the widgets for three frame. (Gender input)
        self.sex_label = tk.Label(self.two_frame, text='Gender:')
        self.click_gender_var = tk.StringVar()
        self.click_gender_var.set("Male/Female")
        self.sex_inp = tk.OptionMenu(self.two_frame,self.click_gender_var, "Male", "Female")
        self.sex_label.pack(side='left')
        self.sex_inp.pack(side='left')

        # Create the widgets for two frame. (Age input)
        self.age_label = tk.Label(self.three_frame, text='Age:')
        self.age_entry = tk.Entry(self.three_frame, bg="white", fg="black", width = 10)
        # self.age_entry.insert(0,'50')
        self.age_label.pack(side='left')
        self.age_entry.pack(side='left')

        # Create the widgets for four frame. (Smoking input)
        self.cp_label = tk.Label(self.four_frame, text='Smoking:')
        self.click_smo_var = tk.StringVar()
        self.click_smo_var.set("Yes/No")
        self.cp_inp = tk.OptionMenu(self.four_frame, self.click_smo_var, "Yes", "No")
        self.cp_label.pack(side='left')
        self.cp_inp.pack(side='left')

        # Create the widgets for four frame. (Yellow fingers input)
        self.cp_label = tk.Label(self.five_frame, text='Yellow fingers:')
        self.click_yf_var = tk.StringVar()
        self.click_yf_var.set("Yes/No")
        self.cp_inp = tk.OptionMenu(self.five_frame, self.click_yf_var, "Yes", "No")
        self.cp_label.pack(side='left')
        self.cp_inp.pack(side='left')

        # Create the widgets for four frame. (Anxiety input)
        self.cp_label = tk.Label(self.six_frame, text='Anxiety:')
        self.click_anx_var = tk.StringVar()
        self.click_anx_var.set("Yes/No")
        self.cp_inp = tk.OptionMenu(self.six_frame, self.click_anx_var, "Yes", "No")
        self.cp_label.pack(side='left')
        self.cp_inp.pack(side='left')

        # Create the widgets for four frame. (Peer Pressure input)
        self.cp_label = tk.Label(self.seven_frame, text='Peer Pressure:')
        self.click_pp_var = tk.StringVar()
        self.click_pp_var.set("Yes/No")
        self.cp_inp = tk.OptionMenu(self.seven_frame, self.click_pp_var, "Yes", "No")
        self.cp_label.pack(side='left')
        self.cp_inp.pack(side='left')

        # Create the widgets for four frame. (Chronic Disease input)
        self.cp_label = tk.Label(self.eight_frame, text='Chronic Disease:')
        self.click_cd_var = tk.StringVar()
        self.click_cd_var.set("Yes/No")
        self.cp_inp = tk.OptionMenu(self.eight_frame, self.click_cd_var, "Yes", "No")
        self.cp_label.pack(side='left')
        self.cp_inp.pack(side='left')

        # Create the widgets for four frame. (Fatigue input)
        self.cp_label = tk.Label(self.nine_frame, text='Fatigue:')
        self.click_fat_var = tk.StringVar()
        self.click_fat_var.set("Yes/No")
        self.cp_inp = tk.OptionMenu(self.nine_frame, self.click_fat_var, "Yes", "No")
        self.cp_label.pack(side='left')
        self.cp_inp.pack(side='left')

        # Create the widgets for four frame. (Allergy input)
        self.cp_label = tk.Label(self.ten_frame, text='Allergy:')
        self.click_all_var = tk.StringVar()
        self.click_all_var.set("Yes/No")
        self.cp_inp = tk.OptionMenu(self.ten_frame, self.click_all_var, "Yes", "No")
        self.cp_label.pack(side='left')
        self.cp_inp.pack(side='left')

        # Create the widgets for four frame. (Wheezing input)
        self.cp_label = tk.Label(self.eleven_frame, text='Wheezing:')
        self.click_whz_var = tk.StringVar()
        self.click_whz_var.set("Yes/No")
        self.cp_inp = tk.OptionMenu(self.eleven_frame, self.click_whz_var, "Yes", "No")
        self.cp_label.pack(side='left')
        self.cp_inp.pack(side='left')

        # Create the widgets for four frame. (Alcohol consuming input)
        self.cp_label = tk.Label(self.twelve_frame, text='Alcohol consuming:')
        self.click_alc_var = tk.StringVar()
        self.click_alc_var.set("Yes/No")
        self.cp_inp = tk.OptionMenu(self.twelve_frame, self.click_alc_var, "Yes", "No")
        self.cp_label.pack(side='left')
        self.cp_inp.pack(side='left')

        # Create the widgets for four frame. (Coughing input)
        self.cp_label = tk.Label(self.thirteen_frame, text='Coughing:')
        self.click_co_var = tk.StringVar()
        self.click_co_var.set("Yes/No")
        self.cp_inp = tk.OptionMenu(self.thirteen_frame, self.click_co_var, "Yes", "No")
        self.cp_label.pack(side='left')
        self.cp_inp.pack(side='left')

        # Create the widgets for four frame. (Shortness of breath input)
        self.cp_label = tk.Label(self.fourteen_frame, text='Shortness of breath:')
        self.click_bre_var = tk.StringVar()
        self.click_bre_var.set("Yes/No")
        self.cp_inp = tk.OptionMenu(self.fourteen_frame, self.click_bre_var, "Yes", "No")
        self.cp_label.pack(side='left')
        self.cp_inp.pack(side='left')

        # Create the widgets for four frame. (Swallowing difficulty input)
        self.cp_label = tk.Label(self.fifteen_frame, text='Swallowing difficulty:')
        self.click_sd_var = tk.StringVar()
        self.click_sd_var.set("Yes/No")
        self.cp_inp = tk.OptionMenu(self.fifteen_frame, self.click_sd_var, "Yes", "No")
        self.cp_label.pack(side='left')
        self.cp_inp.pack(side='left')

        # Create the widgets for four frame. (Chest pain input)
        self.cp_label = tk.Label(self.sixteen_frame, text='Chest pain:')
        self.click_cp_var = tk.StringVar()
        self.click_cp_var.set("Yes/No")
        self.cp_inp = tk.OptionMenu(self.sixteen_frame, self.click_cp_var, "Yes", "No")
        self.cp_label.pack(side='left')
        self.cp_inp.pack(side='left')

        # Create the widgets for fifteen frame = hd (prediction of Lung Cancer)
        self.lc_predict_ta = tk.Text(self.seventeen_frame,height = 10, width = 25,bg= 'light blue')

        # Create predict button and quit button
        self.btn_predict = tk.Button(self.seventeen_frame, text='Predict Lung Cancer', command=self.predict_lc)
        self.btn_quit = tk.Button(self.seventeen_frame, text='Quit', command=self.main_window.destroy)

        self.lc_predict_ta.pack(side='left')
        self.btn_predict.pack()
        self.btn_quit.pack()


        # Pack the frames.
        self.one_frame.pack()
        self.two_frame.pack()
        self.three_frame.pack()
        self.four_frame.pack()
        self.five_frame.pack()
        self.six_frame.pack()
        self.seven_frame.pack()
        self.eight_frame.pack()
        self.nine_frame.pack()
        self.ten_frame.pack()
        self.eleven_frame.pack()
        self.twelve_frame.pack()
        self.thirteen_frame.pack()
        self.fourteen_frame.pack()
        self.fifteen_frame.pack()
        self.sixteen_frame.pack()
        self.seventeen_frame.pack()

        # Enter the tkinter main loop.
        tk.mainloop()
    def predict_lc(self):
        result_string = ""

        self.lc_predict_ta.delete(0.0, tk.END)

        patient_age = self.age_entry.get()

        patient_gender = self.click_gender_var.get()
        if(patient_gender == "Male"):
            patient_gender = 1
        else:
            patient_gender = 0

        patient_smoking = self.click_smo_var.get()
        if(patient_smoking == "Yes"):
            patient_smoking = 1
        else:
            patient_smoking = 0

        patient_yellowFingers = self.click_yf_var.get()
        if(patient_yellowFingers == "Yes"):
            patient_yellowFingers = 1
        else:
            patient_yellowFingers = 0

        patient_anxiety = self.click_anx_var.get()
        if(patient_anxiety == "Yes"):
            patient_anxiety = 1
        else:
            patient_anxiety = 0

        patient_peerPressure = self.click_pp_var.get()
        if(patient_peerPressure == "Yes"):
            patient_peerPressure = 1
        else:
            patient_peerPressure = 0

        patient_chronicDisease = self.click_cd_var.get()
        if(patient_chronicDisease == "Yes"):
            patient_chronicDisease = 1
        else:
            patient_chronicDisease = 0

        patient_fatigue = self.click_fat_var.get()
        if(patient_fatigue == "Yes"):
            patient_fatigue = 1
        else:
            patient_fatigue = 0

        patient_allergy = self.click_all_var.get()
        if(patient_allergy == "Yes"):
            patient_allergy = 1
        else:
            patient_allergy = 0

        patient_wheezing = self.click_whz_var.get()
        if(patient_wheezing == "Yes"):
            patient_wheezing = 1
        else:
            patient_wheezing = 0

        patient_alcohol = self.click_alc_var.get()
        if(patient_alcohol== "Yes"):
            patient_alcohol = 1
        else:
            patient_alcohol = 0

        patient_coughing = self.click_co_var.get()
        if(patient_coughing == "Yes"):
            patient_coughing  = 1
        else:
            patient_coughing  = 0

        patient_shortness_of_breath = self.click_bre_var.get()
        if(patient_shortness_of_breath == "Yes"):
            patient_shortness_of_breath = 1
        else:
            patient_shortness_of_breath = 0

        patient_swallowing_difficulty = self.click_sd_var.get()
        if(patient_swallowing_difficulty == "Yes"):
            patient_swallowing_difficulty  = 1
        else:
            patient_swallowing_difficulty = 0

        patient_chest_pain = self.click_cp_var.get()
        if(patient_chest_pain == "Yes"):
            patient_chest_pain  = 1
        else:
            patient_chest_pain  = 0


        result_string += "===Patient Diagnosis=== \n"
        patient_info = (patient_gender, patient_age, patient_smoking, patient_yellowFingers, patient_anxiety, patient_peerPressure,\
                        patient_chronicDisease, patient_fatigue, patient_allergy, patient_wheezing, patient_alcohol,\
                        patient_coughing, patient_shortness_of_breath, patient_swallowing_difficulty, patient_chest_pain)


        lc_prediction =  best_model.predict([patient_info])
        disp_string = ("This prediction has an accuracy of:", str(model_accuracy))

        if(lc_prediction == [0]):
            result_string = (disp_string, '\n', "0 - You don't have lung cancer")
        else:
            result_string = (disp_string, '\n'+ "1 - You have lung cancer")
        self.lc_predict_ta.insert('1.0',result_string)




my_cvd_GUI = CVD_GUI()
