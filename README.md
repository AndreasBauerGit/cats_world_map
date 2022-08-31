# catsmap
a density map of all the cats (meow)


# Roadmap

 * [ ] train initial Unet for cat detection on few images
 * [ ] write a programm to extract immages from google maps
 should systematically scan a square shaped area, e.g. a city.
 images should be split up and cropped to 600 by 600 pixel.
 see here https://stackoverflow.com/questions/51009488/scrape-google-street-view-images-of-multiple-location
  * [ ] apply unet to google maps images and extract actual cats from google maps
  * [ ] optimize training parameters and iteratively improve network training
  * [ ] construct cat density
  * [ ] consider correction for additional factors (daytime, vegetation, lighting)
  * [ ]  designe website that hosts a map
  * [ ] extract funny/ random ... cat pictures; produce user interaction
  * [ ] automatic hook to social media
