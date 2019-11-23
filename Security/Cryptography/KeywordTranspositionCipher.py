# Enter your code here. Read input from STDIN. Print output to STDOUT
from string import ascii_uppercase as lol

def dec(k,m):
    cipherkey = ''.join([x for i,x in enumerate(k) if k.index(x)==i])
    letter = ''.join([x for x in lol if x not in cipherkey])
    decoder = cipherkey + letter
    columns = sorted([''.join([decoder[x] for x in
                               range(n,len(decoder),len(cipherkey))])
                      for n in range(len(cipherkey))])
    d = {a:b for b,a in zip(lol,''.join(columns))}
    return ''.join( d[x] if x in d else ' ' for x in m)    
    
for _ in range(int(input())):
    cipherkey = input()
    message = input() 
    
    print(dec(cipherkey,message))
