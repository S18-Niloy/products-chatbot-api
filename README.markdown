# Customer Retention Prediction

## Project Overview
This project aims to predict customer churn using machine learning and deep learning techniques. It involves exploratory data analysis (EDA), feature engineering, and training multiple predictive models: Random Forest, XGBoost, LightGBM, and an Artificial Neural Network (ANN). The goal is to identify the best-performing model based on metrics such as Accuracy, Precision, Recall, F1-Score, and AUC (Area Under the ROC Curve).

## Dataset Description
The dataset (`dataset.csv`) contains 1,000 customer records with 15 features:
- **Columns**:
  - `Customer_ID`: Unique identifier for each customer.
  - `Age`: Customer's age.
  - `Gender`: Customer's gender (e.g., Male, Other).
  - `Annual_Income`: Customer's annual income.
  - `Total_Spend`: Total amount spent by the customer.
  - `Years_as_Customer`: Duration of customer relationship.
  - `Num_of_Purchases`: Number of purchases made.
  - `Average_Transaction_Amount`: Average transaction value.
  - `Num_of_Returns`: Number of returns made.
  - `Num_of_Support_Contacts`: Number of times customer contacted support.
  - `Satisfaction_Score`: Customer satisfaction score.
  - `Last_Purchase_Days_Ago`: Days since last purchase.
  - `Email_Opt_In`: Whether customer opted into email marketing (True/False).
  - `Promotion_Response`: Customer's response to promotions (e.g., Responded, Ignored, Unsubscribed).
  - `Target_Churn`: Target variable (True/False) indicating if the customer churned.
- **Shape**: (1000, 15).
- **Missing Values**: None observed.
- **Duplicates**: None observed.
- **Target Distribution**: Visualized using a countplot to show the balance of churned vs. non-churned customers.
- **Correlations**: Explored via a heatmap for numeric features.

## Setup Instructions
To run the project, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone <repository_url>
   cd <repository_directory>
   ```

2. **Install Dependencies**:
   Ensure Python 3 is installed. Install required libraries using pip:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn imbalanced-learn xgboost lightgbm tensorflow
   ```

3. **Prepare the Dataset**:
   Place the `dataset.csv` file in the project directory or update the file path in the script (`data = pd.read_csv("/content/dataset.csv")`) to point to the correct location.

4. **Run the Script**:
   Execute the Python script:
   ```bash
   python customer_retention_prediction.py
   ```
   Alternatively, run it in a Jupyter Notebook environment (e.g., Google Colab, JupyterLab) by converting the `.py` file to `.ipynb` or running it cell-by-cell.

5. **Environment**:
   - Recommended: Use a virtual environment (e.g., `venv` or `conda`) to manage dependencies.
   - The script was originally run in Google Colab, but it is compatible with local Python environments.

## Key Results
- **Data Preprocessing**:
  - Categorical features (e.g., `Gender`, `Promotion_Response`) were encoded using `LabelEncoder`.
  - Numeric features were capped for outliers (1st and 99th percentiles).
  - New features were engineered: ratios, sums, differences, and binary flags based on numeric columns.
  - Highly correlated features (>0.9) were dropped to reduce multicollinearity.
  - Top 20 features were selected based on combined Mutual Information and Random Forest importance scores.
  - Data was scaled using `StandardScaler` and split into train (70%), validation (15%), and test (15%) sets.
  - Class imbalance was addressed using SMOTE for oversampling the training set.

- **Models Trained**:
  - Random Forest (`n_estimators=200`)
  - XGBoost (`eval_metric='logloss'`)
  - LightGBM
  - ANN (128 neurons → Dropout → 64 neurons → Dropout → 1 neuron with sigmoid activation)

- **Model Performance Comparison**:
  The table below summarizes the performance of each model on the test set, based on Accuracy, Precision, Recall, F1-Score, and AUC:

| Model          | Accuracy | Precision | Recall  | F1-Score | AUC     |
|----------------|----------|-----------|---------|----------|---------|
| Random Forest  | 0.467    | 0.494     | 0.519   | 0.506    | 0.464   |
| XGBoost        | 0.440    | 0.470     | 0.494   | 0.481    | 0.437   |
| LightGBM       | 0.453    | 0.481     | 0.481   | 0.481    | 0.452   |
| ANN            | 0.493    | 0.521     | 0.468   | 0.493    | 0.495   |

- **Best Model**:
  - **ANN** achieved the highest AUC of **0.495**.
  - **Observation**: The AUC scores for all models are close to 0.5, indicating near-random performance. This suggests potential issues such as insufficient data, suboptimal feature engineering, or inadequate model tuning. The ANN slightly outperforms others, but its low AUC indicates limited predictive power. Further improvements could include hyperparameter optimization, additional feature engineering, collecting more data, or exploring alternative models.

- **Visualizations**:
  - Confusion matrices and ROC curves were generated for each model to visualize classification performance.
  - A bar plot compared model performance across Accuracy, F1-Score, and AUC.