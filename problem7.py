import numpy as np
def DFT(x, N):
    #N = len(x)
    x = np.concatenate([x, [0]*(N-len(x))])
    n = np.arange(N)
    k = n.reshape((N,1))
    twiddler_mat = np.exp((-2j*np.pi*n*k)/N)
    #print(twiddler_mat)
    
    dft_X = np.dot(twiddler_mat,x)
    
    return dft_X
x = np.array([0,1,2,3])
N = 4
X = DFT(x,N)
print('DFT: ',X)

def IDFT(X, N):
    #N = len(X)
    #print(N)
    k = np.arange(N)
    n = k.reshape((N,1))
    twiddler_mat = np.exp((2j*np.pi*k*n)/N)
    #print(twiddler_mat)
    x = (np.dot(twiddler_mat, X))/N
    
    return x
N = 4
ans = IDFT(X,N)
print('IDFT: ',np.round(ans))

def FIR(x,h,N):
    dft_x = DFT(x,N)
    dft_h = DFT(h,N)
    mul = dft_x * dft_h
    
    idft = IDFT(mul, N)
    return np.round(idft)
x = np.array([1,2,2,1])
h = np.array([1,2,3])

print(FIR(x,h,8))

# N = 8
# dft_x = DFT(x, N)
# #print(dft_x)
# dft_h = DFT(h,N)
# #print(dft_h)
# mul = dft_x * dft_h
# #print(mul)
    
# idft = IDFT(mul, N)
# print(np.round(idft))