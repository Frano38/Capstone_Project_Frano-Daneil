from flask import Flask, Blueprint, render_template, redirect, url_for, request
from werkzeug.middleware.proxy_fix import ProxyFix
import sys
from argparse import ArgumentParser
from cvd_model import *

appweb = Blueprint('hello', __name__)

@appweb.route('/')
def home():
    return render_template("index.html")

@appweb.route('/send', methods=['POST'])
def send(predict=predict):
    if request.method == 'POST':
        patient_gender = request.form['gender']
        patient_age = request.form['age']
        patient_smoking = request.form['smoking']
        patient_yellowFingers = request.form['yellow fingers']
        patient_anxiety = request.form['anxiety']
        patient_peerPressure = request.form['peer pressure']
        patient_chronicDisease = request.form['chronic disease']
        patient_fatigue = request.form['fatigue']
        patient_allergy = request.form['allergy']
        patient_wheezing = request.form['wheezing']
        patient_alcohol = request.form['alcohol']
        patient_coughing = request.form['coughing']
        patient_shortness_of_breath = request.form['shortness of breath']
        patient_swallowing = request.form['swallowing difficulty']
        patient_chest_pain = request.form['chest pain']

        if(patient_gender == "male"):
            patient_gender = 1;
        else:
            patient_gender = 0

        if(patient_smoking == "Yes/No"):
            patient_smoking = 1;
        else:
            patient_smoking = 0;

        if(patient_yellowFingers == "Yes/No"):
            patient_yellowFingers = 1
        else:
            patient_yellowFingers = 0

        if(patient_anxiety == "Yes/No"):
            patient_anxiety = 1
        else:
            patient_anxiety = 0

        if(patient_peerPressure == "Yes/No"):
            patient_peerPressure = 1
        else:
            patient_peerPressure = 0

        if(patient_chronicDisease == "Yes/No"):
            patient_chronicDisease = 1
        else:
            patient_chronicDisease = 0

        if(patient_fatigue == "Yes/No"):
            patient_fatigue = 1
        else:
            patient_fatigue = 0

        if(patient_allergy == "Yes/No"):
            patient_allergy = 1
        else:
            patient_allergy= 0

        if(patient_wheezing == "Yes/No"):
            patient_wheezing = 1
        else:
            patient_wheezing = 0

        if(patient_alcohol == "Yes/No"):
            patient_alcohol = 1
        else:
            patient_alcohol = 0

        if(patient_coughing == "Yes/No"):
            patient_coughing = 1
        else:
            patient_coughing = 0

        if(patient_shortness_of_breath == "Yes/No"):
            patient_shortness_of_breath = 1
        else:
            patient_shortness_of_breath = 0

        if(patient_swallowing == "Yes/No"):
            patient_swallowing = 1
        else:
            patient_swallowing = 0

        if(patient_chest_pain == "Yes/No"):
            patient_chest_pain = 1
        else:
            patient_chest_pain = 0


        # Accuracy of Model
        model.fit(x_train, y_train) #<-- this line
        acc = model.score(x_train, y_train)

        predict_real = model.predict([[patient_age, patient_gender, patient_smoking, patient_yellowFingers,
          patient_anxiety, patient_peerPressure, patient_chronicDisease, patient_fatigue, patient_allergy,
          patient_wheezing, patient_alcohol, patient_coughing, patient_shortness_of_breath,
          patient_swallowing, patient_chest_pain]])

        if(predict_real == [0]):
            predict = "The result returned with " + str(round(acc,2)*100)  + "% accuracy and you don't have lung cancer"
        else:
            predict = "The result returned with " + str(round(acc,2)*100) + "% accuracy and you have lung cancer"


        return render_template('index.html', predict=predict)
        print(predict)

    else:
        return render_template('index.html', predict=predict)
        print(predict)



@appweb.route('/about')
def about():
    return render_template("about.html")



if __name__ == '__main__':

    # arg parser for the standard anaconda-project options
    parser = ArgumentParser(prog="home",
                            description="Simple Flask Application")
    parser.add_argument('--anaconda-project-host', action='append', default=[],
                        help='Hostname to allow in requests')
    parser.add_argument('--anaconda-project-port', action='store', default=3737, type=int,
                        help='Port to listen on')
    parser.add_argument('--anaconda-project-iframe-hosts',
                        action='append',
                        help='Space-separated hosts which can embed us in an iframe per our Content-Security-Policy')
    parser.add_argument('--anaconda-project-no-browser', action='store_true',
                        default=False,
                        help='Disable opening in a browser')
    parser.add_argument('--anaconda-project-use-xheaders',
                        action='store_true',
                        default=False,
                        help='Trust X-headers from reverse proxy')
    parser.add_argument('--anaconda-project-url-prefix', action='store', default='',
                        help='Prefix in front of urls')
    parser.add_argument('--anaconda-project-address',
                        action='store',
                        #default='0.0.0.0',
                        help='IP address the application should listen on.')

    args = parser.parse_args()

    app = Flask(__name__)
    app.register_blueprint(appweb, url_prefix = args.anaconda_project_url_prefix)

    app.config['PREFERRED_URL_SCHEME'] = 'https'

    app.wsgi_app = ProxyFix(app.wsgi_app)
    app.run(host=args.anaconda_project_address, port=args.anaconda_project_port)
