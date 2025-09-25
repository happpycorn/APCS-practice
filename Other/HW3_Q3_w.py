n = int(input())
goodkeyword = ['good', 'best', 'awesome', 'excellent', 'wonderful']
badkeyword = ['bad', 'worst', 'stupid', 'shame']
alist = []
for i in range(n):
    list = input().lower()\
        .replace('.', ' ').replace(',', ' ')\
            .replace(':', ' ').replace(';', ' ')\
                .replace('?', ' ').replace('!', ' ')\
                    .replace('\'', ' ').replace('\"', ' ')\
                        .replace('-', ' ').split()
    aws = 0
    for word in list:
        for key in goodkeyword:
            if word == key:
                aws += 1
        for key in badkeyword:
            if word == key:
                aws -= 1
        
    alist.append(aws)
blist = ','.join(str(k) for k in alist)
print(blist)

#.,:;?!'"-