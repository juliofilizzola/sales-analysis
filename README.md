# Sales Analysis

## Project Description
This project performs sales analysis using Pandas and Matplotlib. It includes data loading, cleaning, metric calculation, and visualization of sales data.

## Requirements
- Python >= 3.12
- Pandas >= 2.2.3, < 3.0.0
- Matplotlib >= 3.10.0, < 4.0.0

## Installation
1. Clone the repository:
    ```sh
    git clone https://github.com/juliofilizzola/sales-analysis.git
    cd sales-analysis
    ```

2. Install dependencies using Poetry:
    ```sh
    poetry install
    ```

## Usage
1. Activate the virtual environment:
    ```sh
    poetry shell
    ```

2. Run the main script:
    ```sh
    python main.py
    ```

## Project Structure
- `data/`: Contains the sales data file `vendas.csv`.
- `outputs/`: Directory where the generated graphs will be saved.
- `scripts/`: Contains the modules for data loading, cleaning, metric calculation, and visualization.
- `main.py`: Main script to run the analysis.

## Scripts
- `data_loader.py`: Loads the sales data from a CSV file.
- `data_cleaner.py`: Cleans the loaded data.
- `analyzer.py`: Calculates metrics from the cleaned data.
- `visualize.py`: Generates graphs from the cleaned data.

## Author
- Julio Filizzola (juliofilizzola@hotmail.com)