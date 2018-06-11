# Video-To-GIF-Converter

<strong><h3>Summary</h3></strong>
Written in Python. Converts any video file to an animated GIF using the MoviePy library, and then optimizes the GIF file to significantly decrease the file size using the Gifsicle library. Optinally, it can upload the GIF to Imgur. Example shown uses .mp4, but any format works.

<hr>

<strong><h3>Usage:</h3></strong>
python vidToGif.py videotoConvert.mp4 outputFile.gif <br>
python vidToGif.py videoToConvert.mp4 outputFile.gif -i

- If the -i flag is given, uploads to Imgur after.

<hr>

<strong><h3>Dependencies:</h3></strong>
MoviePy - https://zulko.github.io/moviepy/index.html

Gifsicle - https://www.lcdf.org/gifsicle/
