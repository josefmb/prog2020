from config import *
from time import Time

@app.route("/")
def inicar():
    return 'Sistema de cadastro de times. '+\
        '<a href="/listar_pessoas">Operação listar</a>'

@app.route("/listar_times")
def listar_times():
    times = db.session.query(Time).all()
    # aplicar o método json que a classe Time possui a cada elemento da lista
    times_em_json = [ x.json() for x in pessoas ]
    # fornecer a lista de times em formato json
    return jsonify(times_em_json)

app.run(debug=True)