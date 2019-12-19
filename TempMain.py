from TrojanDeception import *
import numpy as np
import matplotlib.pyplot as plt



WithDeception = []
WithoutDeception= []
Iteration = []

Num_Trojans = 4
K = 2
Value = np.array([1,2,4,12])
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


def print_vals(PA,SA,Final_Utility_A,Utility_A, PD, SD, Final_Utility_D, Utility_D):
    #print("Probability of Attacker: ", PA)
    #print("Attacker Optimal Strategy: ", SA[np.where(PA == np.amax(PA))])
    print("Total Utility of Attacker: ", Final_Utility_A)
    print("Last Calculated Utility of Attacker: ", Utility_A)

    #print("Probability of Defender: ", PD)
    #print("Defender Optimal Strategy: ", SD[np.where(PD == np.amax(PD))])
    print("Total Utility of Defender", Final_Utility_D)
    print("Last Calculated Utility of Defender: ", Utility_D)


# PA, One_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A_One, Utility_D_One = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
# print(One_PD)
# PA, Five_PD, Final_Utility_A_L, Final_Utility_D_L, _, _ = LearningPhase(SA, SD, original_PA, original_PD, 0.5, Value, F , Defender_Rationality,M)
# print(Five_PD)
# print(Utility_A_One)
# print(Utility_D_One)
#
# PA, _, Final_Utility_A_L, Final_Utility_D_L, _, _ = LearningPhase(SA, SD, original_PA, original_PD, 0.5, Value, F , Defender_Rationality,M)
# print(Utility_A_One)
# print(Utility_D_One)
#
# Final_Utility_A_A , Final_Utility_D_A, Utility_A_Five, Utility_D_Five = GamePhase(SA,SD, PA, PD, Value, F, CA)
# print(Utility_A_Five)
# print(Utility_D_Five)





# PA = []
# WeightedPA = []
#
# for j in np.arange(0.2,1.01,0.2):
#     PA.clear()
#     WeightedPA.clear()
#     for i in np.arange(0.0, 1.01, 0.01):
#         PA.append(i)
#         WeightedPA.append(np.exp(-math.pow(-np.log(i), j)))
#     if j == 0.2:
#         plt.plot(PA, WeightedPA, '-.', label='α = 0.2' )
#     elif j == 0.4:
#         plt.plot(PA, WeightedPA,  marker='^', color='blue', label='α = 0.4', markersize = 3.0)
#     elif j == 0.6000000000000001:
#         plt.plot(PA, WeightedPA, ':',label='α = 0.6'  )
#     elif j == 0.8:
#         plt.plot(PA, WeightedPA, 'k--', label='α = 0.8')
#     elif j == 1.0:
#         plt.plot(PA, WeightedPA, color='red', label='α = 1.0')
#
# plt.ylabel('Subjective Rationality Evaluation')
# plt.xlabel('Objective Probability')
# plt.margins(x=0)
# plt.margins(y=0)
# plt.xticks(np.arange(0, 1, step=0.1))
# plt.yticks(np.arange(0, 1, step=0.1))
# plt.grid(color='black', linestyle='-', linewidth=0.0125)
# plt.legend()
# plt.savefig("/home/tapadhir/Desktop/PaperFigures/rationality.pdf")




# Rationality = []
# New_Attacker_Rationality = 0.4
#
#
#
PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A_One, Utility_D_One = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
print(PA)
OnePA = PA
print(Utility_A_One)
print(Utility_D_One)


PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, 0.5, Value, F , Defender_Rationality,M)
# PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A_Five, Utility_D_Five = LearningPhase(SA, SD, original_PA, original_PD, 0.5, Value, F , Defender_Rationality,M)
#
FivePA = PA
print(PA)
#
#
# Strategies = ['A', 'B', 'C', 'D']
# plt.bar(Strategies, OnePA, color = 'red', label = '$α_{a_{L}}$ = 0.1', align='center', zorder=3)
# plt.bar(Strategies, FivePA, color = 'black', label = '$α_{a_{L}}$ = 0.5', align='center', zorder=3)
#
# plt.ylabel('Attacker Probability')
# plt.xlabel('Attacker Strategy')
# plt.legend()
# plt.grid(zorder = 0)
# plt.savefig('/home/tapadhir/Desktop/PaperFigures/AttackerTotalProfile.pdf')
# print(Utility_A_Five)
# print(Utility_D_Five)
#
#
# Final_Utility_A_A , Final_Utility_D_A, Utility_A_Five, Utility_D_Five = GamePhase(SA,SD, PA, PD, Value, F, CA)
# print(Utility_A_Five)
# print(Utility_D_Five)




# y_pos = ['Attacker','Defender']
# performance = [Utility_A, Utility_D]
# #plt.bar(y_pos, performance, align='center', alpha=0.5, color = 'r')
# # plt.xticks(y_pos)
#
# plt.grid(zorder=0)
# plt.bar('Attacker', Utility_A, align='center', color='red', zorder=3, label = "Attacker Utility")
# plt.bar('Defender', Utility_D, align='center', color='green', zorder=3, label = 'Defender Utility')
#
# plt.xlim([-2,2])
# plt.ylabel('Expected Utilities')
# plt.legend()
#
# plt.savefig("/home/tapadhir/Desktop/PaperFigures/A5D5.pdf")
#
# print(Utility_A)
# print(Utility_D)






