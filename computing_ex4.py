import scipy as sp
import matplotlib.pyplot as py

'Part 1: Solve the simple two-body problem with one-body fixed'

#Here is a hyperlink to some short notes on the implementation
#https://drive.google.com/open?id=1paJBO2oj1ctsxJ_85Gi60XqsSRSxIRnNwJ6gqfcZvKI

class body:
    ''' Defines a massive body object with various properties as defined in __init__
        I would add in here additional functions under init which could be used to get kinetic
        energy etc. '''
    def __init__(self,initState,M):
        self.state = initState      #Current state-point
        self.Ek = 0                 #Kinetic energy
        self.M = M                  #Mass
    def getR(self):
        '''Return position co-ordinates'''
        return (self.state[1],self.state[2])
    def getV(self):
        '''Return velocity co-ordinates'''
        return (self.state[3],self.state[4])

    def propagate(self,F,dx):
        '''Perform one RK4 update for a single body in motion around another'''
        while True:
            var = self.state[1:]  
            K1 = [f(var) for f in F]
            var = [s+dx*k/2 for (s,k) in zip(var,K1)]
            K2 = [f(var) for f in F]
            var = [s+dx*k/2 for (s,k) in zip(var,K2)]
            K3 = [f(var) for f in F]
            var = [s+dx*k for (s,k) in zip(var,K3)]
            K4 = [f(var) for f in F]
            #Update the state. First list is the timestep, second list is the RK update. Does not yet update internally
            yield [self.state[0]+dx] + [x+dx*(k1+2*(k2+k3)+k4)/6 for (x,k1,k2,k3,k4) in zip(self.state[1:],K1,K2,K3,K4)]

'Part 1: Simple orbit around a massive object'
G = 1       #I have used units MG=1
M = 1/G
F = [lambda var:var[2],lambda var: var[3], lambda var:-G*M*var[0]/((var[0]**2+var[1]**2)**1.5),lambda var:-G*M*var[1]/((var[0]**2+var[1]**2)**1.5)]

moon = body([0,0,7,0.36,0],1/G)  #Set up initial state of the moon. These parameters give a decently stable orbit
newState = moon.propagate(F,10**-3)         #newState is a "propagate" function. Calling next(newState) will generate the next state point
trajectory = []                         #Store all position co-ordinates. Could also choose to store only a few
dev = []
for k in range(600000):
    newPoint = next(newState)           #Calculate next state
    if (moon.getR()[0]<0 and moon.getR()[1]>0) and newPoint[1]>0:
        dev.append(newPoint[1:3])
    moon.state = newPoint               #Propagate one timestep and update the state
    if k%10==0:                         #Store each 10th co-ordinate point
        trajectory.append(moon.getR())
trajectory = sp.array(trajectory)
dev = sp.array(dev)
#print(len(dev))
#py.plot(trajectory[:,0],trajectory[:,1])
#py.show()
py.plot(dev[:,1], 'o')
py.show()
