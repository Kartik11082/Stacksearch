# Imports
import requests
import argparse

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


def make_request(tag, query):
	"""
		Sends requests to Stackoverflow and return a JSON response.
	"""
	print("Searching in StackOverflow for " + UIElements['style__CBOLD'] + query + UIElements['__CD'])
	stackoverflowURL = "https://api.stackexchange.com/"+"2.2/search?order=desc&tagged={}&sort=activity&intitle={}&site=stackoverflow".format(tag, query)
	resp  = requests.get(stackoverflowURL)
	return resp.json()


def printResults(items, number):
	print(UIElements['style__CITALIC'] + "Total results" + UIElements['__CD'], len(items))
	for item in items[:number]:
		print("\n", UIElements['style__CBOLD'] + UIElements['color__CBEIGE'] + UIElements['style__CITALIC'] + UIElements['style__CSELECTED'] + "Title: ", item['title'] + UIElements['__CD'])
		print(UIElements['style__CURL'] + UIElements['color__CBEIGE'] + UIElements['style__CITALIC'] + "Link : ", item['link'] + UIElements['__CD'])
		if (item['is_answered']):
			print(UIElements['style__CITALIC'] + UIElements['color__Lime'] + 'Answered->', '\u2713' + UIElements['__CD'], end="\n")
		else:
			print(UIElements['color__CRED']  + UIElements['style__CITALIC'] + 'Answered->', '\u274C' + UIElements['__CD'], end="\n")

	return

if __name__ == "__main__":
	"""
		Defines command line argument parser.
		Inputs 'search query' and 'number of responses to return' from command line arguments.
		Prints title and link to Stackoverflow pages.
	"""
	try:
		# Create the parser
		parser = argparse.ArgumentParser()

		# Add an argument
		parser.add_argument('-q', type=str, required=True)
		parser.add_argument('-n', type=int, required=True)
		parser.add_argument('-t', type=str, required=False, default="python")

		# Parse the argument
		args = parser.parse_args()

		# Send request and print the json response
		jsonResponse = make_request(args.t, args.q)
		items = jsonResponse['items']

		# print(items)

		printResults(items, args.n)

	except IndexError:
		"""
			If user doesn't enter any command line arguments.
		"""
		# print(UIElements['color__CRED'] + "Command line arguments not entered" + UIElements['__CD'])
		print(UIElements['color__CRED']+"Command format: searchStack \"Query\" number_of_reponse"+UIElements['__CD'])