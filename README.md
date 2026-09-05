# Advent of Code

Welcome to my Advent of Code solutions repository. This repository contains my solutions for the Advent of Code
challenges.

## About Advent of Code

[Advent of Code](https://adventofcode.com/) is an annual coding challenge event that takes place in December. Each day,
a new challenge is released, and participants work to solve the puzzles using their programming skills.

## First Time Setup

To set up the project for the first time, follow these steps:

1. Clone the repository:

```sh
git clone https://github.com/CatGamer23/adventofcode.git
cd adventofcode
```

2. Install the required dependencies:

```sh
uv sync
```

3. (**Important**) Delete all input files to avoid incorrect answers, as each input is unique per user.

*Linux/MacOS:*

```sh
find . -type d -name 'Inputs' -exec rm -rf {} +
```

4. Add your Advent of Code session cookie to a `.env` file:

Create a `.env` file in the root directory and add your session cookie:

```
COOKIE=<your-session-cookie>
```

This cookie is required to download the input files automatically.

5. Run the setup script:

```sh
python main.py -s
```

## Running the Solutions

To run the main script, navigate to the root directory and execute `main.py` with the appropriate command-line
arguments. For example:

```sh
python main.py --year 2021 --day 1
```

Here are the available command-line arguments:

- `--year` (`-y`): The year of the challenge (e.g., 2021).
- `--day` (`-d`): The day of the challenge (e.g., 1).
- `--setup` (`-s`): (Optional) Set up the environment for a specific year and day. For example, it can create necessary
  directories and download input files.

## Structure

Each year's solutions are organized into separate directories. Each directory contains the solutions for that year's
challenges.

```
.
├── 2015
│   ├── 01.py
│   ├── 02.py
│   ├── ...
│   └── Inputs
│       ├── Day 01 Input.txt
│       ├── Day 02 Input.txt
│       └── ...
├── 2024
│   ├── 01.py
│   ├── 02.py
│   ├── ...
│   └── Inputs
│       ├── Day 01 Input.txt
│       ├── Day 02 Input.txt
│       └── ...
├── LICENSE
├── main.py
├── README.md
├── pyproject.toml
└── TODO.md
```

## License

This project is licensed under the GNU GPLv2 License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [Advent of Code](https://adventofcode.com/) by Eric Wastl
- [Python](https://www.python.org/)

Happy coding!
