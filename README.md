# Fraud Detection Pipeline

A complete ML pipeline for fraud detection using TensorFlow/Keras, Kubeflow Pipelines, and Vertex AI.

## Structure
- `components/preprocess`: Preprocessing logic
- `components/train`: Training logic
- `pipeline.py`: Main pipeline definition

## Run
1. Upload your dataset to GCS
2. Update `pipeline.py` with your GCS path
3. Compile and run using Vertex AI Pipelines
