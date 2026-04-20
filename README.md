# 💳 Credit Card Fraud Detection System

## 📌 Project Overview
An AI-powered **real-time credit card fraud detection system** that identifies potentially fraudulent transactions with **99.55% accuracy**. Built with Machine Learning and deployed as a web application.

## 🚀 Live Demo
🔗 **Try it here:** [Fraud Detection System](https://fraud-detection-mxehzesljwhhragufwudo5.streamlit.app)

## 📊 Model Performance
| Metric | Score |
|--------|-------|
| **Accuracy** | 99.55% |
| **Precision** | 95.65% |
| **Recall** | 73.33% |
| **F1-Score** | 83.02% |

## 🎯 Features
- ✅ Real-time transaction monitoring
- ✅ Instant fraud risk assessment
- ✅ Interactive web interface
- ✅ Detailed risk factor analysis
- ✅ Automated CI/CD pipeline

## 🛠️ Tech Stack
| Technology | Purpose |
|------------|---------|
| Python | Programming Language |
| Scikit-learn | Machine Learning |
| Streamlit | Web Application |
| GitHub Actions | CI/CD Pipeline |
| Streamlit Cloud | Deployment |

## 📁 Project Structure

## 🔍 How It Works
The system analyzes 5 key factors:
1. **Transaction Amount** - Unusually high amounts trigger alerts
2. **Transaction Time** - Late night transactions are high risk
3. **Location** - International transactions are scrutinized
4. **Device Type** - Unknown devices increase risk score
5. **Transaction Pattern** - Unusual patterns flag fraud

## 🚨 Risk Indicators
| Indicator | Risk Level |
|-----------|------------|
| Amount > $5,000 | 🔴 High |
| Late Night Transaction | 🔴 High |
| International Location | 🔴 High |
| Unknown Device | 🔴 High |
| Suspicious Pattern | 🔴 High |

## 🧪 Test the System

### Normal Transaction (Should be APPROVED)
**Expected Result:** ✅ Transaction Approved (Green)

### Fraud Transaction (Should be BLOCKED)
**Expected Result:** 🚨 FRAUD ALERT (Red)

## 🔧 Installation (Local Setup)

### Prerequisites
- Python 3.11+
- Git

### Steps
```bash
# Clone repository
git clone https://github.com/aroojnawaz98765-art/fraud-detection.git
cd fraud-detection

# Create virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py