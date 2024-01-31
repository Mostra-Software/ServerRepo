from flask import Flask

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/postStart/", methods=['GET', 'POST'])
def post_start():
    return "Start"

@app.route("/postStop/", methods=['GET', 'POST'])
def post_stop():
    return "Stop"

if __name__ == '__main__':
    # Uygulamayı 0.0.0.0 adresine yayınla ve portu belirt
    app.run(host='0.0.0.0', port=5000, debug=True)
