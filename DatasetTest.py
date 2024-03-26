from sklearn import datasets
import pandas as pd
from MLModels import bayesian
from AttributeSelectingGenAlg import AttributeSelectingGenAlg

#data = datasets.load_iris()
data = datasets.load_digits()

target = pd.Series(data.target)

data = pd.DataFrame(data.data)
#print(data)
# mask = '0001101010110111111111100010010101110100110110001011000111100100'
# maskbool = []
# for c in mask:
#     if c == '0':
#         maskbool.append(False)
#     else:
#         maskbool.append(True)
# data = data.loc[:, maskbool]

print(bayesian(data, target, 0.33))
print(AttributeSelectingGenAlg(data, target,
                               mutation_p=0.1,
                               population_power=100,
                               population_cap=50,
                               iteration_amount=100,
                               crossover_type="two_point",
                               weight_of_1=0.65))
