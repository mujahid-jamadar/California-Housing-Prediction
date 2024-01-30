from collections import namedtuple


# This tuple encapsulates configuration parameters related to data ingestion
DataIngestionConfig = namedtuple("DataIngestionConfig",
                                 ["dataset_download_url",  # URL for downloading the dataset
                                  "tgz_download_dir",      # Directory for storing downloaded dataset files (.tgz)
                                  "raw_data_dir",          # Directory for storing raw data after extraction
                                  "ingested_train_dir",    # Directory for preprocessed training data
                                  "ingested_test_dir"])    # Directory for preprocessed test data



# This tuple encapsulates configuration parameters related to data validation
DataValidationConfig = namedtuple("DataValidationConfig",
                                   ["schema_file_path"])  # File path of the schema used for data validation


# This tuple encapsulates configuration parameters related to data transformation and preprocessing
DataTransformationConfig = namedtuple("DataTransformationConfig",
                                      ["add_bedroom_per_room",        # add column in dataset
                                       "transformed_train_dir",      # Directory storing transformed training data
                                       "transformed_test_dir",       # Directory storing transformed test data
                                       "preprocessed_object_file_path"])  # File path of the preprocessed object





# This tuple encapsulates configuration parameters related to model training
ModelTrainerConfig = namedtuple("ModelTrainerConfig",
                                 ["trained_model_file_path",  # File path where the trained model will be saved
                                  "base_accuracy"])           # Base accuracy used as a reference for model evaluation



# This tuple encapsulates configuration parameters related to model evaluation
ModelEvaluationConfig = namedtuple("ModelEvaluationConfig",
                                    ["model_evaluation_file_path",  # File path where model evaluation results will be saved
                                     "time_stamp"])                  # Time stamp indicating when the evaluation occurred



# This tuple encapsulates configuration parameters related to model pushing/exporting
ModelPusherConfig = namedtuple("ModelPusherConfig",
                                ["export_dir_path"])  # Directory path where the model will be exported/pushed



# This tuple encapsulates configuration parameters related to the training pipeline
TrainingPipelineConfig = namedtuple("TrainingPipelineConfig",
                                     ["artifact_dir"])  # Directory path to store pipeline artifacts
