import math

class Vector:
    def __init__(self, compo):
        self.comp = list(compo)
        self.dim = len(self.comp)

    def __add__(self, other):
        return Vector([a+b for a, b in zip(self.comp, other.comp)])

    def __sub__(self, other):
        return Vector([a-b for a,b in zip(self.comp, other.comp)])

    def dot(self,other):
        return sum(a*b for a, b in zip(self.comp, other.comp))

    def magnitude(self):
        return sum(a**2 for a in self.comp) ** 0.5

    def normalization(self):
        mag = self.magnitude()
        return Vector([a/mag for a in self.comp])

    def cosine_similarity(self, other):
        return self.dot(other) / (self.magnitude() * other.magnitude())

    def angle_between(self, other):
        return math.degrees(math.acos(max(-1.0, min(1.0, self.dot(other)/self.magnitude() * other.magnitude()))))

    def __repr__(self):
        return f"Vector({self.comp})" 

v = Vector([3,4])
w = Vector([1,2])
v1 = Vector([1, 0])
v2 = Vector([0, 1])

print(f"Angle: {v1.angle_between(v2)}°")

print(f"sum: {v+w}")
print(f"sub: {v-w}")

print(f"dot: {v.dot(w)}")
print(f"magnitude: {v.magnitude()}")
print(f"normalized: {v.normalization()}")
print(f"cosine similarity: {v.cosine_similarity(w):.4f}")

class Metrix:

    def __init__(self, rows):
        self.rows = [list(row) for row in rows]
        self.dim = [len(self.rows), len(self.rows[0])]

    def __add__(self, other):
        return Metrix([[self.rows[i][j] + other.rows[i][j] for i in range(self.dim[0])]for j in range(self.dim[1])])

    def __matmul__(self, other):

        if(isinstance(other, Vector)):
            return Vector([sum(self.rows[i][j]*other.comp[j] for j in range(self.dim[1])) 
            for i in range(self.dim[0])])

        rows = []
        for i in range(self.dim[0]):
            row = []
            for j in range(other.dim[1]):
                row.append(sum(self.rows[i][k]*other.rows[k][j] for k in range(self.dim[1])))
            rows.append(row)
        return Metrix(rows)

    def transpose(self):
        return Metrix([[self.rows[j][i] for j in range(self.dim[0])] for i in range(self.dim[1])])

    def __repr__(self):
        return f"Metrix({self.rows})"


rotation_90 = Metrix([[0, -1], [1, 0]])
point = Vector([3, 1])

rotated = rotation_90 @ point
print(f"Original: {point}")
print(f"Rotated 90°: {rotated}")

        

    

