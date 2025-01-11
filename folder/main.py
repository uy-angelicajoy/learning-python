import threading

def read_file(filenames):
    try:
        with open(filenames, "r") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: {filenames} not found."
    except Exception as e:
        return f"Error reading {filenames}: {e}"

def multi_threaded_file_reader(Filenames):
    threads = []
    results = {}
    lock = threading.Lock()  

    def read_file_thread(filenames):
        result = read_file(filenames)
        with lock:  
            results[filenames] = result

    for filenames in Filenames:
        thread = threading.Thread(target=read_file_thread, args=(filenames,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return results

if __name__ == "__main__":
    filenamess = ["file1.txt", "file2.txt", "file3.txt", "file4.txt"]
    results = multi_threaded_file_reader(filenamess)
    separator_size = 50
    for filenames, content in results.items():
        print(f"Reading {filenames}:")
        print(content)
        print("-" * separator_size)