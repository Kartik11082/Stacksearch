
# Stacksearch
## _CLI tool Stack Exchange_

Stacksearch is a CLI tool for searching in Stack Exchange websites through terminal

## Features

- Search in any stack exchange site from terminal
- If flags are too uncomfortable there's input mode too
- Know whether question is answered in terminal
- Colored terminal text🤩

## Tech

Stacksearch uses a number of projects to work properly:

- [Requests][requestsSite] - HTTP for Humans
- [Argparse][argparseSite] - Parser for command-line options, arguments

And of course Stacksearch itself is open source with a [repository][githubPage]
 on GitHub.

## Installation

Stacksearch requires [Python][pythonSIte] to run.

Clone the repository in the startup directory of your terminal

```sh
git clone https://github.com/Kartik11082/Stacksearch.git
cd Stacksearch
```
![cloning](https://user-images.githubusercontent.com/49190983/159106823-b894c7bf-5e51-4f31-b81e-b2ddd98fbefc.gif)


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

- ### Example
- Searching in terminal
![run](https://user-images.githubusercontent.com/49190983/159106838-b8489b47-8a14-4b52-b68f-ff2042e5013c.gif)
- Input mode
![inputmode](https://user-images.githubusercontent.com/49190983/159106854-e0911baa-bd30-41ab-9606-282d501da10f.gif)


## License

MIT

**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

   [githubPage]: <https://github.com/Kartik11082/Stacksearch>
   [git-repo-url]: <https://github.com/Kartik11082/Stacksearch.git>
   [requestsSite]: <https://docs.python-requests.org/en/latest/>
   [argparseSite]: <https://docs.python.org/3/library/argparse.html>
   [pythonSite]:  <https://www.python.org/>
