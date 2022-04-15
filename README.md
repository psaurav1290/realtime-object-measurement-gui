# Image Processing Lab
## Term Project
## Object Dimensions Measurement

### Team DEMENTORS
#### Members :
1.	Aditya Kumar Dubey (BTECH/10246/19)
2.	Saurav Priyadarshi (BTECH/10348/19)
3.	Aswat Singh Bisht (BTECH/10402/19)
4.	Nitansh Ritul (BTECH/10438/19)
5.	Saketh Kumar Pabba (BTECH/10602/19)


## Introduction 
"Object Dimension Measurement" is a software for detecting the dimensions of  objects. It takes an image with a white background of known dimension(A4 sheet) with  objects  placed on it and displays its dimensions in the specified measuring units. We have created a system that uses the OpenCV software library to implement the proposed technique.
We determine the reference object, an A4 sheet, before we can calculate the size of each object. Following that, the dimensions of the objects within the reference are calculated and displayed.




## Methodology
In utils.py file, In the Input image contours  were found and processed to find the dimensions of objects .

Created a canny image of the input image. Applied dilation and erosion features so that the process of creating a canny image is smooth.

Determined the white paper's(A4 sheet) constraint, which is a rectangle.

The software takes into account the orientation and perspective of the reference sheet. 
Considered the variation of the edge lengths due to different perspectives and calculated the average lengths of the horizontal edges and vertical edges and the page's orientation is consequently determined. 
Hence it works for both horizontal and vertical orientations.

Applied filter as a rectangle because the background white paper is rectangle. Finalizied the contours appending the length and area. Hence specifying the detection of the A4 sheet. 

With the help of the canny image the dimensions of objects placed on the A4 sheet were measured.

Displayed an arrowed line representing the length and breadth of the objects and estimated their magnitude. 

## Results
![Original Image and Output Image with Measurements](https://github.com/dubeyaditya6232/ObjectsDimensionMeasurement/blob/master/images/readme-image.png)
