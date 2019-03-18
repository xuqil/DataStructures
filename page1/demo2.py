# 图色法（贪心法）
def coloring(G):  # 做图G的着色
    color = 0
    groups = set()
    verts = G
    while verts:
        new_group = set()
        for v in list(verts):
            if not v:
                new_group.add(v)
                verts.remove(v)
        groups.add((color, new_group))
        color += 1
    return groups

G = [1, 2, 3, 5]
# coloring(G)
a = set()
a.add((0, 'ds'))
print(type(a))
print(a)