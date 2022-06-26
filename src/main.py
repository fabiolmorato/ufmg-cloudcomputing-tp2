from fastapi import FastAPI, Response, status
from pydantic import BaseModel
import pickle

app = FastAPI()
trained_model = None

class Payload(BaseModel):
  text: str

@app.get("/api/health")
def health():
  return { "message": "OK" }

@app.post("/api/american")
def is_american_tweet(response: Response, payload: Payload):
  if trained_model == None:
    response.status_code = status.HTTP_503_SERVICE_UNAVAILABLE
    return { "message": "model not loaded yet" }
  
  X_new_count = trained_model["count_vect"].transform([payload.text])
  X_tfidf = trained_model["tfidf_transformer"].transform(X_new_count)
  predicted = trained_model["classifier"].predict(X_tfidf)

  return {
    "is_american": predicted.tolist()[0],
    "version": trained_model["version"],
    "model_date": trained_model["model_date"]
  }

def load_model():
  global trained_model
  try:
    file = open("./model/trained_model.pickle", "rb")
    trained_model = pickle.load(file)
    file.close()
  except:
    print("Could not load trained model!")

load_model()
