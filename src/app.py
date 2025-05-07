import streamlit as st
import pandas as pd
from model.trainer import DietExerciseRecommender
import plotly.express as px
import os

# Get absolute paths
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_dir = os.path.join(base_dir, 'data')
models_dir = os.path.join(base_dir, 'models')

# Load the trained models
recommender = DietExerciseRecommender.load_models(
    os.path.join(models_dir, 'food_model.pkl'),
    os.path.join(models_dir, 'exercise_model.pkl')
)

# Load the datasets
food_df = pd.read_csv(os.path.join(data_dir, 'food_data.csv'))
exercise_df = pd.read_csv(os.path.join(data_dir, 'exercise_data.csv'))

st.set_page_config(
    page_title='Indian Diet & Exercise Planner',
    layout='wide',
    initial_sidebar_state='expanded',
    menu_items={
        'About': 'A personalized diet and exercise recommendation system'
    }
)

# Custom CSS for modern styling
st.markdown("""
<style>
.main {
    padding: 2rem;
    background-color: #f8f9fa;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
}
.stButton>button {
    width: 100%;
    margin-top: 1rem;
    background-color: #4CAF50;
    color: white;
    border-radius: 25px;
    padding: 0.8rem;
    font-size: 1.1rem;
    transition: all 0.3s ease;
    border: none;
    box-shadow: 0 2px 5px rgba(0,0,0,0.2);
}
.stButton>button:hover {
    background-color: #45a049;
    transform: translateY(-2px);
    box-shadow: 0 4px 8px rgba(0,0,0,0.2);
}
.css-1d391kg {
    padding: 2rem;
    border-radius: 15px;
    background-color: white;
    box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    transition: all 0.3s ease;
}
.css-1d391kg:hover {
    transform: translateY(-5px);
    box-shadow: 0 6px 12px rgba(0,0,0,0.15);
}
.stTab {
    background-color: #ffffff;
    padding: 1.5rem;
    border-radius: 15px;
    margin-bottom: 1.5rem;
    box-shadow: 0 2px 4px rgba(0,0,0,0.05);
}
.stSelectbox, .stMultiSelect {
    border-radius: 10px;
    border: 2px solid #e0e0e0;
    padding: 0.5rem;
    transition: all 0.3s ease;
}
.stSelectbox:hover, .stMultiSelect:hover {
    border-color: #4CAF50;
}
.stSlider {
    padding: 1rem 0;
}
.stProgress {
    height: 10px;
    border-radius: 5px;
    background-color: #e0e0e0;
}
.stProgress > div {
    background-color: #4CAF50;
}
.streamlit-expanderHeader {
    background-color: #f5f5f5;
    border-radius: 10px;
    padding: 0.5rem;
    transition: background-color 0.3s ease;
}
.streamlit-expanderHeader:hover {
    background-color: #e0e0e0;
}
</style>
""", unsafe_allow_html=True)

# Title and description with improved styling
st.markdown("""
<div style='background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); padding: 3rem; border-radius: 20px; margin-bottom: 2rem; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1);'>
    <h1 style='color: white; margin-bottom: 1rem; font-size: 2.5rem; font-weight: 600; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);'>🏋️ Indian Diet & Exercise Planner</h1>
    <p style='font-size: 1.3rem; color: rgba(255,255,255,0.9); max-width: 800px; margin: 0 auto; line-height: 1.6;'>Embark on your personalized wellness journey with our AI-powered diet and exercise recommendations, tailored to your lifestyle and goals!</p>
</div>
""", unsafe_allow_html=True)

# Create modern tabs for better organization
st.markdown("""
<style>
    .stTabs [data-baseweb='tab-list'] {
        gap: 24px;
        padding: 0.5rem;
        background-color: #f8f9fa;
        border-radius: 15px;
        margin-bottom: 2rem;
    }
    .stTabs [data-baseweb='tab'] {
        height: 50px;
        padding: 0 24px;
        background-color: white;
        border-radius: 10px;
        color: #4CAF50;
        font-weight: 600;
        transition: all 0.3s ease;
    }
    .stTabs [data-baseweb='tab']:hover {
        background-color: #e8f5e9;
        color: #2e7d32;
    }
    .stTabs [aria-selected='true'] {
        background-color: #4CAF50 !important;
        color: white !important;
        box-shadow: 0 4px 10px rgba(76, 175, 80, 0.3);
    }
</style>
""", unsafe_allow_html=True)

