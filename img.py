import base64
from PIL import Image

image_prompt = f"A real photo of a delicious {cooking_method} {ingredient} dish served as a {dish_type}."

print("\nGenerating Dish Image...")

# Generate image using base64 instead of URL
response_img = client.images.generate(
    model="dall-e-3",
    prompt=image_prompt,
    n=1,
    size="1024x1024",
    response_format="b64_json",
)
 
# Extract base64 image data
if response_img.data and response_img.data[0].b64_json:
    image_base64 = response_img.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    with open("generated_recipe_image.png", "wb") as f:
        f.write(image_bytes)
    print("Image saved as 'generated_recipe_image.png'")

    # Display the image
    img = Image.open("generated_recipe_image.png")
    img.show()
else:
    print("Image generation failed or returned no data.")
