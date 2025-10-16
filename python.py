import os 
os.system("cls")

def desconto_inss(salario):
    if salario >=0 and salario <= 1.518:
        desconto = (salario * 76.0) - (salario)
        print(f"desconto: {desconto}")
        return desconto
    
    elif salario > 1.518 and salario <=2.793:
        desconto = (salario * 0.09) - (salario)
        print(f"desconto: {desconto}")
        return desconto
    
    elif salario >2.793 and salario <= 4.190:
        desconto = (salario * 0.12) - (salario)
        print(f"desconto: {desconto}")
        return desconto
    
    elif salario > 4.190 and salario <= 8.157:
        desconto = (salario * 0.14) - (salario)
        print(f"desconto: {desconto}")
        return desconto
    else:
        print("digite outro salario")


        
       

def desconto_irrf(salario):
    if salario >= 0 and salario <= 2.428:
        print("isento")
        
    elif salario > 2.428 and salario <=2.826:
        desconto = (salario * 76.0) - (salario)
        print(f"desconto: {desconto}")
        return desconto
    
    elif salario > 2.826 and salario <= 3.751:
        desconto = (salario * 0.15) - (salario)
        print(f"desconto: {desconto}")
        return desconto
    
    elif salario > 3.751 and salario <= 4.664:
        desconto = (salario * 0.22,5) - (salario)
        print(f"desconto: {desconto}")
        return desconto
    
    elif salario > 4.664:
        desconto = (salario * 27.5) - (salario)
        print(f"desconto: {desconto}")
        return desconto
    
def vale_transporte(salario):
    resposta_vt = input("deseja o vale transporte? \nuse s ou n para responder: ").lower()
    if resposta_vt == "s":
        desconto = (salario * 0.06) - (salario)
        print(f"desconto: {desconto}")
        return desconto
    else:
        print(f"nao deseja o vale transporte")

def vale_refeicao(salario):
    resposta_vr = input("deseja o vale refeicao? \nuse s ou n para responder: ").lower()
    if resposta_vr == "s":
        desconto = (salario * 0.20) - (salario)
        print(f"desconto: {desconto}")
        return desconto
    else:
        print("nao deseja o vale refeiçao")

def desconto_plano_s(salario):
    dependentes = int(input("digite a quantidade de dependentes: "))
    if dependentes > 0:
        dependentes +=1 
        desconto = (salario - 150.00)
        return desconto

salario = float(input("digte o seu salario: "))

desconto_inss(salario)
desconto_irrf(salario)
vale_transporte(salario)
vale_refeicao(salario)
desconto_plano_s(salario)