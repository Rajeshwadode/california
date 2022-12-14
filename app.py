from  flask import Flask,render_template,request
from function import california
import mysql.connector
app=Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def user():
    data=request.form
    
    
    longitude=float(data["longitude"])
    latitude=float(data["latitude"])
    housing_median_age=float(data["housing_median_age"])
    total_rooms=float(data["total_rooms"])
    total_bedrooms=float(data["total_bedrooms"])
    population=float(data["population"])
    households=float(data["households"])
    median_income=float(data["median_income"])
    ocean_proximity=(data["ocean_proximity"])
    
   
    
    price=california(longitude, latitude,housing_median_age, total_rooms, total_bedrooms, population, households, median_income, ocean_proximity)
    house_price=price.predict()
    print(house_price)
    
    conn = mysql.connector.connect( host= 'localhost',
                                    database = 'california',
                                    user= 'root',
                                    password = 'jaymauli')

    cursor = conn.cursor()

    query = "INSERT INTO house(longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income,ocean_proximity,house_price) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
    data = (longitude,latitude,housing_median_age,total_rooms,total_bedrooms,population,households,median_income,ocean_proximity,house_price)

    cursor.execute(query,data)

    conn.commit()
    conn.close()
    

    return render_template("index.html",final_price=house_price)

if __name__=="__main__":
    app.run(host="0.0.0.0",port=8080 ,debug=True)
    