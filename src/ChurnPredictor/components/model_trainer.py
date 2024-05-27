import pandas as pd
import os
from mlProject import logger
from catboost import CatBoostClassifier
import joblib
from ChurnPredictor.entity.config_entity import ModelTrainerConfig

class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config

    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]]
        test_y = test_data[[self.config.target_column]]


        cb = CatBoostClassifier(learning_rate=self.config.learning_rate, l2_leaf_reg=self.config.l2_leaf_reg, iterations=self.config.iterations, depth=self.config.depth, border_count=self.config.border_count, bagging_temperature=self.config.bagging_temperature)
        cb.fit(train_x, train_y)

        joblib.dump(cb, os.path.join(self.config.root_dir, self.config.model_name))

