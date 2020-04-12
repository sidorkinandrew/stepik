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
    starts = np.linspace(low, high, 11)
    estimates = []
    results = []
    lr = 0.004
        
    for start in starts:
        estimate = start  
        for _ in range(1000):
            estimate -= lr*deriv(estimate)
        estimates.append(estimate)
        results.append(func(estimate))
        
    return estimates[results.index(min(results))]