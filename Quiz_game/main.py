from data import question_data

class Perguntas:
    def __init__(self,texto,resposta) -> None:
        self.text = texto
        self.ansewr = resposta


class QuizBrain:
    def __init__(self,q_lista):
      self.numero_de_perguntas = 0
      self.pergunta_da_lista = q_lista
    
    def proxima_pergunta(self):
        peruntas = self.pergunta_da_lista[self.numero_de_perguntas]
        self.numero_de_perguntas += 1
        print(f"Questao {self.numero_de_perguntas} : {peruntas.text} (True/False): ")





banco_de_perguntas = []
for dict in question_data:
    auxiliar1 = dict["text"]
    auxiliar2 = dict["answer"]
    novas_perguntas = Perguntas(auxiliar1,auxiliar2)
    banco_de_perguntas.append(novas_perguntas)

quiz = QuizBrain(banco_de_perguntas)
quiz.proxima_pergunta()
