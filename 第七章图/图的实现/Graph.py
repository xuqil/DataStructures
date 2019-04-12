class Graph:
    # 基本图类，采用邻接矩阵表示
    def __init__(self, mat, unconn=0):
        vnum = len(mat)
        for x in mat:
            if len(x) != vnum:  # 检查是否为方阵
                raise ValueError("不是方阵")
        self._mat = [mat[i][:] for i in range(vnum)]  # 拷贝
        self._unconn = unconn
        self._vnum =vnum

    def vertex_num(self):
        return self._vnum

    def _invalid(self, v):
        return 0 > v or v >= self._vnum

    def add_vertex(self):
        raise Exception("不支持添加图")

    def add_edge(self, vi, vj, val=1):
        if self._invalid(vi) or self._invalid(vj):
            raise Exception("error")
        self._mat[vi][vj] = val

    def get_edge(self, vi, vj):
        if self._invalid(vi) or self._invalid(vj):
            raise Exception("error")
        return self._mat[vi][vj]

    def out_edges(self, vi):
        if self._invalid(vi):
            raise Exception("error")
        return self._out_edges(self._mat[vi], self._unconn)

    @staticmethod
    def _out_edges(row, unconn):
        edges = []
        for i in range(row):
            if row[i] != unconn:
                edges.append((i, row[i]))
        return edges

    def __str__(self):
        return "[\n" + ",\n".join(map(str, self._mat))\
               + "\n" + "\nUnconnected:" + str(self._unconn)
