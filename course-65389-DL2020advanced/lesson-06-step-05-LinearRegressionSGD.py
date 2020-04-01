import numpy as np

def batch_generator(X, y, batch_size=100):
    """
        Необходимо написать свой генератор батчей.
        Если вы не знаете, что такое генератор, то, возможно,
        вам поможет
        https://habr.com/ru/post/132554/
        В данном генераторе не надо перемешивать данные
    """
    num_samples = X.shape[0]
    # Заметьте, что в данном случае, если num_samples не делится на batch_size,
    # то последние элементы никогда не попадут в обучение
    # в данном случае нас это не волнует
    num_batches = num_samples // batch_size
    for i in range(num_batches - 1):
        # Необходимо отдать batch_size обьектов и соответствующие им target
        yield X[i * batch_size:(i + 1) * batch_size], y[i * batch_size:(i + 1) * batch_size]


class LogisticRegressionSGD:
    def __init__(self, seed=42):
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
        return np.mean(-y * np.log(p) - (1 - y) * np.log(1 - p))

    def get_prob(self, X):
        """
            Данный метод вычисляет P(y=1|X,W)
            Возможно, будет удобнее реализовать дополнительный
            метод для вычисления сигмоиды
        """
        if X.shape[1] != self.W.shape[0]:
            X = self.__extend_X(X)
        return 1 / (1 + np.exp(-X @ self.W))

    def get_acc(self, p, y, threshold=0.5):
        """
            Данный метод вычисляет accuracy:
            acc = \frac{1}{len(y)}\sum_{i=1}^{len(y)}{I[y_i == (p_i >= threshold)]}
        """
        return np.sum(y == (p >= threshold)) / len(y)

    def fit(self, X, y, num_epochs=10, lr=0.001):

        X = self.__extend_X(X)
        self.init_weights(X.shape[1], y.shape[1])

        accs = []
        losses = []
        for _ in range(num_epochs):
            gen = batch_generator(X, y)
            for X_, y_ in gen:
                p = self.get_prob(X_)

                W_grad = np.dot(X_.T, (p - y_)) / len(y_)
                self.W -= W_grad * lr  # YOUR_CODE

                # необходимо для стабильности вычислений под логарифмом
                p = np.clip(p, 1e-10, 1 - 1e-10)

                log_loss = self.get_loss(p, y_)
                losses.append(log_loss)
                acc = self.get_acc(p, y_)
                accs.append(acc)

        return accs, losses


model = LogisticRegressionGD()
accs, losses = model.fit(X_train, y_train)
pd.DataFrame(accs,dtype='float').plot()
pd.DataFrame(losses,dtype='float').plot()

# task 5
accs_mean, losses_mean = np.mean(accs), np.mean(losses)
accuracy = model.get_acc(model.get_prob(X_test),y_test, threshold=0.5)
