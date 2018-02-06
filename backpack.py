import random

class Backpack:
    """docstring for Backpack."""
    def __init__(self, weight=0, benefit=0):
        self.weight = weight
        self.benefit = benefit

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return "(" + str(self.weight) + ", "+str(self.benefit) + ")"

n = 4
capacity = random.randint(20, 50)

objs = [Backpack(random.randint(1,20), random.randint(1,20)) for i in range(n)]
print(objs)

def backpack_rec(
    solution = [-1 for i in range(n)],
    stage = 0,
    backpack_end = [-1 for i in range(n)],
    weight_end = 0, benefit_end = 0):
    i = 0 # this is the option of binary tree (0 or 1)
    print(solution)
    if stage > n-1:
        print("Objets --> ", objs)
        print("Solution --> ", backpack_end)
        print("Weight --> ", weight_end, " Kg")
        print("Benefit --> ", benefit_end, " $")
        return()

    while solution[stage] != 1:
        solution[stage] = i
        if valid(solution, stage, objs):
            weight_end, benefit_end = update_solution(
                solution,
                objs,
                backpack_end,
                weight_end,
                benefit_end)
            backpack_rec(
                solution,
                stage+1,
                backpack_end,
                weight_end,
                benefit_end)
        i += 1

    solution[stage] = -1

def valid(solution, stage, objs):
    weight = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            weight += objs[i].weight
    if weight > capacity:
        return(False)
    return(True)

def update_solution(solution, objs, backpack_end, weight_end, benefit_end):
    _weight_end = 0
    _benefit_end = 0
    for i in range(len(solution)):
        if solution[i] == 1:
            _weight_end += objs[i].weight
            _benefit_end += objs[i].benefit

    if _benefit_end > benefit_end:
        backpack_end = solution[:]
        weight_end = _weight_end
        benefit_end = _benefit_end

    return(weight_end, benefit_end)

backpack_rec()