# import matplotlib.pyplot as plt; plt.rcdefaults()
# import numpy as np
# import matplotlib.pyplot as plt
#
# objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
# y_pos = ['AB','AC','C','D']
# performance = PA
#
# plt.bar(y_pos, performance, align='center', alpha=0.5, color = 'r')
# plt.xticks(y_pos)
#
# plt.grid(zorder=0)
# plt.bar(range(len(y_pos)), PA, align='center', color='red', zorder=3)
#
# plt.ylabel('Probability of playing each strategy')
# plt.xlabel('Attacker strategies')
# plt.title('Attacker strategic profile')
#
# plt.savefig("/home/tapadhir/Desktop/PaperFigures/AttackerGameProfile.pdf")

#Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)


# y_pos = ['Attacker ','Attacker', 'Defender', 'Defender']
# performance = [Utility_A_One, Utility_A_Five, Utility_D_One, Utility_D_Five]
# #plt.bar(y_pos, performance, align='center', alpha=0.5, color = 'r')
# # plt.xticks(y_pos)
#
# plt.grid(zorder=0)
# plt.bar('-2', Utility_A_One, align='center', color='red', zorder=3, label = "Attacker Utility, $α_{a_{L}}$ = 0.1")
# plt.bar('-1.5', Utility_A_Five, align='center', color='blue', zorder=3, label = 'Attacker Utility, $α_{a_{L}}$ = 0.5 ')
# plt.bar('1.5', Utility_D_One, align='center', color='green', zorder=3, label = "Defender Utility, $α_{a_{L}}$ = 0.1")
# plt.bar('2', Utility_D_Five, align='center', color='cyan', zorder=3, label = 'Defender Utility, $α_{a_{L}}$ = 0.5 ')
#
#
# plt.xlim([-4,4])
# plt.xticks([])
# plt.ylabel('Expected Utilities')
# plt.legend()
# plt.title("Deception")
# plt.savefig("/home/tapadhir/Desktop/PaperFigures/Deception.pdf")
#
#
# Utility_A = [Utility_A_Five, Utility_A_One]
# Utility_D = [Utility_D_Five, Utility_D_One]
fig = plt.figure()
ax = fig.add_subplot(111)
ind = np.arange(4)
width = 0.35
rects1 = ax.bar(ind, OnePA, width,
                color='red')
rects2 = ax.bar(ind+width, FivePA, width,
                color='black')

ax.set_ylabel('Attacker Probability')
ax.set_xlabel('Attacker Strategy')
plt.grid(zorder = 0)
ax.set_axisbelow(True)
xTickMarks = ['A', 'B', 'C', 'D' ]
ax.set_xticks(ind+width)
xtickNames = ax.set_xticklabels(xTickMarks)
plt.setp(xtickNames, rotation=0, fontsize=10)
# plt.title("No Deception")
params = {'mathtext.default': 'regular' }
plt.rcParams.update(params)
ax.legend( (rects1[0], rects2[0]), ('$α_{a_{L}}$ = 0.1', '$α_{a_{L}}$ = 0.5') )


plt.savefig("/home/tapadhir/Desktop/PaperFigures/Test.pdf")

plt.clf()



















#
# objects = ('Python', 'C++', 'Java', 'Perl', 'Scala', 'Lisp')
# y_pos = ['AB','AC','AD','BC', 'BD', 'CD']
# performance = PD
#
# plt.bar(y_pos, performance, align='center', alpha=0.5, color = 'r')
# plt.xticks(y_pos)
#
# plt.grid(zorder=0)
# plt.bar(range(len(y_pos)), PD, align='center', color='green', zorder=3)
#
# plt.ylabel('Probability of playing each strategy')
# plt.xlabel('Defender strategies')
# plt.title('Defender strategic profile')
#
# plt.savefig("/home/tapadhir/Desktop/PaperFigures/DefenderLearningProfile.pdf")


# y_pos = ['Attacker','Defender']
# performance = [Utility_A, Utility_D]
# #plt.bar(y_pos, performance, align='center', alpha=0.5, color = 'r')
# # plt.xticks(y_pos)
#
# plt.grid(zorder=0)
# plt.bar('Attacker', Utility_A, align='center', color='red', zorder=3, label = "Attacker Utility")
# plt.bar('Defender', Utility_D, align='center', color='green', zorder=3, label = 'Defender Utility')
#
# plt.xlim([-2,2])
# plt.ylabel('Expected Utilities')
# plt.title('Player Utility')
# plt.legend()
#
# plt.savefig("/home/tapadhir/Desktop/PaperFigures/A1D5.pdf")






#while Game_Iterations < 10:
#while Attacker_Rationality < 1.0:






