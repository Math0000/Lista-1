'''
Esse programa calcula a soma dos multiplos dos numeros
Aluno: Matheus Moreira do Nascimento
DRE: 119042060
Curso: Matemática Aplicada
Disciplina: Topicos da Matemática Aplicada A
'''
print("............................................................................ \n")
print("Nesse programa aqui você pode calcular a soma dos multiplos de 2 numerosos que")
print("são menores que um determinado numero")
print("Pra começar, escolhe ai os numeros que tu quer calcular a soma dos multiplos e"
print("o numero que restringe o valor deles superiormente")
print("............................................................................ \n")

k=True
while True:
    print("")
    a=int(input('Fala um dos numeros que você vai buscar os multiplos \n'))
    b=int(input('Fala o outro ai também \n'))    
    c=int(input('Os multiplos tem que ser menor que qual numero? \n'))
    
    d=0
    e=0
    
    f=1
    g=1
    
    z=0
    
    while d<c:
       z+=d
       d=f*a
       f+=1
       
    while e<c:
        z+=e
        e=g*b
        g+=1
    
    print("A soma de todos os multiplos de ",a," e ",b," menores que ",c," é:")    
    print("................................................................. ")
    print(z)
    print("................................................................. \n")
    print("Se tu quiser calcular com outros numeros ou com outra restrição")
    f=str(input("digita 'sim', se não quiser, digita 'não'"))
    if f!=str('sim'):
        k=False
    print("")
    
print("")   
print("Suave")
print("É nós")
