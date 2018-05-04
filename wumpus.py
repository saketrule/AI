## Implementation of Value iteration algorithm (Bellman Update) to find solution to Bellman equations
# Section 17.2 - AI a modern approach
## Problem definition: -- Given a 2d Matrix of integers, representing R[i][j]
## Condition of unreachable blocks is relaxed for now
## Using Bellman equation, solved by the value-update iterated algorithm
# State variables - U[i][j] represents the utility function at each state position
# 

N,M = 3,4
gamma = 1.0
thresh = 0.1*(1-gamma)/gamma
R = [[-0.04 for i in range(M)] for j in range(N)]
R[0][3] = 1
R[1][3] = -1
# Initializing utility function
U = [[R[j][i] for i in range(M)] for j in range(N)]

## Sketch of the algorithm, updation happens according to the rule:
# U[i][j](t+1) = R[i][j] + gamma * max[a] (sum[s] (P(s'|s,a)*U[s`]) )

# Possible actions
A = [(0,1),(1,0),(-1,0),(0,-1)]
final = [(0,3),(1,3)]
P = 0.8
P_ = 0.1

def move(u,v,a):
	u1,v1 = u+a[0],v+a[1]
	if u1>-1 and v1>-1 and u1<N and v1<M:
		return (u1,v1)
	return (u,v)

def alt_action(a):
	if a[0]!=0:
		return [(0,1),(0,-1)]
	else:
		return [(1,0),(-1,0)]

def exp_util(u,v,a):
	u1,v1 = move(u,v,a)
	res = P*U[u1][v1]
	[a2,a3] = alt_action(a)
	(u2,v2),(u3,v3) = move(u,v,a2),move(u,v,a3)
	res += P_*U[u2][v2] + P_*U[u3][v3]
	return res
	

sig = thresh+1
i = 0
while sig>thresh:
	sig = 0
	i += 1
	for u in range(N):
		for v in range(M):
			if (u,v) in final:
				continue
			U_ = R[u][v] + gamma*max([exp_util(u,v,a) for a in A])
			sig = max(sig,abs(U_-U[u][v]))
			U[u][v] = U_
	print('Iteration {}, sigma {}, thresh {}'.format(i,sig,thresh))			

print("Converged! - resultant Utility values are:\n")

for u in range(N):
	print(U[u])








	
