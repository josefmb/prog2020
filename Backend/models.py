from config import *

class Time(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String(254))
    esporte = db.Column(db.String(254))
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

#teste    
if __name__ == "__main__":
    #apagar o arquivo, se houver
    if os.path.exists(arquivobd):
        os.remove(arquivobd)

    # criar tabelas
    db.create_all()

    # teste da classe Pessoa
    t1 = Time(nome = "FC Bayern München", esporte = "Futebol")
    t2 = Time(nome = "CR Flamengo", esporte = "Futebol")        

    # persistir
    db.session.add(t1)
    db.session.add(t2)
    db.session.commit()
    
    # exibir a pessoa
    print(t1)
    print(t2)

    # exibir a pessoa no format json
    print(t1.json())
    print(t2.json())