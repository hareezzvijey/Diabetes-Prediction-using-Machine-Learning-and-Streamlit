import numpy as np
import joblib
import streamlit as sp

# Load the trained model
model = joblib.load('diabetes_prediction_streamlit/ensemble_model_diabetes.pkl')

# Prediction function
def predict(data):
    prediction = model.predict(np.array(data).reshape(1, -1))
    if prediction[0] == 0:
        return '✅ The person is **not diabetic**'
    else:
        return '⚠️ The person **is diabetic**'

# Prediction function
def main():
    sp.title('🩺 Diabetes Prediction Web App')
    sp.write('This web app predicts whether a person is diabetic based on health data.')

    gender = sp.selectbox('Gender', ['Male', 'Female'])
    gender = 1 if gender == 'Male' else 0

    age = sp.number_input('Age', min_value=0, max_value=120, step=1)

    hypertension = sp.selectbox('Hypertension', ['No', 'Yes'])
    hypertension = 1 if hypertension == 'Yes' else 0

    heart_disease = sp.selectbox('Heart Disease', ['No', 'Yes'])
    heart_disease = 1 if heart_disease == 'Yes' else 0

    smoking_history_input = sp.selectbox(
        'Smoking History', 
        ['never', 'No Info', 'current', 'former', 'ever', 'not current']
    )
    # One-hot encoding with drop='first' means 'never' is dropped, so set all 0 initially
    smoking_onehot = [0, 0, 0, 0, 0]  # ['No Info', 'current', 'former', 'ever', 'not current']

    if smoking_history_input != 'never':
        index_map = {
            'No Info': 0,
            'current': 1,
            'former': 2,
            'ever': 3,
            'not current': 4
        }
        smoking_onehot[index_map[smoking_history_input]] = 1

    bmi = sp.number_input('BMI (Body Mass Index)', min_value=0.0, format="%.2f")

    hba1c = sp.number_input('HbA1c Level', min_value=0.0, format="%.1f")

    glucose = sp.number_input('Blood Glucose Level', min_value=0.0, format="%.1f")

    if sp.button('Predict'):
        # Order matters! Put smoking onehot first, then other features in order:
        input_data = smoking_onehot + [
            gender, age, hypertension, heart_disease, bmi, hba1c, glucose
        ]

        result = predict(input_data)
        sp.success(result)

if __name__ == '__main__':
    main()
