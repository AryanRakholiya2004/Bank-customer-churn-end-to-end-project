# 🔍 Bank Churn Prediction – End-to-End ML Project

This project is an end-to-end machine learning pipeline built to predict customer churn for a fictional bank. It follows professional MLOps practices with proper folder structure, version-controlled data, automated workflows, and modular code to ensure the project is production-ready.

---

## 📌 Project Objective

To develop a machine learning model that identifies customers likely to leave the bank. The goal is to help financial institutions proactively retain customers and improve business decision-making.

---

## 🌄 Previews

### Dashboard Preview
![image](https://github.com/user-attachments/assets/048b4ff6-a90e-4da5-8a24-0982fc4467e6)


---

## 🪧 Links

- For tracking model scores - <a href="https://dagshub.com/AryanRakholiya2004/Bank-customer-churn-end-to-end-project.mlflow/#/experiments/0?searchFilter=&orderByKey=attributes.start_time&orderByAsc=false&startTime=ALL&lifecycleFilter=Active&modelVersionFilter=All+Runs&datasetsFilter=W10%3D">MLflow </a>


## 📁 Project Structure

- END-TO-END-PROJECT/ 
- │ 
- ├── .dvc/ # Data version control files 
- ├── artifacts/ # Saved model files and outputs 
- ├── datascienceproject/ # All ML pipeline scripts (training, evaluation, utils) 
- ├── deployment/ # Contains Deployable Streamlit apps
- ├── logs/ # Logging directory 
- ├── notebook/ 
- │ └── 1.EDA.ipynb # Exploratory Data Analysis notebook 
- │ └── 1.MODEL TRAINING.ipynb # Model training notebook 
- │ └── data/raw.csv # Raw dataset 
- ├── app.py # Flask API for model inference 
- ├── setup.py # Package installation script 
- ├── requirements.txt # List of required Python libraries 
- ├── README.md # Project documentation 
- └── Bank_Churn.csv # Original dataset


---

## 🚀 Features

- ✅ End-to-end ML pipeline from data loading to deployment
- 📊 EDA with insightful visualizations
- 🧠 Feature engineering and model building
- ⚙️ Hyperparameter tuning with GridSearchCV
- 🔁 Model tracking and versioning using **MLFlow and Dagshub**
- 💾 **DVC** - Data Version Control and tracking using <a href="https://dvc.org/">**dvc.org**</a>
- 🔌 Deployed using Flask API (`app.py`)
- 🧪 Ready to integrate **CI/CD** for automated testing and deployment

---

## 🔧 Tech Stack

- Python  
- Pandas, NumPy, Matplotlib, Seaborn  
- Scikit-learn, tensorflow
- Flask (for deployment)  
- DVC (for version control)  
- Mlflow, Dagshub
- Git, GitHub

---

## 📊 Exploratory Data Analysis

The notebook includes detailed EDA with visualizations to understand:
- Churn distribution
- Impact of features like tenure, balance, and credit score
- Correlations and data cleaning

---

## 🚀 Model Building

Multiple models were tested:
- Logistic Regression  
- Decision Tree  
- Random Forest  
- Gradient Boosting
- XGBoost
- CatBoost
- LightGBM

Evaluation metrics like accuracy, precision, and recall were used to select the best-performing model.

---

## 💾 Dataset used

🔗 <a href="https://mavenanalytics.io/data-playground?dataStructure=Single%20table&order=date_added%2Cdesc&search=Bank%20Customer%20Churn">Bank Customer Churn</a>

## 📦 Getting Started

1. Clone the repo  
```bash
git clone https://github.com/your-username/bank-churn-prediction.git
cd bank-churn-prediction
```
2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Run the app.py
```bash
python app.py
```

---

📌 Status
🔧 This project is still under development. I'm actively working on refining the pipeline, improving 📈 performance, and integrating CI/CD for automated 🛠️ testing and 🚀 deployment, also working on 🤖 Neural Network model.

---

## 🤝 Let's Connect
If you have suggestions, want to collaborate, or just want to say hi — feel free to connect with me on LinkedIn!
