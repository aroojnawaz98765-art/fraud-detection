import pandas as pd
import numpy as np
import joblib
import os
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

print("="*60)
print("💳 CREDIT CARD FRAUD DETECTION SYSTEM")
print("="*60)

# Generate realistic transaction data
print("\n📊 Generating transaction data...")
np.random.seed(42)

n_transactions = 10000
fraud_rate = 0.015  # 1.5% fraud (realistic)

# Features: amount, time_score, location_score, device_score, frequency_score
X = np.random.randn(n_transactions, 5)
y = np.zeros(n_transactions)

# Add fraud cases
n_fraud = int(n_transactions * fraud_rate)
fraud_idx = np.random.choice(n_transactions, n_fraud, replace=False)
y[fraud_idx] = 1

# Make fraud transactions look different
X[fraud_idx, 0] = X[fraud_idx, 0] + 2  # Higher amounts
X[fraud_idx, 1] = X[fraud_idx, 1] + 1.5  # Unusual time
X[fraud_idx, 2] = X[fraud_idx, 2] + 1.8  # Unusual location
X[fraud_idx, 3] = X[fraud_idx, 3] + 2.2  # Unknown device
X[fraud_idx, 4] = X[fraud_idx, 4] + 1.9  # Suspicious pattern

print(f"✅ Total transactions: {n_transactions:,}")
print(f"✅ Normal transactions: {n_transactions - n_fraud:,}")
print(f"✅ Fraud transactions: {n_fraud:,}")
print(f"✅ Fraud rate: {fraud_rate*100:.2f}%")

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

print(f"\n📊 Training data: {len(X_train):,} transactions")
print(f"📊 Testing data: {len(X_test):,} transactions")

# Train model
print("\n🚀 Training Random Forest model...")
model = RandomForestClassifier(
    n_estimators=100,
    max_depth=10,
    random_state=42,
    n_jobs=-1
)
model.fit(X_train, y_train)

# Evaluate
y_pred = model.predict(X_test)
y_pred_proba = model.predict_proba(X_test)[:, 1]

accuracy = accuracy_score(y_test, y_pred)
precision = precision_score(y_test, y_pred)
recall = recall_score(y_test, y_pred)
f1 = f1_score(y_test, y_pred)

print("\n" + "="*60)
print("📊 MODEL PERFORMANCE")
print("="*60)
print(f"🎯 Accuracy:  {accuracy*100:.2f}%")
print(f"🎯 Precision: {precision*100:.2f}%")
print(f"🎯 Recall:    {recall*100:.2f}%")
print(f"🎯 F1-Score:  {f1*100:.2f}%")

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\n📊 Confusion Matrix:")
print("                 Predicted")
print("                 Normal  Fraud")
print(f"Actual Normal     {cm[0,0]:5d}  {cm[0,1]:5d}")
print(f"Actual Fraud      {cm[1,0]:5d}  {cm[1,1]:5d}")

# Save model
os.makedirs('models', exist_ok=True)
joblib.dump(model, 'models/fraud_model.pkl')
print("\n💾 Model saved to 'models/fraud_model.pkl'")

# Create confusion matrix visualization
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='RdYlGn_r',
            xticklabels=['Normal', 'Fraud'],
            yticklabels=['Normal', 'Fraud'])
plt.xlabel('Predicted', fontsize=12)
plt.ylabel('Actual', fontsize=12)
plt.title('Credit Card Fraud Detection - Confusion Matrix', fontsize=14)
plt.tight_layout()
os.makedirs('static', exist_ok=True)
plt.savefig('static/confusion_matrix.png', dpi=100)
print("📊 Confusion matrix saved to 'static/confusion_matrix.png'")

# Feature importance
feature_names = ['Amount', 'Time_Risk', 'Location_Risk', 'Device_Risk', 'Pattern_Risk']
importance = model.feature_importances_

plt.figure(figsize=(10, 6))
plt.barh(feature_names, importance, color=['red', 'orange', 'yellow', 'blue', 'green'])
plt.xlabel('Importance Score')
plt.title('Top Factors for Fraud Detection')
plt.tight_layout()
plt.savefig('static/feature_importance.png', dpi=100)
print("📊 Feature importance saved to 'static/feature_importance.png'")

print("\n" + "="*60)
print("✅ TRAINING COMPLETE!")
print("="*60)

# Test prediction
print("\n🧪 Testing with sample transactions:")
sample_normal = np.array([[0.5, 0.2, 0.1, 0.1, 0.2]])
sample_fraud = np.array([[5.0, 1.5, 1.5, 1.5, 1.5]])

normal_pred = model.predict(sample_normal)[0]
fraud_pred = model.predict(sample_fraud)[0]
normal_prob = model.predict_proba(sample_normal)[0][1]
fraud_prob = model.predict_proba(sample_fraud)[0][1]

print(f"\n   Normal transaction → {'FRAUD' if normal_pred==1 else 'NORMAL'} (Risk: {normal_prob*100:.1f}%)")
print(f"   Fraud transaction → {'FRAUD' if fraud_pred==1 else 'NORMAL'} (Risk: {fraud_prob*100:.1f}%)")

if normal_pred == 0 and fraud_pred == 1:
    print("\n✅✅✅ MODEL WORKING PERFECTLY! ✅✅✅")
else:
    print("\n⚠️ Model needs adjustment")