# Defender_Rationality = 0.5
# Rationality = []
# New_Attacker_Rationality = 0.4
#
# while New_Attacker_Rationality < 1.01:
#     #print("SCENARIO 1: ATTACKER DOESN'T CHANGE RATIONALITY")
#     #print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     #print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#
#     # WithoutDeception.append(Final_Utility_A_A)
#     WithoutDeception = [Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A]
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#
#    # print("SCENARIO 2:ATTACKER CHANGES RATIONALITY")
#     #print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_1 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#
#     #print("LEARNING STAGE")
#     # PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, 0.7, Value, F , Defender_Rationality,M)
#     PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA,
#                                                                                             original_PD, New_Attacker_Rationality, Value, F,
#                                                                                             Defender_Rationality, M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_2 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     Attacker_Loss = Attacker_Val_2 - Attacker_Val_1
#     # print("Attacker Loss during Learning", Attacker_Loss)
#
#    # print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD51 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#
#
#     Rationality.append((New_Attacker_Rationality))
#     #Rationality.append((Attacker_Rationality))
#     Iteration.append(Game_Batches)
#     WithDeception.append(AD51)
#     #Game_Iterations = Game_Iterations + 1
#     #Attacker_Rationality = Attacker_Rationality + 0.05
#     New_Attacker_Rationality = New_Attacker_Rationality + 0.1
#
#
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     #print("Attacker Utility when Defender thinks 0.1: ", AD51)
#     #print("************************************************")
#
#     PD = temp_PD
#     #print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD55 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     # print("Attacker Utility when Defender thinks 0.5: ", AD55)
#     # print("************************************************")
#
#     print("Attacker Utility without Deception", AD55)
#
#     Attacker_Gain = AD51 - AD55
#     print("Attacker Utility with Deception", AD51)
#
#     print("Diff", Attacker_Gain)
#
# print("***************")
#
# Defender_Rationality = 0.6
# #Rationality = []
# New_Attacker_Rationality = 0.4
# WithDeceptionSix = []
# WithoutDeceptionSix = []
#
# while New_Attacker_Rationality < 1.01:
#     #print("SCENARIO 1: ATTACKER DOESN'T CHANGE RATIONALITY")
#     #print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     #print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#
#     WithoutDeceptionSix = [Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A]
#
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#
#    # print("SCENARIO 2:ATTACKER CHANGES RATIONALITY")
#     #print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_1 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#
#     #print("LEARNING STAGE")
#     # PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, 0.7, Value, F , Defender_Rationality,M)
#     PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA,
#                                                                                             original_PD, New_Attacker_Rationality, Value, F,
#                                                                                             Defender_Rationality, M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_2 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     Attacker_Loss = Attacker_Val_2 - Attacker_Val_1
#     # print("Attacker Loss during Learning", Attacker_Loss)
#
#     #print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD51 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#
#
#     #Rationality.append((New_Attacker_Rationality))
#     #Rationality.append((Attacker_Rationality))
#     Iteration.append(Game_Batches)
#     WithDeceptionSix.append(AD51)
#     #Game_Iterations = Game_Iterations + 1
#     #Attacker_Rationality = Attacker_Rationality + 0.05
#     New_Attacker_Rationality = New_Attacker_Rationality + 0.1
#
#
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#    # print("Attacker Utility when Defender thinks 0.1: ", AD51)
#     #print("************************************************")
#
#     PD = temp_PD
#     #print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD55 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     # print("Attacker Utility when Defender thinks 0.5: ", AD55)
#     # print("************************************************")
#
#     print("Attacker Utility without Deception", AD55)
#
#     Attacker_Gain = AD51 - AD55
#     print("Attacker Utility with Deception", AD51)
#
#     print("Diff", Attacker_Gain)
#
#
# Defender_Rationality = 0.7
# #Rationality = []
# New_Attacker_Rationality = 0.4
# WithDeceptionSeven = []
# WithoutDeceptionSeven = []
#
# while New_Attacker_Rationality < 1.01:
#     print("SCENARIO 1: ATTACKER DOESN'T CHANGE RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#
#     WithoutDeceptionSeven = [Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A]
#
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#
#     print("SCENARIO 2:ATTACKER CHANGES RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_1 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#
#     print("LEARNING STAGE")
#     # PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, 0.7, Value, F , Defender_Rationality,M)
#     PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA,
#                                                                                             original_PD, New_Attacker_Rationality, Value, F,
#                                                                                             Defender_Rationality, M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_2 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     Attacker_Loss = Attacker_Val_2 - Attacker_Val_1
#     # print("Attacker Loss during Learning", Attacker_Loss)
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD51 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#
#
#     #Rationality.append((New_Attacker_Rationality))
#     #Rationality.append((Attacker_Rationality))
#     Iteration.append(Game_Batches)
#     WithDeceptionSeven.append(AD51)
#     #Game_Iterations = Game_Iterations + 1
#     #Attacker_Rationality = Attacker_Rationality + 0.05
#     New_Attacker_Rationality = New_Attacker_Rationality + 0.1
#
#
#     print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     print("Attacker Utility when Defender thinks 0.1: ", AD51)
#     print("************************************************")
#
#     PD = temp_PD
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD55 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     # print("Attacker Utility when Defender thinks 0.5: ", AD55)
#     # print("************************************************")
#
#     print("Attacker Utility without Deception", AD55)
#
#     Attacker_Gain = AD51 - AD55
#     print("Attacker Utility with Deception", AD51)
#
#
#
# Defender_Rationality = 0.8
# #Rationality = []
# New_Attacker_Rationality = 0.4
# WithDeceptionEight = []
# WithoutDeceptionEight = []
# while New_Attacker_Rationality < 1.01:
#     print("SCENARIO 1: ATTACKER DOESN'T CHANGE RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#
#     WithoutDeceptionEight = [Final_Utility_A_A, Final_Utility_A_A, Final_Utility_A_A, Final_Utility_A_A, Final_Utility_A_A,
#                         Final_Utility_A_A, Final_Utility_A_A]
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#
#     print("SCENARIO 2:ATTACKER CHANGES RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_1 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#
#     print("LEARNING STAGE")
#     # PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, 0.7, Value, F , Defender_Rationality,M)
#     PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA,
#                                                                                             original_PD, New_Attacker_Rationality, Value, F,
#                                                                                             Defender_Rationality, M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_2 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     Attacker_Loss = Attacker_Val_2 - Attacker_Val_1
#     # print("Attacker Loss during Learning", Attacker_Loss)
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD51 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#
#
#     #Rationality.append((New_Attacker_Rationality))
#     #Rationality.append((Attacker_Rationality))
#     Iteration.append(Game_Batches)
#     WithDeceptionEight.append(AD51)
#     #Game_Iterations = Game_Iterations + 1
#     #Attacker_Rationality = Attacker_Rationality + 0.05
#     New_Attacker_Rationality = New_Attacker_Rationality + 0.1
#
#
#     print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     print("Attacker Utility when Defender thinks 0.1: ", AD51)
#     print("************************************************")
#
#     PD = temp_PD
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD55 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     # print("Attacker Utility when Defender thinks 0.5: ", AD55)
#     # print("************************************************")
#
#     print("Attacker Utility without Deception", AD55)
#
#     Attacker_Gain = AD51 - AD55
#     print("Attacker Utility with Deception", AD51)
#
#
# Defender_Rationality = 0.9
# #Rationality = []
# New_Attacker_Rationality = 0.4
# WithDeceptionNine = []
# WithoutDeceptionNine = []
# while New_Attacker_Rationality < 1.01:
#     print("SCENARIO 1: ATTACKER DOESN'T CHANGE RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#
#     WithoutDeceptionNine = [Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A,Final_Utility_A_A]
#
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#
#     print("SCENARIO 2:ATTACKER CHANGES RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_1 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#
#     print("LEARNING STAGE")
#     # PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, 0.7, Value, F , Defender_Rationality,M)
#     PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA,
#                                                                                             original_PD, New_Attacker_Rationality, Value, F,
#                                                                                             Defender_Rationality, M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_2 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     Attacker_Loss = Attacker_Val_2 - Attacker_Val_1
#     # print("Attacker Loss during Learning", Attacker_Loss)
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD51 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#
#
#     #Rationality.append((New_Attacker_Rationality))
#     #Rationality.append((Attacker_Rationality))
#     Iteration.append(Game_Batches)
#     WithDeceptionNine.append(AD51)
#     #Game_Iterations = Game_Iterations + 1
#     #Attacker_Rationality = Attacker_Rationality + 0.05
#     New_Attacker_Rationality = New_Attacker_Rationality + 0.1
#
#
#     print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     print("Attacker Utility when Defender thinks 0.1: ", AD51)
#     print("************************************************")
#
#     PD = temp_PD
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD55 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     # print("Attacker Utility when Defender thinks 0.5: ", AD55)
#     # print("************************************************")
#
#     print("Attacker Utility without Deception", AD55)
#
#     Attacker_Gain = AD51 - AD55
#     print("Attacker Utility with Deception", AD51)
#
#
#
#
#
#
# Defender_Rationality = 1.0
# #Rationality = []
# New_Attacker_Rationality = 0.4
# WithDeceptionWhole = []
# while New_Attacker_Rationality < 1.01:
#     print("SCENARIO 1: ATTACKER DOESN'T CHANGE RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#
#     #WithoutDeception.append(Final_Utility_A_A)
#
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#
#     print("SCENARIO 2:ATTACKER CHANGES RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_1 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#
#     print("LEARNING STAGE")
#     # PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, 0.7, Value, F , Defender_Rationality,M)
#     PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA,
#                                                                                             original_PD, New_Attacker_Rationality, Value, F,
#                                                                                             Defender_Rationality, M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_2 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     Attacker_Loss = Attacker_Val_2 - Attacker_Val_1
#     # print("Attacker Loss during Learning", Attacker_Loss)
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD51 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#
#
#     #Rationality.append((New_Attacker_Rationality))
#     #Rationality.append((Attacker_Rationality))
#     Iteration.append(Game_Batches)
#     WithDeceptionWhole.append(AD51)
#     #Game_Iterations = Game_Iterations + 1
#     #Attacker_Rationality = Attacker_Rationality + 0.05
#     New_Attacker_Rationality = New_Attacker_Rationality + 0.1
#
#
#     print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     print("Attacker Utility when Defender thinks 0.1: ", AD51)
#     print("************************************************")
#
#     PD = temp_PD
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD55 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     # print("Attacker Utility when Defender thinks 0.5: ", AD55)
#     # print("************************************************")
#
#     print("Attacker Utility without Deception", AD55)
#
#     Attacker_Gain = AD51 - AD55
#     print("Attacker Utility with Deception", AD51)

