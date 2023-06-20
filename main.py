import sys
sys.path.append('./src')
#import my_module

from cnnClassifier import logger
from cnnClassifier.pipeline.stg_01_data_ingestion import DataIngestionTrainingPipeline
from cnnClassifier.pipeline.stg_02_prepare_base_model import PrepareBaseModelTrainingPipeline
from cnnClassifier.pipeline.stg_03_training import ModelTrainingPipeline

logger.info("Welcome to the custome log")



STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>>> stage {STAGE_NAME} completed <<<<<<<<<<\n\n X=============X")
except Exception as e:
    logger.exception(e)
    raise e 


STAGE_NAME = "Prepare Base Model"
try:
    logger.info(f"##############################")
    logger.info(f">>>>>> Stage {STAGE_NAME} Started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> Stage {STAGE_NAME} Completed <<<<<<\n\nX=================X")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Training"
try:
    logger.info(f"************************************")
    logger.info(f">>>>>>> Stage {STAGE_NAME} Started <<<<<<<<")
    model_trainer = ModelTrainingPipeline()
    model_trainer.main()
    logger.info(f">>>>>>>>>>>> Stage {STAGE_NAME} Completed <<<<<<< \n\nX================X")
except Exception as e:
    logger.exception(e)
    raise e