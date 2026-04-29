# 🚨 Fraud Detection using Transaction Network Analysis

## 📌 Project Overview

This project focuses on detecting fraudulent financial transactions using **Transaction Network Analysis**. It analyzes transaction data and identifies suspicious patterns such as high-value transfers, unusual frequency, and circular money flow between accounts.

The system is built using **Python, Streamlit, and NetworkX**, and provides an interactive dashboard with visualizations and network graphs.

---

## 🎯 Objective

* Detect fraudulent transactions from transaction data
* Identify suspicious accounts and patterns
* Visualize transaction relationships using network graphs
* Provide insights for decision-making

---

## 🧠 Key Concepts

* Data Analytics (Descriptive & Diagnostic)
* Exploratory Data Analysis (EDA)
* Network Graph Analysis
* Fraud Pattern Detection

---

## 📊 Features

* 📈 Fraud vs Normal Transactions (Pie Chart)
* 📊 Transaction Amount Distribution (Histogram)
* 📉 Transactions Over Time (Line Graph)
* 🕸️ Transaction Network Graph (Node-Link Diagram)
* 📌 Suspicious Accounts Detection

---

## 🗂️ Dataset Description

The dataset contains financial transaction records with the following attributes:

* Sender
* Receiver
* Amount
* Date & Time
* Transaction Type
* Fraud Label (Yes/No)

Each row represents a single transaction.

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Plotly
* NetworkX
* Streamlit

---

## 📁 Project Structure

```
Fraud_Project/
│
├── app.py                # Main Streamlit dashboard
├── data.py              # Dummy data generator
├── transactions.csv     # Dataset
└── README.md            # Project documentation
```

---

## ▶️ How to Run the Project

### 1. Install Dependencies

```
pip install streamlit pandas numpy plotly networkx
```

### 2. Generate Dataset

```
python data.py
```

### 3. Run the Application

```
streamlit run app.py
```

---

## 📊 Output

The system generates:

* Interactive dashboard
* Fraud detection insights
* Network graph visualization
* Suspicious account identification

---

## ✅ Results

* Successfully detected fraudulent transactions
* Identified high-risk accounts
* Visualized fraud connections using network graphs

---

## 🔮 Future Enhancements

* Machine Learning integration (Random Forest, SVM)
* Real-time fraud detection
* Deep learning-based anomaly detection
* Mobile application dashboard

---

## 📚 References

* https://www.kaggle.com/datasets
* https://pandas.pydata.org/docs/
* https://numpy.org/doc/
* https://networkx.org/documentation/stable/
* https://docs.streamlit.io/
* https://plotly.com/python/

---

## 👨‍💻 Author

Mini Project – Data Analytics Lab
Fraud Detection using Transaction Network Analysis
