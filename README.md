# 🥐 SmartBake – Bakery Demand Prediction

A machine learning-based bakery demand prediction application that classifies expected product demand into **Low, Medium, or High** categories. The project combines model training and a Flask web interface to make demand predictions using bakery and environmental factors.

## 🌐 Live Demo

[Open SmartBake – Bakery Demand Prediction](https://smartbake-bakery-demand-prediction.onrender.com/)

## 🚀 Key Features

- **Demand Classification:** Predicts bakery demand as Low, Medium, or High.
- **Multiple ML Models:** Supports Decision Tree, Pruned Decision Tree, and Support Vector Machine (SVM).
- **Interactive Web Interface:** Enter input values and view predictions through a Flask application.
- **10 Input Features:** Uses product, day, weekend, previous sales, 7-day average, price, promotion, temperature, rainfall, and holiday information.
- **Model Selection:** Allows users to select between the available trained models.

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Web Framework | Flask |
| Data Analysis | Pandas, NumPy |
| Development Environment | Jupyter Notebook |
| Frontend | HTML, CSS |
| Model Storage | Pickle (`.pkl`) |

## 🧠 Machine Learning Models

The application includes three trained models:

1. Decision Tree
2. Pruned Decision Tree
3. Support Vector Machine (SVM)

Each model is stored as a serialized `.pkl` file and loaded by the Flask application to generate predictions.

## 📊 Input Features

The prediction pipeline uses the following 10 input features:

- Product
- Day
- Weekend
- Previous Sales
- 7-Day Average
- Price
- Promotion
- Temperature
- Rainfall
- Holiday

## 📁 Project Structure

```text
SmartBake-Bakery-Demand-Prediction/
│
├── models/
│   ├── decision_tree.pkl
│   ├── pruned_decision_tree.pkl
│   └── svm.pkl
│
├── app.py
├── requirements.txt
└── bakery.ipynb
```

## ⚙️ Run Locally

### Prerequisites
- Python 3.x
- pip

### 1. Clone the repository

```bash
git clone https://github.com/keerthi2513/SmartBake-Bakery-Demand-Prediction.git
cd SmartBake-Bakery-Demand-Prediction
```

### 2. Create a virtual environment

```bash
python -m venv venv
```

Activate it:

**Windows**
```bash
venv\Scripts\activate
```

**macOS / Linux**
```bash
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Verify the model files

Ensure the three trained model files are present inside the `models/` directory.

### 5. Run the application

```bash
python app.py
```

Open your browser at:

```text
http://127.0.0.1:5000
```

## 🎯 Prediction Output

The application predicts one of three demand categories:

- **Low Demand**
- **Medium Demand**
- **High Demand**

## 🔮 Future Enhancements

- Integrate real-time sales data.
- Improve model evaluation and comparison.
- Add visual analytics for historical demand patterns.
- Explore time-series forecasting for demand prediction.

## 👩‍💻 Developed By

**Kadali Keerthi Priya**

B.Tech – Computer Science and Engineering (Data Science)  
G. Narayanamma Institute of Technology and Science

[GitHub Profile](https://github.com/keerthi2513)
