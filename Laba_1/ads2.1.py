def orientation(p, q, r):
    val = (q[1] - p[1]) * (r[0] - q[0]) - (q[0] - p[0]) * (r[1] - q[1])
    return 0 if val == 0 else (1 if val > 0 else 2)

def jarvis_march(pts):
    n = len(pts)
    if n < 3: return None

    hull = []

    start = pts.index(min(pts))
    p = start

    while True:
        hull.append(pts[p])
        q = (p + 1) % n

        for r in range(n):
            if orientation(pts[p], pts[r], pts[q]) == 2:
                q = r

        p = q
        if p == start: break  # Замкнули круг

    return hull if len(hull) >= 3 else None

n = int(input("Кол-во точек: "))
points = [tuple(map(float, input(f"{i + 1}: ").split())) for i in range(n)]
res = jarvis_march(points)
print("Оболочка:", res if res else "Не существует")

#6
#0 0
#10 0
#10 10
#0 10
#5 5
#2 12