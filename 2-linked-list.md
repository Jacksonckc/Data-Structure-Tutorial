# Linked List

## Structure

Ever been on a train before? Have you wondered how train cabins are attached together? Yes! Today we are going to learn about how to build a train together! First of all you will need a mechanical degree from BYU-I....

![Train Image](./images/train.webp)
Wrong channel, let's try again!

Today we are going to learn about how to use the train structure to deal with our data.

Let's envision the cabins as pieces of data, we call them nodes. The entire train is the container of the data, which we call it a linked list.

A train has a beginning and an end, we call them head and tail in our linked list. Each cabin is attached to another cabin (Unless it's the head or the tail), we will call the cabin to the left prev and the cabin to the right next.

```python
def __init__(self):
    # Initialize an empty linked list.
    self.head = None
    self.tail = None
```

```python
def __init__(self, data):
    # Initialize the node to the data provided.  Initially
    # the links are unknown so they are set to None.
    self.data = data
    self.next = None # will be replaced by another cabin/node when there is one
    self.prev = None # will be replaced by another cabin/node when there is one
```

It is not an exaggeration to say that the structure of a linked list is the same with the structure of a train, let's examine it a little further below.

## Linked List Manipulation

## Add to/remove from the head

### Adding:

1. Create a new node
2. Set self.next of the new node to the head node of the existing list

```python
new_node.next = self.head
```

3. Set self.prev of the head node of the existing list to the new node

```python
self.head.prev = new_node
```

4. Set the head of the list to the new node

```python
self.head = new_node
```

To visualize this, you can think of this process as adding a new cabin to the front of the train. It requires the new cabin to be hooked up to the existing head cabin of the train, setting self.next of the new cabin to the old head cabin and self.prev of the old cabin to the new cabin. Once they are hook, we need to re-name the cabins. The old head cabin is in the second position now, so we take away the name from it and give it to the new head cabin which is the new cabin added to the head.

### Removing:

1. Set self.prev of the second node to None

```python
self.head.next.prev = None
```

2. Set self.head of the list to the second node

```python
self.head = self.head.next
```

Taking the train example, we first disattach the first cabin of the train, then we re-name the head to the the second cabin of the train.

### Efficiency:

The operation of both processes is O(1)

## Add to/remove from the tail

### Adding:

1. Create a new node
2. Set self.prev of the new node to the tail node of the existing list

```python
new_node.prev = self.tail
```

3. Set self.next of the tail node of the existing list to the new node

```python
self.tail.next = new_node
```

4. Set the tail of the list to the new node

```python
self.tail = new_node
```

You may apply the same principles from adding to the head here to help you visualize this process.

### Removing:

1. Set self.next of the second to the last node to None

```python
self.tail.prev.next = None
```

2. Set self.tail of the list to the second to the last node

```python
self.tail = self.tail.prev
```

Taking the train example, we first disattach the last cabin of the train, then we re-name the tail to the the second to the last cabin of the train.

### Efficiency:

The operation of both processes is O(1)

## Add to/remove from the middle

Adding the middle is the most complex process of the linked list manipulation, let's assume that we are inserting a node after node A

### Adding:

1. Create a new node
2. Set self.next of node A to be the new node

```python
A.next = new_node
```

3. Set self.prev of the new node to node A

```python
new_node.prev = A
```

4. Set self. next of the new node to be the next node after node A

```python
new_node.next = A.next
```

5. Set self. prev of the next node of the A node to be the new node

```python
A.next.prev = new_node
```

To help you understand this process, you can incorporate the method of hooking up 2 sets of cabins using the above example. The only difference is that we are not changing our head or tail of the train, we are only hooking a cabin up to the middle of the train.

### Removing:

Let's assume we are removing node A from somewhere in the list

1. Set the node before node A to be the precious node of the node after node A

```python
A.next.prev = A.prev
```

2. Set the node after node A to be the next node of the node before node A

```python
A.prev.next = A.next
```

### Efficiency:

The operation of both processes is O(n), it takes n times for the program to find the inserting/removing position.

## Search within a Linked List

We often need to find a node in the linked list, we call it accessing from a linked list. Just like the train example we have been using throughout this page, we can think of it as finding a person in the entire train from the cabins.

To find a person from the train, there isn't an efficient way other than going to each cabin from the head cabin down to the tail. If we are lucky, we might find the person in the first one, but luck can't always accompany us, in which we might have to go down to the last cabin, the tail to find our person. The finding operation is O(n). The same as we loop through a linked list and try to find an item, we go through each node and compare its data value with our targeted value.

```python
def findPerson(self):
    # Start at the beginning (the head)
	current = self.head
    person = "Jackson"

	# Loop until we have reached the end (None)
	while current is not None:
        if current.data == person:
		    # Do something with the current node
		    print("We found your person ", current.data, "!")

        # Follow the pointer to the next node
        current = current.next
```

Using the same concept, we can use print() function to display each node value in the linked list by looping through the entire list from the head to the tail. The efficiency of this operation is O(n)

## Linked List Operation & Efficiency

| Operation     | Performance | Explanation                                                                                                                                                                                  |
| ------------- | ----------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| insert_head   | O(1)        | Only needs to adjust the the pointers of the head, the new and old head node.                                                                                                                |
| insert_tail   | O(1)        | Only needs to adjust the the pointers of the tail, the new and old tail node.                                                                                                                |
| insert_middle | O(n)        | Only needs to adjust the the pointers of the middle, the new and old nodes relating to the middle. O(n) performance comes with looping and finding the middle (targeted) insertion location. |
| remove_head   | O(1)        | Only needs to adjust the the pointer of the head, the new head node.                                                                                                                         |
| remove_tail   | O(1)        | Only needs to adjust the the pointer of the tail, the new tail node.                                                                                                                         |
| remove_middle | O(n)        | Only needs to adjust the the pointers of the middle, the nodes relating to the middle. O(n) performance comes with looping and finding the middle (targeted) deletion location.              |
| length        | O(1)        | Built-in python function                                                                                                                                                                     |
| empty         | O(1)        | Just check the length to see if it's 0                                                                                                                                                       |

## Example

## Problem to Solve
