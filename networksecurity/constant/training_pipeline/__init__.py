import os
import sys
import numpy as np
import pandas as pd

'''
common constants
'''
TARGET_COLUMN='Result'
PIPELINE_NAME: str="NetworkSecurity"
ARTIFACT_DIR: str="Artifacts"
FILE_NAME:str="phisingData.csv"

TRAIN_FILE_NAME:str='train.csv'
TEST_FILE_NAME:str='test.csv'


DATA_INGESTION_COLLECTION_NAME: str="NetworkData"
DATA_INGESTION_DATABASE_NAME: str="RAHUL"
DATA_INGESTION_DIR_NAME: str="data_ingestion"
DATA_INGESTION_FEATURE_STORE_DIR:str="feature_score"
DATA_INGESTION_INGESTED_DIR:str="ingested"
DATA_INGESTION_TRAIN_TEST_SPLIT_RATIO:float=0.2