from flask import Flask, render_template, request
import pandas as pd
import joblib
from pathlib import Path

app = Flask(__name__)
MODEL_DIR = Path(__file__).resolve().parent / "models"

MODEL_FILES = {
    "Decision Tree": "decision_tree.pkl",
    "Pruned Decision Tree": "pruned_decision_tree.pkl",
    "SVM": "svm.pkl"
}

MODEL_RESULTS = {
    "Decision Tree": {"accuracy": .76, "precision": .67, "recall": .72, "f1": .69},
    "Pruned Decision Tree": {"accuracy": .80, "precision": .72, "recall": .80, "f1": .75},
    "SVM": {"accuracy": .77, "precision": .70, "recall": .83, "f1": .73}
}

models = {}
for name, filename in MODEL_FILES.items():
    path = MODEL_DIR / filename
    if path.exists():
        try:
            models[name] = joblib.load(path)
        except Exception:
            pass

def make_input(form):
    return pd.DataFrame([{
        "Product": form["Product"],
        "Day": form["Day"],
        "Weekend": int(form["Weekend"]),
        "Prev_Sales": float(form["Prev_Sales"]),
        "7_Day_Avg": float(form["7_Day_Avg"]),
        "Price": float(form["Price"]),
        "Promo": int(form["Promo"]),
        "Temp_C": float(form["Temp_C"]),
        "Rain_mm": float(form["Rain_mm"]),
        "Holiday": int(form["Holiday"])
    }])

@app.route("/", methods=["GET", "POST"])
def index():
    selected = "Pruned Decision Tree"
    prediction = None
    error = None

    values = {
        "Product": "Muffin",
        "Day": "Tue",
        "Weekend": "0",
        "Prev_Sales": "55",
        "7_Day_Avg": "58",
        "Price": "45",
        "Promo": "0",
        "Temp_C": "27",
        "Rain_mm": "2",
        "Holiday": "0"
    }

    if request.method == "POST":

        # Get selected algorithm
        selected = request.form.get("algorithm", selected)

        # Update entered values if this is the prediction form
        if "Product" in request.form:

            for key in values:
                values[key] = request.form.get(key, values[key])

            try:
                if selected not in models:
                    raise RuntimeError(
                        f"{selected} model is not loaded. "
                        "Put its .pkl file in the models folder."
                    )

                prediction = models[selected].predict(
                    make_input(request.form)
                )[0]

            except Exception as exc:
                error = str(exc)

    return render_template(
        "index.html",
        algorithms=list(MODEL_FILES),
        selected_model=selected,
        metrics=MODEL_RESULTS[selected],
        prediction=prediction,
        error=error,
        values=values
    )

if __name__ == "__main__":
    import os
    app.run(
        host="0.0.0.0",
        port=int(os.environ.get("PORT", 5000)),
        debug=False
    )
