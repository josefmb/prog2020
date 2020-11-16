from config import *

class Tecnico(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))

    contrato_tecnico = db.relationship("Instituicao", back_populates="tecnico")

    def __str__(self):
        return str(self.id)+") "+ self.nome

    #Método que transforma a classe em json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome
        }

class Time(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    esporte = db.Column(db.String(254))

    pertence = db.relationship("Instituicao", back_populates="time")

    #Método para expressar o time em formto texto

    def __str__(self):
        return str(self.id)+") "+ self.nome + ", " + self.esporte

    #Método que transforma a classe em json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "esporte": self.esporte
        }

class Instituicao(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))

    tecnico_id = db.Column(db.ForeignKey(Tecnico.id), nullable=False)
    tecnico = db.relationship("Tecnico", back_populates="contrato_tecnico")

    time_id = db.Column(db.ForeignKey(Time.id), nullable=False)
    time = db.relationship("Time", back_populates="pertence")

    def __str__(self):
        return f"{self.id}) {self.nome}; {self.tecnico}; {self.time}"

    #Método que transforma a classe em json
    def json(self):
        return {
            "id": self.id,
            "nome": self.nome,
            "tecnico_id": self.tecnico_id,
            "tecnico": self.tecnico,
            "time_id": self.time_id,
            "time": self.time
        }

#teste    
if __name__ == "__main__":
    #apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    tecnico = Tecnico(nome = "Hans-Dieter Flick")
    db.session.add(tecnico)

    time = Time(nome = "Flamengo", esporte="Futebol")
    db.session.add(time)

    instituicao = Instituicao(nome = "Flamengo", tecnico = tecnico, time = time)  
    db.session.add(instituicao)

    db.session.commit()

    # exibir no format json
    print(time)
    print(time.json())
    print(tecnico)
    print(tecnico.json())
    print(instituicao)
    print(instituicao.json())