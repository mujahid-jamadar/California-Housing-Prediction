from collections import namedtuple



# output structure of each artifact


DatIngestionArtifact=namedtuple("DataIngestionArtifact",
                                ["train_file_path","test_file_path","is_ingested","message"])