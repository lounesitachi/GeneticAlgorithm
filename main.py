import random

import def_adetional as dif
# data :
ville = [1, 2, 3, 4, 5]
destance_ville = [[2, 1], [3, 1], [5, 1], [1, 3], [3, 2]]
# random ville
#moyen colection
moyenes =[]
# get the PI:
list = dif.creat_PI(ville)


for i in range(10):

    print("--------------------------------------------------generation" +str(i+1)+ "-------------------------------------")
    # get the phynotype of list
    list_ph = dif.get_phyno_of(list, destance_ville)
    p1 = dif.qi_define(dif.fit(list_ph))

    # print population
    dif.print_population(p1)
    cupls = dif.select_coupls(p1, 1)
    j=0
    for i in cupls:
        j+= 1
        print("father"+str(j))
        print(i[0])
        print("mother:" +str(j))
        print(i[1])
    children = dif.mix_all_coupels(cupls, 2)
    child_n=0
    for child in children:
        print("chiled:" +str(child_n))
        print(child)
        child_n+=1
    for _ in children:
        list.append(_)
    list = dif.stay(list, destance_ville, 10)
    # points=dif.mix_one_coupel(cupls[0],2)
   # print(len(list))
    moyenes.append(dif.moyen_generation(list,destance_ville))

# write a comment to my self !! do evry think in one line ;):)
moyenes  = dif.reve(moyenes)
print("moyens of the phynotype of generations :")
print(moyenes)
dif.draw_the_graph(moyenes,len(moyenes))