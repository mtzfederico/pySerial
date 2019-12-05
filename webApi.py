#https://programminghistorian.org/en/lessons/creating-apis-with-python-and-flask
import time
from flask import Flask, render_template, request
import serial
ser = serial.Serial('/dev/tty.usbmodem14301', 115200) # Establish the connection on a specific port
app = Flask(__name__)

@app.route("/") #This part is supposed to print an html file, but it doesn't work
def index():
    return "<p>Arduino pySerial API</p>"
    #return render_template('/index.html') #This part is supposed to print an html file, but it doesn't work
@app.route("/<deviceName>/")
def action(deviceName):
    if deviceName == 'red':
        ser.write("red")
        return "<p>red led on</p>"
    if deviceName == 'green':
        ser.write("green")
        return "<p>green led on</p>"
    if deviceName == 'blue':
        ser.write("blue")
        return "<p>blue led on</p>"
    if deviceName == 'off':
        ser.write("off")
        return "<p>led off</p>"
    #return render_template('/index.html')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=False)
