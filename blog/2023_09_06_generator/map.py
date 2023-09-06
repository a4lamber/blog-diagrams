'''
 # @ Author: Your name
 # @ Create Time: 2023-09-06 15:38:41
 # @ Modified by: Your name
 # @ Modified time: 2023-09-06 16:29:08
 # @ Description: map() in also a concept in
 functional programming and related with iterator
 '''


import sys

def main():
    n = 100
    
    x = [i for i in range(n)]

    y = map(lambda i: i**2, x)
    print(f"size of data n: {n}")
    print(f"map memory location: {y}")
    print(f"Size of map object in bytes: {sys.getsizeof(y)}")
    print(f"Size of list object in bytes: {sys.getsizeof(list(y))}") 
    
    # compute at runtime
    for i in y:
        print(i)
        
if __name__ == "__main__":
    main()