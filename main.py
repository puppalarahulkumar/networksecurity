from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.logging.logger import logging
from networksecurity.entity.config_entity import DataIngestionConfig,DataValidationConfig
from networksecurity.entity.config_entity import TrainingPipelineConfig,DataTransformationConfig
from networksecurity.components.data_validation import DataValidation
import sys

if __name__=="__main__":
    try:
        logging.info("enter the try block")
        training_pipeline_config=TrainingPipelineConfig()
        data_ingestion_config=DataIngestionConfig(training_pipeline_config)
        data_ingestion=DataIngestion(data_ingestion_config)
        
        logging.info("initiated the data ingestion")
        dataingestionartifact=data_ingestion.initiate_data_ingestion()
        logging.info("Data initiation completed!")
        print(dataingestionartifact)
        data_validation_config=DataValidationConfig(training_pipeline_config)
        data_validation=DataValidation(dataingestionartifact,data_validation_config)
        
        data_validation_artifact=data_validation.initiate_data_validation()
        logging.info("initiated the data validation")
        print(data_validation_artifact)
        logging.info("data Transformation started")
        data_transformation_config=DataTransformationConfig(training_pipeline_config)
        data_transformation=DataTransformation(data_validation_artifact, data_transformation_config)
        data_transformation_artifact=data_transformation.initiate_data_transformation()
        print(data_transformation_artifact)
        logging.info("data transformation is done")


    
    except Exception as e:
        raise NetworkSecurityException(e,sys)
    