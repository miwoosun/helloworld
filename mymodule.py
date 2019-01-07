def greeting(name):
    print("hello, " + name)

person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")

try:
  f = open("demofile.txt")
  f.write("Lorum Ipsum")
except:
  print("Something went wrong when writing to the file")
finally:
  f.close()