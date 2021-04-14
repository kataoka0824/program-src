# ポンプの一覧を読み込む。
import csv
with open("Snow.pumps.csv", encoding="utf-8") as fp:
    pumps = list(csv.reader(fp))
del pumps[0]

# get_bisector(c0, c1)
#   c0--c1 間の垂直二等分線を求める。
def get_bisector(c0, c1):
    # c0--c1間のベクトルを求める。
    vx = c1[0] - c0[0]
    vy = c1[1] - c0[1]
    # c0--c1間の中点を求める。
    px = (c1[0]+c0[0])/2
    py = (c1[1]+c0[1])/2
    # 垂直二等分線は q0--q1 を通る直線。
    q0 = [px-vy, py+vx]
    q1 = [px+vy, py-vx]
    return [q0, q1]

# get_intersect(p0, p1, q0, q1):
#   線分 p0--p1 と直線 q0--q1 の交点を求める。
def get_intersect(p0, p1, q0, q1):
    # 直線 p,q の方向ベクトル(vpx,vpy)および(vqx,vqy)を求める。
    vpx = p1[0] - p0[0]
    vpy = p1[1] - p0[1]
    vqx = q1[0] - q0[0]
    vqy = q1[1] - q0[1]
    # 行列式 d を求める。0 の場合は並行なので交差しない。
    d = vpy*vqx - vpx*vqy
    if d == 0:
        return []
    # 交点を t と s で媒介変数表示する:
    #   p0[0] + t*vpx == q0[0] + s*vqx
    #   p0[1] + t*vpy == q0[1] + s*vqy
    # 以上を t と s に対して解く:
    t = (vqy*(p0[0]-q0[0]) - vqx*(p0[1]-q0[1])) / d
    s = (vpy*(p0[0]-q0[0]) - vpx*(p0[1]-q0[1])) / d
    # 求めた点 t が線分 p0--p1 の範囲外にあるときは交差しない。
    if t < 0 or 1 <= t:
        return []
    # tを使って交点の座標を求める。
    return [p0[0]+t*vpx, p0[1]+t*vpy]

# cut_polygon(c0, poly, q):
#   点 c0 をセンターとする領域 poly を、直線 q でカットする。
def cut_polygon(c0, poly, q):
    # 多角形 poly の線分のうち、q と交差するものを列挙する。
    interpoint = []
    interline = []
    n = len(poly)
    for i in range(n):
        # 線分 p0--p1 と直線 q の交点を求める。
        p0 = poly[i]
        p1 = poly[(i+1) % n]
        p2 = get_intersect(p0, p1, q[0], q[1])
        if len(p2) == 2:
            # 交差している場合は、その交点および
            # 「何番目の線分が交差しているか」を記録する。
            interpoint.append(p2)
            interline.append(i)
    # poly と q の交点が 2個の場合、
    # それらの交点で polyを切り取る。
    if len(interpoint) == 2:
        t0 = interpoint[0]  # 交点0
        t1 = interpoint[1]  # 交点1
        i0 = interline[0]
        i1 = interline[1]
        # poly[i0+1] 〜 poly[i1] の点を [t0, t1] で置き換える。
        poly = poly[:i0+1] + [t0,t1] + poly[i1+1:]
    return poly

# pumpsの各座標をセンターとしてヴォロノイ図を作成。
centers = []
polygons = []
for row in pumps:
    x = float(row[3])
    y = float(row[4])

# show_poly(poly)
#   多角形を指定された色で表示する。
def show_poly(poly, color):
    s = ""
    for p in poly:
        s = s + f" {p[0]},{p[1]}"
    print(f'<polygon points="{s}" fill="{color}" stroke="black" />')
    return

# 各領域をSVGで描画。
print("<svg xmlns='http://www.w3.org/2000/svg' version='1.1' width='800' height='800'>")
for poly in polygons:
    show_poly(poly, 'none')
print("</svg>")
