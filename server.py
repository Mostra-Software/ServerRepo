from flask import Flask
import subprocess

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/postStart/", methods=['GET', 'POST'])
def post_start():
   print("test")
   return "start"
    

@app.route("/postStop/", methods=['GET', 'POST'])
def post_stop():
    return "Stop"

@app.route("/postredLight/", methods=['GET', 'POST'])
def post_redLight():

    # Python dosyasını çalıştırmak için subprocess kullanımı
    try:
        subprocess.run(["python", "C:/Users/berka/Desktop/Server/deneme.py"])
        return "redLight"
    except Exception as e:
        print("Error:", str(e))
        return "Error"

if __name__ == '__main__':
    # Uygulamayı 0.0.0.0 adresine yayınla ve portu belirt
    app.run(host='0.0.0.0', port=5000, debug=True)
