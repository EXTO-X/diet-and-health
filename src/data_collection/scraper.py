import requests
from bs4 import BeautifulSoup
import pandas as pd
import json

def scrape_food_data():
    # List to store food data
    food_data = []
    
    # Example food data structure with expanded healthy options
    sample_foods = [
        # Traditional Indian Dishes
        {
            'name': 'Dal Tadka',
            'calories': 250,
            'protein': 12,
            'carbs': 35,
            'fats': 8,
            'category': 'Main Course',
            'meal_type': 'lunch',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=6NoQZxB0218',
            'cooking_time': '30 mins',
            'cuisine': 'North Indian'
        },
        {
            'name': 'Vegetable Biryani',
            'calories': 350,
            'protein': 10,
            'carbs': 55,
            'fats': 12,
            'category': 'Main Course',
            'meal_type': 'lunch',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=oV7kBh68M6E',
            'cooking_time': '45 mins',
            'cuisine': 'Indian'
        },
        # Mediterranean Dishes
        {
            'name': 'Greek Salad',
            'calories': 180,
            'protein': 8,
            'carbs': 15,
            'fats': 12,
            'category': 'Salad',
            'meal_type': 'lunch',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=xvpBqX_pC2Y',
            'cooking_time': '15 mins',
            'cuisine': 'Mediterranean'
        },
        {
            'name': 'Shakshuka',
            'calories': 280,
            'protein': 16,
            'carbs': 20,
            'fats': 15,
            'category': 'Breakfast',
            'meal_type': 'breakfast',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=618QsMaVXp8',
            'cooking_time': '25 mins',
            'cuisine': 'Middle Eastern'
        },
        # Asian Fusion
        {
            'name': 'Tofu Stir Fry',
            'calories': 220,
            'protein': 15,
            'carbs': 25,
            'fats': 10,
            'category': 'Main Course',
            'meal_type': 'dinner',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=OdNqWcUdm6I',
            'cooking_time': '20 mins',
            'cuisine': 'Asian Fusion'
        },
        # Healthy Indian Breakfast
        {
            'name': 'Oats Upma',
            'calories': 200,
            'protein': 8,
            'carbs': 30,
            'fats': 5,
            'category': 'Breakfast',
            'meal_type': 'breakfast',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=y9TM5nxpjw0',
            'cooking_time': '15 mins',
            'cuisine': 'Indian Fusion'
        },
        {
            'name': 'Quinoa Upma',
            'calories': 220,
            'protein': 8,
            'carbs': 32,
            'fats': 6,
            'category': 'Breakfast',
            'meal_type': 'breakfast',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=5_JUReD73h8',
            'cooking_time': '20 mins',
            'cuisine': 'Indian Fusion'
        },
        {
            'name': 'Almond Milk Quinoa Porridge',
            'calories': 240,
            'protein': 10,
            'carbs': 35,
            'fats': 8,
            'category': 'Breakfast',
            'meal_type': 'breakfast',
            'diet_type': 'vegan',
            'recipe_video': 'https://www.youtube.com/watch?v=2q8V_eEHhKE',
            'cooking_time': '25 mins',
            'cuisine': 'International'
        },
        {
            'name': 'Sprouted Moong Chilla',
            'calories': 180,
            'protein': 12,
            'carbs': 25,
            'fats': 4,
            'category': 'Breakfast',
            'meal_type': 'breakfast',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=bYZU0Mw6eMY',
            'cooking_time': '20 mins',
            'cuisine': 'North Indian'
        },
        {
            'name': 'Mediterranean Chickpea Bowl',
            'calories': 320,
            'protein': 15,
            'carbs': 45,
            'fats': 12,
            'category': 'Main Course',
            'meal_type': 'lunch',
            'diet_type': 'vegan',
            'recipe_video': 'https://www.youtube.com/watch?v=h3OvE3qf_7U',
            'cooking_time': '25 mins',
            'cuisine': 'Mediterranean'
        },
        {
            'name': 'Grilled Salmon with Quinoa',
            'calories': 420,
            'protein': 35,
            'carbs': 30,
            'fats': 18,
            'category': 'Main Course',
            'meal_type': 'dinner',
            'diet_type': 'non-vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=SQuyOwNtAVM',
            'cooking_time': '30 mins',
            'cuisine': 'Mediterranean'
        },
        {
            'name': 'Lentil and Spinach Soup',
            'calories': 250,
            'protein': 14,
            'carbs': 40,
            'fats': 6,
            'category': 'Soup',
            'meal_type': 'dinner',
            'diet_type': 'vegan',
            'recipe_video': 'https://www.youtube.com/watch?v=OurUbJqBVPY',
            'cooking_time': '35 mins',
            'cuisine': 'Middle Eastern'
        },
        {
            'name': 'Thai Drunken Noodles',
            'calories': 497,
            'protein': 17,
            'carbs': 74,
            'fats': 14,
            'category': 'Main Course',
            'meal_type': 'dinner',
            'diet_type': 'non-vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=L0QDsJUqfl8',
            'cooking_time': '45 mins',
            'cuisine': 'Thai'
        },
        {
            'name': 'Korean Style Pulled Pork Bowl',
            'calories': 450,
            'protein': 37,
            'carbs': 46,
            'fats': 29,
            'category': 'Main Course',
            'meal_type': 'lunch',
            'diet_type': 'non-vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=eHWwH4_BdCk',
            'cooking_time': '40 mins',
            'cuisine': 'Korean'
        },
        {
            'name': 'Mango Chicken with Coconut Sauce',
            'calories': 552,
            'protein': 28,
            'carbs': 46,
            'fats': 28,
            'category': 'Main Course',
            'meal_type': 'dinner',
            'diet_type': 'non-vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=K9XGx_c1u8Y',
            'cooking_time': '50 mins',
            'cuisine': 'Thai Fusion'
        },
        {
            'name': 'Mediterranean Vegetable Stew',
            'calories': 280,
            'protein': 15,
            'carbs': 45,
            'fats': 8,
            'category': 'Main Course',
            'meal_type': 'dinner',
            'diet_type': 'vegan',
            'recipe_video': 'https://www.youtube.com/watch?v=CSF0V_v4QZw',
            'cooking_time': '45 mins',
            'cuisine': 'Mediterranean'
        },
        {
            'name': 'Tofu Paneer Bhurji',
            'calories': 250,
            'protein': 20,
            'carbs': 15,
            'fats': 12,
            'category': 'Main Course',
            'meal_type': 'breakfast',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=TYnmqEXRHAs',
            'cooking_time': '25 mins',
            'cuisine': 'Indian Fusion'
        },
        {
            'name': 'Quinoa Black Bean Bowl',
            'calories': 320,
            'protein': 16,
            'carbs': 53,
            'fats': 8,
            'category': 'Main Course',
            'meal_type': 'lunch',
            'diet_type': 'vegan',
            'recipe_video': 'https://www.youtube.com/watch?v=h3OvE3qf_7U',
            'cooking_time': '30 mins',
            'cuisine': 'Mediterranean'
        },
        {
            'name': 'High Protein Acai Bowl',
            'calories': 473,
            'protein': 39,
            'carbs': 82,
            'fats': 15,
            'category': 'Breakfast',
            'meal_type': 'breakfast',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=kH9XXiYnw-E',
            'cooking_time': '10 mins',
            'cuisine': 'International'
        },
        {
            'name': 'Protein Overnight Oats',
            'calories': 350,
            'protein': 27,
            'carbs': 45,
            'fats': 12,
            'category': 'Breakfast',
            'meal_type': 'breakfast',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=8XKWVuLX9Kg',
            'cooking_time': '5 mins',
            'cuisine': 'International'
        },
        {
            'name': 'Berry Protein Smoothie Bowl',
            'calories': 320,
            'protein': 25,
            'carbs': 40,
            'fats': 8,
            'category': 'Breakfast',
            'meal_type': 'breakfast',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=L7YtB0Dm-rQ',
            'cooking_time': '10 mins',
            'cuisine': 'International'
        },
        {
            'name': 'Chocolate Chia Seed Pudding',
            'calories': 197,
            'protein': 8,
            'carbs': 22,
            'fats': 10,
            'category': 'Dessert',
            'meal_type': 'snack',
            'diet_type': 'vegan',
            'recipe_video': 'https://www.youtube.com/watch?v=HL4Vz_QhKYo',
            'cooking_time': '5 mins',
            'cuisine': 'International'
        },
        {
            'name': 'Protein Peanut Butter Cups',
            'calories': 250,
            'protein': 13,
            'carbs': 15,
            'fats': 18,
            'category': 'Dessert',
            'meal_type': 'snack',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=U4jY6Ggn8bs',
            'cooking_time': '20 mins',
            'cuisine': 'International'
        },
        {
            'name': 'Maple Vanilla Protein Fudge',
            'calories': 180,
            'protein': 10,
            'carbs': 12,
            'fats': 12,
            'category': 'Dessert',
            'meal_type': 'snack',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=JY9XZ2oYg8c',
            'cooking_time': '15 mins',
            'cuisine': 'International'
        },
        {
            'name': 'Butter Chicken',
            'calories': 450,
            'protein': 25,
            'carbs': 15,
            'fats': 30,
            'category': 'Main Course',
            'meal_type': 'dinner',
            'diet_type': 'non-vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=OUY-OsGtB4U',
            'cooking_time': '40 mins',
            'cuisine': 'North Indian'
        },
        {
            'name': 'Dal Makhani',
            'calories': 350,
            'protein': 15,
            'carbs': 45,
            'fats': 12,
            'category': 'Main Course',
            'meal_type': 'lunch',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=ca51e7nMI2g',
            'cooking_time': '45 mins',
            'cuisine': 'North Indian'
        },
        {
            'name': 'Paneer Butter Masala',
            'calories': 400,
            'protein': 18,
            'carbs': 20,
            'fats': 28,
            'category': 'Main Course',
            'meal_type': 'dinner',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=U1LVDFwi8qI',
            'cooking_time': '35 mins',
            'cuisine': 'North Indian'
        },
        {
            'name': 'Masala Dosa',
            'calories': 250,
            'protein': 8,
            'carbs': 45,
            'fats': 6,
            'category': 'Breakfast',
            'meal_type': 'breakfast',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=mDqkxZ3UVzc',
            'cooking_time': '30 mins',
            'cuisine': 'South Indian'
        },
        {
            'name': 'Butter Chicken',
            'calories': 450,
            'protein': 25,
            'carbs': 15,
            'fats': 30,
            'category': 'Main Course',
            'meal_type': 'dinner',
            'diet_type': 'non-vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=a03U45jFxOI',
            'cooking_time': '40 mins',
            'cuisine': 'North Indian'
        },
        {
            'name': 'Chicken Biryani',
            'calories': 550,
            'protein': 28,
            'carbs': 65,
            'fats': 22,
            'category': 'Main Course',
            'meal_type': 'lunch',
            'diet_type': 'non-vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=95BCU1n268w',
            'cooking_time': '50 mins',
            'cuisine': 'Indian'
        },
        {
            'name': 'Fish Curry',
            'calories': 320,
            'protein': 24,
            'carbs': 12,
            'fats': 18,
            'category': 'Main Course',
            'meal_type': 'lunch',
            'diet_type': 'non-vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=FnQ5cw8PNxI',
            'cooking_time': '35 mins',
            'cuisine': 'South Indian'
        },
        {
            'name': 'Chicken Tikka',
            'calories': 380,
            'protein': 32,
            'carbs': 8,
            'fats': 20,
            'category': 'Appetizer',
            'meal_type': 'dinner',
            'diet_type': 'non-vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=BKxGodX9NGg',
            'cooking_time': '45 mins',
            'cuisine': 'North Indian'
        },
        {
            'name': 'Idli Sambar',
            'calories': 180,
            'protein': 6,
            'carbs': 35,
            'fats': 2,
            'category': 'Breakfast',
            'meal_type': 'breakfast',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=mDqkxZ3UVzc',
            'cooking_time': '25 mins',
            'cuisine': 'South Indian'
        },
        {
            'name': 'Aloo Paratha',
            'calories': 300,
            'protein': 8,
            'carbs': 52,
            'fats': 8,
            'category': 'Breakfast',
            'meal_type': 'breakfast',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=MH083m_9lyM',
            'cooking_time': '30 mins',
            'cuisine': 'North Indian'
        },
        {
            'name': 'Dal Makhani',
            'calories': 350,
            'protein': 15,
            'carbs': 45,
            'fats': 12,
            'category': 'Main Course',
            'meal_type': 'lunch',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=UFUxFYWHBZ4',
            'cooking_time': '45 mins',
            'cuisine': 'North Indian'
        },
        {
            'name': 'Chole Bhature',
            'calories': 450,
            'protein': 14,
            'carbs': 65,
            'fats': 18,
            'category': 'Main Course',
            'meal_type': 'lunch',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=FX0GHB6OgwY',
            'cooking_time': '40 mins',
            'cuisine': 'North Indian'
        },
        {
            'name': 'Paneer Butter Masala',
            'calories': 400,
            'protein': 18,
            'carbs': 20,
            'fats': 28,
            'category': 'Main Course',
            'meal_type': 'dinner',
            'diet_type': 'vegetarian',
            'recipe_video': 'https://www.youtube.com/watch?v=a30BLUQiFoc',
            'cooking_time': '35 mins',
            'cuisine': 'North Indian'
        }
    ]
    
    food_data.extend(sample_foods)
    return pd.DataFrame(food_data)

