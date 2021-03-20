'''
Esse programa calcula uma equações do segundo grau
Aluno: Matheus Moreira do Nascimento
DRE: 119042060
Curso: Matemática Aplicada
Disciplina: Topicos da Matemática Aplicada A
'''
print("................................................................................\n")
print("Essa parada aqui calcula equações do segundo grau completas, do tipo ax²+bx+c")
print("Pra começar, escreva as variaveis da sua equação \n")
print("................................................................................\n")

k=True
while k:
    a=float(input('Bota ai o seu coeficiente "a" \n'))
    while (a==0):
        print("Iii meu parceiro, assim a equação não é do segundo grau")
        print("Tenta de novo ai \n")
        a=float(input('Bota ai o seu coeficiente "a" de novo \n'))

    b=float(input('Bota ai o seu coeficiente "b" \n'))

    c=float(input('Bota ai o seu coeficiente "c" \n'))

    delta=b**2-4*a*c
    if delta<0:
        print("Então meu camarada, essa equação não tem raizes reais")
        f=input("Pra calcular outra equação, digita 'sim', se quiser meter o pé, digita 'não'")
        if f==str('não'):
            k=False
        print("")
    elif delta==0:
        print("Essa sua equação ai tem só uma raiz, que é esse numerosinho ai embaixo")
        print(-b/2*a)
        f=input("Pra calcular outra equação, digita 'sim', se quiser meter o pé, digita 'não'")
        if f==str('não'):
            k=False
        print("")
    else:
        print("Essa sua equação ai tem duas raizes, que são esses numerosinho ai embaixo")
        print((-b+delta**0.5)/2*a)
        print((-b-delta**0.5)/2*a)
        f=input("Pra calcular outra equação, digita 'sim', se quiser meter o pé, digita 'não'")
        if f==str('não'):
            k=False
        print("")
    
print("")   
print("Suave")
print("É nós")

