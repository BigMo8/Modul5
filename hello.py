import sys

def customized_hello(first_name, last_name, gender = 'Mrs'):
   print("Hello %s %s %s!" % ( gender, first_name, last_name))

if __name__ == "__main__":
    if len(sys.argv)<4:
        exit(1)
    first_name = sys.argv[1]
    last_name = sys.argv[2]
    gender = sys.argv[3]
    customized_hello(gender, first_name, last_name)