# WithoutDeception.pop(0)
# WithoutDeceptionSix.pop(0)
# WithoutDeceptionSeven.pop(0)
# WithoutDeceptionEight.pop(0)
# WithoutDeceptionNine.pop(0)
#
#
# WithDeception.pop(0)
# WithDeceptionSix.pop(0)
# WithDeceptionSeven.pop(0)
# WithDeceptionEight.pop(0)
# WithDeceptionNine.pop(0)
#
#
# Rationality.pop(0)
# Rationality = np.asarray(Rationality)
#
# WithDeception = np.asarray(WithDeception)
# WithDeceptionSix = np.asarray(WithDeceptionSix)
# WithDeceptionSeven = np.asarray(WithDeceptionSeven)
# WithDeceptionEight = np.asarray(WithDeceptionEight)
# WithDeceptionNine = np.asarray(WithDeceptionNine)
# WithDeceptionWhole = np.asarray(WithDeceptionWhole)
#
#
# WithoutDeception = np.asarray(WithoutDeception)
# WithoutDeceptionSix = np.asarray(WithoutDeceptionSix)
# WithoutDeceptionSeven = np.asarray(WithoutDeceptionSeven)
# WithoutDeceptionEight = np.asarray(WithoutDeceptionEight)
# WithoutDeceptionNine = np.asarray(WithoutDeceptionNine)
#
#
#
# Difference_Utility = WithDeception - WithoutDeception
# Difference_UtilitySix = WithDeceptionSix - WithoutDeceptionSix
# Difference_UtilitySeven = WithDeceptionSeven - WithoutDeceptionSeven
# Difference_UtilityEight = WithDeceptionEight - WithoutDeceptionEight
# Difference_UtilityNine = WithDeceptionNine - WithoutDeceptionNine
# #Difference_UtilityWhole = WithDeceptionWhole - WithoutDeception
#
#
#
#
#
#
# Rationality=np.loadtxt('/home/tapadhir/Desktop/rationality.txt')
# Difference_Utility = np.loadtxt('/home/tapadhir/Desktop/du.txt'  )
# Difference_UtilitySix = np.loadtxt('/home/tapadhir/Desktop/du6.txt'  )
# Difference_UtilitySeven = np.loadtxt('/home/tapadhir/Desktop/du7.txt'  )
# Difference_UtilityEight = np.loadtxt('/home/tapadhir/Desktop/du8.txt'  )
# Difference_UtilityNine = np.loadtxt('/home/tapadhir/Desktop/du9.txt'  )
#
#
#
#
#
#
#
#
# fig = plt.figure()
# ax = fig.add_subplot(111)
# ax.set_axisbelow(True)
#
# plt.plot(Rationality, Difference_Utility, 'r', marker = 'D',Label ='$α_{d}$ = 0.5' , markersize = 4.0)
# plt.plot(Rationality, Difference_UtilitySix, 'b', marker = 'H', Label ='$α_{d}$ = 0.6' , markersize = 4.0 )
# plt.plot(Rationality, Difference_UtilitySeven, 'g', marker = 'o', Label ='$α_{d}$ = 0.7', markersize = 4.0 )
# plt.plot(Rationality, Difference_UtilityEight, 'c', marker='^',  Label ='$α_{d}$ = 0.8', markersize = 4.0 )
# plt.plot(Rationality, Difference_UtilityNine, 'm', marker='p' , Label ='$α_{d}$ = 0.9', markersize = 4.0 )
# #plt.plot(Rationality, Difference_UtilityWhole, 'k', Label ='$α_{A_{A}}$ = 1.0' )
#
#
# plt.grid(zorder = 0)
# ax.set_axisbelow(True)
#
# plt.ylabel("Attacker Utility Gain with Deception")
# plt.xlabel("Attacker Actual rationality")
# plt.legend(fancybox=True, framealpha=0.5)
# plt.subplots_adjust(bottom=.25, left=.25)
# plt.savefig("/home/tapadhir/Desktop/changeinutilityall.pdf")
#
# np.savetxt('/home/tapadhir/Desktop/rationality.txt', Rationality )
# np.savetxt('/home/tapadhir/Desktop/du.txt', Difference_Utility )
# np.savetxt('/home/tapadhir/Desktop/du6.txt', Difference_UtilitySix )
# np.savetxt('/home/tapadhir/Desktop/du7.txt', Difference_UtilitySeven )
# np.savetxt('/home/tapadhir/Desktop/du8.txt', Difference_UtilityEight )
# np.savetxt('/home/tapadhir/Desktop/du9.txt', Difference_UtilityNine )

