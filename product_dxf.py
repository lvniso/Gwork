import  draw
from dxfwrite import DXFEngine as dxf
cnt = 0
num = 0
x1,y1=0,0
res = []
with open('data/tmp.txt','rU',encoding='utf-8') as file:
    for line in file:
        line = line.strip()
        ans = line.split(',')
        res.append(ans)

for ans in res:
    if cnt%5 == 0:
        drawing = dxf.drawing('data/pic'+str(num)+'.dxf')
        num += 1
    d = max(ans[0], ans[1], ans[2], ans[3],ans[4])
    draw.draw_single(drawing, x1, y1,ans[0],ans[1],ans[2],ans[3],ans[4],1)
    draw.draw_single(drawing, x1, y1-2*d, ans[0], ans[1], ans[2], ans[3],ans[4], 2)
    draw.draw_single(drawing, x1, y1-4*d, ans[0], ans[1], ans[2], ans[3], ans[4],3)
    if cnt%5 == 4:
        drawing.save()
    x1 += 2*d
    cnt += 1

if cnt%5 < 4:
    drawing.save()