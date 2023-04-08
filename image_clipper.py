from PIL import Image

img = Image.open("src/test2.jpg")
width, height = img.size
square_size = min(width, height)
img = img.crop(((width-square_size) // 2, (height-square_size) // 2,
        (width+square_size) // 2, (height+square_size) // 2))
block_size = square_size // 5

for i in range(0, 5):
    for j in range(0, 5):
        # Crop the block
        block = img.crop((j*block_size, i*block_size, j*block_size+block_size, i*block_size+block_size))
        
        # Save the block
        block.save(f"src/puzzle/{i}_{j}.png")