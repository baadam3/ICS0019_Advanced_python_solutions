def calculate_area(h,b):

 if not isinstance(h, float):
      try:
        h = float(h)
      except:
          print ("Arguments must be numbers!")
          return 0
 if not isinstance(b, float):
        try:
         b = float(b)
        except:
          print ("Arguments must be numbers!")
          return 0
 if h > 0 and b > 0:
        return (h*b)/2
 else:
        print("Cannot supply negative values as argument!")
      