# 1 To show color image
import cv2

img = cv2.imread(r"d:\pic\flasha\Carton\80721.jpg", cv2.IMREAD_COLOR)
cv2.imshow("a", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2 To show Grayscale image
import cv2

img2 = cv2.imread(r"C:\Users\DELL\Desktop\test\apple.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("b", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 3 To return matrix dimension for color image
import cv2

img = cv2.imread(r"C:\Users\DELL\Desktop\test\apple.jpg", cv2.IMREAD_COLOR)
cv2.imshow("a", img)
print(img.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 4 To Return matrix dimension for grayscale image
import cv2

img2 = cv2.imread(r"d:\pic\flasha\Carton\80721.jpg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("b", img2)
print(img2.shape)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 5 To print the matrix for color image
import cv2

img = cv2.imread(r"d:\pic\flasha\Carton\80721.jpg", cv2.IMREAD_COLOR)
print(img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 6 To print the matrix for Grayscale image
import cv2

img2 = cv2.imread(r"C:\Users\DELL\Desktop\test\apple.jpg", cv2.IMREAD_GRAYSCALE)
print(img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 7 to determine dimension both of color image & grayscale image
# To print the first value for the pixel

import cv2

img = cv2.imread(r"d:\pic\flasha\Carton\80721.jpg", cv2.IMREAD_COLOR)[0, 0, :]
img2 = cv2.imread(r"d:\pic\flasha\Carton\80721.jpg", cv2.IMREAD_GRAYSCALE)[0, 0]
print("first pixel of color image:", img)
print("first pixel of grayscale image", img2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 8 To write text on image
import cv2
from matplotlib import pyplot as plt

img = cv2.imread(r"d:\pic\flasha\Carton\80721.jpg")
b, g, r = cv2.split(img)
img = cv2.merge([r, g, b])
cv2.putText(img, "hello my friend", (10, 300), 0, 3, (255, 0, 0), 3)
plt.imshow(img)
plt.show()
