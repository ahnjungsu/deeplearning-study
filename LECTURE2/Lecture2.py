import torch

"""
w = torch.tensor(2.0, requires_grad=True)
a = w*3
l = a*a

#dl/dw = dl/da * da/dw

l.backward()
print('\nl을 w로 미분한 값은 {}'.format(w.grad))
"""

"""
x_t = 3.0
lr = 0.1

print('\n')

for it in range(100):
    x = torch.tensor(x_t, requires_grad=True)
    y = 0.1 * (x ** 4) + (x ** 3) + 2 * (x ** 2) - 5 * x + 2

    print("x : %f / y : %f" %(x_t, y))

    # y를 최소화 하는게 목적: dy/dx
    y.backward() # x.grad

    x_t = x_t - lr * x.grad
"""

x_t = -7.0
# local minimum problem
print('\n')

for it in range(200):
    # learning rate scheduling
    if it < 100:
        lr = 0.25
    else:
        lr = 0.025

    x = torch.tensor(x_t, requires_grad=True)
    y = 0.1 * (x ** 4) + (x ** 3) + 2 * (x ** 2) - 5 * x + 2

    print("x : %f / y : %f" %(x_t, y))

    # y를 최소화 하는게 목적: dy/dx
    y.backward() # x.grad

    x_t = x_t - lr * x.grad