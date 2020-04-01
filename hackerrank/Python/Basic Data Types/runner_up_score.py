if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    #You are given numbers. Store them in a list and find the second largest number.
    #The first line contains . The second line contains an array [] of integers each separated by a space. 
    #Output the value of the second largest number.
    
    print(sorted(list(set(arr)))[-2])