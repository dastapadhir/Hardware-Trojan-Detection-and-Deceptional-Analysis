from TrojanDeception import *
import numpy as np

H = 0.2

Num_Trojans = 4
K = 2
Num_Stages = 200
Value = np.array([1,2,4,12])
#F = np.array([1.0,1.0,1.0,1.0])
F = np.array([8.0,8.0,8.0,8.0])

Learning_Iterations = 50
counter = 0

M = 100000

#Attacker Rationality
Attacker_Rationality = 0.1

#Defender_Rationality
Defender_Rationality = 0.5


SA = CreateSA(Num_Trojans)
SD = CreateSD(SA, Num_Trojans, K)
PA = np.array([0.2083,0.1667,0.3333,0.2917])


PD = np.array([0.1666,0.2564,0.2564,0.0513,0.0513,0.1795])



PA, PD, Final_Utility_A, Final_Utility_D, Utility_A, Utility_D = LearningPhase(SA, SD, PA, PD, Attacker_Rationality, Learning_Iterations, Value, F , Defender_Rationality,M)
print("Probability of Attacker: " , PA)
print("Attacker Optimal Strategy: ", SA[np.where(PA == np.amax(PA))])
print("Total Utility of Attacker: ", Final_Utility_A)
print("Last Calculated Utility of Attacker: ", Utility_A)

print("Probability of Defender: " , PD)
print("Defender Optimal Strategy: ", SD[np.where(PD == np.amax(PD))])
print("Utility of Defender", Final_Utility_D)
print("Last Calculated Utility of Defender: ", Utility_D)













#PA = Probability(SA)
#PD = Probability(SD)
#PA, PD, tempPA, tempPD, tempPA1,tempPD1,tempPA2,tempPD2 = StartStage(PA, PD, SA, SD, S0iterations)

#Game1(Num_Trojans, K, Num_Stages,Value,F,tempPA,tempPD,SA,SD)
#Game2(Num_Trojans, K, Num_Stages,Value,F,tempPA1,tempPD1,SA,SD)
#Game3(Num_Trojans, K, Num_Stages,Value,F,tempPA2,tempPD2,SA,SD)


#print(PA,PD)

#print(NEA, NED)