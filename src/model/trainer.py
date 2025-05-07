import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.neighbors import NearestNeighbors
import pickle

class DietExerciseRecommender:
    def __init__(self):
        self.food_model = None
        self.exercise_model = None
        self.food_scaler = None
        self.exercise_scaler = None
        self.food_features = None
        self.exercise_features = None

    def prepare_food_features(self, food_df):
        # Select numerical features
        numerical_features = ['calories', 'protein', 'carbs', 'fats']
        # Select categorical features
        categorical_features = ['category', 'meal_type', 'diet_type']

        # Create preprocessing steps
        numeric_transformer = StandardScaler()
        categorical_transformer = OneHotEncoder(handle_unknown='ignore')

        # Combine preprocessing steps
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numerical_features),
                ('cat', categorical_transformer, categorical_features)
            ])

        return preprocessor

    def prepare_exercise_features(self, exercise_df):
        # Select numerical features
        numerical_features = ['calories_burned']
        # Select categorical features
        categorical_features = ['category', 'location', 'difficulty', 'target_muscles', 'equipment_needed']

        # Create preprocessing steps
        numeric_transformer = StandardScaler()
        categorical_transformer = OneHotEncoder(handle_unknown='ignore')

        # Combine preprocessing steps
        preprocessor = ColumnTransformer(
            transformers=[
                ('num', numeric_transformer, numerical_features),
                ('cat', categorical_transformer, categorical_features)
            ])

        return preprocessor

    def train(self, food_df, exercise_df):
        # Prepare food recommendation model
        food_preprocessor = self.prepare_food_features(food_df)
        food_features = food_preprocessor.fit_transform(food_df)
        n_neighbors_food = min(3, len(food_df))
        self.food_model = NearestNeighbors(n_neighbors=n_neighbors_food, metric='cosine')
        self.food_model.fit(food_features)
        self.food_scaler = food_preprocessor
        self.food_features = food_features

        # Prepare exercise recommendation model
        exercise_preprocessor = self.prepare_exercise_features(exercise_df)
        exercise_features = exercise_preprocessor.fit_transform(exercise_df)
        n_neighbors_exercise = min(3, len(exercise_df))
        self.exercise_model = NearestNeighbors(n_neighbors=n_neighbors_exercise, metric='cosine')
        self.exercise_model.fit(exercise_features)
        self.exercise_scaler = exercise_preprocessor
        self.exercise_features = exercise_features

    def recommend_diet(self, user_preferences):
        # Transform user preferences
        user_features = self.food_scaler.transform(user_preferences)
        # Convert sparse matrix to dense if needed
        if hasattr(user_features, 'toarray'):
            user_features = user_features.toarray()
        # Find nearest neighbors
        distances, indices = self.food_model.kneighbors(user_features)
        return indices[0]

    def recommend_exercise(self, user_preferences):
        # Transform user preferences
        user_features = self.exercise_scaler.transform(user_preferences)
        # Convert sparse matrix to dense if needed
        if hasattr(user_features, 'toarray'):
            user_features = user_features.toarray()
        # Find nearest neighbors
        distances, indices = self.exercise_model.kneighbors(user_features)
        return indices[0]

    def save_models(self, food_model_path, exercise_model_path):
        # Save food recommendation model
        with open(food_model_path, 'wb') as f:
            pickle.dump({
                'model': self.food_model,
                'scaler': self.food_scaler,
                'features': self.food_features
            }, f)

        # Save exercise recommendation model
        with open(exercise_model_path, 'wb') as f:
            pickle.dump({
                'model': self.exercise_model,
                'scaler': self.exercise_scaler,
                'features': self.exercise_features
            }, f)

    @classmethod
    def load_models(cls, food_model_path, exercise_model_path):
        recommender = cls()
        
        # Load food recommendation model
        with open(food_model_path, 'rb') as f:
            food_data = pickle.load(f)
            recommender.food_model = food_data['model']
            recommender.food_scaler = food_data['scaler']
            recommender.food_features = food_data['features']

        # Load exercise recommendation model
        with open(exercise_model_path, 'rb') as f:
            exercise_data = pickle.load(f)
            recommender.exercise_model = exercise_data['model']
            recommender.exercise_scaler = exercise_data['scaler']
            recommender.exercise_features = exercise_data['features']

        return recommender

def train_models():
    import os
    
    # Get absolute paths
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_dir = os.path.join(base_dir, 'data')
    models_dir = os.path.join(base_dir, 'models')
    
    # Load data
    food_df = pd.read_csv(os.path.join(data_dir, 'food_data.csv'))
    exercise_df = pd.read_csv(os.path.join(data_dir, 'exercise_data.csv'))

    # Initialize and train recommender
    recommender = DietExerciseRecommender()
    recommender.train(food_df, exercise_df)

    # Save trained models
    recommender.save_models(
        os.path.join(models_dir, 'food_model.pkl'),
        os.path.join(models_dir, 'exercise_model.pkl')
    )

if __name__ == '__main__':
    train_models()