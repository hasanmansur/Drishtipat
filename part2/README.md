# Part 2 ( Windowing | Mean, Standard Deviation | Color Histograms | Histogram Comparison )

 1. Implementing the following exercise from the book "Concise Computer Vision"

    ![Image of picks](https://hasanmansur.github.io/drishtipat/part2/prob1.png)

    code: prob_1.py

 2. For this part we will use the images from ST2MainHall4 folder.

   - Building color histograms for all images in the folder 'ST2MainHall4'. Color histogram should be
   512-bin: [(r/32) ∗ 64 + (g/32) ∗ 8 + b/32] will convert a color value into an index. To be noted that 
   all divisions are integer divisions as in C programming language. That means that they can be accomplished using bit shifts.

   - Writing two functions for histograms comparison: histogram intersection and chisquared measure. 
     - Histogram intersection. Given two color histograms H1(·) and H2(·) their intersection is given by

       ![Image of histintdef](https://hasanmansur.github.io/drishtipat/part2/hist_int_def.png)

       Large values correspond to high similarity.

     - Chi-squared measure(χ2): Given two histograms H1 and H2 the χ2 measure of their similarity is given by

       ![Image of chidef](https://hasanmansur.github.io/drishtipat/part2/chi_def.png)

       Small values correspond to high similarity.

   - Comparing all image pairs with the use of histogram comparison functions.

   code: prob_2.py

Results
-------
https://hasanmansur.github.io/drishtipat/part2/
