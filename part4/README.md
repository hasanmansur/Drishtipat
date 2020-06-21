# Part 4 (Feature Extraction | Curvature & Distance Transform computation | Chamfer matching)

The binary images in the GaitImages folder are images of a moving person imaged from a side. The task is to apply a variety of algorithms for feature
extraction and image recognition to these images. There are several stages to this task:

1. Apply functions listed in "Structural Analysis and Shape Descriptors" section of OpenCV
documentation to compute various features on the silhouettes of the person. Find and display image boundaries/contours. Find polygonal approximation of computed boundaries and
compute convex hull and the deficits of convexity for the shapes. Compute area, perimeter,
and all first and second order image moments for the original image and for the convex hull.
Illustrate the process of feature calculation on two different image and display the contour
with marked polygonal approximation and the convex hull. Note that this means that you
have to mark and draw the corresponding polygons.

2. Create a table with computed values for all frames: display the computed features. For
deficits of convexity compute the number and their total area.

3. Given an image boundary implement the method from the book to compute curvature
along the boundary. Use color coding to display computed values in an image. The color
scheme should be used to display curvature with higher curvature values represented by
‘hotter’ colors. Mark the local maxima of the curvature. You should experiment with the
window size (−k; +k) to determine what works well for curvature estimation. Discuss your
choices.

4. Given a silhouette boundary its distance transform corresponds to distances of nonboundary pixels to nearest boundary point. Compute distance transform for all boundaries.
The algorithm is described in the book. Use Euclidean distance transform. Display at least
two files showing the computed distance transform results.

5. Chamfer matching is a technique used for matching (possibly noisy) image boundaries.
It utilizes distance transform. The method will be described in class and the slides will be
posted. Implement chamfer matching and use it to match all pairs of gait images in the
provided sequence.

6. Analyze the results in parts 2 and 5. What can you conclude.
(a) Is there periodicity and how it shows in results (parts 2 & 5)?
(b) Two most distinct phases of gait correspond to the widest and the narrowest profiles.
Can you detect them from features displayed in 2.
(c) Could you use curvature to detect joints and segment body parts? How?


Code files:
-----------
1,2 : p12.py
3   : p3.py
4   : p4.py
5   : p5.py


