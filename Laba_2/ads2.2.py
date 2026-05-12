import math, itertools

# 1. Пересечение прямых
def intersect_lines(l1, l2):
    a1, b1, c1 = l1
    a2, b2, c2 = l2
    det = a1 * b2 - a2 * b1
    return ((b1 * c2 - b2 * c1) / det, (c1 * a2 - c2 * a1) / det) if abs(det) > 1e-9 else None

# 2. Прямая и отрезок
def intersect_line_segment(a, b, c, p1, p2):
    return (a * p1[0] + b * p1[1] + c) * (a * p2[0] + b * p2[1] + c) <= 0

# 3. Два отрезка
def intersect_segments(p1, p2, p3, p4):
    def v_prod(o, a, b):
        return (a[0]-o[0])*(b[1]-o[1]) - (a[1]-o[1])*(b[0]-o[0])

    cp1 = v_prod(p1, p2, p3)
    cp2 = v_prod(p1, p2, p4)
    cp3 = v_prod(p3, p4, p1)
    cp4 = v_prod(p3, p4, p2)

    # Если они пересекаются крест-накрест
    if ((cp1 > 0 and cp2 < 0) or (cp1 < 0 and cp2 > 0)) and \
       ((cp3 > 0 and cp4 < 0) or (cp3 < 0 and cp4 > 0)):
        return True

    def on_segment(p, a, b):
        return min(a[0], b[0]) <= p[0] <= max(a[0], b[0]) and \
               min(a[1], b[1]) <= p[1] <= max(a[1], b[1])

    if cp1 == 0 and on_segment(p3, p1, p2): return True
    if cp2 == 0 and on_segment(p4, p1, p2): return True
    if cp3 == 0 and on_segment(p1, p3, p4): return True
    if cp4 == 0 and on_segment(p2, p3, p4): return True

    return False

# 4. Прямая и окружность
def intersect_line_circle(a, b, c, xc, yc, r):
    return (abs(a * xc + b * yc + c) / math.sqrt(a ** 2 + b ** 2)) <= r

# 5. Отрезок и окружность
def intersect_segment_circle(p1, p2, xc, yc, r):
    d1 = math.dist(p1, (xc, yc))
    d2 = math.dist(p2, (xc, yc))

    if (d1 < r and d2 > r) or (d1 > r and d2 < r):
        return True

    if d1 > r and d2 > r:

        a = p1[1] - p2[1]
        b = p2[0] - p1[0]
        c = -a * p1[0] - b * p1[1]

        if not intersect_line_circle(a, b, c, xc, yc, r):
            return False

        dot1 = (xc - p1[0]) * (p2[0] - p1[0]) + (yc - p1[1]) * (p2[1] - p1[1])
        dot2 = (xc - p2[0]) * (p1[0] - p2[0]) + (yc - p2[1]) * (p1[1] - p2[1])
        return dot1 > 0 and dot2 > 0

    return False

# 6. Две окружности
def intersect_circles(c1, r1, c2, r2):
    return abs(r1 - r2) <= math.dist(c1, c2) <= r1 + r2

# Вспомогательная: Точка в треугольнике (через площади)
def is_in_tri(tri, p):
    def area(a, b, c): return abs((a[0] * (b[1] - c[1]) + b[0] * (c[1] - a[1]) + c[0] * (a[1] - b[1])) / 2.0)

    a, b, c = tri
    return abs(area(a, b, c) - (area(p, a, b) + area(p, b, c) + area(p, c, a))) < 1e-9

def solve():
    n = int(input("Кол-во точек: "))
    pts = [tuple(map(float, input(f"{i + 1}: ").split())) for i in range(n)]
    triangles = list(itertools.combinations(pts, 3))
    found = False

    for t1, t2 in itertools.combinations(triangles, 2):
        edges1 = [(t1[0], t1[1]), (t1[1], t1[2]), (t1[2], t1[0])]
        edges2 = [(t2[0], t2[1]), (t2[1], t2[2]), (t2[2], t2[0])]

        # Если стороны пересекаются — вложенности нет
        if any(intersect_segments(s1[0], s1[1], s2[0], s2[1]) for s1 in edges1 for s2 in edges2):
            continue

        # Если границы не пересекаются, проверяем вхождение вершин
        if all(is_in_tri(t2, p) for p in t1):
            print(f"Треугольник {t1} в {t2}");
            found = True
        elif all(is_in_tri(t1, p) for p in t2):
            print(f"Треугольник {t2} в {t1}");
            found = True

    if not found: print("Вложенных треугольников нет")

solve()
#6
#0 0
#10 0
#5 10
#4 2
#6 2
#5 4