# fig = plt.figure()
# ax = fig.add_subplot(111)
# ind = np.arange(Game_Iterations-1)
# width = 0.35
# rects1 = ax.bar(ind, WithoutDeception, width,
#                 color='black')
#
# rects2 = ax.bar(ind+width, WithDeception, width,
#                 color='red')
#
# ax.set_ylabel('Attacker Utility')
# ax.set_title('Attacker Utility for number of game iterations')
# xTickMarks = ['Game '+str(i) for i in range(1,10)]
# ax.set_xticks(ind+width)
# xtickNames = ax.set_xticklabels(xTickMarks)
# plt.setp(xtickNames, rotation=45, fontsize=10)
#
# ax.legend( (rects1[0], rects2[0]), ('No Deception', 'Deception') )
#
# plt.savefig("/home/tapadhir/Desktop/attackerutilitycomparison.png")

# plt.clf()


# WithDeception = np.asarray(WithDeception)
# WithoutDeception = np.asarray(WithoutDeception)
#
# Difference_Utility = WithDeception - WithoutDeception
#
# plt.plot(Iteration, Difference_Utility)
# plt.savefig("/home/tapadhir/Desktop/changeinutility.png")



# fig = plt.figure()
# ax = fig.add_subplot(111)
# ind = np.arange(len(Rationality))
# width = 0.35
# rects1 = ax.bar(ind, WithoutDeception, width,
#                 color='black')
#
# rects2 = ax.bar(ind+width, WithDeception, width,
#                 color='red')
#
# ax.set_ylabel('Attacker Utility')
# ax.set_title('Attacker Utility for different rationalities')
# xTickMarks = ['Game '+str(i) for i in range(1,len(Rationality))]
# ax.set_xticks(ind+width)
# xtickNames = ax.set_xticklabels(xTickMarks)
# plt.setp(xtickNames, rotation=45, fontsize=10)
#
# ax.legend( (rects1[0], rects2[0]), ('No Deception', 'Deception') )
#
# plt.savefig("/home/tapadhir/Desktop/variousrationality3.png")
#
# plt.clf()


