# Criar um jogo de aventura com finais diferentes
# baseados nas respostas.

# Qual o cenário: Estou em uma guerra entre duas nações, e nós temos 2 lados: LadoA e LadoB. Somente o LadoA irá vencer, e o LadoB irá
# perder. então eu tenho que tomar decisões corretas para chegar a vitória, que somente o LadoA irá conseguir.

class JogoDeAventura:
    def __init__(self):
        self.pergunta1 = 'Você nasceu no Norte ou no Sul? (n/s)' # norte = LadoA - sul = LadoB
        self.pergunta2 = 'Você prefere a espada ou o escudo? (espada/escudo)' # espada = lado1 - escudo = lado2
        self.pergunta3 = 'Qual é a sua especialidade? (linha de frente/tático)' # linha de frente = lado1 - tático = lado2
        self.finalHistoria1 = 'Você será um heroi na linha de frente.'
        self.finalHistoria2 = 'Você será um heroi protegendo as nossas tropas.'
        self.finalHistoria3 = 'Você ir[a se sacrificar na batalha.'
        self.finalHistoria4 = 'Você não é capaz de lutar nessa batalha.'
        
    def Iniciar(self):
        resposta1 = input(self.pergunta1)
        if resposta1 == 'n':
            resposta1B = input(self.pergunta2)
            if resposta1B == 'espada':
                print(self.finalHistoria1)
            if resposta1B == 'escudo':
                print(self.finalHistoria2)
        if resposta1 == 's':
            resposta1B = input(self.pergunta3)
            if resposta1B == 'linha de frente':
                print(self.finalHistoria3)
            if resposta1B == 'tático':
                print(self.finalHistoria4)
                
        
jogo = JogoDeAventura()
jogo.Iniciar()