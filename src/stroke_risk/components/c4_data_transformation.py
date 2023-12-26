import os
from stroke_risk import logger
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pandas as pd

from stroke_risk.entity.config_entity import DataTransformationConfig


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def encoding(self):
        data= pd.read_csv(self.config.data_file)

        label_encoder = LabelEncoder()
        data['gender'] = label_encoder.fit_transform(data['gender']) # male=1, female=0
        data['ever_married'] = label_encoder.fit_transform(data['ever_married']) # yes=1, no=0
        data['Residence_type'] = label_encoder.fit_transform(data['Residence_type']) # urban=1, rural=0

        data = pd.get_dummies(data, columns=['work_type', 'smoking_status'])
        data.to_csv(os.path.join(self.config.root_dir, "data.csv"),index = False)
        
        logger.info('LabelEncoder & OnehotEncoder applied to Categorical Columns')
        logger.info(f'Encoded data saved in {self.config.root_dir}/data.csv')


    def train_test_spliting(self):
        data = pd.read_csv(os.path.join(self.config.root_dir, "data.csv"))

        train, test = train_test_split(data, test_size=0.2)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(f'train data shape - {train.shape}')
        logger.info(f'test data shape - {test.shape}')