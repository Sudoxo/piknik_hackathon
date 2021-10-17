dni = {"poniedziałek":0,"wtorek":1,"środa":2,"czwartek":3,"piątek":4,"sobota":5,"niedziela":6}
x = input().split(" ")
print(list(dni)[(dni[x[0]]+int(x[1]))%7])
