import numpy        as np
import numpy.random as npr
 
def alias_setup(probs):
    K       = len(probs)
    q       = np.zeros(K)
    J       = np.zeros(K, dtype=np.int)

    smaller = []
    larger  = []
    for kk, prob in enumerate(probs):
        q[kk] = K*prob
        if q[kk] < 1.0:
            smaller.append(kk)
        else:
            larger.append(kk)
 
    while len(smaller) > 0 and len(larger) > 0:
        small = smaller.pop()
        large = larger.pop()
 
        J[small] = large
        q[large] = q[large] - (1.0 - q[small])
 
        if q[large] < 1.0:
            smaller.append(large)
        else:
            larger.append(large)
 
    return J, q
 
def alias_draw(J, q):
    K  = len(J)
    kk = int(np.floor(npr.rand()*K))
    if npr.rand() < q[kk]:
        return kk
    else:
        return J[kk]
 
def test():
    K = 3
    N = 100
    probs = npr.dirichlet(np.ones(K), 1).ravel() 
    J, q = alias_setup(probs)
    X = np.zeros(N)
    for nn in xrange(N):
        X[nn] = alias_draw(J, q)

test()