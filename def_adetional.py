import random
import math
import matplotlib.pyplot as plt
###################################################################################################################################################
#PI ;)
# Create a list of 10 lists with the same length as ville
def creat_PI(ville):
    random_lists = []
    for _ in range(10):
        random_list = random.sample(ville, len(ville))
        random_lists.append(random_list)

    return random_lists
################################################################################################################################################
#evaluation :)
# get the phynotype of list
def get_phyno_of(list,destance_ville):
    list_ph = []
    for i in list:
        list_ph.append([i, get_phyno_type(i, destance_ville)])

    return list_ph
def get_phyno_type(list, list_of_):
    count = 0
    # temp =[]
    for i in range(len(list) - 1):
        # list ==[1,2,3,4,5]
        cordonee_ville = list_of_[list[i] - 1]
        cordonee_ville_suivant = list_of_[list[i + 1] - 1]
        count = count + destance_entre_2_ville(cordonee_ville, cordonee_ville_suivant)
    return count
#chois the city that stay
####
def stay(list,destance_ville,len_ini):
    list =remove_similar_items(list)
    list_ph= get_phyno_of(list,destance_ville)
    list_ph= sort_phynotype(list_ph)
    temp=[]
    for i in range(len_ini):
        temp.append(list_ph[i][0])
    return temp
def sort_phynotype(list_ph):
    temp =[]
    for i in range(len(list_ph)):
        for j in range(len(list_ph)):
            if(list_ph[i][1]>list_ph[j][1]):
                temp=list_ph[i]
                list_ph[i]=list_ph[j]
                list_ph[j]=temp
    return list_ph

def destance_entre_2_ville(cordonee_ville, cordonee_ville_suivant):
    distance = math.sqrt(
        (cordonee_ville[0] - cordonee_ville_suivant[0]) ** 2 + (cordonee_ville[1] - cordonee_ville_suivant[1]) ** 2)
    return round(distance, 4)

# get the fitens
def fit(list):
    temp = []

    totale = 0
    for i in list:
        totale = totale + i[1]
    for i in list:
        temp1 = []
        temp1.append(i[0])
        temp1.append(i[1])
        temp1.append(round( i[1] / totale,3))
        #temp1.clear()
        temp.append(temp1)
    return temp
#get the qi
def qi_define(list):
    temp =[]
    sum =0
    for i in list :
        temp1=[]
        sum=sum+i[2]
        temp1.append(i[0])
        temp1.append(i[1])
        temp1.append(i[2])
        temp1.append(sum)
        temp.append(temp1)
    return temp
# select the parents
def select_coupls(list ,Nc):#Nc is the numbre of coupls that we want to mix :)
    temp=[]
    for i in range(Nc):
        temp.append(select_parents(list))
    return temp
def select_parents(list):
    temp=[]
    temp.append(select_parent(list))
    #list=remove_item(list,temp[0])
    temp.append(select_parent(list))
    return temp
def select_parent(list):
    t=random.random()
    temp =[]
    for i in list :
        if(t<=i[3]):
            return i
#mix (croisement)
# this fonction mix and  the parents to creat a new chiledren  and mut them
def mix_all_coupels(list,Np):
    children=[]
    for i in list :
        children.append( mix_one_coupel(i,Np))
    children =from_listssTolist(children)
    return children
def mix_one_coupel(list, Np):#Np is the nember of mix point ;)
    points= get_the_points_of_mix(list,Np)
    genne_parent=divise_the_parents(list,points)

   # print(genne_parent)
    childs = chiled_maker(genne_parent)
    childs[0],childs[1]=mut_child(childs[0],childs[1])
    return childs
# make the chiledren from the genomme of parents
def chiled_maker(genne_parent):
    chileds =[]
    chiled1=[]
    chiled2=[]
    for i in genne_parent:
        x=random.randint(0,1)
        y = 1-x
        chiled1.append(i[x])
        chiled2.append(i[y])
    chiled1= from_listsTolist(chiled1)
    chiled2 = from_listsTolist(chiled2)
    chileds.append(chiled1)
    chileds.append(chiled2)
    return chileds
def mut_child(child1,child2):
    r=random.random()
    method =random.randint(0,1)
    if r<=0.5 :
        if method==0:
            child1=method_mut1(child1)
            child2 = method_mut1(child2)
        else:
            child1,child2 =method_mut2(child1,child2,random.randint(0,len(child1)-1))
    return child1,child2
#method of mutation
def method_mut1(child):
    x=random.randint(0,len(child)-1)
    y =random.randint(0,len(child)-1)
    c=child[x]
    child[x]=child[y]
    child[y]=c

    return child
def method_mut2(child1,child2,point):
    x=random.randint(0,len(child1)-1)
    c=child1[x]
    child1[x]=child2[x]
    child2[x]=c
    return  child1,child2
#divise the genome of the  parents
def divise_the_parents(parents,points):
    div_parnts=[]
    pure_parents= []
    for i in parents:
        pure_parents.append((pure_parnt(i)))
    first_point=0
    last_point=len(pure_parents[0])
    for i in points:
        temp=[]
        temp.append(div_list_in_2_points(pure_parents[0],first_point,int(i)))
        temp.append(div_list_in_2_points(pure_parents[1], first_point, int(i)))
        div_parnts.append(temp)
        first_point=int(i)
    temp=[]
    temp.append(div_list_in_2_points(pure_parents[0], first_point, last_point))
    temp.append(div_list_in_2_points(pure_parents[1], first_point, last_point))
    div_parnts.append(temp)


    return div_parnts
# print the list and population
def print_population(list):
    print("I ||genotype||phynotype||p1||Qi")
    j = 0
    for i in list:
        j += 1
        print_list(i, j)
def print_list(list,i):
    print("I"+str(i)+"||" + str(list[0]) + "||" + str(list[1]) +"||"+ str(list[2]) +"||" +str(list[3])+"||\n")
#add def
# get the point of mix rndome geting the points of mix
def get_the_points_of_mix(list,Np):
    points = random.sample(range(1, len(list[0][0])), Np)
    points.sort()
    return points
# divise any  list betwine 2 points
def div_list_in_2_points(list,a,b):
    temp=[]
    for i in range(a,b):
        temp.append(list[i])
    return temp
# isolate the genotype from the parent
def pure_parnt(list):
    return list[0]
#geting the pure genom for child
def from_listsTolist(list ):
    temp=[]
    for i in list:
        for j in i :
            temp.append(int(j))
    return temp
def from_listssTolist(list ):
    temp=[]
    for i in list:
        for j in i :
            temp.append(j)
    return temp
def moyen_generation(list,des):
    sum=0
    for i in list :
        sum+=get_phyno_type(i,des)
    sum=sum/len(list)
    return sum
def remove_similar_items(input_list):
    unique_items = []
    for item in input_list:
        if item not in unique_items:
            unique_items.append(item)
    return unique_items
def reve(list):
    return list[::-1]
#############################################################################################################
#draw the graph :
def draw_the_graph(list_,len):
    x = [i for i in range(len)]
    # Create a list of y values from the list
    y = list_
    # Create a figure and axes
    fig, ax = plt.subplots()
    # Plot the x and y values
    ax.plot(x, y)
    # Set the axis labels and title
    ax.set_xlabel("generations")
    ax.set_ylabel("moyens of the phynotype")
    ax.set_title("Graph of moyens of the phynotype of generations")
    # Show the plot
    plt.show()