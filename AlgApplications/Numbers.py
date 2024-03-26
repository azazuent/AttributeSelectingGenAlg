from sklearn import datasets
import pandas as pd

from AttributeSelectingGenAlg import AttributeSelectingGenAlg
from MLModels import bayesian

test_ratio = 0.3

data = datasets.load_digits()

target = pd.Series(data.target)
data = pd.DataFrame(data.data)

result_1 = bayesian(data, target, test_ratio)
result_2 = AttributeSelectingGenAlg(data, target, test_ratio=test_ratio)

print(f"Achieved {result_2[0]} vs {result_1}")
print("With:")
for solution in result_2[1]:
    for i in range(0, 8):
        index = i * 8
        [print('-' if not c else '*', end=' ') for c in solution[index:index+8]]
        print()
    print("\n\n")
