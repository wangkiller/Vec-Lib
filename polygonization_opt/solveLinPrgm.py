##This file contain the code to solve the linear program or quadratic program. It consider that in input it has a set of pixel that correspond to the representation of a convexe set.

##Importation of the solver
from cvxopt import matrix, solvers


#basic stuff
def scalProd(v1,v2):
	#scalar products in R^2
	return v1[0]*v2[0] + v1[1]*v2[1]

def vector(e,f):
	#vector between 2 points e and f: return vector ef->
	return (f[0]-e[0],f[1]-e[1])

#to compute the coefficient relative to e,f1,f2
def coef(e,f1,f2,delta):
	f1e = vector(f1,e)
	f2e = vector(f2,e)
	aux = scalProd(f1e,f2e)-delta
	return abs(aux)-aux

#compute the min real postive and representable
def minReal():
	x,y=0,1,2
	while x!=0:
		y=x
		x=x/2
	return y

#main
def computeLigne(e,liste,delta):
	res = []
	for f1 in liste:
		for f2 in liste:
			res.append(-coef(e,f1,f2,delta))#we put a "-" because in the linPrgm you have >0 and we want the inequality in the other direction to use cvxopt
	return res

def computeAPdelta(convexList,delta):
	#the result res is such that res[e][f1*|convexList|+f2] contains A_{e,f1,f2}
	return [computeLigne(e,convexList,delta) for e in convexList]
	
def concat(l,m);
	#takes list l and matrix m and return m' which the matrix where l has been added at the beginning of each line of m
	return [l+lm for lm in m]

def generateConstraintsZ(n):
	zero_n = [0 for i in range(n)]
	zero_n2 = [0 for i in range(n**2)]
	res = []
	for f1 in range(n):
		for f2 in range(n):
			zero_n2[f1*n+f2]=1
			zero_n[f1] = -1
			res.append(zero_n+zero_n2)
			zero_n[f1]= 0
			zero_n[f2]= -1
			res.append(zero_n+zero_n2)
			zero_n[f2]= 0
			zero_n2[f1*n+f2]= 0
	return res

def solvePdelta(convexList,delta):
	#function to use when you know what distance you want, at most, between each pixel and an edge (the closest one). It compute the better number of point you can use (the min).	 

	n=len(convexList)
	epsilon=minReal()

	#first create the matrix
	#we have |convexList|(|convexList|+1) variables all the x_e and z_{f,f'} that must stand for z_{f,f'}=x_f,x_f'.
	coefs=computeAPdelta(convexList,delta) #all th coef of the form a_{e,f,f'}
	nulConvexList = [0 for e in convexList] #a list of coef 0 for all variable x_e

	#we have to add nulConvexList at the beginning of each ligne e of coefs
	coefs = concat(nulConvexList,coefs)

	#now we have to add the constraints for z_f,f' <= x_f and x_f'
	nulProductVar = [0 for i in range(n**2)]
	constraintZ = generateConstraintsZ(n)

	A=matrix(coefs+constraitZ)

	#now get vectors b and c
	c=matrix([1 for e in convexList]+[-1 for i in range(n**2)]) #objective function
	b=matrix([epsilon for i in range(n)]+[0 for i in range(2*(n**2))])

	sol=solvers.lp(c,A,b)
	return sol['x']
	

def solvePnum(convexList,num):
	
	#first create the matrix