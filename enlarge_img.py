from PIL import Image
import sys

def multiply_img_size(orig_file, new_file, mult):
	orig_img = Image.open(orig_file)
	orig_img_pixels = orig_img.load()
	orig_img_size = orig_img.size

	new_img_size = (orig_img_size[0]*mult, orig_img_size[1]*mult)
	new_img = Image.new("RGB", new_img_size)
	new_img_pixels = new_img.load()
	
	for i in range(new_img_size[0]):
		for j in range(new_img_size[1]):
			new_img_pixels[i,j] = orig_img_pixels[i//mult,j//mult]
			
	new_img.save(new_file)

if __name__ == '__main__':
	if len(sys.argv) == 4:
		multiply_img_size(sys.argv[1], sys.argv[2], int(sys.argv[3]))
	else:
		print('Improper usage! Should be: python.exe enlarge_img.py orig_file new_file mult')
