# importing Flask and other modules
import json
import os

import pandas as pd
from flask import Flask, request, render_template, jsonify

from whitewine_predictor import WhitewinePredictor

# Flask constructor
app = Flask(__name__)


# A decorator used to tell the application
# which URL is associated function
@app.route('/whitewine', methods=["GET", "POST"])
def check_diabetes():
    if request.method == "POST":
        prediction_input = [
            {
                "fixed acidity": float(request.form.get("fixed acidity")),  # getting input with name = ntp in HTML form
                "volatile acidity": float(request.form.get("volatile acidity")),  # getting input with name = pgc in HTML form
                "citric acid": float(request.form.get("citric acid")),
                "residual sugar": float(request.form.get("residual sugar")),
                "chlorides": float(request.form.get("chlorides")),
                "free sulfur dioxide": float(request.form.get("free sulfur dioxide")),
                "total sulfur dioxide": float(request.form.get("total sulfur dioxide")),
                "density": float(request.form.get("density")),
                "pH": float(request.form.get("pH")),
                "sulphates": float(request.form.get("sulphates")),
                "alcohol": float(request.form.get("alcohol"))
            }
        ]
        print(prediction_input)
        dp = WhitewinePredictor()
        df = pd.read_json(json.dumps(prediction_input), orient='records')
        status = dp.predict_single_record(df)
        # return the prediction outcome as a json message. 200 is HTTP status code 200, indicating successful completion
        return jsonify({'result': str(status)}), 200

    return render_template(
        "user_form.html")  # this method is called of HTTP method is GET, e.g., when browsing the link


if __name__ == '__main__':
    app.run(port=int(os.environ.get("PORT", 5000)), host='0.0.0.0', debug=True)
