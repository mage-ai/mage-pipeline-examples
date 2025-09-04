import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from sklearn.model_selection import train_test_split

LABEL_COLUMN = 'Survived'


@data_exporter
def train_model(data, **kwargs) -> None:
    df: pd.DataFrame = data[0]
    imputer: SimpleImputer = data[1]

    X_train, X_test, y_train, y_test = build_training_and_test_set(df)
    
    features = list(X_train.columns)
    print(f'Features: {", ".join(features)}')

    model = LogisticRegression()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)
    score = accuracy_score(y_pred, y_test)
    print(f'Accuracy: {score}')


    return [
        model,
        imputer,
        score,
    ]


def build_training_and_test_set(df: pd.DataFrame) -> None:
    X = df.drop(columns=[LABEL_COLUMN])
    y = df[LABEL_COLUMN]

    return train_test_split(X, y)


@test
def test_score(*args, **kwargs):
    score = args[2]
    minimum_score = 0.5
    assert score > minimum_score, f'The accuracy score of {score} is too low, must be at least {minimum_score}'