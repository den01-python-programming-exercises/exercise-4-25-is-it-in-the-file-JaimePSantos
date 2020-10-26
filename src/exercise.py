def main():
    #write your code below this line
    fileName = input("Name of the file:")
    search = input("Search for:")
    try:
      with open(fileName,'r') as f:
        lines = f.read().splitlines()
        if(search in lines):
          print("Found!")
        else:
          print("Not found.")
    except:
      print("Reading the file %s failed."%fileName)

if __name__ == '__main__':
    main()