tabs = st.tabs(["📋 Set Your Preferences", "📅 Weekly Plan", "📊 Progress Tracking"])

with tabs[0]:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #e8f5e9 0%, #c8e6c9 100%); padding: 1.5rem; border-radius: 15px; margin-bottom: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.05);'>
        <h3 style='color: #2e7d32; font-size: 1.5rem; font-weight: 600; margin: 0;'>✨ Customize Your Wellness Journey</h3>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #f8f9fa 0%, #e8f5e9 100%); padding: 1.5rem; border-radius: 15px; margin-bottom: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.05);'>
            <h4 style='color: #2e7d32; font-size: 1.3rem; font-weight: 600; display: flex; align-items: center; gap: 8px; margin-bottom: 1rem;'>
                <span style='font-size: 1.5rem;'>🍽️</span> Diet Preferences
            </h4>
            <p style='color: #666; margin-bottom: 1rem; font-size: 0.9rem;'>Customize your daily nutrition goals and dietary preferences</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<p style='color: #2e7d32; font-weight: 600; margin-bottom: 0.5rem;'>Daily Calorie Target</p>", unsafe_allow_html=True)
        calories_target = st.slider('Daily Calorie Target', 1000, 3000, 2000, label_visibility='collapsed', help='Set your daily calorie intake target')
        
        st.markdown("<p style='color: #2e7d32; font-weight: 600; margin: 1rem 0 0.5rem;'>Diet Type</p>", unsafe_allow_html=True)
        diet_type = st.multiselect('Diet Type',
                                  ['balanced', 'non-vegetarian', 'vegetarian', 'vegan', 'high-protein'],
                                  ['balanced'],
                                  label_visibility='collapsed',
                                  help='Select your preferred diet types')

        st.markdown("<p style='color: #2e7d32; font-weight: 600; margin: 1rem 0 0.5rem;'>Dietary Restrictions</p>", unsafe_allow_html=True)
        dietary_restrictions = st.multiselect('Dietary Restrictions',
                                            ['gluten-free', 'dairy-free', 'nut-free', 'low-carb', 'low-fat', 'none'],
                                            ['none'],
                                            label_visibility='collapsed',
                                            help='Select any dietary restrictions you have')
        
        st.markdown("<p style='color: #2e7d32; font-weight: 600; margin: 1rem 0 0.5rem;'>Preferred Meals</p>", unsafe_allow_html=True)
        meal_preference = st.multiselect('Preferred Meals',
                                        ['breakfast', 'lunch', 'dinner', 'snacks'],
                                        ['breakfast', 'lunch', 'dinner'],
                                        label_visibility='collapsed',
                                        help='Choose your preferred meal times')
    
    with col2:
        st.markdown("""
        <div style='background: linear-gradient(135deg, #f8f9fa 0%, #e8f5e9 100%); padding: 1.5rem; border-radius: 15px; margin-bottom: 1.5rem; box-shadow: 0 2px 8px rgba(0,0,0,0.05);'>
            <h4 style='color: #2e7d32; font-size: 1.3rem; font-weight: 600; display: flex; align-items: center; gap: 8px; margin-bottom: 1rem;'>
                <span style='font-size: 1.5rem;'>💪</span> Exercise Preferences
            </h4>
            <p style='color: #666; margin-bottom: 1rem; font-size: 0.9rem;'>Set your workout preferences and fitness goals</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("<p style='color: #2e7d32; font-weight: 600; margin: 1rem 0 0.5rem;'>Fitness Level</p>", unsafe_allow_html=True)
        fitness_level = st.select_slider('Fitness Level',
                                        options=['beginner', 'intermediate', 'advanced'],
                                        value='intermediate',
                                        label_visibility='collapsed',
                                        help='Select your current fitness level')

        st.markdown("<p style='color: #2e7d32; font-weight: 600; margin: 1rem 0 0.5rem;'>Activity Level</p>", unsafe_allow_html=True)
        activity_level = st.select_slider('Activity Level',
                                        options=['sedentary', 'lightly active', 'moderately active', 'very active'],
                                        value='moderately active',
                                        label_visibility='collapsed',
                                        help='Select your daily activity level')

        st.markdown("<p style='color: #2e7d32; font-weight: 600; margin: 1rem 0 0.5rem;'>Fitness Goals</p>", unsafe_allow_html=True)
        fitness_goals = st.multiselect('Fitness Goals',
                                    ['weight loss', 'muscle gain', 'endurance', 'flexibility', 'strength', 'general fitness'],
                                    ['general fitness'],
                                    label_visibility='collapsed',
                                    help='Select your fitness goals')
        
        st.markdown("<p style='color: #2e7d32; font-weight: 600; margin: 1rem 0 0.5rem;'>Preferred Location</p>", unsafe_allow_html=True)
        exercise_location = st.multiselect('Preferred Location',
                                          ['indoor', 'gym', 'outdoor'],
                                          ['indoor'],
                                          label_visibility='collapsed',
                                          help='Choose your preferred workout locations')
        
        st.markdown("<p style='color: #2e7d32; font-weight: 600; margin: 1rem 0 0.5rem;'>Exercise Types</p>", unsafe_allow_html=True)
        exercise_type = st.multiselect('Exercise Types',
                                      ['Yoga', 'Strength', 'Cardio', 'Breathing'],
                                      ['Yoga', 'Strength'],
                                      label_visibility='collapsed',
                                      help='Select the types of exercises you prefer')

with tabs[1]:
    if st.button('Generate Weekly Plan 🎯', key='generate_plan'):
        st.markdown("""
        <div style='background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); padding: 2rem; border-radius: 20px; margin-bottom: 2rem; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1);'>
            <h3 style='color: white; font-size: 1.8rem; font-weight: 600; margin-bottom: 1rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);'>📅 Your Personalized Weekly Plan</h3>
            <p style='color: rgba(255,255,255,0.9); font-size: 1.1rem; max-width: 700px; margin: 0 auto; line-height: 1.5;'>Here's your customized weekly schedule of diet and exercise recommendations, tailored to your preferences and goals.</p>
        </div>

        <style>
            .plan-card {
                background: white;
                padding: 1.5rem;
                border-radius: 15px;
                box-shadow: 0 4px 6px rgba(0,0,0,0.1);
                margin-bottom: 1.5rem;
                transition: transform 0.3s ease, box-shadow 0.3s ease;
            }
            .plan-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 6px 12px rgba(0,0,0,0.15);
            }
            .day-header {
                color: #2e7d32;
                font-size: 1.4rem;
                font-weight: 600;
                margin-bottom: 1rem;
                padding-bottom: 0.5rem;
                border-bottom: 2px solid #e8f5e9;
            }
            .meal-section, .exercise-section {
                background: #f8f9fa;
                padding: 1rem;
                border-radius: 10px;
                margin-bottom: 1rem;
            }
            .section-title {
                color: #1b5e20;
                font-size: 1.1rem;
                font-weight: 600;
                margin-bottom: 0.5rem;
            }
        </style>
        """, unsafe_allow_html=True)
        
        days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
        
        for day in days:
            st.markdown(f"""
            <div style='background-color: #e8eaf6; padding: 1rem; border-radius: 10px; margin: 1rem 0;'>
                <h4 style='color: #3f51b5;'>{day}</h4>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns(2)
            
            with col1:
                st.markdown("""
                <div style='background-color: #fff3e0; padding: 1rem; border-radius: 10px;'>
                    <h5 style='color: #e65100;'>🍽️ Meals</h5>
                </div>
                """, unsafe_allow_html=True)
                
                # Get meal recommendations based on diet type and restrictions
                diet_pref = diet_type[0] if diet_type else 'balanced'
                restrictions = [r for r in dietary_restrictions if r != 'none']
                
                # Filter food based on diet preference and restrictions
                filtered_food_df = food_df[
                    ((food_df['diet_type'] == diet_pref) | (food_df['diet_type'] == 'balanced'))
                ]
                
                # Apply dietary restrictions if columns exist
                for restriction in restrictions:
                    if restriction == 'gluten-free' and 'gluten_free' in filtered_food_df.columns:
                        filtered_food_df = filtered_food_df[filtered_food_df['gluten_free'] == True]
                    elif restriction == 'dairy-free' and 'dairy_free' in filtered_food_df.columns:
                        filtered_food_df = filtered_food_df[filtered_food_df['dairy_free'] == True]
                    elif restriction == 'nut-free' and 'nut_free' in filtered_food_df.columns:
                        filtered_food_df = filtered_food_df[filtered_food_df['nut_free'] == True]
                    elif restriction == 'low-carb' and 'carbs' in filtered_food_df.columns:
                        filtered_food_df = filtered_food_df[filtered_food_df['carbs'] < 30]
                    elif restriction == 'low-fat' and 'fat' in filtered_food_df.columns:
                        filtered_food_df = filtered_food_df[filtered_food_df['fat'] < 10]
                
                # Get recommendations for each meal with fallback to full dataset
                breakfast_df = filtered_food_df[filtered_food_df['meal_type'] == 'breakfast']
                if len(breakfast_df) == 0:
                    breakfast_df = food_df[food_df['meal_type'] == 'breakfast']
                breakfast = breakfast_df.sample(1).iloc[0]
                
                lunch_df = filtered_food_df[filtered_food_df['meal_type'] == 'lunch']
                if len(lunch_df) == 0:
                    lunch_df = food_df[food_df['meal_type'] == 'lunch']
                lunch = lunch_df.sample(1).iloc[0]
                
                dinner_df = filtered_food_df[filtered_food_df['meal_type'] == 'dinner']
                if len(dinner_df) == 0:
                    dinner_df = food_df[food_df['meal_type'] == 'dinner']
                dinner = dinner_df.sample(1).iloc[0]
                
                st.markdown(f"""
                **Morning (Breakfast):**
                - {breakfast['name']} ({breakfast['cuisine']})
                - Calories: {breakfast['calories']} kcal
                - Cooking Time: {breakfast['cooking_time']}
                - [Watch Recipe Video]({breakfast['recipe_video']}) 🎥
                
                **Afternoon (Lunch):**
                - {lunch['name']} ({lunch['cuisine']})
                - Calories: {lunch['calories']} kcal
                - Cooking Time: {lunch['cooking_time']}
                - [Watch Recipe Video]({lunch['recipe_video']}) 🎥
                
                **Evening (Dinner):**
                - {dinner['name']} ({dinner['cuisine']})
                - Calories: {dinner['calories']} kcal
                - Cooking Time: {dinner['cooking_time']}
                - [Watch Recipe Video]({dinner['recipe_video']}) 🎥
                """)
            
            with col2:
                st.markdown("""
                <div style='background-color: #e8f5e9; padding: 1rem; border-radius: 10px;'>
                    <h5 style='color: #2e7d32;'>💪 Workouts</h5>
                </div>
                """, unsafe_allow_html=True)
                
                # Adjust workout intensity based on activity level and fitness level
                intensity_map = {
                    ('beginner', 'sedentary'): 'low',
                    ('beginner', 'lightly active'): 'low',
                    ('beginner', 'moderately active'): 'moderate',
                    ('beginner', 'very active'): 'moderate',
                    ('intermediate', 'sedentary'): 'moderate',
                    ('intermediate', 'lightly active'): 'moderate',
                    ('intermediate', 'moderately active'): 'high',
                    ('intermediate', 'very active'): 'high',
                    ('advanced', 'sedentary'): 'moderate',
                    ('advanced', 'lightly active'): 'high',
                    ('advanced', 'moderately active'): 'high',
                    ('advanced', 'very active'): 'very high'
                }
                workout_intensity = intensity_map.get((fitness_level, activity_level), 'moderate')
                
                # Filter exercises based on fitness goals
                goal_exercise_map = {
                    'weight loss': ['Cardio', 'HIIT'],
                    'muscle gain': ['Strength'],
                    'endurance': ['Cardio', 'HIIT'],
                    'flexibility': ['Yoga', 'Stretching'],
                    'strength': ['Strength', 'Bodyweight'],
                    'general fitness': ['Cardio', 'Strength', 'Yoga']
                }
                
                recommended_categories = set()
                for goal in fitness_goals:
                    recommended_categories.update(goal_exercise_map.get(goal, []))
                
                # Get exercise recommendations based on user's preferred locations
                if 'indoor' in exercise_location:
                    yoga_df = exercise_df[
                        (exercise_df['category'] == 'Yoga') & 
                        (exercise_df['location'] == 'indoor')
                    ]
                    if not yoga_df.empty:
                        yoga_df_intensity = yoga_df[yoga_df['difficulty'] == workout_intensity]
                        morning_yoga = yoga_df_intensity.sample(1).iloc[0] if not yoga_df_intensity.empty else yoga_df.sample(1).iloc[0]
                    else:
                        morning_yoga = None
                else:
                    morning_yoga = None
                
                # Different exercises for each day based on user's preferred locations
                if 'gym' in exercise_location:
                    if day == 'Monday':
                        # Chest and Triceps Day
                        gym_df = exercise_df[
                            (exercise_df['category'].isin(recommended_categories)) & 
                            (exercise_df['location'] == 'gym') & 
                            (exercise_df['target_muscles'].isin(['chest', 'triceps']))
                        ]
                        if not gym_df.empty:
                            gym_df_intensity = gym_df[gym_df['difficulty'] == workout_intensity]
                            gym_workout = gym_df_intensity.sample(1).iloc[0] if not gym_df_intensity.empty else gym_df.sample(1).iloc[0]
                        else:
                            gym_workout = None
                    elif day == 'Tuesday':
                        # Back and Biceps Day
                        gym_df = exercise_df[
                            (exercise_df['category'].isin(recommended_categories)) & 
                            (exercise_df['location'] == 'gym') & 
                            (exercise_df['target_muscles'].isin(['back', 'biceps']))
                        ]
                        if not gym_df.empty:
                            gym_df_intensity = gym_df[gym_df['difficulty'] == workout_intensity]
                            gym_workout = gym_df_intensity.sample(1).iloc[0] if not gym_df_intensity.empty else gym_df.sample(1).iloc[0]
                        else:
                            gym_workout = None
                    elif day == 'Wednesday':
                        # Legs Day
                        gym_df = exercise_df[
                            (exercise_df['category'].isin(recommended_categories)) & 
                            (exercise_df['location'] == 'gym') & 
                            (exercise_df['target_muscles'].isin(['legs', 'calves']))
                        ]
                        if not gym_df.empty:
                            gym_df_intensity = gym_df[gym_df['difficulty'] == workout_intensity]
                            gym_workout = gym_df_intensity.sample(1).iloc[0] if not gym_df_intensity.empty else gym_df.sample(1).iloc[0]
                        else:
                            gym_workout = None
                    elif day == 'Thursday':
                        # Shoulders and Abs Day
                        gym_df = exercise_df[
                            (exercise_df['category'].isin(recommended_categories)) & 
                            (exercise_df['location'] == 'gym') & 
                            (exercise_df['target_muscles'].isin(['shoulders', 'abs']))
                        ]
                        if not gym_df.empty:
                            gym_df_intensity = gym_df[gym_df['difficulty'] == workout_intensity]
                            gym_workout = gym_df_intensity.sample(1).iloc[0] if not gym_df_intensity.empty else gym_df.sample(1).iloc[0]
                        else:
                            gym_workout = None
                    elif day == 'Friday':
                        # Full Body Day
                        gym_df = exercise_df[
                            (exercise_df['category'].isin(recommended_categories)) & 
                            (exercise_df['location'] == 'gym') & 
                            (exercise_df['target_muscles'] == 'full body')
                        ]
                        if not gym_df.empty:
                            gym_df_intensity = gym_df[gym_df['difficulty'] == workout_intensity]
                            gym_workout = gym_df_intensity.sample(1).iloc[0] if not gym_df_intensity.empty else gym_df.sample(1).iloc[0]
                        else:
                            gym_workout = None
                    elif day == 'Saturday':
                        # Core and Cardio Day
                        gym_df = exercise_df[
                            (exercise_df['category'].isin(['Cardio', 'HIIT'])) & 
                            (exercise_df['location'] == 'gym') & 
                            (exercise_df['target_muscles'].isin(['core', 'cardio']))
                        ]
                        if not gym_df.empty:
                            gym_df_intensity = gym_df[gym_df['difficulty'] == workout_intensity]
                            gym_workout = gym_df_intensity.sample(1).iloc[0] if not gym_df_intensity.empty else gym_df.sample(1).iloc[0]
                        else:
                            gym_workout = None
                    else:  # Sunday - Rest day from gym
                        gym_workout = None
                else:
                    gym_workout = None
                
                # Get outdoor workout recommendations if outdoor location is selected
                if 'outdoor' in exercise_location:
                    outdoor_df = exercise_df[
                        (exercise_df['category'].isin(recommended_categories)) & 
                        (exercise_df['location'] == 'outdoor')
                    ]
                    if not outdoor_df.empty:
                        outdoor_df_intensity = outdoor_df[outdoor_df['difficulty'] == workout_intensity]
                        outdoor_workout = outdoor_df_intensity.sample(1).iloc[0] if not outdoor_df_intensity.empty else outdoor_df.sample(1).iloc[0]
                    else:
                        outdoor_workout = None
                else:
                    outdoor_workout = None
                
                # Adjust breathing exercises if indoor location is selected
                if 'indoor' in exercise_location:
                    breathing_intensity = 'moderate' if workout_intensity in ['high', 'very high'] else 'low'
                    breathing_df = exercise_df[
                        (exercise_df['category'] == 'Breathing') & 
                        (exercise_df['location'] == 'indoor')
                    ]
                    if not breathing_df.empty:
                        breathing_df_intensity = breathing_df[breathing_df['difficulty'] == breathing_intensity]
                        evening_breathing = breathing_df_intensity.sample(1).iloc[0] if not breathing_df_intensity.empty else breathing_df.sample(1).iloc[0]
                    else:
                        evening_breathing = None
                else:
                    evening_breathing = None
                
                # Display morning yoga if available
                if morning_yoga is not None:
                    st.markdown(f"""
                    **Morning Indoor Routine:**
                    - {morning_yoga['name']} ({morning_yoga['category']})
                    - Duration: 20 mins
                    - Location: {morning_yoga['location']}
                    - [Watch Exercise Tutorial]({morning_yoga['exercise_video']}) 🎥
                    """)
                else:
                    st.markdown(f"""
                    **Morning Indoor Routine:**
                    Recommended exercises:
                    - Sun Salutations (10 mins)
                    - Basic Stretching (5 mins)
                    - Mindful Breathing (5 mins)
                    - [Watch Sun Salutations Tutorial](https://www.youtube.com/watch?v=_eCHrcq5wRY) 🎥
                    """)
                
                # Display gym workout if available and not Sunday
                if day != 'Sunday':
                    if gym_workout is not None:
                        st.markdown(f"""
                        **Gym Session:**
                        - {gym_workout['name']} ({gym_workout['category']})
                        - Duration: 30 mins
                        - Target: {gym_workout['target_muscles']}
                        - Equipment: {gym_workout['equipment_needed']}
                        - [Watch Exercise Tutorial]({gym_workout['exercise_video']}) 🎥
                        """)
                    else:
                        if day == 'Monday':
                            st.markdown(f"""
                            **Home Workout - Chest and Triceps:**
                            - Push-ups (4 sets of 12)
                            - Diamond Push-ups (3 sets of 10)
                            - Tricep Dips (3 sets of 12)
                            - Decline Push-ups (3 sets of 10)
                            - [Watch Push-ups Tutorial](https://www.youtube.com/watch?v=IODxDxX7oi4) 🎥
                            - [Watch Diamond Push-ups](https://www.youtube.com/watch?v=J0DnG1_S92I) 🎥
                            """)
                        elif day == 'Tuesday':
                            st.markdown(f"""
                            **Home Workout - Back and Biceps:**
                            - Pull-ups/Assisted Pull-ups (3 sets of 8)
                            - Inverted Rows (3 sets of 12)
                            - Resistance Band Curls (4 sets of 15)
                            - Superman Holds (3 sets of 30 seconds)
                            - [Watch Pull-ups Tutorial](https://www.youtube.com/watch?v=eGo4IYlbE5g) 🎥
                            - [Watch Inverted Rows Guide](https://www.youtube.com/watch?v=dJ-6tQ02kqM) 🎥
                            """)
                        elif day == 'Wednesday':
                            st.markdown(f"""
                            **Home Workout - Legs:**
                            - Bodyweight Squats (4 sets of 20)
                            - Lunges (3 sets of 15 each leg)
                            - Jump Squats (3 sets of 12)
                            - Calf Raises (4 sets of 25)
                            - [Watch Squats Tutorial](https://www.youtube.com/watch?v=aclHkVaku9U) 🎥
                            - [Watch Lunges Guide](https://www.youtube.com/watch?v=QOVaHwm-Q6U) 🎥
                            """)
                        elif day == 'Thursday':
                            st.markdown(f"""
                            **Home Workout - Shoulders and Abs:**
                            - Pike Push-ups (3 sets of 10)
                            - Plank to Downward Dog (3 sets of 12)
                            - Mountain Climbers (3 sets of 30 seconds)
                            - Russian Twists (3 sets of 20)
                            - [Watch Pike Push-ups](https://www.youtube.com/watch?v=sposDXWEB0A) 🎥
                            - [Watch Ab Workout Guide](https://www.youtube.com/watch?v=DHD1-2P94DI) 🎥
                            """)
                        elif day == 'Friday':
                            st.markdown(f"""
                            **Home Workout - Full Body:**
                            - Burpees (3 sets of 10)
                            - Mountain Climbers (3 sets of 30 seconds)
                            - Jump Squats (3 sets of 12)
                            - Push-ups (3 sets of 10)
                            - [Watch Burpees Guide](https://www.youtube.com/watch?v=dZgVxmf6jkA) 🎥
                            - [Watch Full Body Workout](https://www.youtube.com/watch?v=oAPCPjnU1wA) 🎥
                            """)
                        elif day == 'Saturday':
                            st.markdown(f"""
                            **Home Workout - Core and Cardio:**
                            - High Knees (3 sets of 45 seconds)
                            - Mountain Climbers (3 sets of 30 seconds)
                            - Plank Hold (3 sets of 45 seconds)
                            - Bicycle Crunches (3 sets of 20)
                            - [Watch HIIT Cardio Guide](https://www.youtube.com/watch?v=ml6cT4AZdqI) 🎥
                            - [Watch Core Workout](https://www.youtube.com/watch?v=DHD1-2P94DI) 🎥
                            """)
                else:
                    st.markdown(f"""
                    **Sunday - Active Recovery Day:**
                    Focus on light activities and recovery:
                    - Light Walking (20-30 minutes)
                    - Gentle Stretching (15-20 minutes)
                    - Mobility Exercises (10-15 minutes)
                    - [Watch Stretching Guide](https://www.youtube.com/watch?v=sTxC3J3gQEU) 🎥
                    - [Watch Mobility Routine](https://www.youtube.com/watch?v=g_tea8ZNk5A) 🎥
                    """)
                
                # Display outdoor workout if available
                if outdoor_workout is not None:
                    st.markdown(f"""
                    **Outdoor Activity:**
                    - {outdoor_workout['name']} ({outdoor_workout['category']})
                    - Duration: 20 mins
                    - Intensity: {outdoor_workout['difficulty']}
                    - [Watch Exercise Tutorial]({outdoor_workout['exercise_video']}) 🎥
                    """)
                else:
                    st.markdown(f"""
                    **Outdoor Activity:**
                    Recommended activities:
                    - Brisk Walking (20 mins)
                    - Light Jogging (15 mins)
                    - Park Bench Exercises:
                      * Step-ups (3 sets of 15 each leg)
                      * Incline Push-ups (3 sets of 10)
                    - [Watch Step-ups Tutorial](https://www.youtube.com/watch?v=dQqApCGd5Ss) 🎥
                    - [Watch Incline Push-ups Tutorial](https://www.youtube.com/watch?v=TaBVLhcHcc0) 🎥
                    """)
                
                # Display evening breathing if available
                if evening_breathing is not None:
                    st.markdown(f"""
                    **Evening Cool-down:**
                    - {evening_breathing['name']} ({evening_breathing['category']})
                    - Duration: 10 mins
                    - [Watch Exercise Tutorial]({evening_breathing['exercise_video']}) 🎥
                    """)
                else:
                    st.markdown(f"""
                    **Evening Cool-down:**
                    Recommended relaxation routine:
                    - Deep Breathing Exercise (5 mins)
                      * Inhale for 4 counts
                      * Hold for 4 counts
                      * Exhale for 4 counts
                    - Progressive Muscle Relaxation (5 mins)
                    - Simple Meditation (5 mins)
                    - [Watch Deep Breathing Tutorial](https://www.youtube.com/watch?v=acUZdGd_3Dg) 🎥
                    - [Watch Progressive Muscle Relaxation](https://www.youtube.com/watch?v=86HUcX8ZtAk) 🎥
                    - [Watch Meditation Guide](https://www.youtube.com/watch?v=U9YKY7fdwyg) 🎥
                    """)

