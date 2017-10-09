import numpy as np
import statsmodels.api as sm

def simple_linear_regression(x, y, n_train):
    x = sm.add_constant(x)

    # linear regression
    model = sm.OLS(y[:n_train], x[:n_train])
    results = model.fit()

    params = results.params
    pred = results.predict(x[n_train:])

    print('prediction: ', str(pred))
    print('parameters: ', params)