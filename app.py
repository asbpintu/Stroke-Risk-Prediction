from flask import Flask, render_template, request
import os
app = Flask(__name__)

from stroke_risk.pipeline.prediction import PredictionFromData


@ app.route('/', methods = ['GET', 'POST'])
def home():
    result = ''
    prob = ''
    color = ''
    text1 = ''
    text2 = ''
    if request.method == 'POST':

        name = request.form["name"]

        form_data = {
            "gender": str(request.form["gender"]),
            "age": int(request.form['age']),
            "hyper": str(request.form['hyper']),
            "heart": str(request.form['heart']),
            "marriage": str(request.form['marriage']),
            "resident": str(request.form['resident']),
            "glucose": float(request.form['glucose']),
            "bmi": float(request.form['bmi']),
            "work": str(request.form['work']),
            "smoke": str(request.form['smoke'])
            }
        
        prediction_instance = PredictionFromData(form_data)
        result, prob, color = prediction_instance.predict()

        text1 = 'You have a '
        text2 = ' chance of being affected by a Brain-Stroke.'

        return render_template('index.html', value = result, name = name, prob = prob, text1 = text1, text2 = text2, color = color)
    else:
        return render_template('index.html', value = 'Waiting . . . ', name = '', prob = prob, text1 = text1, text2 = text2, color = color)


@app.route('/training', methods=['GET', 'POST'])
def training():

    stage = 'STAGES'
    result = 'Data Ingestion >> Data Preprocess >> Data Validation >> Data Transformation >> Model Training'
    if request.method == 'POST':
        os.system('python main.py')
        print("Form submitted successfully!")
        result = 'Model Successfully Trained'
        stage = ''
        return render_template('training.html', value=result, value2 = stage)
    else:
        return render_template('training.html', value=result, value2 = stage)







if __name__ == '__main__':
    app.run(host="0.0.0.0", port = 8080)