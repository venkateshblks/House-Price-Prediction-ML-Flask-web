# House Price Prediction Web Application
This repository contains a Flask-based web application for predicting house prices. The application allows users to input various features of a house, and based on those features, it predicts the house price using a machine learning model. The application includes two pages: one for predicting house prices in Bangalore, India, and another for predicting house prices in the USA.

## Table of Contents

- [Overview](#overview)
- [Dataset](#datasets)
- [Setup](#setup)
- [Usage](#usage)
- [Screenshots](#screenshots)
- [Model Implementation](#model-implementation)
## Overview
The application predicts house prices based on input features such as the number of bedrooms, bathrooms, size in square feet, and location. It uses a machine learning model trained on open-source datasets for Bangalore and the USA. The application is divided into two pages:

- **Bangalore House Price Prediction:** Uses features like bedrooms, bathrooms, size, and location to predict house prices in Bangalore.
- **USA House Price Prediction:** Uses additional features like living area, lot area, floors, and more to predict house prices in the USA.

## Datasets

### 1. Bangalore House Price Dataset

- **Description:** This dataset contains information about house prices in Bangalore, India.
- **Features:**
  - `Bedrooms`: Number of bedrooms
  - `Bathrooms`: Number of bathrooms
  - `Size`: Size of the house (in square feet)
  - `Location`: Location of the house

- **Dataset Link:** [Bangalore House Price Dataset](https://www.kaggle.com/datasets/sanjay3454chauhan/bangluru-house-dataset)

### 2. USA House Price Dataset

- **Description:** This dataset contains information about house prices in various regions of the Washington, USA.
- **Features:**
  - `Bedrooms`: Number of bedrooms
  - `Bathrooms`: Number of bathrooms
  - `Living Area`: Living area of the house (in square feet)
  - `Lot Area`: Size of the lot (in square feet)
  - `Floors`: Number of floors
  - `Waterfront`: Yes if the property has a waterfront view, No other-wise
  - `View` : An index from 0 to 4 indicating the quality of the property’s view
  - `Condition`: An index from 1 to 5 rating the condition of the property.
  - `Above Ground Area (Sqft)`: The square footage of the property above the basement
  - `Basement Area (Sqft)`:The square footage of the basement
  - `Year Built`: The year the property was built
  - `Year Renovated`: The year the property was last renovated
  - `Location`:The city where the property is located
  - `Zip Code:`: zip code of the property


- **Dataset Link:** [USA House Price Dataset](https://www.kaggle.com/datasets/fratzcan/usa-house-prices/data)

  ## Setup

To set up the project locally, follow these steps:

1. **Clone the repository:**

    ```bash
    git clone https://github.com/venkateshblks/House-Price-Prediction-ML-Flask-web
    ```
2. **Navigate to the project directory:**
    ```bash
    cd House-Price-Prediction-ML-Flask-web
    ```
3. **Create and activate a virtual environment:**
    ```bash
    python3 -m venv env
    source env/bin/activate   # On Windows, use `env\Scripts\activate`
    ```
4. **Install the required dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run the application:**

    ```bash
    flask run
    ```
    or
   ```bash
   python app.py
   ```
7. **Access the application:**
    Open your browser and go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/).

## Usage
### Bangalore House Price Prediction

1. Navigate to the **Bangalore House Price Prediction** page.
2. Input the following details:
   - Number of bedrooms
   - Number of bathrooms
   - Size of the house
   - Location
3. Click on the **"Predict"** button to get the estimated house price.

### USA House Price Prediction

1. Navigate to the **USA House Price Prediction** page.
2. Input the required features:
   - Number of bedrooms
   - Number of bathrooms
   - Living area
   - Lot Size
   - Number of Floors
   - Waterfront (Yes/No)
   - How is the View?
   - What is the condition of the property?
   - Above Ground Area
   - Basement Area
   - Year Built
   - Year Renovated
   - Location
   - Zip Code
3. Click on the **"Predict"** button to get the estimated house price.

## Screenshots

### Bangalore House Price Prediction

![Screenshot (48)](https://github.com/user-attachments/assets/9b5ab80c-4e3c-4fef-a481-0bdc87f9fd7e)

<br>

![Screenshot (49)](https://github.com/user-attachments/assets/4e4ed59b-66a0-4117-9d5c-a42a25bad123)


### USA House Price Prediction

![screencapture](https://github.com/user-attachments/assets/5280aa95-5469-4fe7-a929-a7d6cb23ce44)


## Model Implementation

The models used for prediction were implemented as follows:

1. **Data Preprocessing:**
   - Datasets were cleaned and features selected.
   - Data was split into training and testing sets.

2. **Model Training:**
   - **Bangalore House Price Prediction:**
     - Implemented using XGBRegressor with `xgboost` library.
     -  Saved model and label encoder:  `label_enocoder.pkl` `house_price_model.pkl`.
       
   - **USA House Price Prediction:** 
     -  Implemented using XGBRegressor with `xgboost` library.
     -  Saved model and label encoder:  `Usa_label1.pkl` `Usa_price1.pkl`.
     


4. **Model Saving:**
   - Models were saved using `pickle`.

5. **Integration with Flask Application:**
   - Saved models are loaded in the Flask application.
   - Predictions are made based on user inputs and displayed in the app.
## Contributing
**Feel free to submit issues or pull requests.**
