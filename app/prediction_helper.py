import joblib
import numpy as np
import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Path to the saved model and its components
MODEL_PATH = 'app/artifacts/model_pipeline.joblib'

# Load the model and its components
pipe = joblib.load(MODEL_PATH)


def prepare_input(input_dict):
    # Create a dictionary with input values and dummy values for missing features

    
    # Ensure all columns for features and cols_to_scale are present
    df = pd.DataFrame(input_dict, index=[0])

    return df

def calculate_credit_score(input_df, base_score=300, scale_length=600):
    # x = np.dot(input_df.values, pipe.named_steps['model'].coef_.coef_.T) + pipe.named_steps['model'].intercept_

    # Apply the logistic function to calculate the probability
    default_probability = pipe.predict_proba(input_df)[:, 1]

    non_default_probability = 1 - default_probability

    # Convert the probability to a credit score, scaled to fit within 300 to 900
    credit_score = base_score + non_default_probability.flatten() * scale_length

    # Determine the rating category based on the credit score
    def get_rating(score):
        if 300 <= score < 500:
            return 'Poor'
        elif 500 <= score < 650:
            return 'Average'
        elif 650 <= score < 750:
            return 'Good'
        elif 750 <= score <= 900:
            return 'Excellent'
        else:
            return 'Undefined'  # in case of any unexpected score

    rating = get_rating(credit_score[0])

    return default_probability.flatten()[0], int(credit_score[0]), rating

def predict(input_dict):
    # Prepare input data
    input_df = prepare_input(input_dict)

    probability, credit_score, rating = calculate_credit_score(input_df)

    return probability, credit_score, rating
