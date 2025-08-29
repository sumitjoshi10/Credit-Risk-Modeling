# 📊 Lauki Finance: Credit Risk Modelling

This is a **Streamlit-based web application** that predicts the credit risk of an applicant based on financial, demographic, and behavioral factors.  
It provides an interactive interface where users can input their details and receive **default probability, credit score, and risk rating** instantly.

---

## 🛑 Problem Statement

Financial institutions face challenges in evaluating credit risk when issuing loans. Traditional methods rely heavily on credit history and manual underwriting, which can be:

- **Time-consuming** – requiring manual checks and verification.  
- **Inconsistent** – prone to human bias and subjective interpretation.  
- **Limited** – failing to incorporate modern behavioral and demographic indicators.  

As a result, lenders struggle to accurately determine:

- The **Probability of Default (PD)** of an applicant.  
- The **Creditworthiness Score** reflecting financial health.  
- The **Risk Rating** (Low, Medium, High) for decision-making.

---

## ✅ Solution Implemented

This project provides a **Streamlit-based Credit Risk Modelling application** that automates and enhances the decision-making process by:

- **Collecting applicant data:** age, income, loan details, credit utilization, delinquency history, residence type, loan type, and purpose.  
- **Calculating derived metrics** such as Loan-to-Income Ratio, a key factor in loan approval.  
- **Handling imbalanced data**:
  - The dataset was highly imbalanced, with far fewer default cases.  
  - The focus was on achieving **recall > 90%** to minimize false negatives (i.e., missing actual defaulters).  
  - Precision was deprioritized since flagged applicants would still undergo **human verification** before final decisions.  

- **Applying Machine Learning models** to:
  - Predict **Default Probability (%)**  
  - Generate **Credit Score**  
  - Assign **Risk Rating** (Low/Medium/High)  

- **Providing instant results** via a **clean and user-friendly UI**, helping lenders and analysts make **faster, more consistent, and data-driven loan approval decisions**.

---

## 📊 Datasets Used

The model was trained on three datasets, each providing unique insights:

1. **Customer Data** – demographic and personal details (age, income, residence type).  
2. **Loan Data** – information on current and past loans (loan amount, tenure, type, purpose).  
3. **Bureau Data** – credit history and repayment behavior (delinquency ratio, DPD, open accounts).  

These datasets were merged and preprocessed to engineer features such as **Loan-to-Income Ratio** and **Credit Utilization Ratio**, improving model accuracy.

---

## 📸 App Demo

🌐 Live Demo:  
👉 [Lauki Finance: Credit Risk Modelling](#)  

---

## 🚀 Features

- Collects applicant details:
  - Age, Income, Loan Amount  
  - Loan Tenure (months), Loan-to-Income Ratio  
  - Delinquency Ratio, Avg DPD per Delinquency  
  - Credit Utilization Ratio, Number of Open Loan Accounts  
  - Residence Type, Loan Purpose, Loan Type  

- Clean UI with **4 rows of input fields arranged neatly** in columns.  
- Dynamically calculates **Loan-to-Income Ratio**.  
- Predicts results using a **trained ML model** (via `predication_helper.py`).  
- Displays:
  - Default Probability (%)  
  - Credit Score  
  - Risk Rating (Low/Medium/High)  

---

## 📂 Project Structure

```
credit-risk-modelling/
│
├── app/
│   ├── artifacts/              # Trained model files (joblib/pickle)
│   ├── main.py                 # Streamlit app
│   ├── predication_helper.py   # Contains predict() function
│
├── experiment/                 # Notebooks, EDA, model training logs
│   └── *.ipynb
│
├── README.md                   # Project documentation
├── requirements.txt            # Python dependencies
```

---

## ⚙️ Installation & Setup

1️⃣ **Clone the repository**  
```bash
git clone https://github.com/sumitjoshi10/credit-risk-modelling.git
cd credit-risk-modelling
```

2️⃣ **Create a virtual environment** (optional but recommended)  
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```

3️⃣ **Install dependencies**  
```bash
pip install -r requirements.txt
```

4️⃣ **Run the app**  
```bash
streamlit run app/main.py
```

---

## 🧠 Model Details

- ML model is stored in `artifacts/` and loaded via `predication_helper.py`.  
- Generates credit risk predictions based on applicant features.  
- **Focuses on high recall** to reduce the chance of approving risky customers.  
- Uses engineered features from **Customer, Loan, and Bureau datasets**.  
- **Models used:** Logistic Regression, Random Forest, XGBoost.  
- **Final model:** Logistic Regression, as it gave the **best recall of 94%, accuracy of 93%, and AUC of 0.98**.  

---

## 🤝 Contributing

Contributions are welcome!  

1. Fork the repo  
2. Create a new branch (`feature/new-feature`)  
3. Commit your changes  
4. Push and open a Pull Request

