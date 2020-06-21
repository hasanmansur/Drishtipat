# Part 4 (Feature Extraction | Curvature & Distance Transform computation | Chamfer matching)

The binary images in the GaitImages folder are images of a moving person imaged from a side. The task is to apply a variety of algorithms for feature
extraction and image recognition to these images. There are several stages to this task:

1. 
   - Finding and displaying image boundaries/contours. 
   - Finding polygonal approximation of computed boundaries and computing convex hull and the deficits of convexity for the shapes. 
   - Computing area, perimeter and all first and second order image moments for the original image and for the convex hull.
   - Illustrating the process of feature calculation on two different image and displaying the contour with marked polygonal approximation and the convex hull.

   code: p12.py

2. 
   - Creating a table with computed values for all frames
   - Displaying the computed features. For deficits of convexity computing the number and their total area.

   code: p12.py

3. 
   - Given an image boundary, implementing the method from the book "Concise Computer Vision" to compute curvature along the boundary. 
   - Using color coding to display computed values in an image. The color scheme should be used to display curvature with higher curvature values represented by
     ‘hotter’ colors. 
   - Experimenting with the window size (−k; +k) to determine what works well for curvature estimation.

   code: p3.py

4. Given a silhouette boundary its distance transform corresponds to distances of nonboundary pixels to nearest boundary point. 
   - Using  Euclidean distance transform to compute distance transform for all boundaries. The algorithm is described in the book "Concise Computer Vision".
   - Displaying at least two files to show the computed distance transform results.

   code: p4.py

5. Chamfer matching is a technique used for matching (possibly noisy) image boundaries.
   - Implementing chamfer matching and using it to match all pairs of gait images in the provided sequence.

   code: p5.py

6. Analysis of the results in steps 2 and 5.
(a) Is there periodicity and how it shows in results (parts 2 & 5)?
(b) Two most distinct phases of gait correspond to the widest and the narrowest profiles. Can we detect them from features displayed in 2.
(c) Could we use curvature to detect joints and segment body parts? How?


Results
-------
https://hasanmansur.github.io/drishtipat/part4/





