def arithematic_arranger(problems, answ = False):
    if len(problems)>5:
        print("Error: Too many problems.")
        quit()

    first_no = []
    second_no = []
    ans = []
    op = []
    n, j = 0, 0
    for problem in problems:
        problem = problem.split()
        first_no.append(problem[0])
        op.append(problem[1])
        second_no.append(problem[2])
        if problem[1] not in "+-":
            print("Error: Operator must be '+' or '-'.")
            quit()
        try:
            if problem[1] == "+":
                ans.append(int(problem[0]) + int(problem[2]))
            elif problem[1] == "-":
                ans.append(int(problem[0]) - int(problem[2]))
        except ValueError:
            print("Error: Numbers must only contain digits.")
        if int(problem[0]) > 9999 or int(problem[2]) > 9999:
            print("Error: Numbers cannot be more than four digits.")
            quit()
        j = len(problem[0])
        if len(problem[2]) > len(problem[0]):
            j = len(problem[2])
        n = n+1
    for i in range(0, n):
        print(first_no[i].rjust(j+6), end="")
    print("  ")
    for i in range(0, n):
        print("    ", end="")
        print(op[i], end="")
        print(second_no[i].rjust(j+1), end="")
    print("")
    for i in range(0, n):
        print("    ", end="")
        for i in range(0, j+2):
            print("_", end="")
    print("")



    if answ == True:

        for i in range(0, n):
            print(str(ans[i]).rjust(j+6), end="")


arithematic_arranger(["5 + 23", "2 - 22", "5 + 22", "22 - 33"], answ = True)
