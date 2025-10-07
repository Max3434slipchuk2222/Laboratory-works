from decorator.decor import check_type

@check_type
def add(a, b):
   return a + b


def main:

  print(add(3, 5))      
  print(add("Hello ", True)) 
  print(add("5", "7"))  

if __name__ == "__main__":
   main()
