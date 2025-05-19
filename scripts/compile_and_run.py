from kfp.v2 import compiler
from pipeline import fraud_pipeline

compiler.Compiler().compile(
    pipeline_func=fraud_pipeline,
    package_path='fraud_pipeline.json'
)
