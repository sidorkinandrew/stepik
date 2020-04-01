import numpy as np

class LogisticRegressionGD:
    '''
    A simple logistic regression for binary classification with gradient descent
    '''

    def __init__(self, seed = 42):
        self.seed = seed

    def __extend_X(self, X):
        """
            Данный метод должен возвращать следующую матрицу:
            X_ext = [1, X], где 1 - единичный вектор
            это необходимо для того, чтобы было удобнее производить
            вычисления, т.е., вместо того, чтобы считать X@W + b
            можно было считать X_ext@W_ext
        """
        return np.hstack((np.ones((X.shape[0], 1)), X))

    def init_weights(self, input_size, output_size):
        """
            Инициализирует параметры модели
            W - матрица размерности (input_size, output_size)
            инициализируется рандомными числами из
            нормального распределения со средним 0 и стандартным отклонением 0.01
        """
        np.random.seed(self.seed)
        self.W = np.random.normal(0, 0.01, (input_size, output_size))  # YOUR_CODE

    def get_loss(self, p, y):
        """
            Данный метод вычисляет логистическую функцию потерь
            @param p: Вероятности принадлежности к классу 1
            @param y: Истинные метки
        """
        #from sklearn.metrics import log_loss
        #return log_loss(y, p)
        return np.mean(-y * np.log(p) - (1 - y) * np.log(1 - p))

    def get_prob(self, X):
        """
            Данный метод вычисляет P(y=1|X,W)
            Возможно, будет удобнее реализовать дополнительный
            метод для вычисления сигмоиды
        """
        if X.shape[1] != self.W.shape[0]:
            X = self.__extend_X(X)
        # import tensorflow as tf
        # _ = tf.nn.sigmoid(X@self.W)
        # return tf.Session().run(_)
        return 1 / (1 + np.exp(-X @ self.W))

    def get_acc(self, p, y, threshold=0.5):
        """
            Данный метод вычисляет accuracy:
            acc = \frac{1}{len(y)}\sum_{i=1}^{len(y)}{I[y_i == (p_i >= threshold)]}
        """
        #from sklearn.metrics import accuracy_score
        #return accuracy_score(y, (int(x>=threshold) for x in p))
        return np.sum(y == (p >= threshold)) / len(y)

    def fit(self, X, y, num_epochs=100, lr=0.001):

        X = self.__extend_X(X)
        self.init_weights(X.shape[1], y.shape[1])

        accs = []
        losses = []
        for _ in range(num_epochs):
            p = self.get_prob(X)

            W_grad = np.dot(X.T, (p - y)) / len(y)
            self.W -= W_grad * lr  # YOUR_CODE

            # необходимо для стабильности вычислений под логарифмом
            p = np.clip(p, 1e-10, 1 - 1e-10)

            log_loss = self.get_loss(p, y)
            losses.append(log_loss)
            acc = self.get_acc(p, y)
            accs.append(acc)

        return accs, losses


model = LogisticRegressionGD()
accs, losses = model.fit(X_train, y_train)
pd.DataFrame(accs,dtype='float').plot()
pd.DataFrame(losses,dtype='float').plot()
