# AI Diet & Exercise Recommendation System 🏋️‍♂️ 🥗

An AI-powered recommendation system that provides personalized diet and exercise suggestions based on user preferences and goals. The system uses machine learning to analyze user inputs and recommend suitable food choices and workout routines for both indoor and gym environments.

## Features

- Personalized diet recommendations based on:
  - Calorie targets
  - Diet preferences (keto, vegetarian, vegan, etc.)
  - Meal types
  - Macronutrient distribution

- Customized exercise recommendations considering:
  - Fitness level
  - Preferred location (indoor/gym)
  - Target muscle groups
  - Available equipment

- Interactive web interface built with Streamlit
- Data visualization using Plotly
- Machine learning-based recommendation engine

## Project Structure

```
project/
├── src/
│   ├── data_collection/
│   │   └── scraper.py
│   ├── model/
│   │   └── trainer.py
│   └── app.py
├── data/
│   ├── food_data.csv
│   └── exercise_data.csv
├── models/
│   ├── food_model.pkl
│   └── exercise_model.pkl
├── requirements.txt
└── README.md
```

## Setup Instructions

1. Clone the repository:
```bash
git clone <repository-url>
cd diet-and-health
```

2. Create and activate a virtual environment (optional but recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

4. Collect and prepare the data:
```bash
python src/data_collection/scraper.py
```

5. Train the recommendation models:
```bash
python src/model/trainer.py
```

6. Run the Streamlit application:
```bash
streamlit run src/app.py
```

## Usage

1. Open the web application in your browser (default: http://localhost:8501)
2. Input your preferences:
   - Set your daily calorie target
   - Choose your preferred diet types
   - Select meal preferences
   - Specify your fitness level
   - Choose your preferred workout location
   - Select target muscle groups
3. Click "Generate Recommendations" to get personalized suggestions
4. View your customized diet and exercise plans with detailed information and visualizations

## Technologies Used

- Python 3.8+
- Streamlit for web interface
- Pandas for data manipulation
- Scikit-learn for machine learning
- Plotly for data visualization
- BeautifulSoup4 for data collection

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Disclaimer

This is a recommendation system based on AI models and general guidelines. Please consult with healthcare and fitness professionals before starting any new diet or exercise program.