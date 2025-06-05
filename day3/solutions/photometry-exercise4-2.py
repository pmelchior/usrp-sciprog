f, s, xm, ym, w = result.x
theta = 0
model = Gaussian2D.evaluate(X, Y, f, xm, ym, w, w, theta) + s

fig,axes = plt.subplots(1,3,figsize=(12,3))
residual = img - model
for data, label, ax in zip([img, model, residual],
                           ["data","model","residual"],axes):
    plt.sca(ax)
    plt.imshow(data)
    plt.colorbar()
    plt.title(label)
plt.tight_layout()