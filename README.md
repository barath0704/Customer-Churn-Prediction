# 📉 Customer Churn Prediction (Machine Learning)

This project analyzes customer churn behavior using real-world telecom data and applies machine learning models to predict customer retention. It includes exploratory data analysis, survival analysis, and predictive modeling to help businesses proactively identify customers at risk of churning.

---

## 🧠 Problem Statement

Telecom companies often struggle with retaining customers due to lack of visibility into churn behavior. The aim of this project is to develop a predictive model that can identify which customers are most likely to leave, enabling the company to implement targeted retention strategies.

---

## 🙋‍♂️ My Role

As the sole contributor to this project, I performed:
- Data cleaning and exploration
- Feature engineering and EDA visualizations
- Survival analysis to understand churn timing
- Machine learning model training for churn classification
- Interpretation of business insights and risk factors

---

## 📊 Project Highlights

- ✅ **EDA**: Explored key churn patterns across tenure, contract types, charges, etc.
- 🔁 **Survival Analysis**: Modeled the duration before customer churn using Kaplan-Meier estimators
- 🤖 **Modeling**: Built a logistic regression model to classify churners vs. loyal customers
- 🧾 **Feature Analysis**: Identified important factors like Monthly Charges and Contract Type
- 📌 **Actionable Insights**: Recommendations to reduce churn via targeted offers and plan adjustments

---

## 📁 Notebooks Included

| Notebook                       | Purpose                                             |
|--------------------------------|-----------------------------------------------------|
| `Exploratory Data Analysis.ipynb` | Visualize trends in churn vs. customer attributes    |
| `Customers Survival Analysis.ipynb` | Use survival curves to estimate customer lifetimes  |
| `Churn Prediction Model.ipynb`     | ML model to predict churn likelihood                |

---

## 📦 Dataset Source

- 📁 Dataset: [Telco Customer Churn – Kaggle](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- 📌 Features: Customer Demographics, Services, Billing, Churn Flag
- 📈 Target: `Churn` (Yes/No)

---

## 🧰 Tools & Technologies

| Tool/Library     | Purpose                                |
|------------------|----------------------------------------|
| Python           | Core programming                       |
| Pandas, NumPy    | Data manipulation                      |
| Matplotlib, Seaborn | Data visualization                   |
| Lifelines        | Survival analysis                      |
| Scikit-learn     | Machine learning modeling              |
| Jupyter Notebook | Development environment                |

---

## 📍 Key Insights

- 📈 Customers with month-to-month contracts are **3x more likely** to churn.
- 💳 Higher **monthly charges** significantly increase churn risk.
- ⌛ Customers typically churn within **first 20 months** if not retained.
- 🔄 Retention offers could focus on longer-term contracts and bundled services.

---

## 🧠 Future Enhancements

- 🔁 Test other ML models like Random Forest and XGBoost
- 🌐 Deploy as a Streamlit app for interactive churn prediction
- 📊 Integrate with a CRM for real-time alerts

---

## 🏁 Conclusion

This project demonstrates how data science can be applied to a practical business problem — churn. The models and insights generated can help companies save millions in lost customers.

