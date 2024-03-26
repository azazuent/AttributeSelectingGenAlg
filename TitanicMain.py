from TitanicDataPreprocessor import get_titanic_data
from MLModels import bayesian


processed_data = get_titanic_data()
result = bayesian(processed_data[0], processed_data[1])

print(result)