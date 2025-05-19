from google.cloud import aiplatform

aiplatform.init(project="your-gcp-project", location="us-central1")

model = aiplatform.Model.upload(
    display_name="fraud-detection-model",
    artifact_uri="gs://your-bucket-root/model",
    serving_container_image_uri="us-docker.pkg.dev/vertex-ai/prediction/tf2-cpu.2-12:latest"
)

endpoint = aiplatform.Endpoint.create(display_name="fraud-detection-endpoint")
model.deploy(endpoint=endpoint, machine_type="n1-standard-2")
