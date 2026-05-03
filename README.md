<<<<<<< HEAD
# ❤️ Heart Disease Prediction App

A machine learning web app that predicts whether a person is at risk of heart disease based on their medical data. You can either check one patient at a time or upload a whole file with many patients and get results for all of them at once.

## 🌐 Live Demo

*Heart_Disease_Prediction* is deployed and running live!

👉 *[Open Live Application](https://heartdiseaseprediction-g5dlgamtmpwfe2mxob2zam.streamlit.app/)*

## What This Project Does

This app takes in basic medical details like age, cholesterol level, blood pressure, and a few other readings — and tells you whether the person is likely to have heart disease or not. It also shows a risk percentage so you know how confident the prediction is.

There are two ways to use it:
- **Single Patient** — fill in the details on the sidebar and click predict
- **Bulk Prediction** — upload a CSV or Excel file with many patients and download the results

---

## Files in This Project

```
heart_disease_prediction/
│
├── HeartDiseasePrediction.ipynb     # The notebook where the model was built and trained
├── heart_cleveland_upload.csv       # The dataset used for training (297 patient records)
├── heart_disease_model.pkl          # The trained model (saved after training)
├── scaler.pkl                       # The scaler used to normalize the input data
└── app.py                           # The main Streamlit web app
```

---

## How I Built This

### Step 1 — Got the Data
I used the Cleveland Heart Disease dataset which has **297 patient records** and **13 medical features** plus a target column called `condition` (0 = no disease, 1 = disease).

The 13 features are:

| Feature | What It Means |
|---|---|
| `age` | Age of the patient |
| `sex` | 1 = Male, 0 = Female |
| `cp` | Chest pain type (0–3) |
| `trestbps` | Resting blood pressure |
| `chol` | Cholesterol level |
| `fbs` | Fasting blood sugar > 120 mg/dl (1 = yes, 0 = no) |
| `restecg` | Resting ECG result (0, 1, or 2) |
| `thalach` | Maximum heart rate achieved |
| `exang` | Exercise-induced chest pain (1 = yes, 0 = no) |
| `oldpeak` | ST depression from exercise |
| `slope` | Slope of the ST segment (0, 1, or 2) |
| `ca` | Number of major vessels seen (0–4) |
| `thal` | Thalassemia type (1, 2, or 3) |

### Step 2 — Cleaned the Data
- Removed duplicate rows
- Checked for missing values
- Did some basic analysis — looked at how features relate to each other using a heatmap, checked age vs condition, chest pain type, etc.

### Step 3 — Trained Multiple Models
I tested four different models to see which one works best:

- Logistic Regression
- Random Forest
- K-Nearest Neighbors (KNN)
- XGBoost

I used **StandardScaler** to scale the data before feeding it into Logistic Regression and KNN (tree-based models like Random Forest and XGBoost don't need scaling).

### Step 4 — Picked the Best Model
After comparing all four, I used **GridSearchCV** to fine-tune the Random Forest model by trying different settings automatically. The best version of Random Forest was saved as the final model.

### Step 5 — Saved the Model
Both the trained model and the scaler were saved as `.pkl` files using `joblib` so the app can load them without retraining every time.

### Step 6 — Built the Web App
Used **Streamlit** to build the interface. The app loads the saved model and scaler, takes input from the user, scales it the same way the training data was scaled, and returns a prediction.

---

## How to Run This App on Your Computer

### Requirements
Make sure you have Python installed. Then install the required packages:

```bash
pip install streamlit pandas scikit-learn joblib xgboost openpyxl
```

### Running the App

1. Put all these files in the same folder:
   - `app.py`
   - `heart_disease_model.pkl`
   - `scaler.pkl`

2. Open your terminal, go to that folder, and run:

```bash
streamlit run app.py
```

3. Your browser will open the app automatically. If it doesn't, go to `http://localhost:8501`

---

## How to Use the App

### Single Patient Mode
1. The sidebar on the left has sliders and dropdowns for each medical field
2. You can use the **🔴 High Risk** or **🟢 Low Risk** buttons to auto-fill demo data and see how the app responds
3. Adjust the values to match the patient's details
4. Click **Predict Single Patient**
5. The result will show as either a red warning (High Risk) or green message (Low Risk) along with a percentage

### Bulk Prediction Mode
1. Select "Bulk Prediction" from the radio button at the top
2. Upload a CSV or Excel file — it must have all 13 columns listed in the table above
3. Click **Predict on Uploaded Data**
4. The results will appear in a table with two new columns: `Prediction` and `Risk_Probability`
5. You can download the results as CSV, Excel, or HTML

---

## Training the Model Yourself

If you want to retrain the model from scratch:

1. Open `HeartDiseasePrediction.ipynb` in Jupyter Notebook or VS Code
2. Run all the cells top to bottom
3. The last cell will save a new `heart_disease_model.pkl` and `scaler.pkl`
4. Use those new files with `app.py`

---

## Example Input (for testing)

**High Risk Patient:**
- Age: 65, Male, Chest Pain Type: 3, BP: 160, Cholesterol: 280
- Fasting Blood Sugar: Yes, ECG: 2, Max Heart Rate: 115
- Exercise Angina: Yes, Oldpeak: 2.5, Slope: 1, Vessels: 2, Thal: 3

**Low Risk Patient:**
- Age: 45, Female, Chest Pain Type: 0, BP: 115, Cholesterol: 180
- Fasting Blood Sugar: No, ECG: 0, Max Heart Rate: 170
- Exercise Angina: No, Oldpeak: 0.0, Slope: 2, Vessels: 0, Thal: 2

---

## Tech Stack

- **Python** — main programming language
- **Pandas & NumPy** — data handling and numbers
- **Scikit-learn** — model training, scaling, evaluation
- **XGBoost** — one of the models tested
- **Matplotlib & Seaborn** — charts and graphs in the notebook
- **Joblib** — saving and loading the model
- **Streamlit** — building the web interface

---

## Note

This app is built for learning and demo purposes. It should not be used as a replacement for actual medical advice or diagnosis. Always consult a doctor for health-related decisions.
=======
# Heart_Disease_Prediction
Heart Disease Prediction App using Machine Learning
>>>>>>> b2efd583b337d55d90ab72b6214e6d2c2b183b10
