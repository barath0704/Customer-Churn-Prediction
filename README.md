# 🔄 Customer Churn Prediction Project

This project uses real-world customer data to analyze patterns in churn behavior and predict which users are likely to leave a service. It includes exploratory data analysis, survival analysis, and machine learning modeling.

---

## 📁 Project Structure

| File                          | Description                                 |
|-------------------------------|---------------------------------------------|
| `1_EDA.ipynb`                 | Exploratory analysis of customer behavior   |
| `2_Survival_Analysis.ipynb`   | Time-to-event (churn) analysis              |
| `3_Churn_Prediction_Model.ipynb` | Logistic regression & decision tree models for churn prediction |
| `dataset.csv` *(optional)*    | The dataset used (if public)                |

---

## ❓ Problem Statement

The goal is to **identify patterns in customer behavior that lead to churn** and build a predictive model to help businesses **retain users** more effectively.

---

## 💻 Tools Used

- Python (Pandas, NumPy, Seaborn, Matplotlib)
- Scikit-learn
- Jupyter Notebook

---

## 📊 Key Insights

- Customers with longer contract durations are less likely to churn.
- Monthly charges and service usage patterns strongly influence churn risk.
- Survival analysis shows churn risk is highest in the first 6 months.

---

## 📈 Models Used

- Logistic Regression
- Decision Tree Classifier
- Accuracy & AUC used for evaluation

---

## 🎯 Outcomes

- Developed a working churn prediction model
- Identified key customer behavior influencing churn
- Useful for telecom, SaaS, or subscription-based services

---

## 📌 Future Improvements

- Use XGBoost or Random Forest for better performance
- Deploy as a Flask app or Streamlit dashboard
