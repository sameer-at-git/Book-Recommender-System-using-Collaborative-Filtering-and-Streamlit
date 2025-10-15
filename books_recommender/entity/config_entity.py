from collections import namedtuple

DataIngestionConfig = namedtuple("DataIngestionConfig",["dataset_download_url",
                                                        "raw_data_dir",
                                                        "ingested_data_dir"
                                                        ])

DataValidationConfig = namedtuple("DataValidationConfig",["clean_data_dir",
                                                          "books_csv_file",
                                                            "ratings_csv_file",
                                                            "serialized_objects_dir"
                                                            ])