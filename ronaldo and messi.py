import matplotlib.pyplot as plt
import matplotlib.image as mpimg

# Load Ronaldo and Messi images
ronaldo_img = mpimg.imread('ronaldo.jpg')
messi_img = mpimg.imread('messi.jpg')

# Display Ronaldo image
plt.imshow(ronaldo_img)
plt.title('Cristiano Ronaldo')
plt.axis('off')
plt.show()

# Display Messi image
plt.imshow(messi_img)
plt.title('Lionel Messi')
plt.axis('off')
plt.show()