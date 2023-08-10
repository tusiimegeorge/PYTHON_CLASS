#1a)
class FileHandler:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.file:
            self.file.close()

# Example usage
filename = 'example.txt'

with FileHandler(filename, 'w') as file:
    file.write('Hello, world!')

# The file is automatically closed outside the context manager

#1b)

import sqlite3

class DatabaseConnection:
    def __init__(self, db_name):
        self.db_name = db_name
        self.connection = None

    def __enter__(self):
        self.connection = sqlite3.connect(self.db_name)
        return self.connection

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.connection:
            self.connection.commit()
            self.connection.close()

# Example usage
db_name = 'example.db'

with DatabaseConnection(db_name) as connection:
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (id INTEGER PRIMARY KEY, name TEXT)")

    # Inserting data into the table
    cursor.execute("INSERT INTO users (name) VALUES ('John')")
    cursor.execute("INSERT INTO users (name) VALUES ('Jane')")

    # Fetching data from the table
    cursor.execute("SELECT * FROM users")
    results = cursor.fetchall()
    for row in results:
        print(row)

# The database connection is automatically closed outside the context manager


#1c)

import threading
import multiprocessing
import time

def task(duration):
    print(f"Starting task with duration {duration} seconds...")
    start_time = time.time()
    while time.time() - start_time < duration:
        pass
    print(f"Task completed after {duration} seconds.")

# Using multithreading
def run_with_threads():
    durations = [1, 2, 3, 4, 5]

    threads = []
    for duration in durations:
        t = threading.Thread(target=task, args=(duration,))
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("All tasks completed with threading.")

# Using multiprocessing
def run_with_processes():
    durations = [1, 2, 3, 4, 5]

    processes = []
    for duration in durations:
        p = multiprocessing.Process(target=task, args=(duration,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All tasks completed with multiprocessing.")

# Run the examples
print("Running with threading:")
run_with_threads()

print("\nRunning with multiprocessing:")
run_with_processes()
