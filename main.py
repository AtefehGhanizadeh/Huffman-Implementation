from Node import Node
import matplotlib.pyplot as plt




# CALCULATE FREQUENCY OF CHARACTERS
# CALCULATE FREQUENCY OF CHARACTERS
# CALCULATE FREQUENCY OF CHARACTERS


def calculateFrequency(data):

    the_characters = dict()

    for character in data:

        if the_characters.get(character) == None:

            the_characters[character] = 1

        else:

            the_characters[character] += 1

    return the_characters


# SORT
# SORT
# SORT

def partition(arr,low,high):
   i = ( low-1 )
   pivot = arr[high].frequency
   for j in range(low , high):

      if arr[j].frequency <= pivot:

         i = i+1
         arr[i],arr[j] = arr[j],arr[i]
   arr[i+1],arr[high] = arr[high],arr[i+1]
   return ( i+1 )

def quickSort(arr,low,high):

   if low < high:

      pi = partition(arr,low,high)
      quickSort(arr, low, pi-1)
      quickSort(arr, pi+1, high)



# HUFFMAN IMPLEMENTATION
# HUFFMAN IMPLEMENTATION
# HUFFMAN IMPLEMENTATION

nodes=[]

def huffman(data):


    characterWithFrecuency = calculateFrequency(data)

    the_characters = characterWithFrecuency.keys()

    for character in the_characters:

        nodes.append(Node(character,characterWithFrecuency.get(character)))

    for i in range(0,len(nodes)+19,2):

            quickSort(nodes, i, len(nodes)-1)
            node = Node(str((nodes[i].frequency)+(nodes[i+1].frequency)),(nodes[i].frequency)+(nodes[i+1].frequency),None,lchild=nodes[i],rchild=nodes[i+1])
            nodes.append(node)
            node.lchild.code=0
            node.rchild.code =1
            nodes[i].parentNode=node
            nodes[i+1].parentNode = node

    return nodes[len(nodes)-1]



# PRODUCE HUFFMANCODE
# PRODUCE HUFFMANCODE
# PRODUCE HUFFMANCODE

the_codes = dict()


def CalculateCodes(node, value=''):

    newValue = value + str(node.code)

    if (node.lchild!=None):
        CalculateCodes(node.lchild, newValue)

    if (node.rchild!=None):
        CalculateCodes(node.rchild, newValue)

    if (node.rchild==None and node.lchild==None):
        the_codes[node.nodeName] = newValue

    return the_codes


def OutputEncoded(the_data, coding):

    encodingOutput = []
    for element in the_data:
        print(coding[element], end='')
        encodingOutput.append(coding[element])

    the_string = ''.join([str(item) for item in encodingOutput])
    return the_string




#DRAW HUFFMAN TREE
#DRAW HUFFMAN TREE
#DRAW HUFFMAN TREE

def drawLchild(root,x,y):



    circle = plt.Circle((x, y), radius=0.4)

    ax.add_patch(circle)

    label = ax.annotate(root.nodeName, xy=(x, y), fontsize=10, ha="center")

    point1 = [x, y]


    if (root.rchild!=None and root.lchild!=None):

        point2 = [x -0.75, y - 3]
        point3 = [x + 0.5, y - 3]

        x_values = [point1[0], point2[0]]

        y_values = [point1[1], point2[1]]

        plt.plot(x_values, y_values)

        x_values1 = [point1[0], point3[0]]

        y_values1 = [point1[1], point3[1]]

        plt.plot(x_values1, y_values1)



        drawLchild(root.lchild,x-0.75,y-3)



        drawRchild(root.rchild, x+0.5 , y - 3)




def drawRchild(root, x, y):


    circle = plt.Circle((x, y), radius=0.4)

    ax.add_patch(circle)

    label = ax.annotate(root.nodeName, xy=(x, y), fontsize=10, ha="center")
    point1 = [x, y]


    if (root.rchild != None and root.lchild != None):

        if ((x-6)%5!=0):

            drawRchild(root.rchild, x + 1, y - 3)
            drawLchild(root.lchild, x - 0.25, y - 3)
            point2 = [x + 1, y - 3]
            point3 = [x - 0.25, y - 3]

            x_values = [point1[0], point2[0]]

            y_values = [point1[1], point2[1]]

            plt.plot(x_values, y_values)

            x_values1 = [point1[0], point3[0]]

            y_values1 = [point1[1], point3[1]]

            plt.plot(x_values1, y_values1)


        else:
            drawRchild(root.rchild, x + 5, y - 3)

            drawLchild(root.lchild, x - 5, y - 3)
            point2 = [x + 5, y - 3]
            point3 = [x - 5, y - 3]

            x_values = [point1[0], point2[0]]

            y_values = [point1[1], point2[1]]

            plt.plot(x_values, y_values)

            x_values1 = [point1[0], point3[0]]

            y_values1 = [point1[1], point3[1]]

            plt.plot(x_values1, y_values1)






def draw(root,x,y):


    circle = plt.Circle((x,y), radius=0.4)

    ax.add_patch(circle)

    label = ax.annotate(root.nodeName, xy=(x, y), fontsize=10, ha="center")


    if (root.rchild!=None and root.lchild!=None):

        drawLchild(root.lchild, x-6, y - 3)

        drawRchild(root.rchild, x+6, y - 3)

        point1=[x,y]
        point2=[x-6,y-3]
        point3=[x+6,y-3]

        x_values = [point1[0], point2[0]]

        y_values = [point1[1], point2[1]]

        plt.plot(x_values, y_values)

        x_values1 = [point1[0], point3[0]]

        y_values1 = [point1[1], point3[1]]

        plt.plot(x_values1, y_values1)




fig, ax = plt.subplots()

ax = fig.add_subplot(111)


data = open("huffmantext.txt" , "r")

data=data.read()

data=data.lower()

data = ''.join(data.split())

draw(huffman(data),0,0)

CalculateCodes(nodes[len(nodes)-1])

OutputEncoded(data,the_codes)


ax.axis('off')
ax.set_aspect('equal')
ax.autoscale_view()

plt.show()



