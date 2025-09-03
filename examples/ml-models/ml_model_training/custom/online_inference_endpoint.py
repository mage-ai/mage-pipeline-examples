@custom
def score(training_output, *args, **kwargs) -> float:
    """
    kwargs:
        Features: Age, Fare, Parch, Pclass, SibSp
    """
    model, imputer, score = training_output

    features = imputer.get_feature_names_out()
    
    feature_vector = [kwargs.get(feature, None) for feature in features]
    
    if all([v is None for v in feature_vector]):
        print('No features in the payload, skipping')
        return

    vectors = imputer.transform([feature_vector])

    scores = model.predict(vectors)

    return scores