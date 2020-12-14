import numpy as np
from geneticalgorithm import geneticalgorithm as ga

array_co = []
def coefficients(spin,nnn):
    length = len(spin)
    temp = 0
    for i in range(length):
        j = (i+nnn) % length
        temp += spin[i] * spin[j]
    #print(temp)

def generalCoefficients(spin,nnn):
    length = len(spin)
    temp = 0
    for i in range(length):
        tempi = spin[i]
        for j in range(len(nnn)):
            if nnn == [0]:
                tempi = tempi
            else:
                k = (i+nnn[j]) % length
                tempi = tempi * spin[k]
        temp += tempi
    #print(temp)
    array_co.append(str(temp)+' ')

def getAll(spin):
    generalCoefficients(spin,[0])
    generalCoefficients(spin,[1])
    generalCoefficients(spin,[2])
    generalCoefficients(spin,[3])
    generalCoefficients(spin,[1,2])
    generalCoefficients(spin,[2,3])
    generalCoefficients(spin,[1,3])
    generalCoefficients(spin,[1,2,3])

def f(spin):
        #print (spin[0] == 0)
    #if (spin[0] != 0) & (spin[1] != 0) & (spin[2] != 0) & (spin[3] != 0) & (spin[4] != 0) & (spin[5] != 0) & (spin[6] != 0) & (spin[7] != 0) & (spin[8] != 0) & (spin[9] != 0) & (spin[10] != 0) & (spin[11] != 0):
            getAll(spin)
            #print (spin)
            co1 = 12*(-11.2432698)
            co2 = float(array_co[0])* (2.01506745)
            co3 = float(array_co[1])* (1.02438188)
            co4 = float(array_co[2])* (0.004414688)
            co5 = float(array_co[3])* (-1.03368526)
            co6 = float(array_co[4]) * (0.001165438)
            co7 = (1/2)*(float(array_co[6])+float(array_co[5])) * (-2.06124239)
            co8 = float(array_co[7])* (-1.03258301)
            toten = co1 + co2 + co3 + co4 + co5 + co6+co7+co8
            #toten = -(co1 + co2 + co3 + co4 + co5 + co6+co7+co8)
            return toten 

varbound=np.array([[-1,1]]*12)

algorithm_param = {'max_num_iteration': 300,\
                   'population_size':10,\
                   'mutation_probability':0.6,\
                   'elit_ratio': 0.01,\
                   'crossover_probability': 0.5,\
                   'parents_portion': 0.3,\
                   'crossover_type':'uniform',\
                   'max_iteration_without_improv':None}

model=ga(function=f,\
            dimension=12,\
            variable_type='int',\
            variable_boundaries=varbound,\
            function_timeout=10,\
            algorithm_parameters=algorithm_param)

model.run()
