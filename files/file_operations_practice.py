import pandas as pd
# Practice file operations and efficient file processing in Python

# 1. Read a file line by line using a for loop
def read_file_line_by_line(filename):
    """Read and print each line from a file one at a time."""
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

# 2. Use a generator to yield lines from a file
def file_line_generator(filename):
    """Generator that yields lines from a file one at a time."""
    with open(filename, 'r') as file:
        for line in file:
            yield line.strip()

# 3. Read a CSV file row by row using csv.reader
import csv

def read_csv_file(filename):
    """Read a CSV file row by row efficiently."""
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)

# 4. Read a pipe-delimited file line by line
def read_pipe_delimited(filename):
    """Read a pipe-delimited file line by line."""
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip().split('|'))

# 5. Convert a CSV file to a Parquet file using pandas
def csv_to_parquet(csv_filename, parquet_filename):
    """Convert a CSV file to a Parquet file using pandas."""
    df = pd.read_csv(csv_filename)
    df.to_parquet(parquet_filename)
    print(f"Converted {csv_filename} to {parquet_filename}")

# 6. Demonstrate usage
def main():
    # Replace 'sample.txt' and 'sample.csv' with your test files
    print("Read file line by line:")
    # read_file_line_by_line('sample.txt')

    print("\nFile line generator:")
    # for line in file_line_generator('sample.txt'):
    #     print(line)

    print("\nRead CSV file:")
    # read_csv_file('sample.csv')

    print("\nRead pipe-delimited file:")
    # read_pipe_delimited('sample_pipe.txt')

    print("\nConvert CSV to Parquet:")
    # csv_to_parquet('sample.csv', 'output.parquet')

if __name__ == "__main__":
    main()
