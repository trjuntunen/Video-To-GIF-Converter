# Python program to convert a portion of a video file
# to a GIF file.

from moviepy.editor import *
import sys
import os

def main():

	argsLength = len(sys.argv)

	# Argument length has to be either 3 or 4 depending on 
	# if the -i flag is given, which uploads the GIF to Imgur.
	validateCommandLineArgumentLength(argsLength)

	# The video file to convert to a GIF.
	clip = sys.argv[1]

	# The name of the output file to write the GIF to.
	outputFile = sys.argv[2]

	# If the video file exists:
	# 	- Validate the name
	#	- Write the GIF to the output file.
	#	- Optimize the GIF to make the file size smaller.
	if videoFileExists(clip):
		outputFile = validateoutputFile(outputFile)
		writeGif(VideoFileClip(clip), outputFile)
		optimizeOutputFile(outputFile)

		# If the "-i" flag is given as an argument, then upload 
		# the gif at the end to Imgur.
		if argsLength == 4 and sys.argv[3] == "-i":
			uploadGifToImgur(outputFile)


# Validate command line argument length, and exit if invalid.
def validateCommandLineArgumentLength(length):
	if length != 3 and length != 4:
		print("Usage: python vidToGif.py <video file to convert> <name of output gif file>")
		exit(0)

# Write a gif from the given clip to the given output file.
def writeGif(clip, outputFile):
	clip.write_gif(outputFile, fps=20)
	print(outputFile,"created successfully.")

# Check if the video fioutputFileNamele exists.
def videoFileExists(videoFile):
	if os.path.isfile(videoFile):
		return True
	print("Video file doesn't exist.")
	return False

# If the given output file name does not contain .gif
# at the end, then add it.
def validateoutputFile(outputFile):
	if outputFile[-4:] != ".gif":
		outputFile += ".gif"
	return outputFile

# Uses Gifsicle library to significantly shrink output GIF file size for better performance.
def optimizeOutputFile(outputFile):

	# Maybe in the future, add functionality to change the scale depending
	# on the size of the original video, as well as the amount of colors to be
	# displayed based on the video.

	command = "gifsicle --batch --optimize=3 --scale 0.5 --colors 256 " + outputFile
	os.system(command)
	print(outputFile,"optimized successfully.")

# Uploads GIF to Imgur and prints to the console the URL.
def uploadGifToImgur(outputFile):
	command = "./imgur.sh " + outputFile
	os.system(command)
	print(outputFile,"uploading to Imgur successfully.")

# Call the main method to start the program.
main()