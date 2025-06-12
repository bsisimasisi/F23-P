import threading

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def check_primes(start, end, result):
    local_primes = [n for n in range(start, end) if is_prime(n)]
    result.extend(local_primes)

def threaded_prime_checker(range_start, range_end, num_threads=4):
    step = (range_end - range_start) // num_threads
    threads = []
    result = []
    result_lock = threading.Lock()

    def thread_wrapper(start, end):
        local = []
        check_primes(start, end, local)
        with result_lock:
            result.extend(local)

    for i in range(num_threads):
        start = range_start + i * step
        end = range_end if i == num_threads - 1 else start + step
        thread = threading.Thread(target=thread_wrapper, args=(start, end))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return result

if __name__ == "__main__":
    primes = threaded_prime_checker(1, 100, num_threads=4)
    print("Primes:", primes)


import threading
from collections import defaultdict

def process_lines(lines, word_count, lock):
    local_count = defaultdict(int)
    for line in lines:
        words = line.strip().lower().split()
        for word in words:
            local_count[word] += 1
    with lock:
        for word, count in local_count.items():
            word_count[word] += count

def threaded_word_counter(file_path, num_threads=4):
    with open(file_path, 'r') as f:
        lines = f.readlines()

    step = len(lines) // num_threads
    threads = []
    word_count = defaultdict(int)
    lock = threading.Lock()

    for i in range(num_threads):
        start = i * step
        end = len(lines) if i == num_threads - 1 else start + step
        thread = threading.Thread(target=process_lines, args=(lines[start:end], word_count, lock))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    return dict(word_count)

if __name__ == "__main__":
    counts = threaded_word_counter("sample.txt", num_threads=4)
    for word, count in sorted(counts.items()):
        print(f"{word}: {count}")

