import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "¡Hola! La aplicación Flask está funcionando."

if __name__ == '__main__':
    # Usar el puerto que Render asigna
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)

