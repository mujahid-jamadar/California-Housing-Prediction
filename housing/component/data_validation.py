from housing.exception import HousingException
from housing.entity.config_entity import DataValidationConfig
from housing.logger import logging
import os,sys
from housing.entity.artifact_entity import DatIngestionArtifact
import pandas as pd
from housing.constant import *
from housing.util.util import *




class DataValidation:
    
    def __init__(self,data_validation_config:DataValidationConfig,
                 data_ingestion_artifact:DatIngestionArtifact):
        try:
            logging.info(f"{'>>'*30}Data Valdaition log started.{'<<'*30} \n\n")
            self.data_validation_config=data_validation_config
            self.data_ingestion_artifact=data_ingestion_artifact
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def is_train_test_file_exsists(self)->bool:
        try:
            logging.info(f"Checking id training and test file is available")
            is_train_file_exist=False
            is_test_file_exist=False
            
            train_file_path=self.data_ingestion_artifact.train_file_path
            test_file_path=self.data_ingestion_artifact.test_file_path

            is_train_file_exist=os.path.exists(train_file_path)
            is_test_file_exist=os.path.exists(test_file_path)

            is_available= is_test_file_exist and is_train_file_exist
            logging.info(f" Is test and train file exists? {is_available}")

            if not is_available:
                train_file_path=self.data_ingestion_artifact.train_file_path
                test_file_path=self.data_ingestion_artifact.test_file_path

                message=f" Training file: {train_file_path} or Testing file :{test_file_path} is not available"
                logging.info(message)
                raise Exception(message)

            return is_available
        except Exception as e:
            raise Exception(e,sys) from e
        
    def get_train_and_test_df(self):
        try:
            train_df = pd.read_csv(self.data_ingestion_artifact.train_file_path)
            test_df = pd.read_csv(self.data_ingestion_artifact.test_file_path)
            return train_df,test_df
        except Exception as e:
            raise HousingException(e,sys) from e
        
    def validate_dataset_schema(self,train_df,test_df)->bool:
        try:
            validate_status=False
            schema_file_path=os.path.join(ROOT_DIR,
                                          CONFIG_DIR,
                                          CONFIG_SCHEMA_FILE_NAME)
            predefined_schema=read_schema_yaml_file(schema_file_path)
            
            def validate_individual_dataset(data: pd.DataFrame) -> bool:
                # Check if dataset columns match predefined schema
                if set(data.columns) != set(predefined_schema["columns"].keys()):
                    return False

                # Check if data types match predefined schema
                for column, dtype in predefined_schema["columns"].items():
                    if data[column].dtype != dtype:
                        return False

                # Check if categorical columns have valid domain values
                for column in predefined_schema["categorical_columns"]:
                    if not set(data[column].unique()).issubset(predefined_schema["domain_values"][column]):
                        return False

                # Check if target column is present
                if predefined_schema["target_column"] not in data.columns:
                    return False

                return True

            # Validate both train and test datasets
            is_train_valid = validate_individual_dataset(train_df)
            is_test_valid = validate_individual_dataset(test_df)
            validate_status= is_train_valid and is_test_valid
            
            if not validate_status:
                raise Exception(f"Schema validate for test and train Fail")
            
            logging.info(f" Is Schema validate for test and train {validate_status}")
            return validate_status
        except Exception as e:
            raise HousingException(e,sys) from e    

    def initiate_data_validation(self):
        try:
            self.is_train_test_file_exists()
            train_df,test_df=self.get_train_and_test_df()
            validate_status=self.validate_dataset_schema(train_df,test_df)
            
            

        except Exception as e:
            raise HousingException(e,sys) from e    
        



    def __del__(self):
        logging.info(f"{'>>'*30}Data Valdaition log completed.{'<<'*30} \n\n")    