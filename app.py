import streamlit as st
import pandas as pd
import joblib

# Load the trained model and encoders
model = joblib.load("pkl/model.pkl")
occupation_encoder = joblib.load("pkl/occ_encoder.pkl")
gender_encoder = joblib.load("pkl/gender_encoder.pkl")
scaler = joblib.load("pkl/scaler.pkl")

# Streamlit page config
st.set_page_config(page_title="Employee Salary Prediction", page_icon="💼", layout="centered")

# Apply background image using custom CSS
page_bg_img = '''
<style>
    .stApp {
        background-image: url("https://github.com/BKY1601/employee-salary-prediction/blob/main/src/img/bg.jpg?raw=true");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }
</style>
'''
st.markdown(page_bg_img, unsafe_allow_html=True)

st.title("💼 Employee Salary Prediction")
st.markdown("Predict whether an employee earns more then 50K or Less then 50K based on input features.")

# Sidebar inputs
st.sidebar.header("Input Employee Details")

age = st.sidebar.slider("Age", 18, 65, 30)

education_levels = {
    "Preschool": 1, "1st-4th": 2, "5th-6th": 3, "7th-8th": 4, "9th": 5,
    "10th": 6, "11th": 7, "12th": 8, "HS-grad": 9, "Some-college": 10,
    "Assoc": 11, "Bachelors": 13, "Masters": 14, "PhD": 16
}
education_label = st.sidebar.selectbox("Education Level", list(education_levels.keys()))
educational_num = education_levels[education_label]

occupation_label = st.sidebar.selectbox("Job Role", [
    "Tech-support", "Craft-repair", "Other-service", "Sales",
    "Exec-managerial", "Prof-specialty", "Handlers-cleaners", "Machine-op-inspct",
    "Adm-clerical", "Farming-fishing", "Transport-moving", "Priv-house-serv",
    "Protective-serv", "Armed-Forces"
])
gender_label = st.sidebar.radio("Gender", ["Male", "Female"])

hours_per_week = st.sidebar.slider("Hours per week", 1, 80, 40)

# Encode occupation and gender using saved encoders
occupation_encoded = occupation_encoder.transform([occupation_label])[0]
gender_encoded = gender_encoder.transform([gender_label])[0]

# Build input DataFrame
input_df = pd.DataFrame({
    'age': [age],
    'educational-num': [educational_num],
    'occupation': [occupation_encoded],
    'gender': [gender_encoded],
    'hours-per-week': [hours_per_week]
})

st.write("### 🔎 Input Data")
st.write(input_df)

# Predict
if st.button("Predict Salary"):
    input_scaled = scaler.transform(input_df)
    prediction = model.predict(input_scaled)[0]
    salary_class = "More than 50K" if prediction == 1 else "Less than or equal to 50K"
    st.success(f"✅ Prediction: {salary_class}")

# Batch prediction
st.markdown("---")
st.markdown("#### 📂 Batch Salary Prediction")
uploaded_file = st.file_uploader("Upload a CSV file for batch prediction", type="csv")

if uploaded_file is not None:
    try:
        batch_data = pd.read_csv(uploaded_file)

        # Encode batch data
        batch_data['occupation'] = occupation_encoder.transform(batch_data['occupation'])
        batch_data['gender'] = gender_encoder.transform(batch_data['gender'])

        batch_data_scaled = scaler.transform(batch_data)
        batch_preds = model.predict(batch_data_scaled)

        batch_data['Predicted Salaries'] = ["More than 50K" if pred == 1 else "Less than or equal to 50K" for pred in batch_preds]

        st.write("✅ Predictions:")
        st.write(batch_data.head())

        csv = batch_data.to_csv(index=False).encode('utf-8')
        st.download_button("Download Predictions CSV", csv, file_name='predicted_Salaries.csv', mime='text/csv')

    except Exception as e:
        st.error(f"❌ Error during batch prediction: {e}")
