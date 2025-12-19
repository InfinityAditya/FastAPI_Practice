import pickle
import pandas as pd

# --- Fix for scikit-learn pickle compatibility ---
import sklearn.compose._column_transformer as ct


class _RemainderColsList(list):
    pass


ct._RemainderColsList = _RemainderColsList


# --- Load trained model ---
with open("C:\Users\Aditya\OneDrive\Desktop\insurance_premium_prediction\model\model.pkl", "rb") as f:
    model = pickle.load(f)

# MLFLOW
MODEL_VERSION = '1.0.0'

# Get class labels from model (important for matching probabilities to class names)
class_labels = model.classes_.tolist()


def predict_output(user_input: dict):
    df = pd.DataFrame([user_input])

    # predict the class
    predicted_class = model.predict(df)[0]

    # Get probabilities for all classes
    probabilities = model.predict_proba(df)[0]
    confidence = max(probabilities)

    # Create mapping: {class name:probability}
    class_probs = dict(zip(class_labels, map(
        lambda p: round(p, 4), probabilities)))

    return {
        "predicted_category": predicted_class,
        "confidence": round(confidence, 4),
        "class_probabilities": class_probs
    }

    
