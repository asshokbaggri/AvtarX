import os

BASE = "backend/models"

folders = [
    "instant_id_weights",
    "ip_adapter_weights",
    "stable_diffusion",
    "wav2lip_weights",
    "sadtalker_weights"
]

print("Preparing model folders...")

for f in folders:
    path = f"{BASE}/{f}"
    os.makedirs(path, exist_ok=True)
    print(f"✓ Created: {path}")

print("\nDownload your model weights and place them inside these folders.")
print("Example:")
print(" - backend/models/instant_id_weights/instantid.pth")
print(" - backend/models/ip_adapter_weights/ip_adapter.bin")
