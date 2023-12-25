from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)
class DataIngestionConfig:
    root_dir: Path
    source_URL: str
    local_data_file: Path
    unzip_dir: Path


@dataclass(frozen=True)
class DataPreprocessConfig:
    root_dir: Path
    data_dir: Path
    dataset_name: Path
    save_data_file: Path


@dataclass(frozen=True)
class DataValidationConfig:
    root_dir: Path
    data_dir: Path
    status_file: str
    all_schema: dict