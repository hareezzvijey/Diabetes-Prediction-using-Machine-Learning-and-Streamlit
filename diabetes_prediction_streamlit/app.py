import numpy as np
import joblib
import streamlit as sp

# Load the trained model
model = joblib.load('svm_model_diabetes.pkl')

# Prediction function
def predict(data):
    prediction = model.predict(np.array(data).reshape(1, -1))
    if prediction[0] == 0:
        return '✅ The person is **not diabetic**'
    else:
        return '⚠️ The person **is diabetic**'

# Streamlit UI
def main():
    sp.title('🩺 Diabetes Prediction Web App')
    sp.write('This web app predicts whether a person is diabetic based on health data.')

    # Gender input (Binary encoding)
    gender = sp.selectbox('Gender', ['Male', 'Female'])
    gender = 1 if gender == 'Male' else 0

    # Age
    age = sp.number_input('Age', min_value=0, max_value=120, step=1)

    # Hypertension (Binary encoding)
    hypertension = sp.selectbox('Hypertension', ['No', 'Yes'])
    hypertension = 1 if hypertension == 'Yes' else 0

    # Heart Disease (Binary encoding)
    heart_disease = sp.selectbox('Heart Disease', ['No', 'Yes'])
    heart_disease = 1 if heart_disease == 'Yes' else 0

    # Smoking History (One-hot encoding with drop='first')
    smoking_history_input = sp.selectbox(
        'Smoking History', 
        ['never', 'No Info', 'current', 'former', 'ever', 'not current']
    )
    smoking_onehot = [0, 0, 0, 0, 0]  # For ['No Info', 'current', 'former', 'ever', 'not current']
    if smoking_history_input != 'never':
        index_map = {
            'No Info': 0,
            'current': 1,
            'former': 2,
            'ever': 3,
            'not current': 4
        }
        smoking_onehot[index_map[smoking_history_input]] = 1

    # BMI
    bmi = sp.number_input('BMI (Body Mass Index)', min_value=0.0, format="%.2f")

    # HbA1c Level
    hba1c = sp.number_input('HbA1c Level', min_value=0.0, format="%.1f")

    # Blood Glucose Level
    glucose = sp.number_input('Blood Glucose Level', min_value=0.0, format="%.1f")

    # Submit button
    if sp.button('Predict'):
        input_data = [
            gender, age, hypertension, heart_disease, 
            bmi, hba1c, glucose
        ] + smoking_onehot

        result = predict(input_data)
        sp.success(result)

if __name__ == '__main__':
    main()
