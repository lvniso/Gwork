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



if __name__ == '__main__':
    drawing = dxf.drawing('shapes.dxf')
    draw_single(drawing,0,0,27, 54, 9, 27,3)
    drawing.save()