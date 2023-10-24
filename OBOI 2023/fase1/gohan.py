n = int(input())

notas = [[int(i) for i in input().split()] for _ in range(n)] 


NotaPedro = 0 
NotaHassum = 0 


for nota in notas:
    # print(nota)
    NotaPedro +=nota[0] # Notass de Pedro
    NotaHassum += nota[1]# nota de hassum
        


if NotaPedro < NotaHassum:
    print(":0 <- Gohan e Feijao")
elif NotaPedro == NotaHassum:
    print("Impasse")
else:
    print(":0 <-X- Gohan e Feijao")
    



