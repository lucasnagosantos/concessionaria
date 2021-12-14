from flask import Flask, flash, request, render_template, jsonify
from werkzeug.utils import redirect, secure_filename
from classes.car import Car
import os

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = './static'


@app.route("/")
def dashboard():
    return render_template('dashboard.html')

@app.route("/createCar", methods=['GET', 'POST'])
def createCar():
    return render_template('createCar.html')

@app.route("/insertCar", methods=['GET', 'POST'])
def insertCar():
    if request.method == 'POST':
        file = request.files['file']
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
        
        imgPath = './static/{0}'.format(file.filename)
        carName  = request.form['name']
        carBrand = request.form['brand']
        carValue = request.form['value']
        carYear  = request.form['year']
        carType  = request.form['type'] 
        
        newCar = Car(carName, carBrand, carYear, carValue, carType, imgPath)
        newCar.createCar()
        
        return '<center>Carro registrado com sucesso<br><a href="http://127.0.0.1:5000">Voltar a dashboard</a></center>' 
    

@app.route("/readAllCars")
def readAllCars():
    newCar = Car()
    return str(newCar.readCar())


if __name__ == '__main__':
    app.run(debug=True)

