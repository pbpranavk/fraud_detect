from google.cloud import aiplatform

aiplatform.init(project="your-gcp-project", location="us-central1")

endpoint = aiplatform.Endpoint(endpoint_name="projects/PROJECT_ID/locations/us-central1/endpoints/ENDPOINT_ID")

instances = [[0.1] * 29]  # Replace with actual scaled features

prediction = endpoint.predict(instances=instances)
print("Prediction:", prediction)
