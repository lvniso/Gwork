from dxfwrite import DXFEngine as dxf
import math
SIN = math.sin(math.radians(40))
COS = math.cos(math.radians(40))
def draw_single(drawing,x1,y1,l1,l2,l3,l4,l5,angle):
    points = cal_points(x1,y1,l1,l2,l3,l4,l5,angle)
    drawing.add(dxf.polyline(points))

def cal_points(x1,y1,l1,l2,l3,l4,l5,angle):
    d = (l1 - l3) / 2
    if angle == 1:
        x2,y2 = x1,y1+l2
        x3,y3 = x2+d,y2
        x4,y4 = x3,y3-l4
        x5,y5 = x4+l3,y4
        x6,y6 = x5,y5+l5
        x8, y8 = x1 + l1, y1
        x7, y7 = x8, y6

    elif angle == 2:
        x2, y2 = x1+l2*SIN, y1 + l2*COS
        x3, y3 = x2+d*COS, y2-d*SIN
        x4, y4 = x3-l4*SIN, y3 - l4*COS
        x5, y5 = x4 + l3*COS, y4-l3*SIN
        x6, y6 = x5+l5*SIN, y5+l5*COS
        x7, y7 = x6+d*COS, y6-d*SIN
        x8, y8 = x7-(l5+l2-l4)*SIN,y7-(l5+l2-l4)*COS
    else:
        x2, y2 = x1-l2*SIN, y1 + l2*COS
        x3, y3 = x2 + d*COS, y2+d*SIN
        x4, y4 = x3+l4 * SIN, y3-l4 * COS
        x5, y5 = x4 + l3 * COS, y4 + l3 * SIN
        x6, y6 = x5 - l5 * SIN, y5 + l5 * COS
        x7, y7 = x6 + d * COS, y6 + d * SIN
        x8, y8 = x7 + (l5+l2-l4) * SIN, y7 - (l5+l2-l4) * COS

    points=[(x1,y1),(x2,y2),(x3,y3),(x4,y4),(x5,y5),(x6,y6),(x7,y7),(x8,y8),(x1,y1)]
    return points



def cal(S,x,rate):
    x *= 10
    S *= 100
    ans = int(S//(x*x))
    # print(ans)
    result = []
    for a in range(3,ans+1):
        for b in range(1,ans+1):
            if a*x*b*x < S*(1-rate):
                continue
            for c in range(1, a-1):
                for d in range(1, b):
                    for e in range(1,b):
                        if (a*b-c*max(d,e)-(a-c)*abs(d-e)/2)*x*x >= S*(1-rate) and (a*b-c*max(d,e)-(a-c)*abs(d-e)/2)*x*x <= S*(1+rate):
                                # result.append([a*x,b*x,c*x,d*x,(a*b-c*d)*x*x])
                            result.append([a * x/10, b * x/10, c * x/10, d * x/10, e*x/10, 1])
                            result.append([a * x/10, b * x/10, c * x/10, d * x/10, e*x/10,2])
                            result.append([a * x/10, b * x/10, c * x/10, d * x/10, e*x/10,3])
                            # result.append([a * x / 10, b * x / 10, c * x / 10, d * x / 10, e * x / 10])
                        elif (a*b-c*max(d,e)-(a-c)*abs(d-e)/2)*x*x > S*(1+rate):
                            continue
    return result



def main(path):
    S = 1500
    x = 9
    ss = [1200,1500,1800,2100,2400,2700,3000]
    xx = [9,8.7,8.4,8.1,7.8,7.5,7.2,6.9,6.6,6.3,6]
    rate = 0.02
    res = cal(S, x,rate)
    print(res)
    # for ans in res:
    #      print(ans)
    # #     print(ans)
    # #     print(ans)
    # file = open('data/result.txt','w',encoding='utf-8')
    # for i in ss:
    #     for j in xx:
    #         if i>=2100:
    #             rate = 0.01
    #         if j < 7:
    #             rate = 0.01
    #         if i>=2100 and j < 8:
    #             rate = 0.005
    #         if i > 2700:
    #             rate = 0.002
    #         res = cal(i, j, rate)
    #         print(i,j,len(res),res)
    #         file.write(str(i)+' '+str(j)+' '+str(len(res))+' '+str(res)+'\n')
    # file.close()
    # print(res)

    # res = []
    # cnt,tmp= 0,0
    # with open('data/ans1.txt','rU',encoding='utf-8') as file:
    #     for line in file:
    #         line = line.strip()
    #         ans = line.split(',')
    #         # print(ans)
    #         # print(cnt)
    #         if cnt!=0:
    #             cnt-=1
    #             continue
    #         if len(ans) == 5:
    #             # res.append([float(ans[0]),float(ans[1]),float(ans[2]),float(ans[3]),float(ans[4])])
    #             res.append([float(ans[0]), float(ans[1]), float(ans[2]), float(ans[3]), float(ans[4]),1])
    #             res.append([float(ans[0]), float(ans[1]), float(ans[2]), float(ans[3]), float(ans[4]),2])
    #             res.append([float(ans[0]), float(ans[1]), float(ans[2]), float(ans[3]), float(ans[4]),3])
    #             cnt = tmp
    #         elif len(ans) == 1:
    #             numm = ans[0].split(' ')
    #             if len(numm) == 3:
    #                 num = int(numm[2])
    #                 # print(num)
    #                 if num < 300:
    #                     cnt = 200
    #                     tmp = 200
    #                 elif num < 500:
    #                     cnt = 400
    #                     tmp = 400
    #                 elif num < 800:
    #                     cnt = 600
    #                     tmp = 600
    #                 elif num < 1000:
    #                     cnt = 600
    #                     tmp = 600
    #                 elif num < 2000:
    #                     cnt = 1500
    #                     tmp = 1500
    #                 elif num <3000:
    #                     cnt = 2000
    #                     tmp=2000
    #                 elif num <4000:
    #                     cnt = 3200
    #                     tmp=3200
    #                 elif num <5000:
    #                     cnt = 3600
    #                     tmp=3600
    #                 elif num <8000:
    #                     cnt = 5600
    #                     tmp = 5600
    #                 elif num <15000:
    #                     cnt = 9000
    #                     tmp =9000
    #                 else:
    #                     cnt = 10000
    #                     tmp = 10000
    #             continue
    # print(res)
    # print(len(res))

    x1, y1 = 0, 0
    cnt = 0
    num = 0
    for ans in res:
        if cnt%5 == 0:
            drawing = dxf.drawing('data/pic'+str(num)+'.dxf')
            num += 1
        d = max(ans[0], ans[1], ans[2], ans[3])
        draw_single(drawing, x1, y1,ans[0],ans[1],ans[2],ans[3],ans[4],1)
        draw_single(drawing, x1, y1-2*d, ans[0], ans[1], ans[2], ans[3], ans[4],2)
        draw_single(drawing, x1, y1-4*d, ans[0], ans[1], ans[2], ans[3], ans[4],3)
        if cnt%5 == 4:
            drawing.save()
        x1 += 2*d
        cnt += 1

    if cnt%5 < 4:
        drawing.save()


if __name__ == '__main__':
    main('')
    

