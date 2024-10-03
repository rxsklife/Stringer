# Stringer - Multi-threaded Line Grepper
A Python script that searches for a specific string in a text file and writes the matching lines to an output file. The script utilizes multithreading to enhance performance and provides a progress bar to indicate the search progress.

## Features

- Multi-threaded searching for improved performance.
- Progress bar to visualize the search progress.
- Handles large files efficiently by dividing the workload among multiple threads.
- User-friendly interface for input and output file paths.

## Requirements

- Python 3.x
- `tqdm` library (automatically installed if not present)

## Usage
1. Run the script:
```bash
python stringer.py
```

3. Follow the prompts to enter:
 - The path of the file to search. (C:\Users\Name\Downloads\bigtextfile.txt)
 - The string to search for.
 - The full path for the output file, including filename and .txt extension. (C:\Users\Name\Downloads\results.txt)

After the search is complete, the script will display the total number of lines found containing the search string.
You can choose to search again or exit.

## Error Handling

If the specified input file is not found, an error message will be displayed.
Any other exceptions will be caught and printed to the console.

## Contributing

Contributions are welcome! If you have suggestions for improvements or new features, feel free to open an issue or submit a pull request.
