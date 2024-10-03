import threading
import os
import time

try:
    from tqdm import tqdm
except ImportError:
    print("The 'tqdm' module is not installed. Installing it now...")
    os.system('pip install tqdm')
    from tqdm import tqdm

def grep_lines(input_file, search_string, output_file):
    def search_and_write(lines, search_string, outfile_path, progress_bar=None, count_list=None):
        count = 0
        search_string = search_string.lower()
        with open(outfile_path, 'a', encoding='utf-8') as outfile:
            for line in lines:
                if search_string in line.lower():
                    outfile.write(line)
                    count += 1
                if progress_bar:
                    progress_bar.update(1)
        if count_list is not None:
            count_list.append(count)

    try:
        with open(input_file, 'r', encoding='utf-8') as infile:
            lines = infile.readlines()
            num_threads = 8
            chunk_size = len(lines) // num_threads
            threads = []
            count_list = []

            progress_bar = tqdm(total=len(lines), desc="[+] Searching", unit="lines")

            for i in range(num_threads):
                start_index = i * chunk_size
                end_index = len(lines) if i == num_threads - 1 else (i + 1) * chunk_size
                thread = threading.Thread(target=search_and_write, args=(lines[start_index:end_index], search_string, output_file, progress_bar, count_list))
                threads.append(thread)
                thread.start()

            for thread in threads:
                thread.join()

            progress_bar.close()

        total_count = sum(count_list)
        print(f"[+] Lines containing '{search_string}' have been written to '{output_file}'. Total lines found: {total_count}")
    except FileNotFoundError:
        print(f"[+] The file '{input_file}' was not found.")
    except Exception as e:
        print(f"[+] An error occurred: {e}")

if __name__ == "__main__":
    while True:
        input_file = input("[+] Enter the path of the file to search: ")
        search_string = input("[+] Enter the string to search for: ")
        output_file = input("[+] Enter the full path for the output file (including filename and .txt extension): ")

        grep_lines(input_file, search_string, output_file)
        
        user_input = input("[+] Enter 'a' to search again, or press Enter to exit: ")
        if user_input.lower() != 'a':
            break
