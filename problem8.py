import math

PI = math.pi
E = math.e

input = [1, 2, 3, 4]
input_len = len(input)
L = 1
M = input_len
root = math.floor(math.sqrt(input_len))
for i in range(root, 0, -1):
    if input_len % i == 0:
        L = i
        M = int(input_len / i)
        break

input_2d = []
output_2d = []
for i in range(L):
    input_2d.append(input[i::L])
    output_2d.append([0 for _ in range(M)])
for p in range(L):
    for q in range(M):
        pq_result = 0
        for l in range(L):
            factor_1 = E ** -(2j * PI * l * q / input_len)
            inner_output = 0
            for m in range(M):
                w_m = E ** -(2j * PI * m*q / M)
                inner_output += (input_2d[l][m] * w_m)
            factor_2 = E ** -(2j * PI * l * p / L)
            pq_result += (factor_1 * inner_output * factor_2)
        output_2d[p][q] = pq_result
output = []
for row in output_2d:
    output.extend(row)

print(output)