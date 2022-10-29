def absDiffr(a, b):

    if (a >= 0 and b >= 0 and a >= b):
        diff = (a - b)
    elif (a >= 0 and b >= 0 and b >= a):
        diff = (b - a)
    elif (a < 0 and b < 0 and a >= b):
        diff = ((-b) - (-a))
    elif (a < 0 and b < 0 and b >= a):
        diff = ((-a) - (-b))
    elif (a < 0 and b >= 0):
        diff = ((-a) + b)
    elif (a >= 0 and b < 0):
        diff = (a + (-b))
    else:
        diff = (a + b)

    return diff


  #from absDiff import absDiffr
  #i = absDiffr(5, -10)
