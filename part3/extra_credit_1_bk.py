# gradients for gray image
sobelx = cv.Sobel(img_gray,cv.CV_32F,1,0,ksize=5)
sobely = cv.Sobel(img_gray,cv.CV_32F,0,1,ksize=5)

# downscaling the image size for faster computation
sobelx = sobelx[::50, ::50]
sobely = sobely[::50, ::50]
print(sobelx.shape, sobely.shape)

# plotting
fig, ax = plt.subplots()
ax.quiver(sobelx, sobely)
ax.set(aspect=1, title='Quiver Plot: Gray Image')
plt.show()
