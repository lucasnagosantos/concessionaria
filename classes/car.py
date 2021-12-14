from typing import Dict, List
import mysql.connector


class Car:
    def __init__(self, carName="", brand="", year="", value="", carType="", imgPath=""):
        self.carName = carName
        self.brand = brand
        self.year = year
        self.value = value
        self.carType = carType
        self.imgPath = imgPath
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="dealership"
        )
    
    def createCar(self):
        cursor = self.conn.cursor()
        sql = "INSERT INTO car (name, brand, value, carYear, carType, imgPath) \
               VALUES(%s, %s, %s, %s, %s, %s)"
        val = (self.carName, self.brand, self.value, self.year, self.carType, self.imgPath)
        cursor.execute(sql, val)
        self.conn.commit()
        return "Car Inserted"
        
    def readCar(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM car")
        myresult = cursor.fetchall()
            
        return myresult

        
    def deleteCar(self):
        cursor = self.conn.cursor()
        sql = "DELETE FROM car WHERE name = %s"
        val = (self.carName)
        cursor.execute(sql, val)
        self.conn.commit()
        print(cursor.rowcount, "record(s) deleted")
        
if __name__ == '__main__':
    newCar = Car("model s", "tesla", 2012, "new")
    newCar.createCar()
        
        

        