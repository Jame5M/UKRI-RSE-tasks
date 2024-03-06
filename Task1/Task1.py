import re
from math import sqrt
from pdfminer.high_level import extract_pages, extract_text
#from matplotlib import pyplot as plt

k=0.3062
# takes in 2 arrays representing a pair of particles and returns energy and truncated energy
def PairwiseEnergy(P1,P2):
    numerator = P1[4]*P2[4]
    denominator = sqrt((P1[1]-P2[1])**2+(P1[2]-P2[2])**2+(P1[3]-P2[3])**2)
    energy=(numerator*k)/denominator
    return(energy,round(energy))

# Reads PDF file of the task sent via the email interview invitation and uses a Regular expression
# search to extract particle data as strings.
text=extract_text("TASK 1 Energy of a system of charged particles.pdf")
DataPattern = re.compile(r"[0-9]+\s[+-][0-9][.]?[0-9]*\s[+-][0-9][.]?[0-9]*\s[+-][0-9][.]?[0-9]*\s[-\s][0-9]+")
RawParticleData = DataPattern.findall(text)



### redundent code used to visualise the system ###
# x=[]
# y=[]
# z=[]
# m=[]
# each particle is a string and needs to be converted into an array of data to be used in calculations
ParticleData = []
for Particle in RawParticleData:
    DataStringArray = Particle.split()
    ParticleData.append([int(DataStringArray[0]),
               float(DataStringArray[1]),
               float(DataStringArray[2]),
               float(DataStringArray[3]),
               int(DataStringArray[4])])
    ### redundent code used to visualise the system ###
    # x.append(float(DataStringArray[1]))
    # y.append(float(DataStringArray[2]))
    # z.append(float(DataStringArray[3]))
    # m.append(int(DataStringArray[4]))
### redundent code used to visualise the system ###
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# img=ax.scatter(x,y, z, c=m,cmap='prism', alpha=1)
# plt.show()


# sets some variables and then calculates energy by calling functions
TrueSystemEnergy=0
EstimatedSystemEnergy=0
PairwiseInteractions=0
while ParticleData !=[]:
    P1= ParticleData[0]
    ParticleData.pop(0)
    for Particle in ParticleData:
        TrueEnergy,EstimatedEnergy=PairwiseEnergy(P1,Particle)
        TrueSystemEnergy=TrueSystemEnergy+TrueEnergy
        EstimatedSystemEnergy=EstimatedSystemEnergy+EstimatedEnergy
        PairwiseInteractions += 1
        

Error=abs(((TrueSystemEnergy-EstimatedSystemEnergy)/TrueSystemEnergy)*100)


#writes results to file
f=open("Task1Results","w")
f.write("Actual System Energy: ")
f.write(str(TrueSystemEnergy))
f.write("\n")
f.write("Estimated System Energy: ",)
f.write(str(EstimatedSystemEnergy))
f.write("\n")
f.write("Error: ")
f.write(str(Error))
f.write("%")
f.write("\n")
f.write("Pairwise Interactions: ")
f.write(str(PairwiseInteractions))
f.write("\n")
f.close()
