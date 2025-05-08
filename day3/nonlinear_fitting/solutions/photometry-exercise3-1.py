img_flat = img.flatten()
model_flat = model.flatten()

const = np.ones(model_flat.shape)
X = np.stack((model_flat, const), axis=1)
theta = np.array((300, 100))
scaled_model_flat = X @ theta

plt.imshow(scaled_model_flat.reshape(33, 33))
plt.colorbar()