def scrape_exercise_data():
    # List to store exercise data
    exercise_data = []
    
    # Example exercise data structure
    sample_exercises = [
        # Strength Training Exercises
        {
            'name': 'Barbell Bench Press',
            'category': 'Strength',
            'location': 'gym',
            'calories_burned': 150,
            'difficulty': 'intermediate',
            'target_muscles': 'chest, shoulders, triceps',
            'equipment_needed': 'barbell, bench',
            'exercise_video': 'https://www.youtube.com/watch?v=vcBig73ojpE'
        },
        {
            'name': 'Deadlift',
            'category': 'Strength',
            'location': 'gym',
            'calories_burned': 180,
            'difficulty': 'intermediate',
            'target_muscles': 'back, glutes, hamstrings',
            'equipment_needed': 'barbell',
            'exercise_video': 'https://www.youtube.com/watch?v=1ZXobu7JvvE'
        },
        {
            'name': 'Squats',
            'category': 'Strength',
            'location': 'gym',
            'calories_burned': 160,
            'difficulty': 'intermediate',
            'target_muscles': 'quads, glutes, core',
            'equipment_needed': 'barbell',
            'exercise_video': 'https://www.youtube.com/watch?v=YaXPRqUwItQ'
        },
        {
            'name': 'Push-ups',
            'category': 'Strength',
            'location': 'indoor',
            'calories_burned': 100,
            'difficulty': 'beginner',
            'target_muscles': 'chest, triceps, shoulders',
            'equipment_needed': 'none',
            'exercise_video': 'https://www.youtube.com/watch?v=IODxDxX7oi4'
        },
        {
            'name': 'Pull-ups',
            'category': 'Strength',
            'location': 'gym',
            'calories_burned': 120,
            'difficulty': 'advanced',
            'target_muscles': 'back, biceps, shoulders',
            'equipment_needed': 'pull-up bar',
            'exercise_video': 'https://www.youtube.com/watch?v=eGo4IYlbE5g'
        },
        {
            'name': 'Downward Facing Dog',
            'category': 'Yoga',
            'location': 'indoor',
            'calories_burned': 50,
            'difficulty': 'beginner',
            'target_muscles': 'shoulders, hamstrings, calves',
            'equipment_needed': 'yoga mat',
            'exercise_video': 'https://www.youtube.com/watch?v=EC7RGJ975iM'
        },
        {
            'name': 'Warrior I Pose',
            'category': 'Yoga',
            'location': 'indoor',
            'calories_burned': 45,
            'difficulty': 'beginner',
            'target_muscles': 'hips, thighs, shoulders',
            'equipment_needed': 'yoga mat',
            'exercise_video': 'https://www.youtube.com/watch?v=k4qaVoAbeHM'
        },
        {
            'name': 'Child\'s Pose',
            'category': 'Yoga',
            'location': 'indoor',
            'calories_burned': 30,
            'difficulty': 'beginner',
            'target_muscles': 'back, hips, shoulders',
            'equipment_needed': 'yoga mat',
            'exercise_video': 'https://www.youtube.com/watch?v=eqVMAPM0O7g'
        },
        {
            'name': 'Triangle Pose',
            'category': 'Yoga',
            'location': 'indoor',
            'calories_burned': 40,
            'difficulty': 'intermediate',
            'target_muscles': 'hips, spine, shoulders',
            'equipment_needed': 'yoga mat',
            'exercise_video': 'https://www.youtube.com/watch?v=upFYdXZjXPw'
        },
        {
            'name': 'Sun Salutation',
            'category': 'Yoga',
            'location': 'indoor',
            'calories_burned': 60,
            'difficulty': 'beginner',
            'target_muscles': 'full body',
            'equipment_needed': 'yoga mat',
            'exercise_video': 'https://www.youtube.com/watch?v=73sjOu0g58M'
        },
        {
            'name': 'Plank',
            'category': 'Strength',
            'location': 'indoor',
            'calories_burned': 100,
            'difficulty': 'beginner',
            'target_muscles': 'core, shoulders, back',
            'equipment_needed': 'none',
            'exercise_video': 'https://www.youtube.com/watch?v=pSHjTRCQxIw'
        },
        {
            'name': 'Dumbbell Shoulder Press',
            'category': 'Strength',
            'location': 'gym',
            'calories_burned': 140,
            'difficulty': 'intermediate',
            'target_muscles': 'shoulders, triceps',
            'equipment_needed': 'dumbbells',
            'exercise_video': 'https://www.youtube.com/watch?v=qEwKCR5JCog'
        },
        {
            'name': 'Lunges',
            'category': 'Strength',
            'location': 'indoor',
            'calories_burned': 120,
            'difficulty': 'beginner',
            'target_muscles': 'quads, glutes, hamstrings',
            'equipment_needed': 'none',
            'exercise_video': 'https://www.youtube.com/watch?v=QOVaHwm-Q6U'
        },
        {
            'name': 'Treadmill Running',
            'category': 'Cardio',
            'location': 'gym',
            'calories_burned': 300,
            'difficulty': 'intermediate',
            'target_muscles': 'legs, core',
            'equipment_needed': 'treadmill',
            'exercise_video': 'https://www.youtube.com/watch?v=kE7RQCgDFxg'
        },
        {
            'name': 'Stationary Cycling',
            'category': 'Cardio',
            'location': 'gym',
            'calories_burned': 250,
            'difficulty': 'beginner',
            'target_muscles': 'legs, core',
            'equipment_needed': 'stationary bike',
            'exercise_video': 'https://www.youtube.com/watch?v=RpgUTaE_Fxw'
        },
        {
            'name': 'Jump Rope',
            'category': 'Cardio',
            'location': 'indoor',
            'calories_burned': 200,
            'difficulty': 'intermediate',
            'target_muscles': 'full body',
            'equipment_needed': 'jump rope',
            'exercise_video': 'https://www.youtube.com/watch?v=FJmRQ5iTXKE'
        },
        {
            'name': 'Burpees',
            'category': 'Cardio',
            'location': 'indoor',
            'calories_burned': 150,
            'difficulty': 'advanced',
            'target_muscles': 'full body',
            'equipment_needed': 'none',
            'exercise_video': 'https://www.youtube.com/watch?v=dZgVxmf6jkA'
        }
    ]
    
    exercise_data.extend(sample_exercises)
    return pd.DataFrame(exercise_data)

def save_data():
    food_df = scrape_food_data()
    exercise_df = scrape_exercise_data()
    
    import os
    
    # Get absolute paths
    base_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    data_dir = os.path.join(base_dir, 'data')
    
    # Save to CSV files
    food_df.to_csv(os.path.join(data_dir, 'food_data.csv'), index=False)
    exercise_df.to_csv(os.path.join(data_dir, 'exercise_data.csv'), index=False)

if __name__ == '__main__':
    save_data()