# fig = plt.figure()
# ax = fig.add_subplot(111)
# ind = np.arange(len(Rationality))
# width = 0.35
# rects1 = ax.bar(ind, WithoutDeception, width,
#                 color='black')
#
# rects2 = ax.bar(ind+width, WithDeception, width,
#                 color='red')
#
# ax.set_ylabel('Attacker Utility')
# ax.set_title('Attacker Utility for different rationalities')
# # xTickMarks = [str(i) for i in np.arange(0.4, 1.01, 0.1)]
# xTickMarks = [0.4, 0.5, 0.6, 0.7, 0.8, 0.9,1.0]
# ax.set_xticks(ind+width)
# xtickNames = ax.set_xticklabels(xTickMarks)
# plt.setp(xtickNames, rotation=0, fontsize=10)
#
# ax.legend( (rects1[0], rects2[0]), ('No Deception', 'Deception') )
#
# plt.savefig("/home/tapadhir/Desktop/variousrationality3.png")
#
# plt.clf()
#


# Defender_Rationality = 0.5
# Rationality = []
# Attacker_Rationality = 0.1
# WithDeceptionWhole = []
# New_Attacker_Rationality = 0.1
# GainOne = []
#
# while Attacker_Rationality < 0.91:
#     print("SCENARIO 1: ATTACKER DOESN'T CHANGE RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#
#     #WithoutDeception.append(Final_Utility_A_A)
#
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#
#     print("SCENARIO 2:ATTACKER CHANGES RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_1 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#
#     print("LEARNING STAGE")
#     # PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, 0.7, Value, F , Defender_Rationality,M)
#     PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA,
#                                                                                             original_PD, New_Attacker_Rationality, Value, F,
#                                                                                             Defender_Rationality, M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_2 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     Attacker_Loss = Attacker_Val_2 - Attacker_Val_1
#     # print("Attacker Loss during Learning", Attacker_Loss)
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD51 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#
#
#     #Rationality.append((New_Attacker_Rationality))
#     #Rationality.append((Attacker_Rationality))
#     Iteration.append(Game_Batches)
#     #WithDeceptionOne.append(AD51)
#     #Game_Iterations = Game_Iterations + 1
#     #Attacker_Rationality = Attacker_Rationality + 0.05
#     Attacker_Rationality = Attacker_Rationality + 0.2
#
#
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     print("Attacker Utility when Defender thinks 0.1: ", AD51)
#     print("************************************************")
#
#     PD = temp_PD
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD55 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     # print("Attacker Utility when Defender thinks 0.5: ", AD55)
#     # print("************************************************")
#
#     print("Attacker Utility without Deception", AD55)
#
#     Attacker_Gain = AD51 - AD55
#     print("Attacker Utility with Deception", AD51)
#     GainOne.append(Attacker_Gain)
#
#
# Defender_Rationality = 0.5
# Rationality = []
# Attacker_Rationality = 0.1
# WithDeceptionWhole = []
# New_Attacker_Rationality = 0.3
# GainThree = []
#
# while Attacker_Rationality < 0.91:
#     print("SCENARIO 1: ATTACKER DOESN'T CHANGE RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#
#     #WithoutDeception.append(Final_Utility_A_A)
#
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#
#     print("SCENARIO 2:ATTACKER CHANGES RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_1 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#
#     print("LEARNING STAGE")
#     # PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, 0.7, Value, F , Defender_Rationality,M)
#     PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA,
#                                                                                             original_PD, New_Attacker_Rationality, Value, F,
#                                                                                             Defender_Rationality, M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_2 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     Attacker_Loss = Attacker_Val_2 - Attacker_Val_1
#     # print("Attacker Loss during Learning", Attacker_Loss)
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD51 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#
#
#     #Rationality.append((New_Attacker_Rationality))
#     #Rationality.append((Attacker_Rationality))
#     Iteration.append(Game_Batches)
#     #WithDeceptionOne.append(AD51)
#     #Game_Iterations = Game_Iterations + 1
#     #Attacker_Rationality = Attacker_Rationality + 0.05
#     Attacker_Rationality = Attacker_Rationality + 0.2
#
#
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     print("Attacker Utility when Defender thinks 0.1: ", AD51)
#     print("************************************************")
#
#     PD = temp_PD
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD55 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     # print("Attacker Utility when Defender thinks 0.5: ", AD55)
#     # print("************************************************")
#
#     print("Attacker Utility without Deception", AD55)
#
#     Attacker_Gain = AD51 - AD55
#     print("Attacker Utility with Deception", AD51)
#     print("************************************************")
#
#     PD = temp_PD
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD55 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     # print("Attacker Utility when Defender thinks 0.5: ", AD55)
#     # print("************************************************")
#
#     print("Attacker Utility without Deception", AD55)
#
#     Attacker_Gain = AD51 - AD55
#     print("Attacker Utility with Deception", AD51)
#     GainThree.append(Attacker_Gain)
#
#
# Defender_Rationality = 0.5
# Rationality = []
# Attacker_Rationality = 0.1
# WithDeceptionWhole = []
# New_Attacker_Rationality = 0.5
# GainFive = []
#
# while Attacker_Rationality < 0.91:
#     print("SCENARIO 1: ATTACKER DOESN'T CHANGE RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#
#     #WithoutDeception.append(Final_Utility_A_A)
#
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#
#     print("SCENARIO 2:ATTACKER CHANGES RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_1 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#
#     print("LEARNING STAGE")
#     # PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, 0.7, Value, F , Defender_Rationality,M)
#     PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA,
#                                                                                             original_PD, New_Attacker_Rationality, Value, F,
#                                                                                             Defender_Rationality, M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_2 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     Attacker_Loss = Attacker_Val_2 - Attacker_Val_1
#     # print("Attacker Loss during Learning", Attacker_Loss)
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD51 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#
#
#     #Rationality.append((New_Attacker_Rationality))
#     #Rationality.append((Attacker_Rationality))
#     Iteration.append(Game_Batches)
#     #WithDeceptionOne.append(AD51)
#     #Game_Iterations = Game_Iterations + 1
#     #Attacker_Rationality = Attacker_Rationality + 0.05
#     Attacker_Rationality = Attacker_Rationality + 0.2
#
#
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     print("Attacker Utility when Defender thinks 0.1: ", AD51)
#     print("************************************************")
#
#     PD = temp_PD
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD55 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     # print("Attacker Utility when Defender thinks 0.5: ", AD55)
#     # print("************************************************")
#
#     print("Attacker Utility without Deception", AD55)
#
#     Attacker_Gain = AD51 - AD55
#     print("Attacker Utility with Deception", AD51)
#     GainFive.append(Attacker_Gain)
#
# Defender_Rationality = 0.5
# Rationality = []
# Attacker_Rationality = 0.1
# WithDeceptionWhole = []
# New_Attacker_Rationality = 0.7
# GainSeven = []
#
# while Attacker_Rationality < 0.91:
#     print("SCENARIO 1: ATTACKER DOESN'T CHANGE RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#
#     #WithoutDeception.append(Final_Utility_A_A)
#
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#
#     print("SCENARIO 2:ATTACKER CHANGES RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_1 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#
#     print("LEARNING STAGE")
#     # PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, 0.7, Value, F , Defender_Rationality,M)
#     PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA,
#                                                                                             original_PD, New_Attacker_Rationality, Value, F,
#                                                                                             Defender_Rationality, M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_2 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     Attacker_Loss = Attacker_Val_2 - Attacker_Val_1
#     # print("Attacker Loss during Learning", Attacker_Loss)
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD51 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#
#
#     #Rationality.append((New_Attacker_Rationality))
#     #Rationality.append((Attacker_Rationality))
#     Iteration.append(Game_Batches)
#     #WithDeceptionOne.append(AD51)
#     #Game_Iterations = Game_Iterations + 1
#     #Attacker_Rationality = Attacker_Rationality + 0.05
#     Attacker_Rationality = Attacker_Rationality + 0.2
#
#
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     print("Attacker Utility when Defender thinks 0.1: ", AD51)
#     print("************************************************")
#
#     PD = temp_PD
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD55 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     # print("Attacker Utility when Defender thinks 0.5: ", AD55)
#     # print("************************************************")
#
#     print("Attacker Utility without Deception", AD55)
#
#     Attacker_Gain = AD51 - AD55
#     print("Attacker Utility with Deception", AD51)
#     GainSeven.append(Attacker_Gain)
#
#
# Defender_Rationality = 0.5
# Rationality = []
# Attacker_Rationality = 0.1
# WithDeceptionWhole = []
# New_Attacker_Rationality = 0.9
# GainNine = []
#
# while Attacker_Rationality < 0.91:
#     print("SCENARIO 1: ATTACKER DOESN'T CHANGE RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#
#     #WithoutDeception.append(Final_Utility_A_A)
#
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#
#     print("SCENARIO 2:ATTACKER CHANGES RATIONALITY")
#     print("LEARNING STAGE")
#     PA, PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, Attacker_Rationality, Value, F , Defender_Rationality,M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_1 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#
#     print("LEARNING STAGE")
#     # PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA, original_PD, 0.7, Value, F , Defender_Rationality,M)
#     PA, temp_PD, Final_Utility_A_L, Final_Utility_D_L, Utility_A, Utility_D = LearningPhase(SA, SD, original_PA,
#                                                                                             original_PD, New_Attacker_Rationality, Value, F,
#                                                                                             Defender_Rationality, M)
#     Final_Utility_A_L = Final_Utility_A_L * CL* Learning_Batches
#     Attacker_Val_2 = Final_Utility_A_L
#     Final_Utility_D_L = Final_Utility_D_L * CL* Learning_Batches
#     #print_vals(PA,SA,Final_Utility_A_L,Utility_A, PD, SD, Final_Utility_D_L, Utility_D,)
#     # print("***************************************")
#
#     Attacker_Loss = Attacker_Val_2 - Attacker_Val_1
#     # print("Attacker Loss during Learning", Attacker_Loss)
#
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD51 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#
#
#     #Rationality.append((New_Attacker_Rationality))
#     #Rationality.append((Attacker_Rationality))
#     Iteration.append(Game_Batches)
#     #WithDeceptionOne.append(AD51)
#     #Game_Iterations = Game_Iterations + 1
#     #Attacker_Rationality = Attacker_Rationality + 0.05
#     Attacker_Rationality = Attacker_Rationality + 0.2
#
#
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     print("Attacker Utility when Defender thinks 0.1: ", AD51)
#     print("************************************************")
#
#     PD = temp_PD
#     print("Game Stage")
#     Final_Utility_A_A , Final_Utility_D_A, Utility_A, Utility_D = GamePhase(SA,SD, PA, PD, Value, F, CA)
#     Final_Utility_A_A = Final_Utility_A_A * CA* Game_Batches
#     AD55 = Final_Utility_A_A
#     Final_Utility_D_A = Final_Utility_D_A * CA* Game_Batches
#     #print_vals(PA,SA,Final_Utility_A_A,Utility_A, PD, SD, Final_Utility_D_A, Utility_D)
#     # print("Attacker Utility when Defender thinks 0.5: ", AD55)
#     # print("************************************************")
#
#     print("Attacker Utility without Deception", AD55)
#
#     Attacker_Gain = AD51 - AD55
#     print("Attacker Utility with Deception", AD51)
#     GainNine.append(Attacker_Gain)
#
# Rationality = np.asarray(Rationality)
# GainOne = np.asarray(GainOne)
# GainFive = np.asarray(GainFive)
# GainThree = np.asarray(GainThree)
# GainSeven = np.asarray(GainSeven)
# GainNine = np.asarray(GainNine)


