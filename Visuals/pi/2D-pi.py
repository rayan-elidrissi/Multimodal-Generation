from mpmath import mp
import numpy as np
import matplotlib.pyplot as plt
import math
import datetime

timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
filename = f"C:/Users/re234371/Pictures/pi/pi_rgb_image_{timestamp}.png"

# Number of digits
N = 10000000 #don't go over 1M on local computing

# Ensure N is a perfect square multiple of 3
sqrt_N = int(math.sqrt(N // 3 * 3))
N = (sqrt_N * sqrt_N) * 3

# Get pi digits using mpmath
mp.dps = N + 1  # Set decimal places for pi generation to account for "3."
pi_digits_large = str(mp.pi)[2:N + 2]  # Slice to get only the N decimal digits

# Convertion from string to an integers list
pi_digits_list_large = [int(digit) for digit in pi_digits_large]

# Calculate the number of digits per channel
digits_per_channel = N // 3

# Calculate the rows and columns for a square shape for each channel
rows = cols = int(math.sqrt(digits_per_channel))

# Split the list into three channels and reshape each
r_channel = np.array(pi_digits_list_large[0:digits_per_channel]).reshape((rows, cols))
g_channel = np.array(pi_digits_list_large[digits_per_channel:2 * digits_per_channel]).reshape((rows, cols))
b_channel = np.array(pi_digits_list_large[2 * digits_per_channel:3 * digits_per_channel]).reshape((rows, cols))

# Stack to form an RGB image (normalize values for visualization)
rgb_image = np.stack((r_channel, g_channel, b_channel), axis=-1) / 9.0

# Display the generated RGB image
plt.imshow(rgb_image)
plt.axis('off')
#plt.savefig(filename, format="png", dpi=300, bbox_inches="tight")
plt.show()
