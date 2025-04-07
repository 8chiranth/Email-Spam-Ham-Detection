import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

# Load dataset
data = pd.read_csv("SMS_Data_Training_Set_Sobered.unknown", sep="\t", names=["class", "messages"])

# Train model
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(data["messages"])
y = data["class"]

model = MultinomialNB()
model.fit(X, y)

# Prediction function
def predict_message(message: str) -> str:
    msg_vect = vectorizer.transform([message])
    prediction = model.predict(msg_vect)
    return prediction[0]

# Run a sample test if executed directly
if __name__ == "__main__":
    test_email = "Congratulations! You have won a free lottery. Click here now."
    result = predict_message(test_email)
    print("Prediction:", result)
