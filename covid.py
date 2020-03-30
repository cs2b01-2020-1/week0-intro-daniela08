import os

genoma1 = "AY274119.txt"
genoma2 = "AY278488.2.txt"
genoma3 = "MN908947.txt"
genoma4 = "MN988668.txt"
genoma5 = "MN988669.txt"

files = [genoma1, genoma2, genoma3, genoma4, genoma5]
matrix = [[0]*(len(files)+1) for i in range(len(files)+1)]
