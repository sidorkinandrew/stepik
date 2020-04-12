import numpy as np

test_cases = {
    "TEST 1 (poly1)": {"func": lambda x: x ** 4 + 3 * x ** 3 + x ** 2 - 1.5 * x + 1,
                       "deriv": lambda x: 4 * x ** 3 + 9 * x ** 2 + 2 * x - 1.5,
                       "start": 1, "answer": -1.8772786458333335, "low": -3, "high": 3,
                       },  # -1.877  # -1.897231611784638
    "TEST 2 (poly2)": {"func": lambda x: x ** 4 + 3 * x ** 3 + x ** 2 - 2 * x + 1.0,
                       "deriv": lambda x: 4 * x ** 3 + 9 * x ** 2 + 2 * x - 2.0,
                       "start": 1, "answer": 0.3337, "low": -3, "high": 3,
                       },  # 0.33377777777777773
    "TEST 3 (poly3)": {"func": lambda x: x ** 6 + 3 * x ** 3 + x ** 2 - 2 * x + 1.0,
                      "deriv": lambda x: 6 * x ** 5 + 9 * x ** 2 + 2 * x - 2.0,
                      "start": 1, "answer": 0.39437, "low": -3, "high": 3,
                      },  # 0.3943737373737375
    "TEST 4 (another poly)": {"func": lambda x: x ** 6 + x ** 4 - 10 * x ** 2,
                              "deriv": lambda x: 6 * x ** 5 + 4 * x ** 3 - 20 * x,
                              "start": 1, "answer": 1.2338867187499973, "low": 0, "high": 2,
                              },  # 1.234  # 1.23  # 1.226821473826445  # 1.2327070707070706
    "TEST 5 (another yet poly)": {"func": lambda x: x ** 6 + x ** 4 - 10 * x ** 2 - x,
                                  "deriv": lambda x: 6 * x ** 5 + 4 * x ** 3 - 20 * x - 1,
                                  "start": 1, "answer": 1.2325151515151513, "low": -2, "high": 2,
                                  },  # 1.2325151515151513
    "TEST 6 (and another yet poly)": {"func": lambda x: x ** 20 + x ** 2 - 20 * x + 10,
                                      "deriv": lambda x: 20 * x ** 19 + 2 * x - 20,
                                      "start": 1, "answer": 1.0, "low": -1, "high": 2,
                                      },  # 0.994 # 0.9944531641016026 # 1.0003333333333333
    "TEST 7 (1 - exp(log^2(x)) with constants)": {
        "func": lambda x: 1 - 3 / 2 * 1 / x * np.exp(-(np.log(x)) ** 2 / 2 * (3 / 2) ** 2),
        "deriv": lambda x: (3 * np.exp(-9 / 8 * (np.log(x)) ** 2) * (4 + 9 * np.log(x))) / (8 * x ** 2),
        "start": 1, "answer": 0.6411318154091585, "low": 0, "high": 2,
    },  # 0.641  # 0.6255984124239972    #0.6411318154091585 # 0.6471414141414141
    "TEST 8 (|x|/x^2 - x + sqrt(-x) + (even polynom))": {
        "func": lambda x: 5 * np.abs(x) / x ** 2 - 0.5 * x + 0.1 * np.sqrt(-x) + 0.01 * x ** 2,
        "deriv": lambda x: -0.5 - 0.05 / np.sqrt(-x) + 0.02 * x + 5 / (x * np.abs(x)) - (10 * np.abs(x)) / x ** 3,
        "start": 1, "answer": -2.917049893465909, "low": -5, "high": -2,
    },  # -2.917 #-2.917059466693251 # -2.9087878787878787
}


def grad_descent_v2(func, deriv, low=None, high=None, callback=None):
    """
    Реализация градиентного спуска для функций с несколькими локальным минимумами,
    но с известной окрестностью глобального минимума.
    Все тесты будут иметь такую природу.
    :param func: float -> float — функция
    :param deriv: float -> float — её производная
    :param low: float — левая граница окрестности
    :param high: float — правая граница окрестности
    """
    extremums = {}
    for i in np.arange(low, high, 0.001):
        if i == 0.0:
            continue
        if deriv(i) < 0.001:
            extremums[func(i)] = i
    return extremums[min(extremums)]


def callback(x, y):
    print('x = {:.6}, y = {:.6}, dx/dy = {:.6}'.format(float(x), float(y), float(deriv_func(x))))


for idx, atest in enumerate(test_cases):
    print(atest, "low:", test_cases[atest]["low"], "high:", test_cases[atest]["high"], end=" ")
    func = test_cases[atest]["func"]
    deriv_func = test_cases[atest]["deriv"]
    res = grad_descent_v2(func, deriv_func, low=test_cases[atest]["low"], high=test_cases[atest]["high"],
                          callback=callback)
    print("result:", round(res, 5), "answer:", test_cases[atest]["answer"], "diff:", round(test_cases[atest]["answer"] - res, 5))
