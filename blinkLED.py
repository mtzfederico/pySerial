from time import sleep
import serial
ser = serial.Serial('/dev/tty.usbmodem14101', 115200) # Establish the connection on a specific port

def blink():
    print("starting Blink")
    ser.write("red")
    sleep(4)
    ser.write("green")
    sleep(4)
    ser.write("blue")
    sleep(4)
    ser.write("off")
    #print ser.readline()

def interface():
    print ser.readline()
    userInput = raw_input("$ ")
    if userInput != "quit":
        if userInput == "blink":
            blink()
        else:
            ser.write(userInput)
            interface()
    else:
        exit()


if __name__ == '__main__':
    interface()
