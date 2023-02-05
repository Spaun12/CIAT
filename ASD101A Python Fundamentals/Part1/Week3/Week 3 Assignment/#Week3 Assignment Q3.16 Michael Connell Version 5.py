#Week3 Assignment Q3.16 Michael Connell Version 5still not working right


import evaluate

a = 2
b = 4
c = 6

comparison = input("Enter a comparison phrase (e.g. 'a >= -1' or 'a <= b'): ")

result = evaluate.evaluate(comparison, variables={"a": a, "b": b, "c": c})

if result:
    print("True")
else:
    print("False")

