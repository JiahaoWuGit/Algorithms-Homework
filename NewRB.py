# -*- coding: UTF-8 -*-
from Tkinter import *
import math
import random
success = 'success rotate'
rotateFail = 'rotate fail'
red = 'red'
black = 'black'
color = 'color'
parent = 'parent'
largest = 'largest'
lchild = 'lchild'
rchild = 'rchild'
low = 'low'
high = 'high'

lap = 1
unlap = 0
Troot = 0
nil = 1
nilxy = -1
def creatNode(left,right,intervalL,intervalH,l,p,colour):
    dictionary = {color : colour, \
                    parent : p,\
                    largest: l, \
                    lchild: left, \
                    rchild: right, \
                    low: intervalL, \
                    high: intervalH}
    return dictionary

def search(lowInterval, highInterval,treeNodes):
    temp = treeNodes[Troot]
    while temp != nil:
        print treeNodes[temp][low]
        if treeNodes[temp][low] == lowInterval and treeNodes[temp][high] == highInterval:
            return temp
        if treeNodes[temp][low] >= lowInterval:
            temp = treeNodes[temp][lchild]
        else:
            temp = treeNodes[temp][rchild]
    return nil

def overlap(node1,node2,treeNodes):
    if node2[low] > node1[high] or node1[low] > node2[high]:
        return unlap
    return lap

def findOverlap(iNode,treeNodes):
    temp = treeNodes[Troot]
    while temp != nil and overlap(iNode,treeNodes[temp],treeNodes) == unlap:
		if treeNodes[temp][lchild] != nil and treeNodes[treeNodes[temp][lchild]][largest] >= iNode[low]:
			temp = treeNodes[temp][lchild];
		else:
			temp= treeNodes[temp][lchild];
    return  temp

