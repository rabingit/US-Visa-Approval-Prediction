'''from us_visa.logger import logging
from us_visa.exception import USvisaException
import sys

try:
    a = 1 / "10"
except Exception as e:
    logging.info(e)
    raise USvisaException(e, sys)
    '''

#from us_visa.constants import DATABASE_NAME
#print(DATABASE_NAME)

from us_visa.pipeline.training_pipeline import TrainPipeline

pipline = TrainPipeline()
pipline.run_pipeline()