#Cassio Valezzi - RM551059
#Gustavo Kenzo - RM98481
#Ian Cancian - RM98387
#Henri de Olveira - RM98347
#Vitor Shimizu - RM550390

feedbackData = {
    "Login": {"alunos": [], "professores": []},
    "Envio de Trabalho": {"alunos": [], "professores": []},
    "Correção Automática": {"alunos": [], "professores": []}
}

def criarMvp():
    print("MVP criado com funcionalidades essenciais.")
    funcionalidades = list(feedbackData.keys())
    print("Funcionalidades disponíveis no MVP: ", funcionalidades)
    return funcionalidades

def coletarFeedback(funcionalidade, usuario, feedback):
    feedbackData[funcionalidade][usuario].append(feedback)
    print(f"Feedback recebido de {usuario} sobre {funcionalidade}: {feedback}")

def desenvolverProdutoFinal():
    print("Desenvolvendo o produto final com base no feedback.")
    for funcionalidade, feedbacks in feedbackData.items():
        print(f"Feedback sobre {funcionalidade}:")
        for usuario, listaFeedback in feedbacks.items():
            print(f"  {usuario.capitalize()}: {listaFeedback}")
    print("Produto final desenvolvido com novas funcionalidades baseadas no feedback.")

def entregaFinal():
    print("Produto final entregue com todas as funcionalidades e ajustes feitos.")
    return "Entrega concluída"

def fluxoCompleto():
    funcionalidadesMvp = criarMvp()
    
    coletarFeedback("Login", "alunos", "Gostei da interface, mas o login está lento.")
    coletarFeedback("Correção Automática", "professores", "A correção automática precisa de mais opções.")
    coletarFeedback("Envio de Trabalho", "alunos", "Fácil de usar, mas seria bom ter confirmação de envio.")
    
    desenvolverProdutoFinal()
    
    resultado = entregaFinal()
    print(resultado)

fluxoCompleto()
