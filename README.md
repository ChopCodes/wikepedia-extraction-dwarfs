# Wikipedia Extraction Dwarfs

This repository contains Python code to extract data from a Wikipedia page and save it to a CSV file. Specifically, the code extracts data about brown dwarfs from the following Wikipedia page: https://en.wikipedia.org/wiki/List_of_brown_dwarfs.

## Requirements

To run this code, you need to have Python 3.x and the following packages installed:

- `beautifulsoup4`
- `pandas`
- `requests`

You can install these packages using `pip` and `requirements.txt`. For example:
`pip install requirements.txt`

## Usage

To use this code, simply run the `extract.py` file. This will scrape the data from the Wikipedia page and save it to a CSV file named `dwarfstars.csv`.

# Create A Virtual-env
`python -m venv myenv`
## Activate the virtual environment
Windows: `myenv\Scripts\activate`
macOS/Linux: `source myenv/bin/activate`
