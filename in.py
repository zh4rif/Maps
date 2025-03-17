import torch
import torch.nn as nn
import torch.optim as optim
import numpy as np
import rasterio
import matplotlib.pyplot as plt

# Function to load InSAR image
def load_insar_image(file_path):
    with rasterio.open(file_path) as src:
        img = src.read(1)  # Read first band (interferogram)
    img = np.nan_to_num(img)  # Replace NaNs with 0
    img = (img - np.min(img)) / (np.max(img) - np.min(img))  # Normalize
    return img

# CNN Model for Denoising
class DenoiseCNN(nn.Module):
    def __init__(self):
        super(DenoiseCNN, self).__init__()
        self.encoder = nn.Sequential(
            nn.Conv2d(1, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 32, kernel_size=3, padding=1),
            nn.ReLU()
        )
        self.decoder = nn.Sequential(
            nn.Conv2d(32, 16, kernel_size=3, padding=1),
            nn.ReLU(),
            nn.Conv2d(16, 1, kernel_size=3, padding=1)
        )

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x

# Load and preprocess data
image_path = "dem_0.tiff"  # Change to your file path
img = load_insar_image(image_path)

# Convert to PyTorch tensor
img_tensor = torch.tensor(img, dtype=torch.float32).unsqueeze(0).unsqueeze(0)  # Add batch & channel dims

# Initialize model, loss, and optimizer
model = DenoiseCNN()
criterion = nn.MSELoss()
optimizer = optim.Adam(model.parameters(), lr=0.001)

# Dummy training loop (for demonstration)
for epoch in range(5):  # Only 5 epochs for quick run
    optimizer.zero_grad()
    output = model(img_tensor)
    loss = criterion(output, img_tensor)  # Loss between input and output (autoencoder style)
    loss.backward()
    optimizer.step()
    print(f"Epoch {epoch+1}, Loss: {loss.item():.6f}")

# Convert output back to NumPy array
denoised_img = output.detach().squeeze().numpy()

# Visualize before & after denoising
fig, ax = plt.subplots(1, 2, figsize=(10, 5))
ax[0].imshow(img, cmap='gray')
ax[0].set_title("Original InSAR Image")
ax[1].imshow(denoised_img, cmap='gray')
ax[1].set_title("Denoised InSAR Image")
plt.show()
