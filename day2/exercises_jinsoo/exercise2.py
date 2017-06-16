import numpy as np

def fibonacci_gen(n):
    fibo_list = [1,1]
    for i in range(2,n):
        next_seq = fibo_list[i-1] + fibo_list[i-2]
        fibo_list.append(next_seq)
    return fibo_list

fibo_arr = np.zeros([16,64])
fibo_seq = fibonacci_gen(16)

for i in range(len(fibo_arr[0])):
    for j in range(len(fibo_arr)):
        fibo_arr[j,i] = fibo_seq[j]

print(fibo_arr)
even_arr = fibo_arr[fibo_arr%2==0]
print("even number array is ", np.asarray(sorted(list(set(even_arr)))))
