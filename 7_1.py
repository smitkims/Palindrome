from queue import LifoQueue

inp = str(input("Enter string to check: "))
stack = LifoQueue()
check = 0

#if it's odd or even, split it up
if len(inp) % 2 == 0:
    for k in range(int(len(inp)/2)):
        stack.put(inp[k])
    for m in range(int(len(inp)/2), len(inp)):
        if stack.get() != inp[m]:
            print(str(inp) + " is not a palindrome")
            exit()
    print(str(inp) + " is a palindrome")
    
else:
    for k in range(int((len(inp)/2) + 1)):
        stack.put(inp[k])
    stack.get() #pop out the middle value (not needed)
    for m in range(int((len(inp)/2) + 1), len(inp)):
        if stack.get() != inp[m]:
            print(str(inp) + " is not a palindrome")
            exit()
    print(str(inp) + " is a palindrome")