import numpy

def min(a,b,c):
    if a<=b and a<=c:
        return a
    if b<=a and b<=c:
        return b
    if c<=a and c<=b:
        return c

def max(a,b):
    if(a<b):
        return b
    else:
        return a

def normalize(x,size):
    if len(x)<size:
        fark=size-len(x)
        for i in range(fark):
            x=x+" "
    return x

def LevenshteinMesafesi(a,b):
    k=numpy.zeros((len(a)+1,len(b)+1))
    a_len=len(a)
    b_len=len(b)
    for i in range(a_len):
        k[i][0]=i
    for i in range(b_len):
        k[0][i]=i
    silme=0
    ekleme=0
    yerdegistirme=0
    for i in range(1,a_len+1):
        for j in range(1,b_len+1):
            if a[i-1]==b[j-1]:
                k[i][j]=k[i-1][j-1]
            else:
                silme=k[i-1][j]+1
                ekleme=k[i][j-1]+1
                yerdegistirme=k[i-1][j-1]+1
                k[i][j]=min(silme,ekleme,yerdegistirme)
    return k[b_len-1][a_len-1]


print("1.kelime giriniz:")
kelime1=input()
print("2.kelime giriniz:")
kelime2=input()
max_len=max(len(kelime1),len(kelime2))

kelime1=normalize(kelime1, max_len)
kelime2=normalize(kelime2, max_len)
mesafe=LevenshteinMesafesi(kelime1, kelime2)

print(kelime1+" "+kelime2 +" arasındaki Levenshtein Mesafesi:")
print(mesafe)
benzerlikOranı=(max_len-mesafe)/max_len
print(benzerlikOranı)






