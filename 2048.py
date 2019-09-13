n = int(input())
MainL = []
for i in range(4):
    MainL.append(list(map(int,input().strip().split())))

def UpKey():
    global unchanged_flag
    for col in range(0, 4):
        if MainL[0][col] == 0 and MainL[1][col] != 0 and MainL[2][col] == 0 and MainL[3][col] == 0:
            MainL[0][col] = MainL[1][col]
            MainL[1][col] = 0
            MainL[2][col] = 0
            MainL[3][col] = 0

        elif MainL[0][col] == 0 and MainL[1][col] == 0 and MainL[2][col] != 0 and MainL[3][col] == 0:
            MainL[0][col] = MainL[2][col]
            MainL[1][col] = 0
            MainL[2][col] = 0
            MainL[3][col] = 0

        elif MainL[0][col] == 0 and MainL[1][col] == 0 and MainL[2][col] == 0 and MainL[3][col] != 0:
            MainL[0][col] = MainL[3][col]
            MainL[1][col] = 0
            MainL[2][col] = 0
            MainL[3][col] = 0

        elif MainL[0][col] == 0 and MainL[1][col] != 0 and MainL[2][col] != 0 and MainL[2][col] != MainL[1][col] \
                and MainL[3][col] == 0:
            MainL[0][col] = MainL[1][col]
            MainL[1][col] = MainL[2][col]
            MainL[2][col] = 0
            MainL[3][col] = 0

        elif MainL[0][col] == 0 and MainL[1][col] != 0 and MainL[2][col] == 0 and MainL[3][col] != 0 \
                and MainL[3][col] != MainL[1][col]:
            MainL[0][col] = MainL[1][col]
            MainL[1][col] = MainL[3][col]
            MainL[2][col] = 0
            MainL[3][col] = 0

        elif MainL[0][col] == 0 and MainL[1][col] == 0 and MainL[2][col] != 0 and MainL[3][col] != 0 \
                and MainL[3][col] != MainL[2][col]:
            MainL[0][col] = MainL[2][col]
            MainL[1][col] = MainL[3][col]
            MainL[2][col] = 0
            MainL[3][col] = 0

        elif MainL[0][col] == 0 and MainL[1][col] != 0 and MainL[2][col] != 0 and MainL[3][col] != 0 \
                and MainL[3][col] != MainL[2][col] and MainL[1][col] != MainL[2][col]:
            MainL[0][col] = MainL[1][col]
            MainL[1][col] = MainL[2][col]
            MainL[2][col] = MainL[3][col]
            MainL[3][col] = 0

        elif MainL[0][col] != 0 and MainL[1][col] == 0 and MainL[2][col] != 0 and MainL[3][col] == 0 \
                and MainL[2][col] != MainL[0][col]:
            MainL[0][col] = MainL[0][col]
            MainL[1][col] = MainL[2][col]
            MainL[2][col] = 0
            MainL[3][col] = 0

        elif MainL[0][col] != 0 and MainL[1][col] == 0 and MainL[2][col] == 0 and MainL[3][col] != 0 \
                and MainL[3][col] != MainL[0][col]:
            MainL[0][col] = MainL[0][col]
            MainL[1][col] = MainL[3][col]
            MainL[2][col] = 0
            MainL[3][col] = 0

        elif MainL[0][col] != 0 and MainL[1][col] == 0 and MainL[2][col] != 0 and MainL[3][col] != 0 \
                and MainL[3][col] != MainL[2][col] and MainL[0][col] != MainL[2][col]:
            MainL[0][col] = MainL[0][col]
            MainL[1][col] = MainL[2][col]
            MainL[2][col] = MainL[3][col]
            MainL[3][col] = 0

        elif MainL[0][col] != 0 and MainL[1][col] != 0 and MainL[2][col] == 0 and MainL[3][col] != 0 \
                and MainL[3][col] != MainL[1][col] and MainL[1][col] != MainL[0][col]:
            MainL[0][col] = MainL[0][col]
            MainL[1][col] = MainL[1][col]
            MainL[2][col] = MainL[3][col]
            MainL[3][col] = 0

        elif MainL[0][col] != 0 and MainL[1][col] == MainL[0][col] and MainL[2][col] == 0 and MainL[3][col] != 0:
            MainL[0][col] *= 2
            MainL[1][col] = MainL[3][col]
            MainL[2][col] = 0
            MainL[3][col] = 0

        elif MainL[0][col] != 0 and MainL[1][col] == MainL[0][col] and (
                MainL[2][col] != MainL[3][col] or (MainL[2][col] == 0 and MainL[3][col] == 0)):
            MainL[0][col] *= 2
            MainL[1][col] = MainL[2][col]
            MainL[2][col] = MainL[3][col]
            MainL[3][col] = 0

        elif MainL[0][col] != 0 and MainL[1][col] == 0 and MainL[2][col] == MainL[0][col]:
            MainL[0][col] *= 2
            MainL[1][col] = MainL[3][col]
            MainL[2][col] = 0
            MainL[3][col] = 0

        elif MainL[0][col] != 0 and MainL[1][col] == 0 and MainL[2][col] == 0 and MainL[3][col] == MainL[0][col]:
            MainL[0][col] *= 2
            MainL[1][col] = 0
            MainL[2][col] = 0
            MainL[3][col] = 0

        elif MainL[0][col] == 0 and MainL[1][col] != 0 and MainL[2][col] == MainL[1][col]:
            MainL[0][col] = MainL[1][col];
            MainL[0][col] *= 2
            MainL[1][col] = MainL[3][col]
            MainL[2][col] = 0
            MainL[3][col] = 0

        elif MainL[0][col] == 0 and MainL[1][col] != 0 and MainL[2][col] == 0 and MainL[3][col] == MainL[1][col]:
            MainL[0][col] = MainL[1][col];
            MainL[0][col] *= 2
            MainL[1][col] = 0
            MainL[2][col] = 0
            MainL[3][col] = 0

        elif MainL[0][col] != 0 and MainL[1][col] != 0 and MainL[2][col] == MainL[1][col] and MainL[0][col] != MainL[1][
            col]:
            MainL[0][col] = MainL[0][col]
            MainL[1][col] *= 2
            MainL[2][col] = MainL[3][col]
            MainL[3][col] = 0

        elif MainL[0][col] != 0 and MainL[1][col] != 0 and MainL[2][col] == 0 and MainL[3][col] == MainL[1][col] \
                and MainL[0][col] != MainL[1][col]:
            MainL[0][col] = MainL[0][col]
            MainL[1][col] *= 2
            MainL[2][col] = 0
            MainL[3][col] = 0

        elif MainL[0][col] == 0 and MainL[1][col] == 0 and MainL[2][col] != 0 and MainL[3][col] == MainL[2][col]:
            MainL[0][col] = MainL[2][col];
            MainL[0][col] *= 2
            MainL[1][col] = 0
            MainL[2][col] = 0
            MainL[3][col] = 0

        elif MainL[0][col] != 0 and MainL[1][col] == 0 and MainL[2][col] != 0 and MainL[2][col] != MainL[0][col] \
                and MainL[3][col] == MainL[2][col]:
            MainL[0][col] = MainL[0][col]
            MainL[1][col] = MainL[2][col];
            MainL[1][col] *= 2
            MainL[2][col] = 0
            MainL[3][col] = 0

        elif MainL[0][col] == 0 and MainL[1][col] != 0 and MainL[2][col] != 0 and MainL[2][col] != MainL[1][col] \
                and MainL[3][col] == MainL[2][col]:
            MainL[0][col] = MainL[1][col]
            MainL[1][col] = MainL[2][col];
            MainL[1][col] *= 2
            MainL[2][col] = 0
            MainL[3][col] = 0

        elif MainL[0][col] != 0 and MainL[1][col] != 0 and MainL[1][col] != MainL[0][col] and MainL[2][col] != 0 \
                and MainL[2][col] != MainL[1][col] and MainL[3][col] == MainL[2][col]:
            MainL[0][col] = MainL[0][col]
            MainL[1][col] = MainL[1][col]
            MainL[2][col] *= 2
            MainL[3][col] = 0

        elif MainL[0][col] != 0 and MainL[1][col] == MainL[0][col] and MainL[2][col] != 0 and MainL[3][col] == MainL[2][
            col]:
            MainL[0][col] *= 2
            MainL[1][col] = MainL[2][col];
            MainL[1][col] *= 2
            MainL[2][col] = 0
            MainL[3][col] = 0
    return

