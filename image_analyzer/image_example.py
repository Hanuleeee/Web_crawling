from skimage import data, io
from matplotlib import pyplot as plt

camera = data.camera() # camera image ; grey scale
io.imshow(camera)  # 함수이용해서 불러옴 512*512
plt.show()
print(type(camera), camera.shape)
print(camera)

cat = data.chelsea() # cat is a 300-by-451 pixel image with three channels (red, green, and blue)
io.imshow(cat)
plt.show()
print(type(cat), cat.shape)
print(cat)