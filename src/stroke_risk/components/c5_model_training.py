import pandas as pd
import os
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib
from stroke_risk import logger

from stroke_risk.entity.config_entity import ModelTrainingConfig


class ModelTraining:
    def __init__(self, config: ModelTrainingConfig):
        self.config = config

    
    def training(self):
        train_data = pd.read_csv(self.config.train_data_path)

        x_train = train_data.drop([self.config.target_column], axis=1)
        y_train = train_data[self.config.target_column]

        scaler = StandardScaler()
        x_train = scaler.fit_transform(x_train)

        model = RandomForestClassifier(
            n_estimators = self.config.n_estimators,
            criterion = self.config.criterion,
            max_depth=self.config.max_depth,
            min_samples_split = self.config.min_samples_split,
            min_samples_leaf = self.config.min_samples_leaf,
            max_features='sqrt',
            bootstrap=True,
            random_state=42
            )
        
        model.fit(x_train, y_train)

        joblib.dump(model, os.path.join(self.config.root_dir, self.config.model_name))
        logger.info('Model Trained')