def DownKey():
    global unchanged_flag
    for col in range(0, 4):

        if MainL[3][col] == 0 and MainL[2][col] != 0 and MainL[1][col] == 0 and MainL[0][col] == 0:
            MainL[3][col] = MainL[2][col]
            MainL[2][col] = 0
            MainL[1][col] = 0
            MainL[0][col] = 0

        elif MainL[3][col] == 0 and MainL[2][col] == 0 and MainL[1][col] != 0 and MainL[0][col] == 0:
            MainL[3][col] = MainL[1][col]
            MainL[2][col] = 0
            MainL[1][col] = 0
            MainL[0][col] = 0

        elif MainL[3][col] == 0 and MainL[2][col] == 0 and MainL[1][col] == 0 and MainL[0][col] != 0:
            MainL[3][col] = MainL[0][col]
            MainL[2][col] = 0
            MainL[1][col] = 0
            MainL[0][col] = 0

        elif MainL[3][col] == 0 and MainL[2][col] != 0 and MainL[1][col] != 0 and MainL[1][col] != MainL[2][col] \
                and MainL[0][col] == 0:
            MainL[3][col] = MainL[2][col]
            MainL[2][col] = MainL[1][col]
            MainL[1][col] = 0
            MainL[0][col] = 0

        elif MainL[3][col] == 0 and MainL[2][col] != 0 and MainL[1][col] == 0 and MainL[0][col] != 0 \
                and MainL[0][col] != MainL[2][col]:
            MainL[3][col] = MainL[2][col]
            MainL[2][col] = MainL[0][col]
            MainL[1][col] = 0
            MainL[0][col] = 0

        elif MainL[3][col] == 0 and MainL[2][col] == 0 and MainL[1][col] != 0 and MainL[0][col] != 0 \
                and MainL[0][col] != MainL[1][col]:
            MainL[3][col] = MainL[1][col]
            MainL[2][col] = MainL[0][col]
            MainL[1][col] = 0
            MainL[0][col] = 0

        elif MainL[3][col] == 0 and MainL[2][col] != 0 and MainL[1][col] != 0 and MainL[0][col] != 0 \
                and MainL[0][col] != MainL[1][col] and MainL[2][col] != MainL[1][col]:
            MainL[3][col] = MainL[2][col]
            MainL[2][col] = MainL[1][col]
            MainL[1][col] = MainL[0][col]
            MainL[0][col] = 0

        elif MainL[3][col] != 0 and MainL[2][col] == 0 and MainL[1][col] != 0 and MainL[0][col] == 0 \
                and MainL[1][col] != MainL[3][col]:
            MainL[3][col] = MainL[3][col]
            MainL[2][col] = MainL[1][col]
            MainL[1][col] = 0
            MainL[0][col] = 0

        elif MainL[3][col] != 0 and MainL[2][col] == 0 and MainL[1][col] == 0 and MainL[0][col] != 0 \
                and MainL[0][col] != MainL[3][col]:
            MainL[3][col] = MainL[3][col]
            MainL[2][col] = MainL[0][col]
            MainL[1][col] = 0
            MainL[0][col] = 0

        elif MainL[3][col] != 0 and MainL[2][col] == 0 and MainL[1][col] != 0 and MainL[0][col] != 0 \
                and MainL[0][col] != MainL[1][col] and MainL[1][col] != MainL[3][col]:
            MainL[3][col] = MainL[3][col]
            MainL[2][col] = MainL[1][col]
            MainL[1][col] = MainL[0][col]
            MainL[0][col] = 0

        elif MainL[3][col] != 0 and MainL[2][col] != 0 and MainL[1][col] == 0 and MainL[0][col] != 0 \
                and MainL[0][col] != MainL[2][col] and MainL[2][col] != MainL[3][col]:
            MainL[3][col] = MainL[3][col]
            MainL[2][col] = MainL[2][col]
            MainL[1][col] = MainL[0][col]
            MainL[0][col] = 0

        elif MainL[3][col] != 0 and MainL[2][col] == MainL[3][col] and MainL[1][col] == 0 and MainL[0][col] != 0:
            MainL[3][col] *= 2
            MainL[2][col] = MainL[0][col]
            MainL[1][col] = 0
            MainL[0][col] = 0

        elif MainL[3][col] != 0 and MainL[2][col] == MainL[3][col] and (
                MainL[1][col] != MainL[0][col] or (MainL[1][col] == 0 and MainL[0][col] == 0)):
            MainL[3][col] *= 2
            MainL[2][col] = MainL[1][col]
            MainL[1][col] = MainL[0][col]
            MainL[0][col] = 0

        elif MainL[3][col] != 0 and MainL[2][col] == 0 and MainL[1][col] == MainL[3][col]:
            MainL[3][col] *= 2
            MainL[2][col] = MainL[0][col]
            MainL[1][col] = 0
            MainL[0][col] = 0

        elif MainL[3][col] != 0 and MainL[2][col] == 0 and MainL[1][col] == 0 and MainL[0][col] == MainL[3][col]:
            MainL[3][col] *= 2
            MainL[2][col] = 0
            MainL[1][col] = 0
            MainL[0][col] = 0

        elif MainL[3][col] == 0 and MainL[2][col] != 0 and MainL[1][col] == MainL[2][col]:
            MainL[3][col] = MainL[2][col];
            MainL[3][col] *= 2
            MainL[2][col] = MainL[0][col]
            MainL[1][col] = 0
            MainL[0][col] = 0

        elif MainL[3][col] == 0 and MainL[2][col] != 0 and MainL[1][col] == 0 and MainL[0][col] == MainL[2][col]:
            MainL[3][col] = MainL[2][col];
            MainL[3][col] *= 2
            MainL[2][col] = 0
            MainL[1][col] = 0
            MainL[0][col] = 0

        elif MainL[3][col] != 0 and MainL[2][col] != 0 and MainL[1][col] == MainL[2][col] and MainL[3][col] != MainL[2][
            col]:
            MainL[3][col] = MainL[3][col]
            MainL[2][col] *= 2
            MainL[1][col] = MainL[0][col]
            MainL[0][col] = 0

        elif MainL[3][col] != 0 and MainL[2][col] != 0 and MainL[1][col] == 0 and MainL[0][col] == MainL[2][col]:
            MainL[3][col] = MainL[3][col]
            MainL[2][col] *= 2
            MainL[1][col] = 0
            MainL[0][col] = 0

        elif MainL[3][col] == 0 and MainL[2][col] == 0 and MainL[1][col] != 0 and MainL[0][col] == MainL[1][col]:
            MainL[3][col] = MainL[1][col];
            MainL[3][col] *= 2
            MainL[2][col] = 0
            MainL[1][col] = 0
            MainL[0][col] = 0

        elif MainL[3][col] != 0 and MainL[2][col] == 0 and MainL[1][col] != 0 and MainL[1][col] != MainL[3][col] \
                and MainL[0][col] == MainL[1][col]:
            MainL[3][col] = MainL[3][col]
            MainL[2][col] = MainL[1][col];
            MainL[2][col] *= 2
            MainL[1][col] = 0
            MainL[0][col] = 0

        elif MainL[3][col] == 0 and MainL[2][col] != 0 and MainL[1][col] != 0 and MainL[1][col] != MainL[2][col] \
                and MainL[0][col] == MainL[1][col]:
            MainL[3][col] = MainL[2][col]
            MainL[2][col] = MainL[1][col];
            MainL[2][col] *= 2
            MainL[1][col] = 0
            MainL[0][col] = 0

        elif MainL[3][col] != 0 and MainL[2][col] != 0 and MainL[2][col] != MainL[3][col] and MainL[1][col] != 0 \
                and MainL[1][col] != MainL[2][col] and MainL[0][col] == MainL[1][col]:
            MainL[3][col] = MainL[3][col]
            MainL[2][col] = MainL[2][col]
            MainL[1][col] *= 2
            MainL[0][col] = 0

        elif MainL[3][col] != 0 and MainL[2][col] == MainL[3][col] and MainL[1][col] != 0 and MainL[0][col] == MainL[1][
            col]:
            MainL[3][col] *= 2
            MainL[2][col] = MainL[1][col];
            MainL[2][col] *= 2
            MainL[1][col] = 0
            MainL[0][col] = 0

    return

