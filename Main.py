from TrojanDeception import *
import numpy as np
import matplotlib.pyplot as plt



WithDeception = []
WithoutDeception= []
Iteration = []

Num_Trojans = 4
K = 2
Value = np.array([1,2,4,12])
#Value = np.array([2,4,1,12])

#F = np.array([1.0,1.0,1.0,1.0])
F = np.array([8,6,2,4])

M = 100000

#Attacker Rationality
Attacker_Rationality = 0.1

#Defender_Rationality
Defender_Rationality = 0.5


SA = CreateSA(Num_Trojans)
SD = CreateSD(SA, Num_Trojans, K)

original_PA = np.array([0.2083,0.1667,0.3333,0.2917])
original_PD = np.array([0.1666,0.2564,0.2564,0.0513,0.0513,0.1795])

CL = 1000 #Number of ICs checked
CA = 100

Learning_Batches = 5
Game_Batches = 100

def testrun():
    PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A_One, Utility_D_One = LearningPhase(SA, SD, original_PA,
                                                                                               original_PD,
                                                                                               Attacker_Rationality,
                                                                                               Value, F,
                                                                                               Defender_Rationality, M)
    # print("Attacker Utility Learning: ", Utility_A_One)
    # print("Defender Utility Learning: ", Utility_D_One)
    PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A_One, Utility_D_One = LearningPhase(SA, SD, original_PA,
                                                                                               original_PD, 0.5, Value,
                                                                                               F, Defender_Rationality,
                                                                                               M)
    print("Attacker Mixed Strategy without Deception", PA)
    print("Defender Mixed Strategy without Deception", PD)

    Final_Utility_A_A, Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA, SD, PA, PD, Value, F, CA)
    #print("Attacker Utility without Deception: ", Utility_A)
    #print("Defender Utility without Deception", Utility_D)


    PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A_One, Utility_D_One = LearningPhase(SA, SD, original_PA,
                                                                                               original_PD,
                                                                                               Attacker_Rationality,
                                                                                               Value, F,
                                                                                               Defender_Rationality, M)
    PA, _, Final_Utility_A_L, Final_Utility_D_L, Utility_A_One, Utility_D_One = LearningPhase(SA, SD, original_PA,
                                                                                              original_PD, 0.5, Value,
                                                                                              F, Defender_Rationality,
                                                                                              M)
    print("Attacker Mixed Strategy with Deception", PA)
    print("Defender Mixed Strategy with Deception", PD)
    Final_Utility_A_A, Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA, SD, PA, PD, Value, F, CA)
    #print("Attacker Utility with Deception: ", Utility_A)
    #print("Defender Utility with Deception", Utility_D)

def print_vals(PA,SA,Final_Utility_A,Utility_A, PD, SD, Final_Utility_D, Utility_D):
    #print("Probability of Attacker: ", PA)
    #print("Attacker Optimal Strategy: ", SA[np.where(PA == np.amax(PA))])
    print("Total Utility of Attacker: ", Final_Utility_A)
    print("Last Calculated Utility of Attacker: ", Utility_A)

    #print("Probability of Defender: ", PD)
    #print("Defender Optimal Strategy: ", SD[np.where(PD == np.amax(PD))])
    print("Total Utility of Defender", Final_Utility_D)
    print("Last Calculated Utility of Defender: ", Utility_D)



testrun()




# Xaxis = []
# Yaxis = []
#
# Attacker_Rationality = 0.1
# New_Attacker_Rationality = 0.6
#
# while New_Attacker_Rationality <= 0.92:
#     Attacker_Rationality = 0.1
#     Xaxis.clear()
#     Yaxis.clear()
#     while Attacker_Rationality <= 0.52:
#         Xaxis.append(Attacker_Rationality)
#         PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A_One, Utility_D_One = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#         Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#         Non_Deception_Utility = Final_Utility_A_A * CA* Game_Batches
#
#         PA, _, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, New_Attacker_Rationality, Value, F , Defender_Rationality,M)
#         Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#         Deception_Utility = Final_Utility_A_A* CA* Game_Batches
#
#         Yaxis.append(Deception_Utility-Non_Deception_Utility)
#         Attacker_Rationality = Attacker_Rationality + 0.1
#
#
# plt.legend()
# plt.savefig("/home/tapadhir/Desktop/ChangeUtility.pdf")
# plt.show()

























