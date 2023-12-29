import os
import pandas as pd
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from urllib.parse import urlparse
import mlflow
import mlflow.sklearn
import numpy as np
import joblib

from stroke_risk.entity.config_entity import ModelEvaluationConfig
from stroke_risk.utils.common import save_json
from pathlib import Path
from stroke_risk import logger


try:
    from stroke_risk.config.set_env_variables import my_mlflow_uri

    os.environ["MLFLOW_TRACKING_URI"] = my_mlflow_uri.my_uri()['url']
    os.environ["MLFLOW_TRACKING_USERNAME"] = my_mlflow_uri.my_uri()['user']
    os.environ["MLFLOW_TRACKING_PASSWORD"] = my_mlflow_uri.my_uri()['passwd']
except:
    logger.info('ENV Variables Not Found for MLFlow tracking')

class ModelEvaluation:
    def __init__(self, config: ModelEvaluationConfig):
        self.config = config

    
    def eval_metrics(self,actual, pred):
        rmse = np.sqrt(mean_squared_error(actual, pred))
        mae = mean_absolute_error(actual, pred)
        r2 = r2_score(actual, pred)
        return rmse, mae, r2
    


    def log_into_mlflow(self):

        test_data = pd.read_csv(self.config.test_data_path)
        model = joblib.load(self.config.model_path)

        x_test = test_data.drop([self.config.target_column], axis=1)
        y_test = test_data[[self.config.target_column]]


        mlflow.set_registry_uri(self.config.mlflow_uri)
        tracking_url_type_store = urlparse(mlflow.get_tracking_uri()).scheme


        with mlflow.start_run():

            y_pred = model.predict(x_test)

            (rmse, mae, r2) = self.eval_metrics(y_test, y_pred)
            
            # Saving metrics local
            scores = {"rmse": rmse, "mae": mae, "r2": r2}
            save_json(path=Path(self.config.metric_file_name), data=scores)

            mlflow.log_params(self.config.all_params)

            mlflow.log_metric("rmse", rmse)
            mlflow.log_metric("r2", r2)
            mlflow.log_metric("mae", mae)


            if tracking_url_type_store != "file":
                mlflow.sklearn.log_model(model, "model", registered_model_name="RandomForest")
            else:
                mlflow.sklearn.log_model(model, "model")