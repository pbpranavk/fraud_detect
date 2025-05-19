💳 Fraud Detection Pipeline (Vertex AI + KFP)

This project builds a full machine learning system to detect fraudulent credit card transactions using anonymized financial data. It uses TensorFlow/Keras for modeling, Kubeflow Pipelines (KFP) for orchestration, and Vertex AI for scalable training, deployment, and monitoring.

📦 Features
- Preprocess credit card fraud dataset from GCS
- Scale features and handle class imbalance
- Train a neural network using TensorFlow/Keras
- Deploy the model to a Vertex AI endpoint
- Make real-time predictions via local script

🧠 Tech Stack
- Google Cloud Platform
- Vertex AI Pipelines (KFP v2)
- Vertex AI Models & Endpoints
- Cloud Storage
- Python 3.12
- TensorFlow / Keras
- pandas, scikit-learn, joblib

🔧 Setup Instructions

1. Install dependencies  
```bash
pip install -r requirements.txt
```

2. Create a `.env` file in the root directory:
```
PROJECT_ID=
ENDPOINT_ID=
LOCATION=
```
> ⚠️ Do not commit this file to version control.

💡 Pipeline Overview
- Upload the `creditcard.csv` dataset to a GCS bucket
- Run the Vertex AI pipeline via `scripts/compile_and_run.py`
  - Preprocesses data (scaling, label split)
  - Trains a Keras neural network model
  - Saves model in SavedModel format
- Deploy the model using `scripts/deploy.py`

🚀 Predict Locally
Once deployed, make predictions using:
```bash
python scripts/predict.py
```

📂 Project Structure
fraud_detection_pipeline/
├── components/  
│   ├── preprocess/component.py  
│   └── train/component.py  
├── scripts/  
│   ├── compile_and_run.py  
│   ├── deploy.py  
│   └── predict.py  
├── pipeline.py  
├── requirements.txt  
└── README.md  

⚠️ Notes
- Model expects 29 pre-scaled features (including Time, Amount, V1–V28)
- Ensure input vectors for prediction match training distribution

👤 Author  
Built by Pranav to showcase real-world ML deployment using GCP, TensorFlow, and Kubeflow Pipelines.
