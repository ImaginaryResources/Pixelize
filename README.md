# Pixelize <img src="https://github.com/ImaginaryResources/Pixelize/blob/master/examples/icon.png" width = "25">

This program takes an image and pixelizes it by enlarging certain pixels and overriding neighboring pixels with it's color

## How to Use
  - Click "Select File" and pick a valid image file such as png or jpeg. Others **may** work, in this case click all files in file dialog. The image selected will be displayed on top
  - Enter the number of pixels you want to skip in the entry box
  - Click "Pixelize!"
  - Loading bar will complete and the new image will be shown
  - The output image will save where the py file is ran

<img src="https://github.com/ImaginaryResources/Pixelize/blob/master/examples/GUI.png" width = "275"><img src="https://github.com/ImaginaryResources/Pixelize/blob/master/examples/GUI2.png" width = "275">

## Example
I used my multi function in order to create 100 pixelized images from the original image, skipping pixels from 1-100. Then using a video editor I complied them into a gif to show here

<img src="https://github.com/ImaginaryResources/Pixelize/blob/master/examples/pixelizedImages.gif" width = "500">

If you want to use the multi function do the following
```python
# Change this line in the pixelizeButton function from
button = Button(self, text="Pixelize!", command=self.pixelize)
# to 
button = Button(self, text="Pixelize!", command=self.multi)
```

## How it Works
The first two nexted loops visit each pixel if skipBy is one, if skipBy is one then it returns the same image. When skipBy is larger than one, for example two, then it reads every two pixels in the x and y coord of that specific pixel, leaving everything else blank.
```python
for x in range(0, width, skipBy):
  for y in range(0, height, skipBy):
    newPix[x, y] = pixels[x, y]
```
This produces the following image if skipBy is 20, not filled

<img src="https://github.com/ImaginaryResources/Pixelize/blob/master/examples/imageNotFilled.png" width = "500">

In order to fill the blank spots with the selected pixel(x, y) two other for loops are needs in order to visit each pixel in that empty block

```python
for x in range(0, width, skipBy):
  for y in range(0, height, skipBy):
    for r in range(skipBy):
      for c in range(skipBy):
        newPix[x + r, y + c] = pixels[x, y]
```

This produces the following image if skipBy is 20, filled

<img src="https://github.com/ImaginaryResources/Pixelize/blob/master/examples/imageFilled.png" width = "500">

The try block in the code deals with pixels that are out of range
```python
for x in range(0, width, skipBy):
  for y in range(0, height, skipBy):
    for r in range(skipBy):
      for c in range(skipBy):
        try:
          newPix[x + r, y + c] = pixels[x, y]
        except IndexError:
          pass
```

#### Side Notes
Because the pixelize function has to visit every pixel and change it's neighboring pixels by using 4 nested loops it is recommended to use images that aren't too large, the less pixels the better. Speed decreases as image quality increases due to the 4 nested loops that run

The program can run faster with the progress bar commented out, but I find it useful to know when an image is going to finish in cases of larger images and it's satisfying. If you plan on removing the progress bar I suggest to try it with the progress bar first to get an estimated finish time to know relatively how long it should take without the progress bar

Also the wallpaper used in this example can be found [here](http://genchi.info/img/kitkat-hd-wallpapers-24.png) and there are other simliar ones found [here](http://genchi.info/kitkat-hd-wallpaper)

