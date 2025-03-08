 
# PubMed Fetcher

## Overview
PubMed Fetcher is a Python-based command-line tool designed to retrieve research papers from PubMed, filter non-academic authors affiliated with pharmaceutical/biotech companies, and output the results as a CSV file.

## Features
- Fetches research papers from PubMed
- Filters non-academic authors based on heuristics (e.g., email addresses, keywords like 'university', 'labs')
- Outputs results in a structured CSV format
- Implemented as a modular Python package
- CLI tool for easy execution

## Installation

### Prerequisites
- Python 3.8+
- Poetry (for dependency management)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/gopilakke/pubmed-fetcher.git
   cd pubmed-fetcher
   ```
2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```
3. Activate the virtual environment:
   ```sh
   poetry shell
   ```

## Usage

### Running the CLI tool
To fetch and filter research papers, use:
```sh
get-papers-list --query "diabetes" --output results.csv
```
Options:
- `--query` : Search term for PubMed
- `--output` : Output CSV filename

### Running as a Python Module
```python
from pubmed_fetcher import fetch_papers
fetch_papers("diabetes", "results.csv")
```

## Project Structure
```
pubmed-fetcher/
│── cli/
│   ├── main.py  # CLI entry point
│── pubmed_fetcher/
│   ├── fetch.py  # Core fetching logic
│   ├── filter.py  # Author filtering logic
│── pyproject.toml  # Poetry config
│── README.md
```

## Contributing
1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Push to your fork and submit a PR

## License
This project is licensed under the MIT License.
