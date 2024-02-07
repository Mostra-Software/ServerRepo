from flask import Flask, request
import subprocess
import json

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/postStart/", methods=['GET', 'POST'])
def post_start():
    #START 
    #Main dosyasını çalıştırmak
    try:
        #subprocess.Popen("C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Python 3.12.exe C:/Users/berka/Desktop/Server/deneme.py", shell=True)
        ##Burada python 3.7 nin bilgisayarda kurulu oldugu dizin gereklidir.
       
        subprocess.run(["python", "C:/Users/berka/Desktop/Server/deneme.py"])
        return "python file worked"
    except Exception as e:
        print("Error:", str(e))
        return "Error"
    

@app.route("/postStop/", methods=['GET', 'POST'])
def post_stop():
    with open('stop.txt', 'w') as f:
        f.write("Stop")  # Koordinatları dosyaya yaz
    ##STOP  ###TXT File 
    return "Stop"

@app.route("/postredLight/", methods=['GET', 'POST'])
def post_redLight():
    return "Red Light"

    
@app.route("/postgreenLight/", methods=['GET', 'POST'])
def post_greenLight():
    return "Green Light"

@app.route("/postCoordinates/", methods=['GET','POST'])
def post_sendCoordinates():
    try:
        data = request.json
        coordinates = data.get('coordinates')

        print("Received coordinates:", coordinates)
        coordinates_list = coordinates.split()

        #print("Received coordinates:", coordinates_list)
        with open('coordinates.txt', 'w') as f:
            f.write(coordinates)  # Koordinatları dosyaya yaz

        #json_veri = json.dumps(coordinates_list)

        return data
    except Exception as e:
        print("Error:", str(e))
        return "Error"

if __name__ == '__main__':
    # Uygulamayı 0.0.0.0 adresine yayınla ve portu belirt
    app.run(host='0.0.0.0', port=5000, debug=True)
