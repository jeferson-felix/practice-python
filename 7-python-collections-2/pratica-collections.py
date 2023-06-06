from collections import Counter

texto1 = """
O ChatGPT é um modelo de linguagem avançado desenvolvido pela OpenAI. Ele é baseado na arquitetura GPT, que significa Generative Pre-trained Transformer, em inglês.

Baseado na arquitetura GPT-3.5, foi treinado em uma grande quantidade de dados textuais para gerar respostas relevantes e coerentes em uma ampla variedade de tópicos. Ele é projetado para conversar e interagir com pessoas usuárias, fornecendo informações, esclarecendo dúvidas, oferecendo sugestões e auxiliando em várias tarefas. Ou seja, o chat tem a capacidade de gerar respostas em linguagem natural, de forma similar a uma conversa.

De maneira breve, a relevância do ChatGPT, no campo da Inteligência Artificial, reside na sua capacidade de compreender e responder a perguntas, além de fornecer informações e realizar tarefas baseadas em texto de maneira eficiente. Ele utiliza técnicas de aprendizado de máquina – Machine Learning – e foi treinado em uma ampla variedade de dados, o que inclui textos da web, conferindo uma compreensão razoável da linguagem humana.
"""

texto2 = """
O Trello é uma ferramenta que oferece um plano gratuito para organizar desde nossas tarefas pessoais até demandas coletivas de uma equipe. Ele possibilita que criemos quadros com listas e adicionemos nelas cartões – ou cards, como costumamos dizer no dia a dia – com itens e tarefas, que são úteis para organizar times e atividades específicas para um determinado conjunto de pessoas.

Esta divisão contribui para a gestão visual, facilitando o acompanhamento das tarefas por meio de cards móveis que contêm a descrição de cada atividade e de evolução de projeto.

Assim, se um membro do time de Maria escolher uma atividade para fazer, esta pessoa deve mover o card, seguindo o fluxo de trabalho utilizado no Kanban.

O card inicia na coluna Backlog, e, à medida que é atualizado, transita pelas colunas de A Fazer, Em Andamento e, por fim, Concluído. Essa é uma forma de acompanhar o andamento do fluxo de atividades e suas respectivas informações, como demostrado no GIF a seguir:
"""


def analisa_frequencia_de_letras(texto):
    aparicoes = Counter(texto.lower())
    total_de_caracteres = sum(aparicoes.values())

    proporcoes = [(letra, frequencia / total_de_caracteres) for letra, frequencia in aparicoes.items()]
    proporcoes = Counter(dict(proporcoes))
    mais_comuns = proporcoes.most_common(10)
    for caractere, proporcao in mais_comuns:
        print(f'{caractere} => {proporcao * 100:.2f}%')


print(analisa_frequencia_de_letras(texto1))

print(analisa_frequencia_de_letras(texto2))
