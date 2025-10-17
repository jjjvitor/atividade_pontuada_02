import os 


mat = str(input("digite a mariculado funcionario:\n"))
os.system("cls")
sen = str(input("digite senha:\n"))
os.system("cls")
sal = str(input("digite a base salarial do funcionario:\n"))
os.system("cls")
v_t = str(input("deseja receber vale tranporte (s ou n):\n"))
os.system("cls")
v_r = str(input("digite o valor do vale refeicao:\n"))
os.system("cls")
q_d= str(input("digite a quantidade de dependentes do funcionario:\n"))
os.system("cls")

def inss(sal):
    if sal >= 8157.69:
        sal_inss = 951.62
    elif sal <= 8157.69 and sal >= 4190.84:
        sal_inss = (sal * 0.14)
    elif sal <= 4190.83 and sal >= 2793.89:
        sal_inss = (sal * 0.12)
    elif sal <= 2793.88 and sal >= 1518.01:
        sal_inss = (sal * 0.09)
    else:
        sal_inss = (sal * 0.075)
    return sal_inss
    
def irrf (sal):
    if sal >= 4664.69:
        sal_irrf = (sal * 0.275)
    elif sal <= 4664.68 and sal >= 3751.06:
        sal_irrf = (sal * 0.225)
    elif sal <= 3751.05 and sal >= 2826.66:
        sal_irrf = (sal * 0.15)
    elif sal <= 2826.65 and sal >= 2259.21:
        sal_irrf = (sal * 0.075)
    else:
        sal_irrf = 0
    return sal_irrf

def valetrans (sal.v_t):
    if v_t == "s":
        vvalet = (sal * 0.06)
    else:
        vvalet = 0
    return vvalet

def vale_ref (v_r):
    v_rpf = v_r * 0.2
    return v_rpf

def p_s (q_d):
    planosaude = (q_d * 150)
    return planosaude

def resposta
(sal, sal_inss, sal_irrf, vvalet,
v_rpf, planosaude, q_d, v_r):

sal_liquido = sal-(sal_inss+sal_
irrf+vvalet+v_rpf+planosaude)
print("""salario
base/bruto(R$):\t dependentes:\tvale
transporte:/tinss(R$):\tirrf(R$):\tvalor
do vale refeicao(R$):\tvalor do plano de saude(R$):\talario liquido(R$):
\t{sal:.2f}\t\t{q_d}\t\t{vvale
t:.2f}\t\t\t{sal_inss:.2f}\t\
t{sal_irrf:.2f}\t\t\t{v_r:.2f}
\t\t\t\t{planosaude:.2f}\t\t\
t{sal_liquido:.2f}
        """)

a= {mat}
print(f"matricula do funcionario: {a}")

