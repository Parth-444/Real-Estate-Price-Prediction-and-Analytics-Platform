🏠 Real Estate Price Prediction and Analytics Platform

An end-to-end web application for predicting real estate prices, analyzing property data, and recommending personalized listings.
Built using Machine Learning, Python, and Streamlit, this platform allows users to explore property insights, predict prices, and receive tailored recommendations — all through an intuitive, interactive interface.

🚀 Features
🔹 Price Prediction

Predict property prices instantly using a trained regression model.

Models optimized via feature engineering and hyperparameter tuning to achieve 93% accuracy.

🔹 Property Analytics

Visualize and analyze property trends, pricing distribution, and location-based insights.

Interactive dashboards powered by Streamlit and Pandas.

🔹 Recommendation System

Get personalized property recommendations based on user preferences and property similarities.

Enhanced recommendation accuracy using weighted similarity metrics.

🧱 Project Structure
Real-Estate-Price-Prediction-and-Analytics/
│
├── data/                     # Raw and cleaned datasets (not uploaded due to size)
│
├── notebooks/                # Jupyter notebooks for end-to-end data processing
│   ├── data_cleaning.ipynb   # Data extraction, cleaning, and preprocessing
│   ├── feature_engineering.ipynb
│   ├── model_training.ipynb  # Model training and evaluation
│
├── app.py                    # Main Streamlit app file (entry point)
│
├── pages/                    # Streamlit multi-page structure
│   ├── 1_Price_Predictor.py  # ML-based price prediction page
│   ├── 2_Property_Analytics.py  # Data visualization and EDA insights
│   ├── 3_Recommendations.py  # Personalized property recommendations
│
├── models/                   # Saved trained models and scalers
│
├── requirements.txt          # Python dependencies
│
├── README.md                 # Project documentation
│
└── utils/                    # Helper scripts for preprocessing, prediction, etc.

⚙️ Tech Stack
Category	Technologies
Programming Language	Python 🐍
Frontend / UI	Streamlit
Data Analysis	Pandas, NumPy
Modeling	Scikit-learn, XGBoost, RandomForest
Visualization	Matplotlib, Seaborn
Deployment	AWS EC2
Version Control	Git, GitHub
📊 Workflow Overview
1. Data Pipeline

Extracted property listings from 99acres.com

Cleaned, standardized, and engineered features to improve data quality by ~25%

2. Model Development

Trained regression models with feature selection and tuning

Achieved 93% accuracy and reduced MAE by 18%

3. Web Application

Integrated models into an interactive Streamlit app

Implemented multi-page architecture (Predictor, Analytics, Recommendation)

Improved user query response time by 30%

4. Deployment

Deployed on AWS for scalable and accessible usage

💻 How to Run Locally
1. Clone the Repository
git clone https://github.com/<your-username>/Real-Estate-Price-Prediction-and-Analytics.git
cd Real-Estate-Price-Prediction-and-Analytics

2. Create Virtual Environment
python -m venv venv
source venv/bin/activate   # For macOS/Linux
venv\Scripts\activate      # For Windows

3. Install Dependencies
pip install -r requirements.txt

4. Run Streamlit App
streamlit run app.py


Then open your browser at 👉 http://localhost:8501/

📸 Screenshots

(You can add screenshots later once your app is running and styled — ideally showing predictor page, analytics dashboard, and recommendation page.)

📈 Results & Performance
Metric	Before Optimization	After Optimization
Model Accuracy	85%	93%
Mean Absolute Error	Baseline	↓ 18%
Data Consistency	–	↑ 25%
Query Response Time	–	↓ 30%
🧩 Future Enhancements

Add Geospatial Visualization using Folium / Plotly Maps

Integrate Real-time Property Data APIs

Include User Authentication for personalized dashboards

Expand to Rental Price Prediction module

🙌 Acknowledgments

Data sourced from 99acres.com (publicly available listings)

Inspired by real-world property analytics platforms

Developed with ❤️ using Python, Streamlit, and Machine Learning
