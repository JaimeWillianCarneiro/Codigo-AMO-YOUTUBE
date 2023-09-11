a, v = map(int, input().split())
medalhasAzuis = [int(i) for i in input().split()]

medalhasVermelhas = [int(i) for i in input().split()]



medalhas = medalhasAzuis + medalhasVermelhas
medalhas = sorted(medalhas)


medalhasVermelhas = sorted(medalhasVermelhas)
medalhasAzuis = sorted(medalhasAzuis)

descartes = 0 

v-=1
a-=1

t = a + v +1





while True:
    
    if (medalhas[t] == medalhasAzuis[a] and medalhas[t-1] ==medalhasVermelhas[v]) or (medalhas[t] == medalhasVermelhas[v] and medalhas[t-1]==medalhasAzuis[a]):
        break
    
    else:
        
        descartes+=1
        
        
        if medalhas[t] == medalhasVermelhas[v]:
            v-=1
        elif medalhasAzuis[a] == medalhas[t]:
            a-=1
        
        t-=1 
            


print(descartes)