#ex1
'''
N=int(input( "Premier entier :"))
M=int(input("Deuxième entier :"))
print("Somme:",N+M)
print("Difference:",N-M)
'''
#ex2
'''
P=int(input("Prix en euros:"))
print("Prix en dhs:",P*10.627)
'''
#ex3
'''
a=int(input("Entier a=?"))
b=int(input("Entier b=?"))
s=a+b
if s >= 100 :
    print("La somme dépasse 100")
else :
    print("la somme est",s)
'''
#ex4
'''
print("Maximum de trois entiers")
a=int(input("1er entier= "))
b=int(input("2eme entier= "))
c=int(input( "3eme entier="))
if b>a :
    Max=b
else :
    Max=a
if c>Max  :
    Max=c
print("Le maximum est : ",Max)
'''
#ex5
'''
a=int(input("Combien de \"la\" pour l'écho?"))
print("Début:\"la\"")
print("la"*a)
'''
#ex6
'''
while True :
    N=int(input("Nombre:"))
    print("Le carre de ce nombre est ",N**2)
    c=str(input("Voulez-vous recommencer? "))
    if c=='non' :
        print("au revoir")
        break
        '''

#ex7
'''
while True :
    N=int(input(' Nombre impair :'))
    if N%2!=0 :
        print('Merci')
        break
    else:
        c=str(input("J'ai demandé un nombre impair !"))
        '''

#ex8
'''
a=int(input('Numero de début:'))
b=int(input('Numero de fin:'))
z=int(input('Nombre de z:'))  
s="z"*z+"zigzag"
for i in range(a,b+1):
    if i%2==0 :
        print(f"{i}{s}")
    else :
        print(f"{s}{i}")
        '''
#ex9
'''
while True :
    n=int(input('n=?'))
    FACT=1
    if n>0 :
        for i in range(1,n+1):
            FACT*=i
        print("La factorielle de", n,"vaut", FACT)
    elif n==0:
        print("La factorielle de 0 vaut 1 ")
    else :
        print("La factorielle n'est pas définie pour les nombres négatifs")
        
       '''
#ex10
'''
while True :
    N=int(input('Nombre max de lettres ? '))
    mot=''
    for i in range(N):
        L=str(input( ' Lettre : '))
        if L.lower()=='stop':
            break
        mot+=L
    
    print(mot)
    '''
#ex11
#a
'''
N=int(input('entrer un entier:'))
for i in range(1,N+1):
    if i <N:
        print(i,end=",")
    else :
        print(i)
        '''
#b
'''
N=int(input('entrer un entier:'))
for i in range(N,1,-1):
    print(i,end=",")
print(1)
#c
for i in range(1,N):
    if i%2!=0 :
        print(i,end=",")
        '''
#d
N=int(input('entrer un entier:'))
for i in range(N):
    for j in range(N):
        if i==j:
            print(1,end="")
        else :
            print(" ",end="")
    
   