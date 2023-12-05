front_of_queue_pointer = 0
end_of_queue_pointer = -1
queue = ["","","","","","","", ""] # pretending to be a fixed sized queue
animals = ["Frog", "Cat", "Fish", "Elk", "Wasp", "Bee", "Mouse", "Ant", "Dolphin", "Shark"]

def print_queue():
    """
    Prints the current state of the queue
    :return:
    """
    for i in range(8):
        if i == front_of_queue_pointer and i == end_of_queue_pointer:
            print("front & end queue pointers -> ",end="")
        elif i == front_of_queue_pointer:
            print("front queue pointer        -> ", end="")
        elif i == end_of_queue_pointer:
            print("end queue pointer          -> ", end="")
        else:
            print(" "*30,end="")

        print(i,"|",queue[i])

def enqueue(item):
    """
    This add an item to the queue
    :param item: The item you want to add
    :return:
    """
    global front_of_queue_pointer
    global end_of_queue_pointer

    #if front_of_queue_pointer-1 == end_of_queue_pointer and end_of_queue_pointer!=-1:
        #print("Queue is full")
    #elif front_of_queue_pointer==0 and end_of_queue_pointer == 6:
        #print("Queue is full")
    if front_of_queue_pointer-1 == end_of_queue_pointer and end_of_queue_pointer!=-1:
        print("Queue is full")
    else:
        if end_of_queue_pointer < 7:
            end_of_queue_pointer += 1
            print("Moving end of queue pointer +1")
        else:
            end_of_queue_pointer = 0
            print("Moving end of queue pointer to 0")
        print("Inserting",item)
        queue[end_of_queue_pointer]=item

def dequeue():
    """
    This removes the item from the queue and gives it back to you.
    :return: the item at front of queue
    """
    global front_of_queue_pointer
    global end_of_queue_pointer
    if end_of_queue_pointer == front_of_queue_pointer:
        #item_from_queue = queue[front_of_queue_pointer]
        #queue[front_of_queue_pointer] = ""
        #front_of_queue_pointer=0
        #end_of_queue_pointer = -1
        print('Empty')
    elif end_of_queue_pointer == -1:
        print("Empty")

    else:
        item_from_queue = queue[front_of_queue_pointer]
        #queue[front_of_queue_pointer] =""
        if front_of_queue_pointer == 7:
            front_of_queue_pointer =0
        else:
            front_of_queue_pointer+=1
        return item_from_queue

print("Welcome to your very own queue")
print("You can use print_queue(), enqueue(item) and dequeue() to use the circular queue. The list is pretending to be a fixed sized array although its not fussy about data types.")
print("You can even ask for help using e.g. help(print_queue)")

#seqeunce of the question
for i in range(4):
    enqueue(animals[i])
print_queue()

for i in range(4, 7):
    enqueue(animals[i])
dequeue()
dequeue()
print_queue()

enqueue(animals[7])
enqueue(animals[0])
enqueue(animals[1])
for i in range(7):
    dequeue()
for i in range(2, 7):
    enqueue(animals[i])
dequeue()
dequeue()
print_queue()

dequeue()
enqueue(animals[8])
enqueue(animals[9])
print_queue()

