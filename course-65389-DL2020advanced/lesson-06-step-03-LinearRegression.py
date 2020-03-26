import numpy as np  

class LinearRegression:
	def __init__(self, l_p_metric=2, seed=42):
		"""
		:param l_p_metric: Задаёт метрику для оптимизации.
		Значение 1 соответсвует MAE, 2 — MSE.
		:param seed: radom_seed для случайной инициализации весов
		"""
    # Используйте np.linalg.norm
		self.metric = lambda preds, y: np.sum(abs(preds-y)**l_p_metric)/y.shape[0]
		#self.metric = lambda preds, y: np.linalg.norm(preds - y, (None if l_p_metric == 2 else 1))/y.shape[0]
		self.seed = seed

		self.W = None
		self.b = None

	def init_weights(self, input_size, output_size):
		"""
		Инициализирует параметры модели
		:param W: - матрица размерности (input_size, output_size)
		инициализируется рандомными числами из
		нормального распределения со средним 0 и стандартным отклонением 0.01
		:param b: - вектор размерности (1, output_size)
		инициализируется нулями
		"""
		np.random.seed(self.seed)
		self.W = np.random.normal(0,0.01,(input_size, output_size))# YOUR_CODE
		self.b = np.zeros((1, output_size), dtype=float) # YOUR_CODE

	def fit(self, X, y, num_epochs=1000, lr=0.001):
		"""
			Обучение модели линейной регрессии методом градиентного спуска
			:param X: размерности (num_samples, input_shape)
			:param y: размерности (num_samples, output_shape)
			:param num_epochs: количество итераций градиентного спуска
			:param lr: шаг градиентного спуска
			:return metrics: вектор значений метрики на каждом шаге градиентного
			спуска. Метрика контролируется параметром l_p_metric в конструкторе
		"""
		self.init_weights(X.shape[1], y.shape[1])
		metrics = []
		for _ in range(num_epochs):
			preds = self.predict(X)
			# сделайте вычисления градиентов без циклов,
			# используя только numpy
            
			W_grad = 2/X.shape[0]*X.T.dot(preds - y)
			b_grad = np.mean(2*(preds - y), axis=0)
			self.W -= W_grad * lr # YOUR_CODE
			self.b -= b_grad * lr # YOUR_CODE
			metrics.append(self.metric(preds, y))
		return metrics

	def predict(self, X):
		"""
		Думаю, тут все понятно. Сделайте свои предсказания :)
		"""
		return X.dot(self.W)+self.b #  YOUR_CODE