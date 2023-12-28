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


@dataclass(frozen=True)
class DataTransformationConfig:
    root_dir: Path
    data_file: Path


@dataclass(frozen=True)
class ModelTrainingConfig:
    root_dir: Path
    train_data_path: Path
    model_name: str
    n_estimators: int
    criterion: str
    max_depth: int
    min_samples_split: int
    min_samples_leaf: int
    target_column: str