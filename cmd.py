import argparse

def readArguments():
	ap = argparse.ArgumentParser()
	ap.add_argument("-n", "--name", required=True,
		help="image name, if name == TIME, then the name will be the timestamp of the moment")
	return vars(ap.parse_args())