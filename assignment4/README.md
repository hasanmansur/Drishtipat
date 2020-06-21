# Part 4

Feature Extraction | Curvature & Distance Transform computation | Chamfer matching
----------------------------------------------------------------------------------

The goal is too use image
features to detected phases of gait. The binary images in the GaitImages folder are images of a moving person imaged from a
side. The task is to apply a variety of algorithms for feature
extraction and image recognition to these images.
There are several stages to this assignment:

1. Apply functions listed in \Structural Analysis and Shape Descriptors" section of OpenCV
documentation to compute various features on the silhouettes of the person. Find and display image boundaries/contours. Find polygonal approximation of computed boundaries and
compute convex hull and the deficits of convexity for the shapes. Compute area, perimeter,
and all first and second order image moments for the original image and for the convex hull.
Illustrate the process of feature calculation on two different image and display the contour
with marked polygonal approximation and the convex hull. Note that this means that you
have to mark and draw the corresponding polygons.
