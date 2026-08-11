from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Aplicación desplegada con AWS CI/CD"

app.run(host="0.0.0.0", port=5000)
