'''
 # @ Author: Your name
 # @ Create Time: 2023-09-06 15:27:51
 # @ Modified by: Your name
 # @ Modified time: 2023-09-06 16:26:17
 # @ Description: Using iterator with range() to
 # avoid the trouble of saving it in memory.
'''


import sys

def main():
    # size of the list
    n = 20
    
    # store entire sequences of number in memory 
    x = [i for i in range(n)]

    print("store in memory")
    print(f"Size in bytes: {sys.getsizeof(x)}")
    
    for element in x:
        print(element)
    print()
    print("Don't store in memory")
    print(f"Size in bytes: {sys.getsizeof(range(1,11))}")
    
    # iterator with range()    
    for i in range(0,n):
        print(i)

if __name__ == "__main__":
    main()
    
