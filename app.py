from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from Mlproject.pipeline.prediction import PredictionPipeline

template_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'templates'))
static_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'static'))

print(f"Template directory: {template_dir}")
print(f"Template exists: {os.path.exists(template_dir)}")
print(f"index.html exists: {os.path.exists(os.path.join(template_dir, 'index.html'))}")

app = Flask(__name__,
           template_folder=template_dir,
           static_folder=static_dir)


@app.route('/', methods=['GET'])
def homepage():
    return render_template("index.html")


@app.route('/train', methods=['GET'])
def training():
    os.system("python main.py")
    return "training successful"


@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get data from form
            input_data = {
                'fixed_acidity': float(request.form['fixed_acidity']),
                'volatile_acidity': float(request.form['volatile_acidity']),
                'citric_acid': float(request.form['citric_acid']),
                'residual_sugar': float(request.form['residual_sugar']),
                'chlorides': float(request.form['chlorides']),
                'free_sulfur_dioxide': float(request.form['free_sulfur_dioxide']),
                'total_sulfur_dioxide': float(request.form['total_sulfur_dioxide']),
                'density': float(request.form['density']),
                'pH': float(request.form['pH']),
                'sulphates': float(request.form['sulphates']),
                'alcohol': float(request.form['alcohol'])
            }
            
            # Convert to numpy array for prediction
            data = np.array(list(input_data.values())).reshape(1, -1)
            
            obj = PredictionPipeline()
            prediction = obj.predict(data)

            # Return results page with prediction and input data
            return render_template("results.html", 
                                prediction=prediction[0],
                                input_data=input_data)
            
        except Exception as e:
            print(e)
            return render_template("index.html", error="Error occurred during prediction")
    
    # If GET request, show the prediction form
    return render_template("index.html")


@app.route('/about')
def about():
    return "About Page" 


@app.route('/contact')
def contact():
    return "Contact Page"  


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)