def LeftKey():
    global unchanged_flag
    for row in range(0, 4):

        if MainL[row][0] == 0 and MainL[row][1] != 0 and MainL[row][2] == 0 and MainL[row][3] == 0:
            MainL[row][0] = MainL[row][1]
            MainL[row][1] = 0
            MainL[row][2] = 0
            MainL[row][3] = 0

        elif MainL[row][0] == 0 and MainL[row][1] == 0 and MainL[row][2] != 0 and MainL[row][3] == 0:
            MainL[row][0] = MainL[row][2]
            MainL[row][1] = 0
            MainL[row][2] = 0
            MainL[row][3] = 0

        elif MainL[row][0] == 0 and MainL[row][1] == 0 and MainL[row][2] == 0 and MainL[row][3] != 0:
            MainL[row][0] = MainL[row][3]
            MainL[row][1] = 0
            MainL[row][2] = 0
            MainL[row][3] = 0

        elif MainL[row][0] == 0 and MainL[row][1] != 0 and MainL[row][2] != 0 and MainL[row][2] != MainL[row][1] \
                and MainL[row][3] == 0:
            MainL[row][0] = MainL[row][1]
            MainL[row][1] = MainL[row][2]
            MainL[row][2] = 0
            MainL[row][3] = 0

        elif MainL[row][0] == 0 and MainL[row][1] != 0 and MainL[row][2] == 0 and MainL[row][3] != 0 \
                and MainL[row][3] != MainL[row][1]:
            MainL[row][0] = MainL[row][1]
            MainL[row][1] = MainL[row][3]
            MainL[row][2] = 0
            MainL[row][3] = 0

        elif MainL[row][0] == 0 and MainL[row][1] == 0 and MainL[row][2] != 0 and MainL[row][3] != 0 \
                and MainL[row][3] != MainL[row][2]:
            MainL[row][0] = MainL[row][2]
            MainL[row][1] = MainL[row][3]
            MainL[row][2] = 0
            MainL[row][3] = 0

        elif MainL[row][0] == 0 and MainL[row][1] != 0 and MainL[row][2] != 0 and MainL[row][3] != 0 \
                and MainL[row][3] != MainL[row][2] and MainL[row][1] != MainL[row][2]:
            MainL[row][0] = MainL[row][1]
            MainL[row][1] = MainL[row][2]
            MainL[row][2] = MainL[row][3]
            MainL[row][3] = 0

        elif MainL[row][0] != 0 and MainL[row][1] == 0 and MainL[row][2] != 0 and MainL[row][3] == 0 \
                and MainL[row][2] != MainL[row][0]:
            MainL[row][0] = MainL[row][0]
            MainL[row][1] = MainL[row][2]
            MainL[row][2] = 0
            MainL[row][3] = 0

        elif MainL[row][0] != 0 and MainL[row][1] == 0 and MainL[row][2] == 0 and MainL[row][3] != 0 \
                and MainL[row][3] != MainL[row][0]:
            MainL[row][0] = MainL[row][0]
            MainL[row][1] = MainL[row][3]
            MainL[row][2] = 0
            MainL[row][3] = 0

        elif MainL[row][0] != 0 and MainL[row][1] == 0 and MainL[row][2] != 0 and MainL[row][3] != 0 \
                and MainL[row][3] != MainL[row][2] and MainL[row][0] != MainL[row][2]:
            MainL[row][0] = MainL[row][0]
            MainL[row][1] = MainL[row][2]
            MainL[row][2] = MainL[row][3]
            MainL[row][3] = 0

        elif MainL[row][0] != 0 and MainL[row][1] != 0 and MainL[row][2] == 0 and MainL[row][3] != 0 \
                and MainL[row][3] != MainL[row][1] and MainL[row][1] != MainL[row][0]:
            MainL[row][0] = MainL[row][0]
            MainL[row][1] = MainL[row][1]
            MainL[row][2] = MainL[row][3]
            MainL[row][3] = 0

        elif MainL[row][0] != 0 and MainL[row][1] == MainL[row][0] and MainL[row][2] == 0 and MainL[row][3] != 0:
            MainL[row][0] *= 2
            MainL[row][1] = MainL[row][3]
            MainL[row][2] = 0
            MainL[row][3] = 0

        elif MainL[row][0] != 0 and MainL[row][1] == MainL[row][0] and (
                MainL[row][2] != MainL[row][3] or (MainL[row][2] == 0 and MainL[row][3] == 0)):
            MainL[row][0] *= 2
            MainL[row][1] = MainL[row][2]
            MainL[row][2] = MainL[row][3]
            MainL[row][3] = 0

        elif MainL[row][0] != 0 and MainL[row][1] == 0 and MainL[row][2] == MainL[row][0]:
            MainL[row][0] *= 2
            MainL[row][1] = MainL[row][3]
            MainL[row][2] = 0
            MainL[row][3] = 0

        elif MainL[row][0] != 0 and MainL[row][1] == 0 and MainL[row][2] == 0 and MainL[row][3] == MainL[row][0]:
            MainL[row][0] *= 2
            MainL[row][1] = 0
            MainL[row][2] = 0
            MainL[row][3] = 0

        elif MainL[row][0] == 0 and MainL[row][1] != 0 and MainL[row][2] == MainL[row][1]:
            MainL[row][0] = MainL[row][1];
            MainL[row][0] *= 2
            MainL[row][1] = MainL[row][3]
            MainL[row][2] = 0
            MainL[row][3] = 0

        elif MainL[row][0] == 0 and MainL[row][1] != 0 and MainL[row][2] == 0 and MainL[row][3] == MainL[row][1]:
            MainL[row][0] = MainL[row][1];
            MainL[row][0] *= 2
            MainL[row][1] = 0
            MainL[row][2] = 0
            MainL[row][3] = 0

        elif MainL[row][0] != 0 and MainL[row][1] != 0 and MainL[row][2] == MainL[row][1] and MainL[row][0] != \
                MainL[row][1]:
            MainL[row][0] = MainL[row][0]
            MainL[row][1] *= 2
            MainL[row][2] = MainL[row][3]
            MainL[row][3] = 0

        elif MainL[row][0] != 0 and MainL[row][1] != 0 and MainL[row][2] == 0 and MainL[row][3] == MainL[row][1] \
                and MainL[row][0] != MainL[row][1]:
            MainL[row][0] = MainL[row][0]
            MainL[row][1] *= 2
            MainL[row][2] = 0
            MainL[row][3] = 0

        elif MainL[row][0] == 0 and MainL[row][1] == 0 and MainL[row][2] != 0 and MainL[row][3] == MainL[row][2]:
            MainL[row][0] = MainL[row][2];
            MainL[row][0] *= 2
            MainL[row][1] = 0
            MainL[row][2] = 0
            MainL[row][3] = 0

        elif MainL[row][0] != 0 and MainL[row][1] == 0 and MainL[row][2] != 0 and MainL[row][2] != MainL[row][0] \
                and MainL[row][3] == MainL[row][2]:
            MainL[row][0] = MainL[row][0]
            MainL[row][1] = MainL[row][2];
            MainL[row][1] *= 2
            MainL[row][2] = 0
            MainL[row][3] = 0

        elif MainL[row][0] == 0 and MainL[row][1] != 0 and MainL[row][2] != 0 and MainL[row][2] != MainL[row][1] \
                and MainL[row][3] == MainL[row][2]:
            MainL[row][0] = MainL[row][1]
            MainL[row][1] = MainL[row][2];
            MainL[row][1] *= 2
            MainL[row][2] = 0
            MainL[row][3] = 0

        elif MainL[row][0] != 0 and MainL[row][1] != 0 and MainL[row][1] != MainL[row][0] and MainL[row][2] != 0 \
                and MainL[row][2] != MainL[row][1] and MainL[row][3] == MainL[row][2]:
            MainL[row][0] = MainL[row][0]
            MainL[row][1] = MainL[row][1]
            MainL[row][2] *= 2
            MainL[row][3] = 0

        elif MainL[row][0] != 0 and MainL[row][1] == MainL[row][0] and MainL[row][2] != 0 and MainL[row][3] == \
                MainL[row][2]:
            MainL[row][0] *= 2
            MainL[row][1] = MainL[row][2];
            MainL[row][1] *= 2
            MainL[row][2] = 0
            MainL[row][3] = 0
    return

