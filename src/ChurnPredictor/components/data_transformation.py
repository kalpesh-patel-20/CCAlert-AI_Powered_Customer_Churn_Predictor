import os
import pandas as pd
import numpy as np
from mlProject import logger
from imblearn.over_sampling import SMOTE
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import LabelEncoder
from sklearn.preprocessing import StandardScaler
from ChurnPredictor.entity.config_entity import DataTransformationConfig

class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config

    def data_manipulation(self, df: pd.DataFrame) -> pd.DataFrame:
        df = df.drop(['customerID'], axis = 1)
        df['TotalCharges'] = pd.to_numeric(df.TotalCharges, errors='coerce')

        df.drop(labels=df[df['tenure'] == 0].index, axis=0, inplace=True)
        df["SeniorCitizen"]= df["SeniorCitizen"].map({0: "No", 1: "Yes"})

        return df
    
    def object_to_int(self, df: pd.DataFrame) -> pd.DataFrame:
        if df.dtype=='object':
            df = LabelEncoder().fit_transform(df)
        
        return df

    def data_transformation(self):
        data = pd.read_csv(self.config.data_path)

        data = self.data_manipulation(data)
        logger.info("Data Manipulation Done")

        data = data.apply(lambda x: self.object_to_int(x))
        logger.info("Converted from object to int type")

        X = data.drop(columns = ['Churn'])
        y = data['Churn'].values

        X_train, X_test, y_train, y_test = train_test_split(X,y,test_size = 0.30, random_state = 40, stratify=y)

        smote = SMOTE(random_state=42)
        X_train_resampled, y_train_resampled = smote.fit_resample(X_train, y_train)
        logger.info("Resampling Done")

        num_cols = ["tenure", 'MonthlyCharges', 'TotalCharges']
        df_std = pd.DataFrame(StandardScaler().fit_transform(data[num_cols].astype('float64')),
                       columns=num_cols)
        
        scaler= StandardScaler()

        X_train_resampled[num_cols] = scaler.fit_transform(X_train_resampled[num_cols])
        X_test[num_cols] = scaler.transform(X_test[num_cols])
        logger.info("Scaling completed")

        if isinstance(X_train_resampled, np.ndarray):
            X_train_resampled = pd.DataFrame(X_train_resampled, columns=[f'feature_{i}' for i in range(X_train_resampled.shape[1])])

        if isinstance(y_train_resampled, np.ndarray):
            y_train_resampled = pd.Series(y_train_resampled, name='Churn')

        if isinstance(y_train_resampled, pd.Series):
            y_train_resampled = y_train_resampled.to_frame()

        train = pd.concat([X_train_resampled, y_train_resampled], axis=1)


        if isinstance(X_test, np.ndarray):
            X_test = pd.DataFrame(X_test, columns=[f'feature_{i}' for i in range(X_test.shape[1])])

        if isinstance(y_test, np.ndarray):
            y_test = pd.Series(y_test, name='Churn')

        if isinstance(y_test, pd.Series):
            y_test = y_test.to_frame()

        test = pd.concat([X_test, y_test], axis=1)

        train.to_csv(os.path.join(self.config.root_dir, "train.csv"),index = False)
        test.to_csv(os.path.join(self.config.root_dir, "test.csv"),index = False)

        logger.info("Splited data into training and test sets")
        logger.info(train.shape)
        logger.info(test.shape)

        print(train.shape)
        print(test.shape)