with tabs[2]:
    st.markdown("""
    <div style='background: linear-gradient(135deg, #4CAF50 0%, #45a049 100%); padding: 2rem; border-radius: 20px; margin-bottom: 2rem; text-align: center; box-shadow: 0 4px 15px rgba(0,0,0,0.1);'>
        <h3 style='color: white; font-size: 1.8rem; font-weight: 600; margin-bottom: 1rem; text-shadow: 2px 2px 4px rgba(0,0,0,0.2);'>📊 Track Your Progress</h3>
        <p style='color: rgba(255,255,255,0.9); font-size: 1.1rem; max-width: 700px; margin: 0 auto; line-height: 1.5;'>Monitor your fitness journey with detailed insights and progress visualization.</p>
    </div>
    
    <style>
        .metric-card {
            background: white;
            padding: 1.5rem;
            border-radius: 15px;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
            margin-bottom: 1.5rem;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }
        .metric-card:hover {
            transform: translateY(-5px);
            box-shadow: 0 6px 12px rgba(0,0,0,0.15);
        }
        .metric-title {
            color: #2e7d32;
            font-size: 1.2rem;
            font-weight: 600;
            margin-bottom: 1rem;
        }
        .metric-value {
            font-size: 2rem;
            font-weight: 700;
            color: #1b5e20;
            margin: 1rem 0;
        }
        .progress-bar {
            height: 10px;
            background: #e8f5e9;
            border-radius: 5px;
            margin: 1rem 0;
            overflow: hidden;
        }
        .progress-bar-fill {
            height: 100%;
            background: linear-gradient(90deg, #4CAF50, #45a049);
            border-radius: 5px;
            transition: width 0.3s ease;
        }
    </style>
    """, unsafe_allow_html=True)
    
    progress_col1, progress_col2 = st.columns(2)
    
    # Define days of the week for progress tracking
    tracking_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    
    with progress_col1:
        # Sample weekly calorie chart
        weekly_calories = pd.DataFrame({
            'Day': tracking_days,
            'Calories': [2100, 2300, 1900, 2000, 2200, 1800, 2400]
        })
        fig = px.line(weekly_calories, x='Day', y='Calories',
                    title='Weekly Calorie Intake',
                    markers=True)
        st.plotly_chart(fig)
    
    with progress_col2:
        # Sample weekly exercise chart
        weekly_exercise = pd.DataFrame({
            'Day': tracking_days,
            'Minutes': [45, 60, 30, 45, 60, 30, 45]
        })
        fig = px.bar(weekly_exercise, x='Day', y='Minutes',
                    title='Daily Exercise Duration',
                    color_discrete_sequence=['#4CAF50'])
        st.plotly_chart(fig)

# Footer
st.markdown('---')
st.markdown("""
<div style='text-align: center; color: #666;'>
    <p><strong>Disclaimer:</strong> This is an AI-powered recommendation system based on Indian dietary and exercise practices.
    Please consult with healthcare and fitness professionals before starting any new wellness program.</p>
</div>
""", unsafe_allow_html=True)