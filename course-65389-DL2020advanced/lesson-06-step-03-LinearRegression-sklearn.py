from sklearn.linear_model import LinearRegression as LR
from sklearn.metrics import mean_squared_error, mean_absolute_error

np.random.seed(42)

model2 = LR()
model2.fit(X_train, Y_train)

pred2 = model2.predict(X_train)

norm_gen = lambda p: lambda preds, y: np.mean(np.linalg.norm(preds - y, ord=p, axis=1)**p)
#norm_gen_correct = lambda p: lambda preds, y: np.mean(np.linalg.norm(preds-y, ord=p, axis=0)**p/len(y))

mae, mse = [norm_gen(l_p_metric) for l_p_metric in [1,2]]
#mae_correct, mse_correct = [norm_gen_correct(l_p_metric)  for l_p_metric in [1,2]]

print(mse(pred2, Y_train), mae(pred2, Y_train))
print(mean_squared_error(pred2, Y_train), mean_absolute_error(pred2, Y_train))
#print(mse_correct(pred2, Y_train), mae_correct(pred2, Y_train))