def equation(a, b):
    x1 = float(a.split(';')[0])
    y1 = float(a.split(';')[1])
    x2 = float(b.split(';')[0])
    y2 = float(b.split(';')[1])
    if x2 - x1 != 0 and y2 - y1 != 0:
        k = (y1 - y2) / (x1 - x2)
    else:
        k = 0
    if x1 == x2:
        print(float(x1))
    elif y1 == y2:
        print(float(y1))
    else:
        h = y2 - k * x2
        print(float(k), float(h))
