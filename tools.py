import os

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


def check_filename(filename):
    n=[0]
    def check_meta(file_name):
        file_name_new = file_name
        if os.path.isfile(file_name):
            file_name_new=file_name[:file_name.rfind('.')]+'_'+str(n[0])+file_name[file_name.rfind('.'):]
            n[0]+=1
        if os.path.isfile(file_name_new):
            file_name_new=check_meta(file_name)
        return file_name_new

    return_name = check_meta(filename)
    return return_name