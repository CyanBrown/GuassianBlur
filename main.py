from PIL import Image
import numpy as np
import math

im = Image.open('mushrooms.jpg').convert("RGB")
im_matrix = np.array(im)
new_image = im_matrix.copy()


def f_gaussian(x, y, std):
    return math.pow(math.e, (-(x ** 2) - (y ** 2)) / (2 * std ** 2)) / (2 * math.pi * (std ** 2))


def norm_kernel(k):
    sum = 0
    for i in k:
        sum += math.fsum(i)

    for y in range(len(k)):
        for x in range(len(k)):
            k[y][x] = k[y][x] / sum

    return k


def gen_kernel(rad):
    k = []
    std = max(rad / 2, 1)

    for y in range(-rad, rad + 1):
        temp = []
        for x in range(-rad, rad + 1):
            temp.append(f_gaussian(x, y, std))
        k.append(temp)

    return norm_kernel(k)


rad = 5
k = gen_kernel(rad)

for y in range(rad, len(im_matrix)-rad):
    print(y)
    for x in range(rad, len(im_matrix[0])-rad):

        rgb = [0,0,0]

        for k_y in range(-rad, rad+1):
            for k_x in range(-rad, rad+1):
                px = im_matrix[y+k_y][x+k_x]

                rgb[0] += k[rad+k_y][rad+k_x] * px[0]
                rgb[1] += k[rad+k_y][rad+k_x] * px[1]
                rgb[2] += k[rad+k_y][rad+k_x] * px[2]

        new_image[y][x] = tuple(rgb)

new_image_obj = Image.fromarray(new_image)
new_image_obj.save("gaussian_blur.jpg")