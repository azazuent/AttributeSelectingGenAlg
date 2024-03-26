from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB, GaussianNB
from sklearn.metrics import f1_score
from sklearn.pipeline import make_pipeline


def bayesian(data, target, test_size=0.33) -> float:
    data_train, data_test, target_train, target_test = train_test_split(
        data, target, test_size=test_size, random_state=125
    )

    #model = make_pipeline(TfidfVectorizer(), MultinomialNB())
    model = GaussianNB()
    model.fit(data_train, target_train)

    prediction = model.predict(data_test)
    f1 = f1_score(prediction, target_test, average="weighted")

    return f1


model_types = {
    "bayesian": bayesian
}
