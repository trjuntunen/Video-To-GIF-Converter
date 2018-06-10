# Python program to convert a portion of a video file
# to a GIF file.

from moviepy.editor import *
import sys
import os

def main():

	validateCommandLineArgumentLength()

	clip = sys.argv[1]
	outputFileName = sys.argv[2]

	# If the video file exists, then write it to the given output file.
	if videoFileDoesExist(clip):
		writeGif(VideoFileClip(clip), validateOutputFileName(outputFileName))

# Validate command line argument length, and exit if invalid.
def validateCommandLineArgumentLength():
	if len(sys.argv) != 3:
		print("Usage: python vidToGif.py <video file to convert> <name of output gif file>")
		exit(0)

# Write a gif from the given clip to the given output file.
def writeGif(clip, outputFileName):
	clip.write_gif(outputFileName)

# Check if the video file exists.
def videoFileDoesExist(videoFile):
	if os.path.isfile(videoFile):
		return True
	print("Video file doesn't exist.")
	return False

# If the given output file name does not contain .gif
# at the end, then add it.
def validateOutputFileName(outputFileName):
	if outputFileName[-4:] != ".gif":
		outputFileName += ".gif"
	return outputFileName

# Call the main method to start the program.
main()