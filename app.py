from flask import Flask, render_template, request, jsonify
import pickle

app = Flask(__name__)


with open('models/house_price_model.pkl', 'rb') as file:
    house_model = pickle.load(file)

with open('models/label_encoder.pkl', 'rb') as file:
    house_encoder = pickle.load(file)

with open('models/Usa-price1.pkl', 'rb') as file:
    new_model = pickle.load(file)

with open('models/Usa_label1.pkl', 'rb') as file:
    Us_encoder = pickle.load(file)

@app.route('/', methods=['GET', 'POST'])
def home():
    locations = house_encoder.classes_
    prediction = None

    if request.method == 'POST':
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        size_sqft = int(request.form['size_sqft'])
        location = request.form['location']
        
        location_encoded = house_encoder.transform([location])[0]
        features = [[bedrooms, bathrooms, size_sqft, location_encoded]]
        prediction = round(house_model.predict(features)[0],2)
        return render_template('index.html',features=features, locations=locations, prediction=prediction)



    return render_template('index.html', locations=locations, prediction=prediction)

@app.route('/usa', methods=['GET', 'POST'])
def new():
    prediction = None
    us_loc = Us_encoder.classes_

    if request.method == 'POST':
        bedrooms = int(request.form['bedrooms'])
        bathrooms = int(request.form['bathrooms'])
        sqft_living = int(request.form['sqft_living'])
        sqft_lot = int(request.form['sqft_lot'])
        floors = int(request.form['floors'])
        waterfront = int(request.form['waterfront'])
        view = int(request.form['view'])
        condition = int(request.form['condition'])
        sqft_above = int(request.form['sqft_above'])
        sqft_basement = int(request.form['sqft_basement'])
        yr_built = int(request.form['yr_built'])
        yr_renovated = int(request.form['yr_renovated'])
        city = request.form['city']
        statezip = int(request.form['statezip'])

        city_encoded = Us_encoder.transform([city])[0]
        features = [[bedrooms, bathrooms, sqft_living, sqft_lot, floors, waterfront, view, condition, sqft_above, sqft_basement, yr_built, yr_renovated, city_encoded, statezip]]
        prediction = round(new_model.predict(features)[0],2)
        return render_template('usa.html',locs=us_loc,features=features, bedrooms=bedrooms, bathrooms=bathrooms, sqft_living=sqft_living, sqft_lot=sqft_lot, floors=floors, waterfront=waterfront, view=view, condition=condition, sqft_above=sqft_above, sqft_basement=sqft_basement, yr_built=yr_built,  yr_renovated=yr_renovated, city=city, statezip=statezip, prediction=prediction)
    else:
        return render_template('usa.html', locs=us_loc,prediction=prediction)

if __name__ == '__main__':
    app.run(debug=True)
