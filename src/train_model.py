from sklearn.feature_extraction.text import CountVectorizer, TfidfTransformer
from sklearn.naive_bayes import MultinomialNB
import csv
import pickle
from datetime import datetime

data = {
  "data": [],
  "target": []
}
reader = csv.DictReader(open("./data/training.csv"), delimiter=";")
for row in reader:
  data["data"].append(row["text"])
  data["target"].append(1 if row["country_code"] == "US" else 0)

count_vect = CountVectorizer(lowercase=False)
X_train_counts = count_vect.fit_transform(data["data"])
tfidf_transformer = TfidfTransformer()
X_train_tfidf = tfidf_transformer.fit_transform(X_train_counts)

clf = MultinomialNB().fit(X_train_tfidf, data["target"])

test_reader = csv.DictReader(open("./data/test.csv"), delimiter=";")
test_data = {
  "data": [],
  "target": []
}

for row in test_reader:
  test_data["data"].append(row["text"])
  test_data["target"].append(1 if row["country_code"] == "US" else 0)

X_new_counts = count_vect.transform(test_data["data"])
X_new_tfidf = tfidf_transformer.transform(X_new_counts)

predicted = clf.predict(X_new_tfidf)

correct_predictions = 0
for i in range(len(predicted)):
  if predicted[i] == test_data["target"][i]:
    correct_predictions += 1

print(f"Correct predictions (Naive Bayes): {correct_predictions} ({correct_predictions / len(predicted)})")

version = 0
try:
  file = open("./model/trained_model.pickle", "rb")
  last_model = pickle.load(file)
  version = last_model.version + 1
except:
  pass

persist = {
  "count_vect": count_vect,
  "tfidf_transformer": tfidf_transformer,
  "classifier": clf,
  "accuracy": correct_predictions / len(predicted),
  "version": version,
  "model_date": datetime.now().isoformat()
}

file = open("./model/trained_model.pickle", "wb")
pickle.dump(persist, file)
file.close()

print("Trained model saved at \"models/trained_model.pickle\"")
