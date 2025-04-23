import os
import sys

from dataclasses import dataclass

from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout
from tensorflow.keras.optimizers import Adam


from datascienceproject.exception import CustomException
from datascienceproject.logger import logging
from datascienceproject.components.model_evaluation import ModelEvaluation
from datascienceproject.utils import save_object

@dataclass
class DeepTrainerConfig:
    train_model_file_path = os.path.join('artifacts', 'deep_model.h5')
    model_json_path = os.path.join('artifacts', 'deep_model.json')
    model_weights_path = os.path.join('artifacts', 'deep_model_weights.weights.h5')
    model_summary_path = os.path.join('artifacts', 'deep_model_summary.txt')
    model_history_path = os.path.join('artifacts', 'deep_model_history.txt')
    scaler_path = os.path.join('artifacts', 'scaler.pkl')
    encoder_path = os.path.join('artifacts', 'encoder.pkl')

class DeepTrainer:
    def __init__(self):
        self.deep_trainer_config = DeepTrainerConfig()
        self.model = None

    def create_model(self, input_shape, X, y):
        try:
            logging.info("Creating Deep Learning Model Started !")
            model = Sequential()
            model.add(Dense(128, activation='relu', input_shape=(input_shape-1,)))
            model.add(Dropout(0.2))
            model.add(Dense(64, activation='relu'))
            model.add(Dropout(0.2))
            model.add(Dense(32, activation='relu'))
            model.add(Dropout(0.2))
            model.add(Dense(16, activation='relu'))
            model.add(Dense(1))

            optimizer = Adam(learning_rate=0.001)

            model.compile(optimizer=optimizer, loss='mean_squared_error', metrics=['mae'])
            model.fit(X, y, epochs=100, batch_size=32, validation_split=0.2)
            self.model = model
            model_json = model.to_json()

            # Save the entire model to a file
            model.save(self.deep_trainer_config.train_model_file_path)

            # Save the model architecture to a JSON file
            with open(self.deep_trainer_config.model_json_path, 'w') as json_file:
                json_file.write(model_json)

            # Save the model weights to a file
            model.save_weights(self.deep_trainer_config.model_weights_path)

            # Save the model summary to a text file
            with open(self.deep_trainer_config.model_summary_path, 'w', encoding='utf-8') as f:
                model.summary(print_fn=lambda x: f.write(x + '\n'))

            # Save the training history to a text file
            with open(self.deep_trainer_config.model_history_path, 'w', encoding='utf-8') as f:
                f.write(str(model.history.history))


            # Save the scaler and encoder objects to pickle files
            scaler_path = self.deep_trainer_config.scaler_path
            encoder_path = self.deep_trainer_config.encoder_path

            if hasattr(self, 'scaler') and self.scaler is not None:
                save_object(scaler_path, self.scaler)
                logging.info(f"Scaler object saved at {scaler_path}")

            if hasattr(self, 'encoder') and self.encoder is not None:
                save_object(encoder_path, self.encoder)
                logging.info(f"Encoder object saved at {encoder_path}")


            logging.info("Deep Learning Model Created Successfully!")
        except Exception as ex:
            raise CustomException(ex, sys)
