import tkinter as tk
from cvd_model_BMI import *


class CVD_GUI:
    def __init__(self):

        # Create the main window.
        self.main_window = tk.Tk()
        self.main_window.title("Heart Disease Predictor")

        # Create two frames to group widgets.
        self.one_frame = tk.Frame()
        self.two_frame = tk.Frame()
        self.three_frame = tk.Frame()
        self.four_frame = tk.Frame()
        self.five_frame = tk.Frame()


        # Create the widgets for one frame. (title display)
        self.title_label = tk.Label(self.one_frame, text='BMI Calculator',fg="Blue", font=("Helvetica", 18))
        self.title_label.pack()

        # Create the widgets for two frame. (sex/gender input)
        self.gender_label = tk.Label(self.two_frame, text='Sex:')
        self.click_gender_var = tk.StringVar()
        self.click_gender_var.set("Male")
        self.gender_inp = tk.OptionMenu(self.two_frame, self.click_gender_var, "Male", "Female")
        self.gender_label.pack(side='left')
        self.gender_inp.pack(side='left')

        # Create the widgets for three frame. (age input)
        self.height_label = tk.Label(self.three_frame, text='Height:')
        self.height_entry = tk.Entry(self.three_frame, bg="white", fg="black", width = 10)
        self.height_label.pack(side='left')
        self.height_entry.pack(side='left')

        # Create the widgets for four frame. (age input)
        self.weight_label = tk.Label(self.four_frame, text='Weight:')
        self.weight_entry = tk.Entry(self.four_frame, bg="white", fg="black", width=10)
        self.weight_label.pack(side='left')
        self.weight_entry.pack(side='left')


        #Create the widgets for fifteen frame = hd (prediction of heart disease)
        self.index_predict_ta = tk.Text(self.five_frame,height = 10, width = 25,bg= 'light blue')

        #Create predict button and quit button
        self.btn_predict = tk.Button(self.five_frame, text='Predict BMI', command=self.predict_index)
        self.btn_quit = tk.Button(self.five_frame, text='Quit', command=self.main_window.destroy)


        self.index_predict_ta.pack(side='left')
        self.btn_predict.pack()
        self.btn_quit.pack()

        # Pack the frames.
        self.one_frame.pack()
        self.two_frame.pack()
        self.three_frame.pack()
        self.four_frame.pack()
        self.five_frame.pack()


        # Enter the tkinter main loop.
        tk.mainloop()

    def predict_index(self):

        result_string = ""

        self.index_predict_ta.delete(0.0, tk.END)

        patient_gender = self.click_gender_var.get()
        if(patient_gender == "Male"):
            patient_gender = 1
        else:
            patient_gender = 0

        patient_height = self.height_entry.get()

        patient_weight = self.weight_entry.get()



        # Accuracy of Model
        model.fit(x_train, y_train) #<-- this line
        acc = model.score(x_train, y_train)

        result_string += "===BMI Calculation=== \n"
        patient_info = (patient_gender,patient_height,patient_weight)

        bmi_predict =  best_model.predict([patient_info])
        disp_string = ("This prediction has an accuracy of:", str(model_accuracy))

        result = bmi_predict


        if(bmi_predict == [0]):
            result_string = (disp_string, '\n', "Your BMI is: ", result)
        else:
            result_string = (disp_string, '\n'+ "Your BMI is: ", result)

        self.index_predict_ta.insert('1.0', result_string)




my_cvd_GUI = CVD_GUI()
