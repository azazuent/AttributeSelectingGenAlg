import pandas

from MLModels import bayesian
from AttributeSelectingGenAlg import AttributeSelectingGenAlg

test_ratio = 0.4

data = pandas.read_csv("../datasets/Tic_tac_toe.csv", header=None)

data = data.replace("b", 0)
data = data.replace("o", 1)
data = data.replace("x", 2)
data = data.replace("positive", True)
data = data.replace("negative", False)

target = data.iloc[:, 9]
data = data.drop(columns=9)

res1 = bayesian(data, target, test_ratio)
res2 = AttributeSelectingGenAlg(data, target,
                                mutation_p=0.1,
                                test_ratio=test_ratio,
                                population_power=200,
                                population_cap=50,
                                iteration_amount=100,
                                crossover_type="uniform")
print(f"Achieved {res2[0]} vs {res1}")
print("With:")
for solution in res2[1]:
    print(solution)
