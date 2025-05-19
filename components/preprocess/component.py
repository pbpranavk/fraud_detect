import pandas as pd
from sklearn.preprocessing import StandardScaler
import joblib
import os

def preprocess_data(gcs_path, output_dir):
    df = pd.read_csv(gcs_path)
    X = df.drop("Class", axis=1)
    y = df["Class"]

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)

    os.makedirs(output_dir, exist_ok=True)
    pd.DataFrame(X_scaled).to_csv(os.path.join(output_dir, "X.csv"), index=False)
    pd.DataFrame(y).to_csv(os.path.join(output_dir, "y.csv"), index=False)
    joblib.dump(scaler, os.path.join(output_dir, "scaler.pkl"))
