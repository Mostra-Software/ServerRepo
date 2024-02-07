import time

while True:
    with open('coordinates.txt', 'r') as f:
        coordinates = f.read()  # Dosyadan koordinatları oku
        print("Coordinates:", coordinates)
    time.sleep(1)  # Bir saniye bekleyin, tekrar istek yapmadan önce 
 

""" 
import requests

response = requests.get('http://10.10.24.58:5000/postCoordinates/')  # Flask sunucusunun URL'sini kullanarak GET isteği yapın
if response.status_code == 200:
    try:
        data = response  #Sunucudan gelen veriyi JSON olarak alın
        print("Server response:", data)  #Sunucudan gelen JSON veriyi yazdırın
    except ValueError as e:
        print("Error:", e)  #JSON dönüşüm hatası
else:
    print("Error:", response.status_code) """
