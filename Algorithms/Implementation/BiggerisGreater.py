for _ in range(int(input())):
    w = input().strip()
    n = len(w)+1
    for k in range(-2,-n,-1):
        if w[k]<w[k+1]:
            print(w[:k],end='')
            v = w[:k:-1]
            for j in range(-k-1):
                if w[k]<v[j]:
                    print(v[j]+v[:j]+w[k]+v[j+1:])
                    break
            else:
                print(v+w[k])
            break
    else:
        print('no answer')
