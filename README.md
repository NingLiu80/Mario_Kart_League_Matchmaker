## Table of Contents

- [Table of Contents](#table-of-contents)
- [About The Project](#about-the-project)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [How To Run](#how-to-run)
- [License](#license)
- [Contact](#contact)

## About The Project

When i was organizing a local tournament for Mario Kart 8 Deluxe on the switch with several people,
i realized:

- It's really hard to manually create a match plan
- No success in Google search attempts finding a tool to create match plans for 4 players simultaneously
- Also ChatGPT was no help

This tool creates a csv file with a match plan for x people, playing y times, where x and y are variable

## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisites

This project was tested with Python 3.9.13.

### How To Run

Just type in shell or terminal:
```sh
python MarioKartLeague.py
```
which generates a default mariokart.csv file with the match lists of 10 players, who are playing 2
matches against each other.

If you want to change the parameters, refer to the help
```sh
optional arguments:
  -h, --help       show this help message and exit
  --player PLAYER  How many Player
  --times TIMES    How many times each Player needs to play
  --fname FNAME    Name of CSV File
```

## License

This program is free software: you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation, version 3. See
<http://www.gnu.org/licenses/>
