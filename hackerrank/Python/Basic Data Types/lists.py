if __name__ == '__main__':
    N = int(input())
    l = []

    #insert i e: Insert integer at position .
    #print: Print the list.
    #remove e: Delete the first occurrence of integer .
    #append e: Insert integer at the end of the list.
    #sort: Sort the list.
    #pop: Pop the last element from the list.
    #reverse: Reverse the list.    
    
    for i in range(1, N+1):
        s = str(input()).split()
        if s[0] == "insert":
            l.insert(int(s[1]),int(s[2]))
        elif s[0] == "print":
            print(l)
        elif s[0] == "remove":
            l.remove(int(s[1]))
        elif s[0] == "append":
            l.append(int(s[1]))
        elif s[0] == "sort":
            l.sort()
        elif s[0] == "pop":
            l.pop()
        else:
            l.reverse()