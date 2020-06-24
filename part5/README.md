# Part 5 (Stereo Matching | Disparity | Depth Image | Belief Propagation)

You are given a pair of small stereo images (21 × 21). You can assume that the stereo
cameras were in a canonical position with f = 20mm (500 pixels) for both cameras and the
baseline b = 20cm.

<img src="images/left.png" width="200">        <img src="images/right.png" width="200">

Use the images in the folder 'Images'. You can assume that the maximum disparity in these images is dmax = 6. Write a Python program to do the following:

- Using EZCEN (zero-mean normalized cenzus) as the data error term compute all dmax + 1 initial message boards for the entire image and disparities d = 0, . . . , dmax. Print the values obtained for rows 9, 10, 11.
- Show which disparities would be picked immediately after initialization of the message boards for all points of the image. In the case of the same value for multiple disparities leave the value as undefined. Print the values obtained for rows 9, 10, 11. Compute depths of all points in the image for computed disparities. Display the results as an image and print the results obtained for rows 9, 10, 11.
- Use belief-propagation matching algorithm to smooth the disparities. What should the smoothness term be if you want the disparities to be piecewise constant, i.e. the cost does not change as the disparity difference changes, it is the same whether the difference
is 1 or dmax? You should show two steps of BPM algorithm. What disparities did you get?

Code: part5.py
