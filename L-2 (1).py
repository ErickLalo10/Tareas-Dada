bas = 5
space = bas - 1
conta = 1

for x in range(bas):

    while space >=0:

        print ('%s%s%s'%((' '*space), ('*'*conta),(' '*space)))

        space -=1
        conta +=2