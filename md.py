## First molecular dynamics code
## Atomic units used consistently. See wikipedia page for more details of atomic units.
## See the provided pdf for details
## Consider a single coordinate 'x' with potential V=0.5*mass*omg**2*x**2
## Output: a file called 'coordinates.out' containing 3 columns: time, position, velocity

##############################################
#Calculates potential and acceleration as a function of x for SHO: 
# pot = 0.5*mass*omega**2*(x-x0)**2
# acc = -1/mass * dV/dx = - omega**2*(x-x0)
#Input: x - position
#Returns: pot,acc - potential,acceleration
##############################################
def compute_pot(x):
  pot=0.5*mass*omega**2*(x-x0)**2
  acc=-omega**2*(x-x0)
  return pot,acc
##############################################
 

##############################################
# Main program begins here
# 3 main steps:
#     1. Setting parameters
#     2. Setting initial conditions
#     3. Evolving
##############################################

# 0. Defining useful constants
pi=3.14159265359
##############################################

# 1. Setting parameters
mass        = 1837.0
omega       =           ### Fill in the blank. Convert 4000 cm-1 to atomic units. Close to 0.01
x0          = 2.0
dt          = 1/50.0 * 2*pi/omega
total_time  = 20.0   * 2*pi/omega
##############################################

# 2. Setting initial conditions
pos=                  ## Fill in the blanks. See the pdf  for details
vel=                  ## Fill in the blanks. See the pdf  for details
pot,acc=compute_pot(pos)    ## Acceleration will be needed for the first time step.
##############################################

# 3. Evolving
nsteps=int(total_time/dt)  ## The number of time steps. Note use of int here.
tim=0.0                    ## variable that reports on time
file_pos = open('coordinates.out', 'w')
## Starting the loop for evolution
for i in range(nsteps):
  ## Fourier expansion. See pdf - you need to code in Eqs. 4 and 5 here
  ## Notation: x -> pos, v -> vel, and a -> acc
  print(tim,pos,vel,file=file_pos)
  pos=pos+vel*dt+0.5*acc*dt*dt
  vel=vel+acc*dt

  pot,acc=compute_pot(pos)     ## getting updated acceleration and potential
  tim=tim+dt                   ## Updating current time
  ## End of for loop

