result = []
with open("input2", mode="r") as file:
    n = int(file.readline())
    for i in range(n):
        line = file.readline().split()
        result.append(line)
    m = int(file.readline())
    for i in range(m):
        line = file.readline().replace("\n", '')
        for j in range(n):
            if line in result[j]:
             print(result[j][0])
