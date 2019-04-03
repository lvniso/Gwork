def selectN(total, energy, n):
    res = []
    for i in range(len(energy)):
        area = total[i][0] * total[i][1] - total[i][2] * max(total[i][3], total[i][4]) - (total[i][0] - total[i][
            2]) * abs(total[i][3] - total[i][4]) / 2
        ans = energy[i] / area * 100
        res.append([total[i][0], total[i][1], total[i][2], total[i][3], total[i][4], total[i][5], area, ans])
    res.sort(key=lambda x: x[7])
    # print(res[:n])
    if len(res) < n:
        return res
    return res[:n]