Rationality=np.loadtxt('/home/tapadhir/Desktop/rationality.txt')
GainOne = np.loadtxt('/home/tapadhir/Desktop/g1.txt'  )
GainThree = np.loadtxt('/home/tapadhir/Desktop/g3.txt'  )
GainFive = np.loadtxt('/home/tapadhir/Desktop/g5.txt'  )
GainSeven = np.loadtxt('/home/tapadhir/Desktop/g7.txt'  )
GainNine = np.loadtxt('/home/tapadhir/Desktop/g9.txt'  )

Rationality = [0.1,0.3,0.5,0.7]


fig = plt.figure()
ax = fig.add_subplot(111)
ax.set_axisbelow(True)




plt.plot([0.1], GainOne[0], 'r', marker = 'D',Label ='$α_{a_{A}}$ = 0.1' , markersize = 4.0)

plt.plot([0.1,0.3], [GainThree[0],GainThree[1]], 'b', marker = 'H', Label ='$α_{a_{A}}$ = 0.3' , markersize = 4.0 )

plt.plot([0.1,0.3,0.5], [GainFive[0], GainFive[1], GainFive[2]], 'g', marker = 'o', Label ='$α_{a_{A}}$ = 0.5', markersize = 4.0 )

plt.plot([0.1,0.3,0.5,0.7], [GainSeven[0], GainSeven[1], GainSeven[2], GainSeven[3]], 'c', marker='^',  Label ='$α_{a_{A}}$ = 0.7', markersize = 4.0 )
plt.plot([0.1,0.3,0.5,0.7,0.9], GainNine, 'm', marker='p' , Label ='$α_{a_{A}}$ = 0.9', markersize = 4.0 )
#
#




plt.grid(zorder = 0)
ax.set_axisbelow(True)

plt.ylabel("Attacker Utility Gain with Dummy Rationality")
plt.xlabel("Attacker Deception Rationality $α_{a_{L}}$")
plt.legend(fancybox=True, framealpha=0.5)
plt.subplots_adjust(bottom=.25, left=.25)
plt.savefig("/home/tapadhir/Desktop/attackerutilitygain.pdf")

#np.savetxt('/home/tapadhir/Desktop/rationalitygain.txt', Rationality)
np.savetxt('/home/tapadhir/Desktop/g1.txt', GainOne )
np.savetxt('/home/tapadhir/Desktop/g3.txt', GainThree )
np.savetxt('/home/tapadhir/Desktop/g5.txt', GainFive )
np.savetxt('/home/tapadhir/Desktop/g7.txt', GainSeven )
np.savetxt('/home/tapadhir/Desktop/g9.txt', GainNine )


