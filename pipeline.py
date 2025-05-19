from kfp.v2 import dsl
from kfp.v2.dsl import Dataset, Model, Input, Output
from kfp.v2.compiler import Compiler

@dsl.component
def preprocess_component(gcs_path: str, output_data: Output[Dataset]):
    from components.preprocess.component import preprocess_data
    preprocess_data(gcs_path, output_data.path)

@dsl.component
def train_component(input_data: Input[Dataset], output_model: Output[Model]):
    from components.train.component import train_model
    train_model(input_data.path, output_model.path)

@dsl.pipeline(name="fraud-detection-pipeline", pipeline_root="gs://your-bucket-root")
def fraud_pipeline(gcs_path: str):
    preprocess_task = preprocess_component(gcs_path=gcs_path)
    train_task = train_component(input_data=preprocess_task.outputs["output_data"])

if __name__ == "__main__":
    Compiler().compile(pipeline_func=fraud_pipeline, package_path="fraud_pipeline.json")
