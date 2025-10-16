from PIL import Image, ImageEnhance, ImageFilter
import matplotlib.pyplot as plt

# Load your image (update the path to where your image is saved)
img = Image.open(r"ramo.jpg").convert("RGB")

# 1. Reduce brightness slightly
enhancer_brightness = ImageEnhance.Brightness(img)
img = enhancer_brightness.enhance(0.95)

# 2. Reduce saturation for a more natural tone
enhancer_color = ImageEnhance.Color(img)
img = enhancer_color.enhance(0.85)

# 3. Reduce sharpness slightly
enhancer_sharpness = ImageEnhance.Sharpness(img)
img = enhancer_sharpness.enhance(0.8)

# 4. Apply a slight blur to restore skin texture
img = img.filter(ImageFilter.GaussianBlur(radius=0.5))

# Show result
plt.imshow(img)
plt.axis("off")
plt.title("Professional Look")
plt.show()

# Save the result
img.save("professional_headshot.jpg")
