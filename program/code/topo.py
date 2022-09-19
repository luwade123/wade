dijk_list = [[9999 for _ in range(45)] for _ in range(45)]

dijk_inedx = 0
while(dijk_inedx<18):
    dijk_list[dijk_inedx][dijk_inedx+18] = 1
    dijk_list[dijk_inedx][dijk_inedx+19] = 1
    dijk_list[dijk_inedx][dijk_inedx+20] = 1
    dijk_list[dijk_inedx+1][dijk_inedx+18] = 1
    dijk_list[dijk_inedx+1][dijk_inedx+19] = 1
    dijk_list[dijk_inedx+1][dijk_inedx+20] = 1
    dijk_list[dijk_inedx+2][dijk_inedx+18] = 1
    dijk_list[dijk_inedx+2][dijk_inedx+19] = 1
    dijk_list[dijk_inedx+2][dijk_inedx+20] = 1
    dijk_list[dijk_inedx+18][dijk_inedx] = 1
    dijk_list[dijk_inedx+19][dijk_inedx] = 1
    dijk_list[dijk_inedx+20][dijk_inedx] = 1
    dijk_list[dijk_inedx+18][dijk_inedx+1] = 1
    dijk_list[dijk_inedx+19][dijk_inedx+1] = 1
    dijk_list[dijk_inedx+20][dijk_inedx+1] = 1
    dijk_list[dijk_inedx+18][dijk_inedx+2] = 1
    dijk_list[dijk_inedx+19][dijk_inedx+2] = 1
    dijk_list[dijk_inedx+20][dijk_inedx+2] = 1
    dijk_inedx+=3

for dijk_inedx in range(18,36):
    for j in range(36,45):
        dijk_list[dijk_inedx][j] = 1
        dijk_list[j][dijk_inedx] = 1

for dijk_inedx in dijk_list:
    print(dijk_inedx)