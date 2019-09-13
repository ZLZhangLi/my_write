n = int(input())
MainL = []
for i in range(4):
    MainL.append(list(map(int,input().strip().split())))


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

if __name__ == '__main__':

    LeftKey()
    for i in range(4):
        for j in range(4):
            if j < 3:
                print(MainL[i][j], end = ' ')
            else:
                print(MainL[i][j])