import random
count =0.0
inside_circle = 0.0
while True:
    x = random.random()
    y = random.random()
    distance = (x**2 + y**2)**0.5
    count = count+1
    if distance < 1:
        inside_circle = inside_circle  + 1

    ratio = 4 * (inside_circle/count)
    expected = ratio
    print " {}  :: {}".format(count, expected)
