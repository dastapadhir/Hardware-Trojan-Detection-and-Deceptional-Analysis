import numpy as np
from functools import reduce
import operator as op
from itertools import combinations
import matplotlib.pyplot as plt
import math


def SizeofSpace(Num_Trojans, K):
    K = min(K, Num_Trojans - K)
    numer = reduce(op.mul, range(Num_Trojans, Num_Trojans - K, -1), 1)
    denom = reduce(op.mul, range(1, K + 1), 1)
    return numer / denom


def CreateSA(Num_Trojans):
    a = []
    for x in range(1, Num_Trojans + 1):
        a.append(x)
    a = np.array(a)
    return a


def CreateSD(SA, Num_Trojans, K):
    Size = SizeofSpace(Num_Trojans, K)
    test = int(Size)
    comb = combinations(SA, K)
    val = np.array(list(comb))
    li2 = [y for x in val for y in x]
    ','.join(map(str, li2))
    num = []
    for x in range(0, test):
        num.append(x)
    for x in range(0, len(li2), 2):
        num[int(x / 2)] = int(str(li2[x]) + str(li2[x + 1]))
    return np.asarray(num)


def Payoff_Check_Attacker(SA, Strategy_D, Value, F):
    num, rem = divmod(Strategy_D, 10)
    if SA == num or SA == rem:
        return -F
    else:
        return Value


def Payoff_Check_Defender(SD, Strategy_A, Value, F):
    num, rem = divmod(SD, 10)
    if Strategy_A == num or Strategy_A == rem:
        return F
    else:
        return -Value


def AttackerOptimalStrategy(SA, PA, weight_PD, Value, Strategy_D, F, Attacker_Rationality):
    weight_PD = np.asarray(weight_PD)
    output = np.zeros((SA.shape[0], weight_PD.shape[0]), dtype="float32")
    Weighted_Sigma = GetWeights(weight_PD, Attacker_Rationality)
    for i in range(0, SA.shape[0]):
        for j in range(0, weight_PD.shape[0]):
            output[i][j] = Weighted_Sigma[j] * Payoff_Check_Attacker(SA[i], Strategy_D[j], Value[i], F[i])
    sum_output = np.sum(output, axis=1)
    return SA[np.argmax(sum_output)]


def Update_Empirical_Frequency_Attacker(PA, K, SA, Optimal, Old_Optimal):
    output = np.zeros(SA.shape[0], dtype="float32")
    for i in range(0, SA.shape[0]):
        if i == Optimal - 1:
            output[i] = ((K - 1) / K) * PA[i] + (1 / K)
        else:
            output[i] = ((K - 1) / K) * PA[i]
    return np.asarray(output)


def Update_Empirical_Frequency_Defender(PA, K, SA, Optimal, Old_Optimal):
    output = np.zeros(SA.shape[0], dtype="float32")
    for i in range(0, SA.shape[0]):
        results = np.where(SA == Optimal)
        listi = list(zip(results[0]))
        index = listi[0][0]
        if i == index:
            output[i] = ((K - 1) / K) * PA[i] + (1 / K)
        else:
            output[i] = ((K - 1) / K) * PA[i]
    return np.asarray(output)


def Convergence(OldD, NewD, OldA, NewA):
    val = []
    for i in range(0, len(OldD)):
        val.append(abs(NewD[i] - OldD[i]))
    for i in range(0, len(OldA)):
        val.append(abs(NewA[i] - OldA[i]))
    return val


def Check(diff, M):
    count = 0
    for i in range(0, len(diff)):
        if diff[i] < 1 / M:
            count = count + 1
    return count


def DefenderOptimalStrategy(SD, PD, weight_PD, Value, Strategy_A, F, Defender_Rationality):
    weight_PD = np.asarray(weight_PD)
    output = np.zeros((SD.shape[0], PD.shape[0]), dtype="float32")
    sum_output = np.zeros(SD.shape[0], dtype="float32")
    Weighted_Sigma = GetWeights(PD, Defender_Rationality)
    for i in range(0, SD.shape[0]):
        for j in range(0, PD.shape[0]):
            output[i][j] = Weighted_Sigma[j] * Payoff_Check_Defender(SD[i], Strategy_A[j], Value[j], F[j])
    sum_output = np.sum(output, axis = 1)


    return SD[np.argmax(sum_output)]

