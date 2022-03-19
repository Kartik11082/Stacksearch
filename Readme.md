
# Stacksearch
## _CLI tool Stack Exchange_

Dillinger is a cloud-enabled, mobile-ready, offline-storage compatible,
AngularJS-powered HTML5 Markdown editor.

- Type some Markdown on the left
- See HTML in the right
- ✨Magic ✨

## Features

- Search in any stack exchange site from terminal
- If flags are too uncomfortable there's input mode too
- Know whether question is answered in terminal
- Colored terminal text🤩

## Tech

Dillinger uses a number of projects to work properly:

- [Requests][requestsSite] - HTTP for Humans
- [Argparse][argparseSite] - Parser for command-line options, arguments

And of course Dillinger itself is open source with a [repository][githubPage]
 on GitHub.

## Installation

Stacksearch requires [Python][pythonSIte] to run.

Clone the repository in the startup directory of your terminal

```sh
git clone https://github.com/Kartik11082/Stacksearch.git
cd Stacksearch
```

Install all requirements

```sh
pip install -r requirement.txt
```

## Command Formats

- ### Flags

    - -i: for input mode
    - -q "_Query_": for query to search in title
    - -n _number_:number of responses to return
    - -t "_tags_": for tags
    - -s "_sitename_": for website name

- ### Example commands
    - 

## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [githubPage]: <https://github.com/Kartik11082/Stacksearch>
   [git-repo-url]: <https://github.com/Kartik11082/Stacksearch.git>
   [requestsSite]: <https://docs.python-requests.org/en/latest/>
   [argparseSite]: <https://docs.python.org/3/library/argparse.html>
   [pythonSite]:  <https://www.python.org/>
