import matplotlib.pyplot as plt
import numpy as np

x = np.array([2023, 2024, 2025, 2026])
y1 = np.array([15, 25, 30, 20])
y2 = np.array([17, 23, 38, 51])
y3 = np.array([1, 23, 38, 5])

line_style = dict(marker=".",
                  markersize=30,
                  markerfacecolor="#1cd3fc",
                  markeredgecolor="#1cd3fc",
                  linestyle="solid",
                  linewidth=4,
                  )

plt.plot(x, y1,color="#1c5bfc", **line_style)
plt.plot(x, y2,color = "#890a24", **line_style)
plt.plot(x, y3,color = "#098729", **line_style)

plt.show()