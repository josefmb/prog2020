from config import *
from models import Time, Tecnico, Instituicao

@app.route("/")
def inicar():
    return 'Sistema de cadastro de times. '+\
        '<a href="/listar_times">Operação listar</a>'

@app.route("/listar_times")
def listar_times():
    times = db.session.query(Time).all()

    times_em_json = [ x.json() for x in times ]
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

@app.route("/excluir_time/<int:idTime>", methods = ["DELETE"])
def excluir_time(idTime):
    resposta = jsonify({"resultado": "ok", "detalhes": "ok"})

    try:
        Time.query.filter(Time.id == idTime).delete()
        db.session.commit()
    except Exception as e:
        resposta = jsonify({"resultado": "erro", "detalhes": str(e)})

    resposta.headers.add("Access-Control-Allow-Origin", "*")
    return resposta

@app.route("/listar_tecnicos")
def listar_tecnicos():
    tecnicos = db.session.query(Tecnico).all()

    tecnicos_em_json = [ x.json() for x in tecnicos ]
    lista_em_json = jsonify(tecnicos_em_json)
    lista_em_json.headers.add("Access-Control-Allow-Origin", "*")
    return lista_em_json

@app.route("/listar_instituicoes")
def listar_instituicoes():
    instituicoes = db.session.query(Instituicao).all()

    instituicoes_em_json = [ x.json() for x in instituicoes ]
    lista_em_json = jsonify(instituicoes_em_json)
    lista_em_json.headers.add("Access-Control-Allow-Origin", "*")
    return lista_em_json


app.run(debug=True)