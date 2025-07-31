### How to use Image Generation with API key and DALL-e-3 ###
import base64

# Image Prompt
image_prompt = "Add your prompt here (i.e. A photo of a labrador swimming)"

print("\nGenerating Image...")

# Generate image response
response_img = client.images.generate(
    model="dall-e-3",
    prompt=image_prompt,
    n=1,
    size="1024x1024",
    response_format="b64_json",
)
 
# Write and save image data
if response_img.data and response_img.data[0].b64_json:
    image_base64 = response_img.data[0].b64_json
    image_bytes = base64.b64decode(image_base64)

    with open("generated_image.png", "wb") as f:
        f.write(image_bytes)
    print("Image saved as 'generated_image.png'")
else:
    print("Image generation failed or returned no data.")