def max(a,b,c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

def rotateL(rn,treeNodes):
    rnP = treeNodes[rn][parent]
    y = treeNodes[rn][rchild]
    treeNodes[rn][rchild] = treeNodes[y][lchild]
    if treeNodes[y][lchild] != nil:
        treeNodes[treeNodes[y][lchild]][parent] = rn
    treeNodes[y][parent] = rnP
    if rnP == nil:
        treeNodes[Troot] = y
    elif rn == treeNodes[rnP][lchild]:
        treeNodes[rnP][lchild] = y
    else:
        treeNodes[rnP][rchild] = y
    treeNodes[y][lchild] = rn
    treeNodes[rn][parent] = y
    treeNodes[y][largest] = treeNodes[rn][largest]
    treeNodes[rn][largest] = max(treeNodes[rn][high],treeNodes[treeNodes[rn][lchild]][largest],treeNodes[treeNodes[rn][rchild]][largest])
    return success
def rotateR(rn,treeNodes):
    rnP = treeNodes[rn][parent]
    rnL = treeNodes[rn][lchild]
    treeNodes[rn][lchild] = treeNodes[rnL][rchild]
    if treeNodes[rnL][rchild] != nil:
        treeNodes[treeNodes[rnL][rchild]][parent] = rn
    treeNodes[rnL][parent] = rnP
    if treeNodes[rn][parent] == nil:
        treeNodes[Troot] = rnL
    elif rn == treeNodes[rnP][lchild]:
        treeNodes[rnP][lchild] = rnL###########
    else:
        treeNodes[rnP][rchild] = rnL############
    treeNodes[rnL][rchild] = rn
    treeNodes[rn][parent] = rnL
    treeNodes[rnL][largest] = treeNodes[rn][largest]
    treeNodes[rn][largest] = max(treeNodes[rn][high],treeNodes[treeNodes[rn][lchild]][largest],treeNodes[treeNodes[rn][rchild]][largest])
    return success

def TreeSuccessor(z,treeNodes):#ｒｅｔｕｒｎ the mid-next node of this node
    print '中序后继'
    if treeNodes[z][rchild] != nil:
        x = treeNodes[z][rchild]
        while treeNodes[x][lchild] != nil:
            x = treeNodes[x][lchild]
        return x
    else:
        x = treeNodes[z][parent]
        while x!= nil and z == treeNodes[x][rchild]:
            z = x
            x = treeNodes[x][parent]
        return x
def deleteFixup(x,treeNodes):
    print 'deletefix'
    while x != treeNodes[Troot] and treeNodes[x][color] == black:
        print 'fix while'
        if x == treeNodes[treeNodes[x][parent]][lchild]:#x 是父节点的左孩子
            w = treeNodes[treeNodes[x][parent]][rchild]
            if treeNodes[w][color] == red:#case1
                treeNodes[w][color] = black
                treeNodes[treeNodes[x][parent]][color] = red
                rotateL(treeNodes[x][parent],treeNodes)
                w = treeNodes[treeNodes[x][parent]][rchild]# case1
            if treeNodes[treeNodes[w][lchild]][color] == black and treeNodes[treeNodes[w][rchild]][color] == black:
                treeNodes[w][color] = red#case2
                x=treeNodes[x][parent]
            elif treeNodes[treeNodes[w][rchild]][color] == black:#case3
                treeNodes[treeNodes[w][lchild]][color] = black
                treeNodes[w][color] = red
                rotateR(w,treeNodes)
                w = treeNodes[treeNodes[x][parent]][rchild]
                print 'fixcase3'
                    #case4
                treeNodes[w][color] = treeNodes[treeNodes[x][parent]][color]
                treeNodes[treeNodes[x][parent]][color] = black
                treeNodes[treeNodes[w][rchild]][color] = black
                rotateL(treeNodes[x][parent],treeNodes)
                x = treeNodes[Troot]
            else:#case4
                treeNodes[w][color] = treeNodes[treeNodes[x][parent]][color]
                treeNodes[treeNodes[x][parent]][color] = black
                treeNodes[treeNodes[w][rchild]][color] = black
                rotateL(treeNodes[x][parent],treeNodes)
                x = treeNodes[Troot]

        else:
            w = treeNodes[treeNodes[x][parent]][lchild]
            if treeNodes[w][color] == red:#case1
                treeNodes[w][color] = black
                treeNodes[treeNodes[x][parent]][color] = red
                rotateR(treeNodes[x][parent],treeNodes)
                w = treeNodes[treeNodes[x][parent]][lchild]# case1
            if treeNodes[treeNodes[w][lchild]][color] == black and treeNodes[treeNodes[w][rchild]][color] == black:
                treeNodes[w][color] = red#case2
                x=treeNodes[x][parent]
            elif treeNodes[treeNodes[w][lchild]][color] == black:#case3
                treeNodes[treeNodes[w][rchild]][color] = black
                treeNodes[w][color] = red
                rotateL(w,treeNodes)
                w = treeNodes[treeNodes[x][parent]][lchild]
                print 'fixcase3'
                    #case4
                treeNodes[w][color] = treeNodes[treeNodes[x][parent]][color]
                treeNodes[treeNodes[x][parent]][color] = black
                treeNodes[treeNodes[w][lchild]][color] = black
                rotateR(treeNodes[x][parent],treeNodes)
                x = treeNodes[Troot]
            else:#case4
                treeNodes[w][color] = treeNodes[treeNodes[x][parent]][color]
                treeNodes[treeNodes[x][parent]][color] = black
                treeNodes[treeNodes[w][lchild]][color] = black
                rotateR(treeNodes[x][parent],treeNodes)
                x = treeNodes[Troot]
    treeNodes[x][color]= black
def delete(delNode,treeNodes):
    print 'delete'
    if delNode == nil:
        return nil
    if treeNodes[delNode][lchild] == nil or treeNodes[delNode][rchild] == nil:#case 1,2
        y = delNode
    else: # two of node's kids are not NULL
        y = TreeSuccessor(delNode,treeNodes)# thsi is the midNext node of it
        print treeNodes[y]
    # now y is the parent-node of deleteNode
    if treeNodes[y][lchild] != nil:#case 1,2,3
        x = treeNodes[y][lchild]
    else:
        x = treeNodes[y][rchild]
    treeNodes[x][parent] = treeNodes[y][parent]
    if treeNodes[y][parent] == nil:# y is the root of tree
        treeNodes[Troot] = x
    else: # y is not the root of a tree
        if y == treeNodes[treeNodes[y][parent]][lchild]:#y is the left kid of its parent
            treeNodes[treeNodes[y][parent]][lchild] = x
        else:
            treeNodes[treeNodes[y][parent]][rchild] = x

    #deal with the largest problem
    g = treeNodes[y][parent]
    treeNodes[g][largest] = max(treeNodes[g][high],treeNodes[treeNodes[g][lchild]][largest],treeNodes[treeNodes[g][rchild]][largest])
    g = treeNodes[g][parent]
    while treeNodes[g][largest] == treeNodes[y][largest]:
        treeNodes[g][largest] = max(treeNodes[g][high],treeNodes[treeNodes[g][lchild]][largest],treeNodes[treeNodes[g][rchild]][largest])
        g = treeNodes[g][parent]

    if y != delNode:# case 3
        print 'case3'
        treeNodes[delNode][low] = treeNodes[y][low]
        treeNodes[delNode][high] = treeNodes[y][high]

    #deal with the largest problem
    g = delNode
    treeNodes[g][largest] = max(treeNodes[g][high],treeNodes[treeNodes[g][lchild]][largest],treeNodes[treeNodes[g][rchild]][largest])
    g = treeNodes[g][parent]
    while treeNodes[g][largest] == treeNodes[delNode][largest]:
        treeNodes[g][largest] = max(treeNodes[g][high],treeNodes[treeNodes[g][lchild]][largest],treeNodes[treeNodes[g][rchild]][largest])
        g = treeNodes[g][parent]

    if treeNodes[y][color] == black:
        deleteFixup(x,treeNodes)# adjust the tree
    return y


def insertFix(treeNodes):
    node = len(treeNodes) - 1
    x = node
    while treeNodes[treeNodes[node][parent]][color] == red:
        if treeNodes[node][parent] == treeNodes[treeNodes[treeNodes[node][parent]][parent]][lchild]:
            y = treeNodes[treeNodes[treeNodes[node][parent]][parent]][rchild]
            if treeNodes[y][color] ==red:
                treeNodes[treeNodes[node][parent]][color] = black#case1
                treeNodes[y][color] = black#case1
                treeNodes[treeNodes[treeNodes[node][parent]][parent]][color] = red#case1
                node = treeNodes[treeNodes[node][parent]][parent]#case1
            else:
                if node == treeNodes[treeNodes[node][parent]][rchild]:#case2
                    node = treeNodes[node][parent]#case 2
                    rotateL(node,treeNodes)#case
                else:
                    treeNodes[treeNodes[node][parent]][color] = black#case 3
                    treeNodes[treeNodes[treeNodes[node][parent]][parent]][color] = red# this is the pparent of the current node
                    rotateR(treeNodes[treeNodes[node][parent]][parent],treeNodes)
        else:
            y = treeNodes[treeNodes[treeNodes[node][parent]][parent]][lchild]
            if treeNodes[y][color] ==red:
                treeNodes[treeNodes[node][parent]][color] = black#case1
                treeNodes[y][color] = black
                treeNodes[treeNodes[treeNodes[node][parent]][parent]][color] = red
                node = treeNodes[treeNodes[node][parent]][parent]
            else:
                if node == treeNodes[treeNodes[node][parent]][lchild]:
                    node = treeNodes[node][parent]#case 2
                    rotateR(node,treeNodes)
                else:
                    treeNodes[treeNodes[node][parent]][color] = black#case 3
                    treeNodes[treeNodes[treeNodes[node][parent]][parent]][color] = red# this is the pparent of the current node
                    rotateL(treeNodes[treeNodes[node][parent]][parent],treeNodes)   #case 3
        #treeNodes[nil][color] = black
    treeNodes[treeNodes[Troot]][color] = black
def insert(treeNodes):
    newNode = len(treeNodes) - 1
    y = nil
    x = treeNodes[0]#root of the tree
    while x != nil:#find the leaf place it should be
        if treeNodes[x][largest] < treeNodes[newNode][largest]:
            treeNodes[x][largest] = treeNodes[newNode][largest]
        y = x
        if treeNodes[newNode][low] < treeNodes[x][low]:
            x = treeNodes[x][lchild]
        else:
            x = treeNodes[x][rchild]
    treeNodes[newNode][parent] = y
    if y == nil:# newnode is the root
        treeNodes[0] = newNode
    elif treeNodes[newNode][low] < treeNodes[y][low]:
        treeNodes[y][lchild] = newNode
    else:
         treeNodes[y][rchild] = newNode
    treeNodes[newNode][lchild] = nil
    treeNodes[newNode][rchild] = nil
    treeNodes[newNode][color] = red
    insertFix(treeNodes)
    return 'success'
def printResult(treeNodes,node,frm,fontL):
    if node != nil:
        Label(frm, text=treeNodes[node][low],font=('Arial', fontL), fg = treeNodes[node][color]).pack()
        frm_L = Frame(frm)
        frm_R =Frame(frm)
        frm_M = Frame(frm)

        printResult(treeNodes,treeNodes[node][lchild],frm_L,fontL-5)
        frm_L.pack(side=LEFT)
        Label(frm_M, text="    ",font=('Arial', fontL), fg = treeNodes[node][color]).pack()
        frm_M.pack(side=LEFT)
        printResult(treeNodes,treeNodes[node][rchild],frm_R,fontL-5)
        frm_R.pack(side=RIGHT)
    return 0
#init a tree

def printNodes(treeNodes,frm,fontL):
    for node in range(2,len(treeNodes)):
        information = 'interval:(' + str(treeNodes[node][low]) +','+ str(treeNodes[node][high])+') '+'largest:'+str(treeNodes[node][largest])
        frm_L = Frame(frm)
        Label(frm_L, text=information,font=('Arial', fontL), fg = treeNodes[node][color]).pack()
        frm_L.pack(side=TOP)

    return 0
nodes = []
nodes.append(nil) #开始的时候ｎｉｌ节点是ｒｏｏｔ
#creatNode(left,right,intervalL,intervalH,l,p,colour)
Tnil = creatNode(nil,nil,nilxy,nilxy,nilxy,nil,black)#nil节点的左右孩子和父母节点全部指向自己并且区间设置为－１，，１
nodes.append(Tnil)

#begin
#n = int(input('please enter the number of nodes you want to test:'))
num = int(input('please input the number of nodes you want to test:'))
for j in range(1,num+1):
    print j
    rand = random.randint(1,100)
    randH = random.randint(rand+1,200)
    if search(rand,randH,nodes) != nil:
        j = j - 1
        continue
    new = creatNode(len(nodes),len(nodes),rand,randH,randH,len(nodes),red)
    nodes.append(new)#初始化认为孩子ｐａｒｅｎｔ全是他自己
    insert(nodes)
    nodes[nil][color] = black


i = nodes[Troot]
print 'information of nodes'
for i in nodes:
    print i
print 'and nil'
print nodes[nil]
print 'information of root'
print nodes[nodes[Troot]]

while 1:
    root = Tk()
    root.title("B&R Tree")
    root.geometry('1200x1000')
    root.resizable(width=True, height=True)
    frm1 = Frame(root)
    printResult(nodes,nodes[Troot],frm1,50)
    frm1.pack()
    frm2 = Frame(root)
    printNodes(nodes,frm2,20)
    frm2.pack()
    root.mainloop()
    n = int(input('what do you want to do : 1、insert  2、delete 3、search　overlap 4、show the graph 5、exit\n'))
    if n == 1:
        num = list(input('enter the interval you want to insert:(divide low and high by COMMA):'))
        if int(num[0]) > int(num[1]):
            print 'wrong interval',num[0],num[1]
            continue
        new = creatNode(len(nodes),len(nodes),int(num[0]),int(num[1]),int(num[1]),len(nodes),red)
        print new
        nodes.append(new)#初始化认为孩子ｐａｒｅｎｔ全是他自己
        insert(nodes)
        nodes[nil][color] = black
    elif n == 2:
        num = list(input('enter the interval you want to delete:(divide low and high by COMMA):'))
        # num 读进来是一个（ｎｕｍ１，ｎｕｍ２）这样的元组
        find = search(int(num[0]),int(num[1]),nodes)
        if find == nil:
            print 'could not find the interval'
            continue
        delete(find,nodes)
    elif n == 3:
        num = list(input('enter the interval you want to search:(divide low and high by COMMA):'))
        # num 读进来是一个（ｎｕｍ１，ｎｕｍ２）这样的元组
        findNode = creatNode(len(nodes),len(nodes),int(num[0]),int(num[1]),int(num[1]),len(nodes),red)
        find = findOverlap(findNode,nodes)
        if find == nil:
            print 'There is no interval overlapped with it'
        else:
            print nodes[find]
    elif n == 4:
        continue
    else:
        break
