import pandas as pd
import numpy as np
from stroke_risk import logger

from stroke_risk.entity.config_entity import DataPreprocessConfig
from pathlib import Path
import os



class DataPreprocess:
    def __init__(self, config: DataPreprocessConfig):
        self.config = config


    def preprocess(self):

        data_dir=self.config.data_dir
        dataset_name=self.config.dataset_name
        save_data_file=self.config.save_data_file

        data = pd.read_csv(Path(data_dir,dataset_name))

        data.age = data.age.astype(np.int64)
        data = data[data['gender'] != 'Other']
        cata_col = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
        data[cata_col] = data[cata_col].astype('category')
        logger.info('Datatype Fixed')

        data['smoking_status'] = data['smoking_status'].replace('Unknown', 'formerly smoked')
        data['work_type'] = data['work_type'].replace('children', 'Never_worked')
        logger.info('Data Substituted')

        data['age_bin'] = pd.cut(data['age'], bins=[0, 35, 50, 65, 75, np.inf], labels=['0-35', '36-50', '51-65', '65-75', '75+'])
        data = data[~data.age_bin.isnull()]

        data.loc[:,'gender_age']=data.gender.astype(str) + '_' + data.age_bin.astype(str)

        logger.info('age-bin and gender-age created')

        mean_bmi = data.groupby('gender_age')['bmi'].transform('mean')
        data.loc[data['bmi'].isnull(), 'bmi'] = mean_bmi

        logger.info('Null value in bmi imputed')

        col_to_drop = ['id', 'age_bin', 'gender_age']
        data = data.drop(columns=col_to_drop)

        logger.info('Unnessary columns deleted')

        data.to_csv(os.path.join(save_data_file),index = False)
        data = pd.read_csv(os.path.join(save_data_file))
        cata_col = ['gender', 'ever_married', 'work_type', 'Residence_type', 'smoking_status']
        data[cata_col] = data[cata_col].astype('category')


        logger.info(f'File saved in {save_data_file}')