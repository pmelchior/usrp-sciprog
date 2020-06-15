Sigma_1 = np.diag(1 / img_flat)

np.linalg.inv(X.T @ Sigma_1 @ X) @ X.T @ Sigma_1 @ img_flat
