## Titanic Survival Prediction Pipeline

This pipeline performs the following steps:

### Data Loading
   - Fetches the Titanic dataset from a GitHub repository
   - Performs basic validation checks on rows (≥891) and columns (≥12)

### Data Transformation
   - Selects specific numeric features: Age, Fare, Parch, Pclass, SibSp, and Survived
   - Handles missing values using median imputation via `SimpleImputer`
   - Returns both the transformed DataFrame and the fitted imputer

### Model Training and Evaluation
   - Splits data into training and test sets
   - Trains a Logistic Regression model on the preprocessed data
   - Evaluates model performance using accuracy score
   - Enforces a minimum accuracy threshold of 0.5
   - Returns the trained model, imputer, and accuracy score

The pipeline is designed to predict passenger survival on the Titanic using machine learning, with built-in data validation and quality checks at each stage.