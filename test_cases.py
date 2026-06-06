# =====================================================
# TEST CASES UNTUK EVALUASI EXTENSION
# Research: LLM Code Intelligence
# Cara pakai: 
# 1. Buka file ini di VS Code
# 2. Select salah satu fungsi
# 3. Klik kanan → pilih fitur LLM
# 4. Catat hasilnya untuk paper
# =====================================================


# ─────────────────────────────────────────────────────
# KATEGORI 1: BUG DETECTION TEST CASES
# (Kode yang sengaja ada bugnya)
# ─────────────────────────────────────────────────────

# TC-BUG-01: Division by zero
def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)  # BUG: crash jika list kosong


# TC-BUG-02: Index out of range
def get_first_and_last(lst):
    first = lst[0]   # BUG: crash jika list kosong
    last = lst[-1]
    return first, last


# TC-BUG-03: Wrong logic operator
def is_valid_age(age):
    if age > 0 or age < 150:   # BUG: harusnya 'and' bukan 'or'
        return True
    return False


# TC-BUG-04: SQL Injection vulnerability
def get_user(username, db):
    query = f"SELECT * FROM users WHERE name = '{username}'"  # BUG: SQL injection
    return db.execute(query)


# TC-BUG-05: Infinite loop
def countdown(n):
    while n != 0:   # BUG: jika n negatif → infinite loop
        print(n)
        n -= 1


# TC-BUG-06: Wrong return type
def multiply_all(numbers):
    result = 0      # BUG: harusnya result = 1 untuk perkalian
    for n in numbers:
        result *= n
    return result


# TC-BUG-07: Missing exception handling
def read_file(filename):
    with open(filename, 'r') as f:   # BUG: tidak ada try-except
        return f.read()


# TC-BUG-08: Off-by-one error
def get_last_n_items(lst, n):
    return lst[len(lst)-n+1:]   # BUG: off by one, harusnya len(lst)-n


# ─────────────────────────────────────────────────────
# KATEGORI 2: TEST GENERATION TEST CASES
# (Kode bersih yang perlu dibuatkan test-nya)
# ─────────────────────────────────────────────────────

# TC-TEST-01: String manipulation
def reverse_words(sentence):
    """Membalik urutan kata dalam kalimat."""
    words = sentence.split()
    return ' '.join(reversed(words))


# TC-TEST-02: Number operations
def is_prime(n):
    """Mengecek apakah bilangan adalah prima."""
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True


# TC-TEST-03: List operations
def remove_duplicates(lst):
    """Menghapus duplikat dari list sambil menjaga urutan."""
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result


# TC-TEST-04: Dictionary operations
def group_by_length(words):
    """Mengelompokkan kata berdasarkan panjangnya."""
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    return groups


# TC-TEST-05: Math operations
def celsius_to_fahrenheit(celsius):
    """Mengkonversi suhu dari Celsius ke Fahrenheit."""
    return (celsius * 9/5) + 32


# ─────────────────────────────────────────────────────
# KATEGORI 3: CODE REVIEW TEST CASES
# (Kode yang berfungsi tapi kualitasnya buruk)
# ─────────────────────────────────────────────────────

# TC-REVIEW-01: Tidak efisien & tidak readable
def f(x):
    r = []
    for i in range(len(x)):
        if x[i] % 2 == 0:
            r.append(x[i] * x[i])
    return r


# TC-REVIEW-02: Magic numbers & poor naming
def calc(a, b, c):
    x = a * 3.14159 * b * b
    y = (1/3) * x * c
    return y


# TC-REVIEW-03: Duplicate code
def get_student_grade(score):
    if score >= 90:
        print("Grade: A")
        print("Status: Excellent")
        return "A"
    if score >= 80:
        print("Grade: B")
        print("Status: Good")
        return "B"
    if score >= 70:
        print("Grade: C")
        print("Status: Average")
        return "C"
    if score >= 60:
        print("Grade: D")
        print("Status: Below Average")
        return "D"
    print("Grade: F")
    print("Status: Fail")
    return "F"


# TC-REVIEW-04: No input validation
def create_user(name, age, email):
    user = {
        "name": name,
        "age": age,
        "email": email
    }
    return user


# TC-REVIEW-05: Hardcoded credentials
def connect_database():
    host = "localhost"
    user = "admin"
    password = "admin123"   # REVIEW: jangan hardcode password!
    database = "mydb"
    return f"mysql://{user}:{password}@{host}/{database}"


# ─────────────────────────────────────────────────────
# KATEGORI 4: CODE EXPLANATION TEST CASES
# (Kode kompleks yang perlu dijelaskan)
# ─────────────────────────────────────────────────────

# TC-EXPLAIN-01: Recursion
def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]


# TC-EXPLAIN-02: List comprehension kompleks
def matrix_transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))]


# TC-EXPLAIN-03: Generator
def infinite_counter(start=0, step=1):
    current = start
    while True:
        yield current
        current += step


# TC-EXPLAIN-04: Decorator
def retry(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
                    print(f"Attempt {attempt + 1} failed: {e}")
        return wrapper
    return decorator


# TC-EXPLAIN-05: Binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


# ─────────────────────────────────────────────────────
# PANDUAN EVALUASI UNTUK PAPER
# ─────────────────────────────────────────────────────
"""
CARA EVALUASI:

1. BUG DETECTION (TC-BUG-01 s/d TC-BUG-08):
   - Select fungsi → Klik kanan → LLM: Detect Bugs
   - Catat: Apakah LLM berhasil temukan bug? (Ya/Tidak)
   - Catat: Apakah solusi yang diberikan benar? (Ya/Tidak)
   - Hitung: Precision, Recall, F1-Score

2. TEST GENERATION (TC-TEST-01 s/d TC-TEST-05):
   - Select fungsi → Klik kanan → LLM: Generate Tests
   - Catat: Berapa test case yang dihasilkan?
   - Jalankan test: pytest → berapa yang pass?
   - Hitung: Code Coverage Rate

3. CODE REVIEW (TC-REVIEW-01 s/d TC-REVIEW-05):
   - Select fungsi → Klik kanan → LLM: Review Code
   - Catat: Apakah masalah teridentifikasi? (Ya/Tidak)
   - Nilai relevansi: 1-5
   - Hitung: BLEU Score, ROUGE Score

4. CODE EXPLANATION (TC-EXPLAIN-01 s/d TC-EXPLAIN-05):
   - Select fungsi → Klik kanan → LLM: Explain Code
   - Nilai kejelasan: 1-5
   - Nilai akurasi: 1-5
   - Hitung: Clarity Score rata-rata
"""
