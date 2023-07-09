def hello():
    print("hello user")

hello()

def pack_lunch(a,b,c):
  return [a,b,c]

print(pack_lunch(1,2,3))


def eat_lunch(list):
   if len(list) == 0:
      print("no lunch for you")
   else:
      for i in range(len(list)):
         if i == 0:
            print(f"Fist I eat my {list[0]}")
      else:
         print(f"Next i eat {list[i]}")

# eat_lunch(["sandwich"])
eat_lunch(["apple","banana","sandwich","cookie"])