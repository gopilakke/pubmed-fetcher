# PubMed Fetcher

## Overview
PubMed Fetcher is a Python command-line tool designed to fetch research papers from PubMed, filter out non-academic authors affiliated with pharmaceutical/biotech companies, and output the results as a CSV file.

## Features
- Fetches research papers from PubMed.
- Identifies papers with at least one non-academic author.
- Supports CSV output for filtered results.
- Implements heuristics to detect non-academic affiliations.
- Provides a CLI interface for ease of use.

## Installation
### Prerequisites
- Python 3.8+
- Poetry (for dependency management)

### Install from TestPyPI
```sh
pip install --index-url https://test.pypi.org/simple/ --no-deps gopi-pubmed-fetcher
```

### Clone and Install Locally
```sh
git clone https://github.com/yourusername/pubmed-fetcher.git
cd pubmed-fetcher
poetry install
```

## Usage
### CLI Usage
Run the command-line tool to fetch papers based on a search query:
```sh
get-papers-list --query "diabetes" --output results.csv
```

### Arguments
- `--query`: Search query for PubMed.
- `--output`: File path for the CSV output.
- `--debug`: Enable debug mode for logging.

## Project Structure
```
├── cli
│   ├── __init__.py
│   ├── main.py
├── pubmed_fetcher
│   ├── __init__.py
│   ├── fetch.py
│   ├── filter.py
│   ├── export.py
├── tests
│   ├── test_filter.py
├── pyproject.toml
├── poetry.lock
├── README.md
```

## Development
### Running Tests
```sh
pytest tests/
```

### Building the Package
```sh
poetry build
```

### Publishing to TestPyPI
```sh
poetry publish -r testpypi
```

## License
This project is licensed under the MIT License.