def MatrixCreation(SA,SD,Value,F):
    table = np.zeros((SA.shape[0],SD.shape[0]), dtype= "float32")
    for i in range(0,SA.shape[0]):
        for j in range(0,SD.shape[0]):
            num, rem = divmod(SD[j], 10)
            if SA[i] == num or SA[i] == rem:
                table[i][j] = F[i]
            else:
                table[i][j] = -Value[i]
    return table

def CalculateUtilities(Value, F, SigmaD, PA, SigmaA, PD, SA, SD, Optimal_A, Optimal_D, Attacker_Rationality, Defender_Rationality):
    tabledefender = MatrixCreation(SA,SD,Value,F)
    tabledefender = tabledefender.T
    attacker_payoffs = np.zeros(PA.shape[0])
    defender_payoffs = np.zeros((PD.shape[0]))
    tableattacker = -tabledefender.T
    defender_payoffs =np.dot(np.dot(SigmaA, tabledefender),SigmaD)
    attacker_payoffs = np.dot(np.dot(SigmaD, tableattacker), SigmaA)

    return attacker_payoffs, defender_payoffs







def MixedStrategies(SA, SD, PA, PD, M, Value, F, Defender_Rationality, Attacker_Rationality):
    Sigma_A = PD
    Sigma_D = PA
    C_Test = 0
    K = 2
    Old_Optimal_A = 230
    Optimal_A = SA[np.argmax(PA)]
    Old_Optimal_D = 230
    Optimal_D = SD[np.argmax(PD)]

    Final_Utility_A = 0.0
    Final_Utility_D = 0.0

    while C_Test == 0:

        Old_Sigma_D = Sigma_D
        Old_Sigma_A = Sigma_A
        Old_Optimal_A = Optimal_A
        #Optimal_A, Utility_A = AttackerOptimalStrategy(SA, Sigma_D, Sigma_A, Value, SD, F, Attacker_Rationality)
        Optimal_A = AttackerOptimalStrategy(SA, Sigma_D, Sigma_A, Value, SD, F, Attacker_Rationality)
        Old_Optimal_D = Optimal_D

        #Optimal_D, Utility_D = DefenderOptimalStrategy(SD, Sigma_D, Sigma_A, Value, SA, F, Defender_Rationality)
        Optimal_D = DefenderOptimalStrategy(SD, Sigma_D, Sigma_A, Value, SA, F, Defender_Rationality)
        Sigma_D = Update_Empirical_Frequency_Attacker(Old_Sigma_D, K, SA, Optimal_A, Old_Optimal_A)
        Sigma_A = Update_Empirical_Frequency_Defender(Old_Sigma_A, K, SD, Optimal_D, Old_Optimal_D)

        diff = Convergence(Old_Sigma_D, Sigma_D, Old_Sigma_A, Sigma_A)
        check = Check(diff, M)
        Utility_A , Utility_D = CalculateUtilities(Value, F, Sigma_D, PA, Sigma_A, PD, SA, SD, Optimal_A, Optimal_D, Attacker_Rationality,
                           Defender_Rationality)
        Final_Utility_A = Final_Utility_A + Utility_A
        Final_Utility_D = Final_Utility_D + Utility_D
        if check == len(SA) + len(SD):
            C_Test = 1
        K = K + 1
        #print("Utility of Attacker: ",Utility_A )
        #print("Utility of Defender: ", Utility_D)
    print(K)
    #Utility_A, Utility_D = CalculateUtilities(Value, F, Sigma_D, PA, Sigma_A, PD, SA, SD, Optimal_A, Optimal_D, Attacker_Rationality, Defender_Rationality)

    return Sigma_D, Sigma_A, Final_Utility_A, Final_Utility_D, Utility_A, Utility_D


def GetWeights(PA, Deception_Rationality):
    weight_PA = []
    for i in range(0, len(PA)):
        val1 = np.exp(-math.pow(-np.log(PA[i]), Deception_Rationality))
        weight_PA.append(val1)
    return weight_PA


def LearningPhase(SA, SD, PA, PD, Attacker_Rationality, Learning_Iterations, Value, F, Defender_Rationality,M):
    PA, PD, Final_Utility_A, Final_Utility_D, Utility_A, Utility_D = MixedStrategies(SA, SD, PA, PD, M, Value, F, Defender_Rationality, Attacker_Rationality)
    return PA, PD, Final_Utility_A, Final_Utility_D, Utility_A, Utility_D