from config import *

class Tecnico(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))

    contrato = db.relationship("Time", back_populates="tecnico")

    def __str__(self):
        return str(self.id)+") "+ self.nome

    #Método que transforma a classe em json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
        }


class Auxiliar(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))

    contrato = db.relationship("Time", back_populates="auxiliar")

    def __str__(self):
        return str(self.id)+") "+ self.nome

    #Método que transforma a classe em json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
        }

class Time(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    esporte = db.Column(db.String(254))

    tecnico_id = db.Column(db.ForeignKey(Tecnico.id), nullable=False)
    tecnico = db.relationship("Tecnico", back_populates="contrato")

    auxiliar_id = db.Column(db.ForeignKey(Auxiliar.id), nullable=False)
    auxiliar = db.relationship("Auxiliar", back_populates="contrato")
    #Método para expressar o time em formto texto
    
    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " + self.esporte

    #Método que transforma a classe em json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "esporte": self.esporte,
            "tecnico_id": self.tecnico_id,
            "tecnico": self.tecnico,
            "auxiliar_id": self.auxiliar_id,
            "auxiliar": self.auxiliar
        }


#teste    
if __name__ == "__main__":
    #apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    tecnico = Tecnico(nome = "Hans-Dieter Flick")
    auxiliar_tecnico = Auxiliar(nome = "Tite")
    time = Time(nome = "FC Bayern München", esporte = "Futebol", tecnico = tecnico, auxiliar = auxiliar_tecnico)  

    # persistir
    db.session.add(tecnico)
    db.session.add(auxiliar_tecnico)
    db.session.add(time)
    db.session.commit()

    # exibir no format json
    print(auxiliar_tecnico)
    print(auxiliar_tecnico.json())
    print(tecnico)
    print(tecnico.json())
    print(time)
    print(time.json())