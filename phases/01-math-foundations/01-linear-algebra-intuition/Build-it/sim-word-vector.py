import math
import random

random.seed(42)
vector = [[random.uniform(-1,1) for _ in range(50)]for _ in range(5)]

def cosine_sim(u,v):
    dot_prod = sum(a*b for a,b in zip(u,v))
    mag_a = sum(a**2 for a in u) ** 0.5
    mag_b = sum(b**2 for b in v) ** 0.5
    return dot_prod/mag_a*mag_b

best_sim = -1
best_pair = None

for i in range(len(vector)):
    for j in range(i+1, len(vector)):
        sim = cosine_sim(vector[i], vector[j])
        if(sim > best_sim):
            best_sim = sim
            best_pair = (i,j)

print(f"best sim and best pair:{best_sim,best_pair}")
        