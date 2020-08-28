from config import *
from models import Time

@app.route("/")
def inicar():
    return 'Sistema de cadastro de times. '+\
        '<a href="/listar_times">Operação listar</a>'

@app.route("/listar_times")
def listar_times():
    times = db.session.query(Time).all()
    # aplicar o método json que a classe Time possui a cada elemento da lista
    times_em_json = [ x.json() for x in times ]
    # fornecer a lista de times em formato json
    lista_em_json = jsonify(times_em_json)
    lista_em_json.headers.add("Access-Control-Allow-Origin", "*")
    return lista_em_json

@app.route("/incluir_times", methods = ["POST"])
def incluir_times():
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})
    dados = request.get_json()
    try:
        novo = Time(**dados)
        db.session.add(novo)
        db.session.commit()

    except Exception as e:
        resposta = jsonify({"resultado":"erro", "detalhes":str(e)})
    
    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

app.run(debug=True)