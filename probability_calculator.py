import random as rd
def experiment(Hat, expected_balls,num_balls_drawn, num_experiments):
  prob = 0
  for i in range (num_experiments):
    result = []
    for j in range(num_balls_drawn):
      result.append(Hat.contents.pop(rd.randrange(len(Hat.contents))))
    Hat.contents+=result
    check = 0
    for key in expected_balls.keys():
      true = len(expected_balls.keys())
      if result.count(key)>=expected_balls.get(key):
        check = check+1
      if check == true:
        prob +=1
  return prob

class Hat:
  def __init__(self, red=0, orange=0, black=0, blue=0, pink=0, striped=0, yellow=0, green=0):
    self.contents = []
    self.colors = ["red", "orange", "black" ,"blue", "pink", "striped", "yellow", "green"]
    for i in range(red):
      self.contents.append("red")
    for i in range(orange):
      self.contents.append("orange")
    for i in range(black):
      self.contents.append("black")
    for i in range(blue):
      self.contents.append("blue")
    for i in range(pink):
      self.contents.append("pink")
    for i in range(striped):
      self.contents.append("striped")
    for i in range(yellow):
      self.contents.append("yellow")
    for i in range(green):
      self.contents.append("green")
    print(self.contents)
  def draw(self, no):
    for i in range(no):
      print(self.contents.pop(rd.randrange(len(self.contents))), end=" ")


hat = Hat(red=4, black=6, green=3)
probability = experiment(hat,
                         expected_balls = {"red":2, "green":1},
                         num_balls_drawn=5,
                         num_experiments=2000)
