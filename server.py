from flask import Flask, request
import subprocess

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/postStart/", methods=['GET', 'POST'])
def post_start():
   print("start")
   return "start"
    

@app.route("/postStop/", methods=['GET', 'POST'])
def post_stop():
    return "Stop"

@app.route("/postredLight/", methods=['GET', 'POST'])
def post_redLight():

    # Python dosyasını çalıştırmak için subprocess kullanımı
    try:
        subprocess.run(["python", "C:/Users/berka/Desktop/Server/deneme.py"])
        return "redLight python file worked"
    except Exception as e:
        print("Error:", str(e))
        return "Error"
    
@app.route("/postgreenLight/", methods=['GET', 'POST'])
def post_greenLight():
    return "Green Light"

@app.route("/postCoordinates/", methods=['POST'])
def post_sendCoordinates():
    try:
        data = request.json
        coordinates = data.get('coordinates')
        print("Received coordinates:", coordinates)
        coordinates_list = coordinates.split()
        print("Received coordinates:", coordinates_list)
        print(len(coordinates_list))
        return "Coordinates received"
    except Exception as e:
        print("Error:", str(e))
        return "Error"

if __name__ == '__main__':
    # Uygulamayı 0.0.0.0 adresine yayınla ve portu belirt
    app.run(host='0.0.0.0', port=5000, debug=True)
