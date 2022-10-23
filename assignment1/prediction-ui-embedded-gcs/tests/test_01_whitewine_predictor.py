# content of test_sysexit.py
import os
import pytest
import pandas as pd

# content of test_class.py
import whitewine_predictor


class TestWhitewinePredictor:

    @pytest.fixture(scope="session", autouse=True)
    def execute_before_any_test(self):
        os.environ["MODEL_NAME"] = "testResources/lrmodel.pkl"

    # your setup code goes here, executed ahead of first test
    def test_predict_single_record(self):
        with open('testResources/prediction_request.json') as json_file:
            data = pd.read_json(json_file)
        dp = whitewine_predictor.WhitewinePredictor()
        status = dp.predict_single_record(data)
        assert bool(status[0]) is not None
        assert bool(status[0]) is False
