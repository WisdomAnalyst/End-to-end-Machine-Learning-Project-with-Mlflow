from dataclasses import dataclass
from pathlib import Path


CONFIG_FILE_PATH = Path("config\config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
SCHEMA_FILE_PATH = Path("schema.yaml")

@dataclass
class DataIngestionConfig:
    root_dir: Path
    STATUS_FILE: str
    unzip_data_dir: Path
    all_schema: dict