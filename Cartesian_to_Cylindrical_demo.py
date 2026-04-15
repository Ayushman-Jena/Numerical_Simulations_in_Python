import numpy as np
import matplotlib.pyplot as plt

# -------------------------------
# Create Cartesian Grid
# -------------------------------
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)

X, Y = np.meshgrid(x, y)

# -------------------------------
# Convert to Cylindrical Coordinates
# -------------------------------
R = np.sqrt(X**2 + Y**2)          # radial distance
Theta = np.arctan2(Y, X)          # angle in radians

# -------------------------------
# Plotting
# -------------------------------
plt.figure(figsize=(12, 5))

# --- Cartesian Space ---
plt.subplot(1, 2, 1)
plt.contourf(X, Y, R)
plt.colorbar(label="Radius (r)")
plt.title("Cartesian Space (x, y)")
plt.xlabel("x")
plt.ylabel("y")
plt.axis('equal')

# --- Cylindrical Space ---
plt.subplot(1, 2, 2)
plt.contourf(Theta, R, R)
plt.colorbar(label="Radius (r)")
plt.title("Cylindrical Space (r, θ)")
plt.xlabel("θ (radians)")
plt.ylabel("r")

plt.tight_layout()
plt.show()