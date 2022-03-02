# Imports
import sys
import requests


# Colors and text styles for terminal texts
UIElements = {
	"style__CBOLD"		:'\33[1m',
	"style__CITALIC"	:'\33[3m',
	"style__CURL"		:'\33[4m',
	"style__CSELECTED"	:'\33[7m',
	"color__CBEIGE"		:'\33[36m',
	"color__CWHITE"		:'\33[37m',
	"color__Lime"		:'\33[92m',
	"color__CBLUE"		:'\33[34m',
	"color__CRED"		:'\33[31m',
	"color__CREDBG"		:'\33[41m',
	"__CD"				:'\033[0m',
}

def make_request(args):
	"""
		Sends requests to Stackoverflow and return a JSON response.
	"""
	print("Searching in StackOverflow for " + UIElements['style__CBOLD'] + args)
	stackoverflowURL = "https://api.stackexchange.com/"+"2.2/search?order=desc&tagged=python&sort=activity&intitle={}&site=stackoverflow".format(args)
	resp  = requests.get(stackoverflowURL)
	return resp.json()


def printResults(items, cmdArgs):
	print(UIElements['style__CITALIC'] + "Total results", len(items))
	for item in items[:int(cmdArgs[1])]:
		print(UIElements['style__CBOLD'] + UIElements['color__CBEIGE'] + UIElements['style__CITALIC'] + UIElements['style__CSELECTED'] + "Title: ", item['title'] + UIElements['__CD'])
		print(UIElements['style__CURL'] + UIElements['color__CBLUE'] + UIElements['style__CITALIC'] + "Link : ", item['link'] + UIElements['__CD'], end="\n\n")


if __name__ == "__main__":
	"""
		Inputs 'search query' and 'number of responses to return' from command line arguments.
		Prints title and link to Stackoverflow pages.
	"""
	try:
		cmdArgs = sys.argv[1:]
		jsonResponse = make_request(cmdArgs[0])
		items = jsonResponse['items']
		printResults(items, cmdArgs)
	except IndexError:
		"""
			If user doesn't enter any command line arguments.
		"""
		print(UIElements['color__CRED'] + "Command line arguments not entered" + UIElements['__CD'])
		print(UIElements['color__CRED'] + "Command format: searchStack 'Query' number_of_reponses" + UIElements['__CD'])