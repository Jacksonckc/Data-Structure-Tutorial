queue = []

def checkIsAgent(number):
    # Return is the number starts with 333
    return number.startswith('333')

def enqueue(caller):
    if checkIsAgent(caller) == False:
        # Put the caller to the front of the queue
        queue.append(caller)
    else:
        # Put the caller to the end of the queue
        queue.insert(0, caller)

def dequeue(caller = ''):
    if len(queue) == 0:
        pass
    else:
        if caller == '':
            # Dequeue from the end
            queue.pop(0)
        else:
            for i in range(len(queue)):
                # Loop through the queue to find the caller who wants to exist the queue.
                if queue[i] == caller:
                    queue.pop(i)


# Test cases
enqueue('123456789')
enqueue('968158561')
enqueue('345623413')
enqueue('333908531')
dequeue()
dequeue("345623413")
print(queue) # ['123456789', '968158561']