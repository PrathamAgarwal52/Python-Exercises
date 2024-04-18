from __future__ import print_function

if __name__ == '__main__':
    expression = input().strip()
    result = eval(expression)
    
    if result is not None:
        print(result)
