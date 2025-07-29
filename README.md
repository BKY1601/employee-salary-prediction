# 💼 Employee Salary Prediction App

This project is a **Machine Learning web application** built using **Streamlit** that predicts whether an employee earns more than 50K or less than or equal to 50K annually based on features like age, education, occupation, gender, hours per week, etc.

---

## 🚀 Project Overview

The app uses a trained **Logistic Regression** model. The dataset includes demographic and employment information of individuals to predict their income bracket.

---

## 📊 Features Used for Prediction

- Age
- Educational level (converted to numeric)
- Occupation (Label Encoded)
- Gender (Label Encoded)
- Hours per week

---

## 🧠 Model Training

- **Preprocessing:**  
  - Label Encoding for `occupation` and `gender`
  - Numeric scaling (if used, with `StandardScaler`)
- **Model Used:**  
  - Logistic Regression (with `class_weight=balanced`)  
- **Model Evaluation:**  
  - Accuracy Score
- **Imbalanced Dataset Handling:**  
  - Optional: class balancing via model parameter (`class_weight`)

---

## 🗂️ Project Structure

```````
.
├── app.py # Streamlit app
├── model.pkl # Trained model file
├── occ_encoder.pkl # Saved occupation encoder
├── gender_encoder.pkl # Saved gender encoder
├── scaler.pkl (optional) # Saved scaler if used
├── requirements.txt # Python dependencies
└── README.md # Project documentation

```````
---


---

## 🖥️ How to Run the App

### 1. Clone the Repository
bash
git clone https://github.com/your-username/employee-salary-prediction.git
cd employee-salary-prediction

### 2. Install Dependencies
pip install -r requirements.txt

### 3. Run the Streamlit App
streamlit run app.py

-----

### 📥 Batch Prediction
The app allows batch predictions via CSV file upload. Ensure the CSV includes the same columns used during training:

### 1. age
### 2. educational-num
### 3. occupation
### 4. gender
### 5. hours-per-week

The app will encode these using the saved label encoders and return salary class predictions.

---

### 📸 Screenshot

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/5dc28add-f2d6-401b-9dfd-64b923915861" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/870cc4ff-13af-42fd-b561-729a1ead9067" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/b090b82f-c29c-4e3b-b5d4-ae4eb8a8c2e9" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/dd9351fe-6e05-476a-81cb-c89de8077e33" />

<img width="1366" height="768" alt="image" src="https://github.com/user-attachments/assets/48fbda78-44e6-4961-a714-2ba75d13b6fa" />

---

## 👨‍💻 Author

**Bipin Yadav**  
📧 bipinyadav919@gmail.com  
🔗 [LinkedIn](https://linkedin.com/in/bipin-yadav-jan16)  
🔗 [GitHub](https://github.com/BKY1601)                                                                                                   
🔗 [Live project Link](https://employee-salary-prediction-by-bky.streamlit.app/)