def RightKey():
    global unchanged_flag
    for row in range(0, 4):

        if MainL[row][3] == 0 and MainL[row][2] != 0 and MainL[row][1] == 0 and MainL[row][0] == 0:
            MainL[row][3] = MainL[row][2]
            MainL[row][2] = 0
            MainL[row][1] = 0
            MainL[row][0] = 0

        elif MainL[row][3] == 0 and MainL[row][2] == 0 and MainL[row][1] != 0 and MainL[row][0] == 0:
            MainL[row][3] = MainL[row][1]
            MainL[row][2] = 0
            MainL[row][1] = 0
            MainL[row][0] = 0

        elif MainL[row][3] == 0 and MainL[row][2] == 0 and MainL[row][1] == 0 and MainL[row][0] != 0:
            MainL[row][3] = MainL[row][0]
            MainL[row][2] = 0
            MainL[row][1] = 0
            MainL[row][0] = 0

        elif MainL[row][3] == 0 and MainL[row][2] != 0 and MainL[row][1] != 0 and MainL[row][1] != MainL[row][2] \
                and MainL[row][0] == 0:
            MainL[row][3] = MainL[row][2]
            MainL[row][2] = MainL[row][1]
            MainL[row][1] = 0
            MainL[row][0] = 0

        elif MainL[row][3] == 0 and MainL[row][2] != 0 and MainL[row][1] == 0 and MainL[row][0] != 0 \
                and MainL[row][0] != MainL[row][2]:
            MainL[row][3] = MainL[row][2]
            MainL[row][2] = MainL[row][0]
            MainL[row][1] = 0
            MainL[row][0] = 0

        elif MainL[row][3] == 0 and MainL[row][2] == 0 and MainL[row][1] != 0 and MainL[row][0] != 0 \
                and MainL[row][0] != MainL[row][1]:
            MainL[row][3] = MainL[row][1]
            MainL[row][2] = MainL[row][0]
            MainL[row][1] = 0
            MainL[row][0] = 0

        elif MainL[row][3] == 0 and MainL[row][2] != 0 and MainL[row][1] != 0 and MainL[row][0] != 0 \
                and MainL[row][0] != MainL[row][1] and MainL[row][2] != MainL[row][1]:
            MainL[row][3] = MainL[row][2]
            MainL[row][2] = MainL[row][1]
            MainL[row][1] = MainL[row][0]
            MainL[row][0] = 0

        elif MainL[row][3] != 0 and MainL[row][2] == 0 and MainL[row][1] != 0 and MainL[row][0] == 0 \
                and MainL[row][1] != MainL[row][3]:
            MainL[row][3] = MainL[row][3]
            MainL[row][2] = MainL[row][1]
            MainL[row][1] = 0
            MainL[row][0] = 0

        elif MainL[row][3] != 0 and MainL[row][2] == 0 and MainL[row][1] == 0 and MainL[row][0] != 0 \
                and MainL[row][0] != MainL[row][3]:
            MainL[row][3] = MainL[row][3]
            MainL[row][2] = MainL[row][0]
            MainL[row][1] = 0
            MainL[row][0] = 0

        elif MainL[row][3] != 0 and MainL[row][2] == 0 and MainL[row][1] != 0 and MainL[row][0] != 0 \
                and MainL[row][0] != MainL[row][1] and MainL[row][1] != MainL[row][3]:
            MainL[row][3] = MainL[row][3]
            MainL[row][2] = MainL[row][1]
            MainL[row][1] = MainL[row][0]
            MainL[row][0] = 0

        elif MainL[row][3] != 0 and MainL[row][2] != 0 and MainL[row][1] == 0 and MainL[row][0] != 0 \
                and MainL[row][0] != MainL[row][2] and MainL[row][2] != MainL[row][3]:
            MainL[row][3] = MainL[row][3]
            MainL[row][2] = MainL[row][2]
            MainL[row][1] = MainL[row][0]
            MainL[row][0] = 0

        elif MainL[row][3] != 0 and MainL[row][2] == MainL[row][3] and MainL[row][1] == 0 and MainL[row][0] != 0:
            MainL[row][3] *= 2
            MainL[row][2] = MainL[row][0]
            MainL[row][1] = 0
            MainL[row][0] = 0

        elif MainL[row][3] != 0 and MainL[row][2] == MainL[row][3] and (
                MainL[row][1] != MainL[row][0] or (MainL[row][1] == 0 and MainL[row][0] == 0)):
            MainL[row][3] *= 2
            MainL[row][2] = MainL[row][1]
            MainL[row][1] = MainL[row][0]
            MainL[row][0] = 0

        elif MainL[row][3] != 0 and MainL[row][2] == 0 and MainL[row][1] == MainL[row][3]:
            MainL[row][3] *= 2
            MainL[row][2] = MainL[row][0]
            MainL[row][1] = 0
            MainL[row][0] = 0

        elif MainL[row][3] != 0 and MainL[row][2] == 0 and MainL[row][1] == 0 and MainL[row][0] == MainL[row][3]:
            MainL[row][3] *= 2
            MainL[row][2] = 0
            MainL[row][1] = 0
            MainL[row][0] = 0

        elif MainL[row][3] == 0 and MainL[row][2] != 0 and MainL[row][1] == MainL[row][2]:
            MainL[row][3] = MainL[row][2];
            MainL[row][3] *= 2
            MainL[row][2] = MainL[row][0]
            MainL[row][1] = 0
            MainL[row][0] = 0

        elif MainL[row][3] == 0 and MainL[row][2] != 0 and MainL[row][1] == 0 and MainL[row][0] == MainL[row][2]:
            MainL[row][3] = MainL[row][2];
            MainL[row][3] *= 2
            MainL[row][2] = 0
            MainL[row][1] = 0
            MainL[row][0] = 0

        elif MainL[row][3] != 0 and MainL[row][2] != 0 and MainL[row][1] == MainL[row][2] and MainL[row][3] != \
                MainL[row][2]:
            MainL[row][3] = MainL[row][3]
            MainL[row][2] *= 2
            MainL[row][1] = MainL[row][0]
            MainL[row][0] = 0

        elif MainL[row][3] != 0 and MainL[row][2] != 0 and MainL[row][1] == 0 and MainL[row][0] == MainL[row][2]:
            MainL[row][3] = MainL[row][3]
            MainL[row][2] *= 2
            MainL[row][1] = 0
            MainL[row][0] = 0

        elif MainL[row][3] == 0 and MainL[row][2] == 0 and MainL[row][1] != 0 and MainL[row][0] == MainL[row][1]:
            MainL[row][3] = MainL[row][1];
            MainL[row][3] *= 2
            MainL[row][2] = 0
            MainL[row][1] = 0
            MainL[row][0] = 0

        elif MainL[row][3] != 0 and MainL[row][2] == 0 and MainL[row][1] != 0 and MainL[row][1] != MainL[row][3] \
                and MainL[row][0] == MainL[row][1]:
            MainL[row][3] = MainL[row][3]
            MainL[row][2] = MainL[row][1];
            MainL[row][2] *= 2
            MainL[row][1] = 0
            MainL[row][0] = 0

        elif MainL[row][3] == 0 and MainL[row][2] != 0 and MainL[row][1] != 0 and MainL[row][1] != MainL[row][2] \
                and MainL[row][0] == MainL[row][1]:
            MainL[row][3] = MainL[row][2]
            MainL[row][2] = MainL[row][1];
            MainL[row][2] *= 2
            MainL[row][1] = 0
            MainL[row][0] = 0

        elif MainL[row][3] != 0 and MainL[row][2] != 0 and MainL[row][2] != MainL[row][3] and MainL[row][1] != 0 \
                and MainL[row][1] != MainL[row][2] and MainL[row][0] == MainL[row][1]:
            MainL[row][3] = MainL[row][3]
            MainL[row][2] = MainL[row][2]
            MainL[row][1] *= 2
            MainL[row][0] = 0

        elif MainL[row][3] != 0 and MainL[row][2] == MainL[row][3] and MainL[row][1] != 0 and MainL[row][0] == \
                MainL[row][1]:
            MainL[row][3] *= 2
            MainL[row][2] = MainL[row][1];
            MainL[row][2] *= 2
            MainL[row][1] = 0
            MainL[row][0] = 0

    return

if __name__ == '__main__':

    if n == 1:  # "w"键
        UpKey()
    elif n == 2:  # "s"键
        DownKey()
    elif n == 3:  # "a"键
        LeftKey()
    elif n == 4:  # "d"键
        RightKey()

    for i in range(4):
        for j in range(4):
            if j < 3:
                print(MainL[i][j], end = ' ')
            else:
                print(MainL[i][j])