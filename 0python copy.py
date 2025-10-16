import os 
os.system("cls")

def desconto_inss(salario):
    if salario >=0 and salario <= 1518.00:
        salario_com_desconto = (salario * 76.0 - salario)
        print(f"salario_com_desconto: {salario_com_desconto}")
        return salario_com_desconto
    
    elif salario > 1518.00 and salario <=2793.00:
        salario_com_desconto = (salario * 0.09) - (salario)
        print(f"salario_com_desconto: {salario_com_desconto}")
        return salario_com_desconto
    
    elif salario >2793.00 and salario <= 4190.00:
        salario_com_desconto = (salario * 0.12) - (salario)
        print(f"salario_com_desconto: {salario_com_desconto}")
        return salario_com_desconto
    
    elif salario > 4190.00 and salario <= 8157.00:
        salario_com_desconto = (salario) * 0.14 - (salario)
        print(f"salario_com_desconto: {salario_com_desconto}")
        return salario_com_desconto
    else:
        print("digite outro salario")

def desconto_irrf(salario):
    if salario >= 0 and salario <= 2428.00:
        print("isento")
        
    elif salario > 2428.00 and salario <=2826.00:
        salario_com_desconto = (salario * 76.0) - (salario)
        print(f"salario_com_desconto: {salario_com_desconto}")
        return salario_com_desconto
    
    elif salario > 2826.00 and salario <= 3751.00:
        salario_com_desconto = (salario * 0.15) - (salario)
        print(f"salario_com_desconto: {salario_com_desconto}")
        return salario_com_desconto
    
    elif salario > 3751.00 and salario <= 4664.00:
        salario_com_desconto = (salario * 0.22,5) - (salario)
        print(f"salario_com_desconto: {salario_com_desconto}")
        return salario_com_desconto
    
    elif salario > 4664.00:
        salario_com_desconto = (salario * 27.5) - (salario)
        print(f"salario_com_desconto: {salario_com_desconto}")
        return salario_com_desconto

salario = float(input("digte o seu salario: "))











