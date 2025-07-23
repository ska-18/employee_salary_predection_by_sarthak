# 💼 Employee Salary Prediction by Sarthak

This project predicts whether an employee's salary is **greater than 100K** or **less than or equal to 100K**, based on features such as age, education, job title, hours per week, and more. It uses various classification algorithms and data preprocessing techniques to build a web-based salary prediction app using **Streamlit**.

---

## 🎯 Objective

To develop a **machine learning-powered web application** that accurately classifies an employee's salary category (`>100K` or `≤100K`) using their input attributes.

---

## 📁 Dataset Details

- **Dataset Name**: `employee_data.csv` (custom dataset)  
- **Source**: Provided or manually created  
- **Size**: ~2,000 to 3,000 entries (after preprocessing)

### 🔢 Features (Columns)

- Age  
- Education Level  
- Job Title / Occupation  
- Years of Experience  
- Gender *(optional)*  
- Hours per Week *(optional)*  
- Native Country *(optional)*  
- Marital Status, Race, etc.

### 🎯 Target Variable

- `Salary`: Binary classification → `>100K` or `<=100K`

---

## 🤖 Machine Learning Models Used

The following ML models were trained, evaluated, and compared:

- ✅ Logistic Regression  
- ✅ Random Forest Classifier  
- ✅ K-Nearest Neighbors (KNN)  
- ✅ Support Vector Machine (SVM)  
- ✅ Gradient Boosting Classifier  

> The **best-performing model** (based on accuracy score) is saved as `best_model.pkl`.

---

## 🛠️ System Requirements

### ✅ OS Compatibility

- Windows / macOS / Linux

### ✅ Hardware

- At least 8 GB RAM recommended

### ✅ Python Version

- Python 3.8 or above

---

## 📦 Python Dependencies

Install all required libraries using:

```bash
pip install -r requirements.txt
