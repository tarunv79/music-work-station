from pygame import mixer
import winsound
import serial

PORT = 'COM4'
ser = serial.Serial(PORT)

while 1:
    data = ser.readline().strip()
    data = data.decode("ascii")
    print(data)
    if data == '0':
        winsound.PlaySound('s_1tom.wav',winsound.SND_FILENAME)
    elif data == '1':
        winsound.PlaySound('s_2tam.wav', winsound.SND_FILENAME)
    elif data == '2':
        winsound.PlaySound('s_3crash.wav', winsound.SND_FILENAME)
    elif data == '3':
        winsound.PlaySound('s_4hihat.wav', winsound.SND_FILENAME)
    elif data == '4':
        winsound.PlaySound('s_5kicks.wav', winsound.SND_FILENAME)
    elif data == '5':
        winsound.PlaySound('s_shakers.wav', winsound.SND_FILENAME)
