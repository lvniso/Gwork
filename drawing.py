from dxfwrite import DXFEngine as dxf
import math

SIN = math.sin(math.radians(40))
COS = math.cos(math.radians(40))


def draw_single(drawing, x1, y1, l1, l2, l3, l4, angle):
    d = (l1 - l3) / 2
    if angle == 1:
        x2, y2 = x1, y1 + l2
        x8, y8 = x1 + l1, y1
        x7, y7 = x8, y2
        x3, y3 = x2 + d, y2
        x4, y4 = x3, y3 - l4
        x5, y5 = x4 + l3, y4
        x6, y6 = x5, y2
    elif angle == 2:
        x2, y2 = x1 + l2 * SIN, y1 + l2 * COS
        x3, y3 = x2 + d * COS, y2 - d * SIN
        x4, y4 = x3 - l4 * SIN, y3 - l4 * COS
        x5, y5 = x4 + l3 * COS, y4 - l3 * SIN
        x6, y6 = x5 + l4 * SIN, y5 + l4 * COS
        x7, y7 = x6 + d * COS, y6 - d * SIN
        x8, y8 = x7 - l2 * SIN, y7 - l2 * COS
    else:
        x2, y2 = x1 - l2 * SIN, y1 + l2 * COS
        x3, y3 = x2 + d * COS, y2 + d * SIN
        x4, y4 = x3 + l4 * SIN, y3 - l4 * COS
        x5, y5 = x4 + l3 * COS, y4 + l3 * SIN
        x6, y6 = x5 - l4 * SIN, y5 + l4 * COS
        x7, y7 = x6 + d * COS, y6 + d * SIN
        x8, y8 = x7 + l2 * SIN, y7 - l2 * COS

    drawing.add(
        dxf.polyline(
            points=[(x1, y1), (x2, y2), (x3, y3), (x4, y4), (x5, y5), (x6, y6), (x7, y7), (x8, y8), (x1, y1)]
        )
    )


def cal(S, x, rate):
    x *= 10
    S *= 100
    ans = int(S // (x * x))
    result = []
    for a in range(3, ans + 1):
        for b in range(1, ans + 1):
            if a * x * b * x < S * (1 - rate):
                continue
            for c in range(1, ans + 1):
                # print(a,b,c)
                if a - c < 2:
                    continue
                for d in range(1, ans + 1):
                    if d >= b:
                        continue
                    if (a * b - c * d) * x * x >= S * (1 - rate) and (a * b - c * d) * x * x <= S * (1 + rate):
                        # result.append([a*x,b*x,c*x,d*x,(a*b-c*d)*x*x])
                        # result.append([a * x / 10, b * x / 10, c * x / 10, d * x / 10, 1])
                        # result.append([a * x / 10, b * x / 10, c * x / 10, d * x / 10, 2])
                        # result.append([a * x / 10, b * x / 10, c * x / 10, d * x / 10, 3])
                        result.append([a * x / 10, b * x / 10, c * x / 10, d * x / 10])
                    elif (a * b - c * d) * x * x > S * (1 + rate):
                        continue
    return result


def main(path):
    S = 1200
    x = 9
    ss = [1200, 1500, 1800, 2100, 2400, 2700, 3000]
    xx = [9, 8.7, 8.4, 8.1, 7.8, 7.5, 7.2, 6.9, 6.6, 6.3, 6]
    rate = 0.02
    res = cal(S, x, rate)
    # for ans in res:
    #     print(ans)
    #     print(ans)
    #     print(ans)
    # print(res)
    # print(len(res))

    # file = open('data/result2.txt', 'w', encoding='utf-8')
    # for i in ss:
    #     for j in xx:
    #         res = cal(i, j, rate)
    #         print(i, j, len(res), res)
    #         file.write(str(i) + ' ' + str(j) + ' ' + str(len(res)) + ' ' + str(res) + '\n')
    # file.close()
    cnt,tmp= 0,0
    with open('data/ans2.txt','rU',encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            ans = line.split(',')
            # print(ans)
            # print(cnt)
            if cnt!=0:
                cnt-=1
                continue
            if len(ans) == 4:
                res.append([float(ans[0]),float(ans[1]),float(ans[2]),float(ans[3])])
                cnt = tmp
            elif len(ans) == 1:
                numm = ans[0].split(' ')
                # print(numm)
                if len(numm) == 3:
                    num = int(numm[2])
                    if num < 50:
                        cnt = 21
                        tmp = 21
                    elif num < 100:
                        cnt = 39
                        tmp = 39
                    elif num <300:
                        cnt = 125
                        tmp=125
                    elif num <500:
                        cnt = 210
                        tmp=210
                    elif num <1000:
                        cnt = 339
                        tmp = 339
                    else:
                        cnt = 525
                        tmp =525
                continue

    print(len(res))
    print(res)
    x1, y1 = 0, 0
    cnt = 0
    num = 0
    for ans in res:
        if cnt % 5 == 0:
            drawing = dxf.drawing('data/pic' + str(num) + '.dxf')
            num += 1
        d = max(ans[0], ans[1], ans[2], ans[3])
        draw_single(drawing, x1, y1, ans[0], ans[1], ans[2], ans[3], 1)
        draw_single(drawing, x1, y1 - 2 * d, ans[0], ans[1], ans[2], ans[3], 2)
        draw_single(drawing, x1, y1 - 4 * d, ans[0], ans[1], ans[2], ans[3], 3)
        if cnt % 5 == 4:
            drawing.save()
        x1 += 2 * d
        cnt += 1

    if cnt % 5 < 4:
        drawing.save()


if __name__ == '__main__':
    main('')


