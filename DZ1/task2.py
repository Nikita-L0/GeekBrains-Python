for X in range(0,2):
    for Y in range(0,2):
        for Z in range(0,2):
            if X == 0:
                X1 = True
            else:
                X1 = False
            if Y == 0:
                Y1 = True
            else:
                Y1 = False
            if Z == 0:
                Z1 = True
            else:
                Z1 = False
            if (not (X1 or Y1 or Z1)) == ((not X1) and (not Y1) and (not Z1)):
                print(f'not ({X} or {Y} or {Z}) = (not {X}) and (not {Y}) and (not {Z}) is TRUE')
            else:
                print(f'not ({X} or {Y} or {Z}) = (not {X}) and (not {Y}) and (not {Z}) is FALSE')
        Z = 0
    Y = 0
