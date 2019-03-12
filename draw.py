from dxfwrite import DXFEngine as dxf
import math
SIN = math.sin(math.radians(40))
COS = math.cos(math.radians(40))
def draw_single(drawing,x1,y1,l1,l2,l3,l4,angle):
    d = (l1 - l3) / 2
    if angle == 1:
        x2,y2 = x1,y1+l2
        x8,y8 = x1+l1,y1
        x7,y7 = x8,y2
        x3,y3 = x2+d,y2
        x4,y4 = x3,y3-l4
        x5,y5 = x4+l3,y4
        x6,y6 = x5,y2
    elif angle == 2:
        x2, y2 = x1+l2*SIN, y1 + l2*COS
        x3, y3 = x2+d*COS, y2-d*SIN
        x4, y4 = x3-l4*SIN, y3 - l4*COS
        x5, y5 = x4 + l3*COS, y4-l3*SIN
        x6, y6 = x5+l4*SIN, y5+l4*COS
        x7, y7 = x6+d*COS, y6-d*SIN
        x8, y8 = x7-l2*SIN,y7-l2*COS
    else:
        x2, y2 = x1-l2*SIN, y1 + l2*COS
        x3, y3 = x2 + d*COS, y2+d*SIN
        x4, y4 = x3+l4 * SIN, y3-l4 * COS
        x5, y5 = x4 + l3 * COS, y4 + l3 * SIN
        x6, y6 = x5 - l4 * SIN, y5 + l4 * COS
        x7, y7 = x6 + d * COS, y6 + d * SIN
        x8, y8 = x7 + l2 * SIN, y7 - l2 * COS

    drawing.add(
        dxf.polyline(
            points=[(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5),(x6,y6),(x7,y7),(x8,y8),(x1,y1)]
        )
    )


def cal(S,x):
    rate = 0.015
    ans = S//(x*x)
    result = []
    for a in range(3,ans+1):
        for b in range(1,ans+1):
            if a*x*b*x < S*(1-rate):
                continue
            for c in range(1, ans + 1):
                # print(a,b,c)
                if a-c< 2:
                    continue
                for d in range(1, ans + 1):
                    if d >= b:
                        continue
                    if (a*b-c*d)*x*x >= S*(1-rate) and (a*b-c*d)*x*x <= S*(1+rate):
                        result.append([a*x,b*x,c*x,d*x,(a*b-c*d)*x*x])
                    elif (a*b-c*d)*x*x > S*(1+rate):
                        continue

    return result

def main(path):
    S = 1200
    x = 9
    res = cal(S, x)
    # for ans in res:
    #     print(ans)
    #     print(ans)
    #     print(ans)
    print(res)
    print(len(res))
    x1, y1 = 0, 0
    cnt = 0
    num = 0
    for ans in res:
        if cnt%5 == 0:
            drawing = dxf.drawing(path+'/data'+str(num)+'.dxf')
            num += 1
        d = max(ans[0], ans[1], ans[2], ans[3])
        draw_single(drawing, x1, y1,ans[0],ans[1],ans[2],ans[3],1)
        draw_single(drawing, x1, y1-2*d, ans[0], ans[1], ans[2], ans[3], 2)
        draw_single(drawing, x1, y1-4*d, ans[0], ans[1], ans[2], ans[3], 3)
        if cnt%5 == 4:
            drawing.save()
        x1 += 2*d
        cnt += 1

    if cnt%5 < 4:
        drawing.save()


if __name__ == '__main__':
    main('')
    

