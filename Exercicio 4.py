'''
Esse programa calcula a distância entre sua localização e os postos
Aluno: Matheus Moreira do Nascimento
DRE: 119042060
Curso: Matemática Aplicada
Disciplina: Topicos da Matemática Aplicada A
'''
print("............................................................................ \n")
print("Com esse bagulho aqui você pode ver quantos postos em um raio de X km")
print("existem perto de você \n")
print("Pra começar, escreve a sua localização como se fossem coordenadas de um")
print("plano cartesiano (x,y) de 50x50 \n")
print("............................................................................ \n")

P1x=1
P1y=2
      
P2x=10
P2y=7

P3x=35
P3y=15

P4x=43
P4y=12

P5x=9
P5y=27

P6x=4
P6y=32

P7x=41
P7y=28

P8x=15
P8y=25

P9x=4
P9y=37

P10x=23
P10y=44

P11x=27
P11y=48

P12x=12
P12y=14

P13x=8
P13y=35

k=True
while k:
    T=[]    
    print("Escreve ai a coordenada x da sua localização")
    a=float(input("Lembrando que 0 < x < 50 "))
    print("")

    print("Agora escreve a coordenanda y também ")
    b=float(input("Lembrando que 0 < y < 50 "))
    print("")
    
    r=float(input("Em que raio em Km você quer checar se existem postos? "))
    print("")
    if ((P1x-a)**2+(P1y-b)**2<=r**2):
        T .append(str("Posto 1"))

    if ((P2x-a)**2+(P2y-b)**2<=r**2):
        T .append(str("Posto 2"))

    if ((P3x-a)**2+(P3y-b)**2<=r**2):
        T .append(str("Posto 3"))   
 
    if ((P4x-a)**2+(P4y-b)**2<=r**2):
        T .append(str("Posto 4"))

    if ((P5x-a)**2+(P5y-b)**2<=r**2):
        T .append(str("Posto 5"))

    if ((P6x-a)**2+(P6y-b)**2<=r**2):
        T .append(str("Posto 6"))

    if ((P7x-a)**2+(P7y-b)**2<=r**2):
        T .append(str("Posto 7"))

    if ((P8x-a)**2+(P8y-b)**2<=r**2):
        T .append(str("Posto 8"))

    if ((P9x-a)**2+(P9y-b)**2<=r**2):
        T .append(str("Posto 9"))

    if ((P10x-a)**2+(P10y-b)**2<=r**2):
        T .append(str("Posto 10"))

    if ((P11x-a)**2+(P11y-b)**2<=r**2):
        T .append(str("Posto 11"))

    if ((P12x-a)**2+(P12y-b)**2<=r**2):
        T .append(str("Posto 12"))

    if ((P13x-a)**2+(P13y-b)**2<=r**2):
        T .append(str("Posto 13"))

    if not T:
        print("Então brother, não tem nenhum posto num raio de",r,"km de você")
        print("")
        
    else:
        print("")
        print("Os postos que estão num raio de",r,"km de você são:")
        print(T)
        print("")

    print("Se quiser calcular com outra posição ou outro raio")
    e=input("digita 'sim', se quiser meter o pé, digita 'não'")
    if e==str('não'):
        k=False
    print("")
    
print("")   
print("Suave")
print("É nós")
    

