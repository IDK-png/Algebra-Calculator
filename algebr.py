import numpy as np
class First:
    def __init__(self, primer):
      tonext = [];letter = [];nums = [];what = [];lastnum = []
      for a in primer:
            try:
                tonext.append(int(a))
            except ValueError:
                if ord(a.upper()) != 32:
                    tonext.append(a)
      for b,a in enumerate(tonext): #  If the letter before equal
          try:
                  print(a)
                  if type(a) == int and type(tonext[b+2]) == str and len(letter) < 2 and tonext.index("=")>tonext.index(a) and tonext[b+2].isalpha():
                      letter.append(tonext[tonext.index(a)+1]);letter.append(a);letter.append(0);tonext.pop(tonext.index(a));tonext.pop(tonext.index(tonext[b+2]))
                  if type(a) == int and type(tonext[b+2]) == str and len(letter) < 2 and tonext.index("=")<tonext.index(a) and tonext[b+2].isalpha():
                      letter.append(a);letter.append(0);tonext.pop(tonext.index(a))
                  elif type(a) == str and tonext.index("=")<tonext.index(a) and a.isalpha(): # If the letter after equal
                      letter.append(a);letter.append(1);tonext.pop(tonext.index(a))
                  print(letter)
          except IndexError:
              print("")
      for b,a in enumerate(tonext):
        try:
          if "+" in tonext:
              what.append("+")
              if type(a) == int and type(tonext[b+2]) == int:
                  nums.append(int(str(a) + str(tonext[b+2])))
              elif type(a) == int and type(tonext[b+2]) == str:
                  nums.append(int(a))
          elif "-" in tonext:
              what.append("-")
              if type(a) == int and type(tonext[b+2]) == int:
                  nums.append(int(str(a) + str(tonext[b+2])))
              elif type(a) == int and type(tonext[b+2]) == str:
                  nums.append(int(a))
        except IndexError:
              print("")
      if 1 in letter:
          if "+" in what:
            print(f"{letter[0]} = {sum(nums)}")
          elif "-" in what:
              for a,b in enumerate(nums[1::]):
                  try:
                    c = np.subtract(nums[0], b);nums[0] = c;nums.pop(1)
                  except:
                      print("")
              print(f'X = {c}')
          if "-" in what:
              acs = len(tonext)-1 
              for a,b in enumerate(tonext):
                  if acs - tonext.index("=") > 1:
                      for a in tonext[tonext.index("=")+1::]:
                          lastnum.append(str(a))
                      print(lastnum)
      elif 0 in letter:
          if "-" in what:
            for a,b in enumerate(nums):
                if nums.index(b) != 0:
                    nums.pop(a)
            nums.pop(1)
            for a,b in enumerate(tonext):
              acs = len(tonext)-1 
              if acs - tonext.index("=") > 1:
                  for a in tonext[tonext.index("=")+1::]:
                     lastnum.append(str(a))
                  lastnum = "".join(lastnum)
                  for a in tonext[tonext.index("=")+1::]:
                     tonext.pop(tonext.index(a))
                  nums.append(int("".join(lastnum)))
            print(f"{letter[0]} = {sum(nums)}")
          if "+" in what:
            for a,b in enumerate(tonext):
              acs = len(tonext)-1 
              if acs - tonext.index("=") > 1:
                  for a in tonext[tonext.index("=")+1::]:
                     lastnum.append(str(a))
                  lastnum = "".join(lastnum)
                  for a in tonext[tonext.index("=")+1::]:
                     tonext.pop(tonext.index(a))
                  nums.append(int("".join(lastnum)))
              nums.reverse()
              for a,b in enumerate(nums[1::]):
                      c = np.subtract(nums[0], b);nums[0] = c;nums.pop(1)
                      print(f"{letter[0]} = {c}")
s = str(input(" האוושמ בותכת : "))
test = First(s)
#              if type(b) != int and tonext.index("=")>a:
 #                     tonext.pop(a)
   #           elif type(b) == int and tonext.index("=")>a:
  #                    tonext.append(a);tonext.pop(a)
   #           for a,b in enumerate(tonext):
    #              if type(tonext[0]) == int:
    #                tonext[len(tonext)-1] = tonext[len(tonext)-1] + tonext[0];tonext.pop(0)