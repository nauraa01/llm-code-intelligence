"""
=====================================================
AUTO EVALUASI - LLM Code Intelligence Research
Groq + Mistral + OpenRouter
=====================================================
Cara pakai:
1. pip install groq mistralai openai openpyxl pandas python-dotenv
2. python auto_eval.py
3. Hasil otomatis tersimpan di hasil_evaluasi.xlsx
"""

import os
import time
import pandas as pd
from dotenv import load_dotenv
from datetime import datetime

load_dotenv()

# ─── API CLIENTS ─────────────────────────────────────────────
from groq import Groq
from mistralai import Mistral
from openai import OpenAI

groq_client = Groq(api_key=os.getenv("GROQ_API_KEY"))
mistral_client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
openrouter_client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1"
)

# ─── CALL EACH LLM ───────────────────────────────────────────
def call_groq(prompt):
    try:
        start = time.time()
        res = groq_client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024
        )
        elapsed = round(time.time() - start, 2)
        return res.choices[0].message.content, elapsed
    except Exception as e:
        return f"ERROR: {e}", 0

def call_mistral(prompt):
    try:
        start = time.time()
        res = mistral_client.chat.complete(
            model="mistral-small-latest",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024
        )
        elapsed = round(time.time() - start, 2)
        return res.choices[0].message.content, elapsed
    except Exception as e:
        return f"ERROR: {e}", 0

def call_openrouter(prompt):
    try:
        start = time.time()
        res = openrouter_client.chat.completions.create(
            model="openai/gpt-oss-120b:free",
            messages=[{"role": "user", "content": prompt}],
            max_tokens=1024
        )
        elapsed = round(time.time() - start, 2)
        return res.choices[0].message.content, elapsed
    except Exception as e:
        return f"ERROR: {e}", 0

# ─── TEST CASES ───────────────────────────────────────────────
test_cases = {
    "bug_detection": [
        {
            "id": "TC-BUG-01",
            "name": "Division by Zero",
            "code": """def calculate_average(numbers):
    total = sum(numbers)
    return total / len(numbers)""",
            "expected_bug": "ZeroDivisionError when list is empty"
        },
        {
            "id": "TC-BUG-02",
            "name": "Index Out of Range",
            "code": """def get_first_and_last(lst):
    first = lst[0]
    last = lst[-1]
    return first, last""",
            "expected_bug": "IndexError when list is empty"
        },
        {
            "id": "TC-BUG-03",
            "name": "Wrong Logic Operator",
            "code": """def is_valid_age(age):
    if age > 0 or age < 150:
        return True
    return False""",
            "expected_bug": "Should use 'and' not 'or'"
        },
        {
            "id": "TC-BUG-04",
            "name": "SQL Injection",
            "code": """def get_user(username, db):
    query = f"SELECT * FROM users WHERE name = '{username}'"
    return db.execute(query)""",
            "expected_bug": "SQL injection vulnerability"
        },
        {
            "id": "TC-BUG-05",
            "name": "Infinite Loop",
            "code": """def countdown(n):
    while n != 0:
        print(n)
        n -= 1""",
            "expected_bug": "Infinite loop when n is negative"
        },
        {
            "id": "TC-BUG-06",
            "name": "Wrong Initial Value",
            "code": """def multiply_all(numbers):
    result = 0
    for n in numbers:
        result *= n
    return result""",
            "expected_bug": "result should start at 1 not 0"
        },
        {
            "id": "TC-BUG-07",
            "name": "Missing Exception Handling",
            "code": """def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()""",
            "expected_bug": "No try-except for FileNotFoundError"
        },
        {
            "id": "TC-BUG-08",
            "name": "Off-by-One Error",
            "code": """def get_last_n_items(lst, n):
    return lst[len(lst)-n+1:]""",
            "expected_bug": "Off by one, should be len(lst)-n"
        },
    ],
    "test_generation": [
        {
            "id": "TC-TEST-01",
            "name": "Reverse Words",
            "code": """def reverse_words(sentence):
    words = sentence.split()
    return ' '.join(reversed(words))"""
        },
        {
            "id": "TC-TEST-02",
            "name": "Is Prime",
            "code": """def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True"""
        },
        {
            "id": "TC-TEST-03",
            "name": "Remove Duplicates",
            "code": """def remove_duplicates(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result"""
        },
        {
            "id": "TC-TEST-04",
            "name": "Group By Length",
            "code": """def group_by_length(words):
    groups = {}
    for word in words:
        length = len(word)
        if length not in groups:
            groups[length] = []
        groups[length].append(word)
    return groups"""
        },
        {
            "id": "TC-TEST-05",
            "name": "Celsius to Fahrenheit",
            "code": """def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32"""
        },
    ],
    "code_review": [
        {
            "id": "TC-REVIEW-01",
            "name": "Poor Readability",
            "code": """def f(x):
    r = []
    for i in range(len(x)):
        if x[i] % 2 == 0:
            r.append(x[i] * x[i])
    return r"""
        },
        {
            "id": "TC-REVIEW-02",
            "name": "Magic Numbers",
            "code": """def calc(a, b, c):
    x = a * 3.14159 * b * b
    y = (1/3) * x * c
    return y"""
        },
        {
            "id": "TC-REVIEW-03",
            "name": "Duplicate Code",
            "code": """def get_student_grade(score):
    if score >= 90:
        print("Grade: A")
        return "A"
    if score >= 80:
        print("Grade: B")
        return "B"
    if score >= 70:
        print("Grade: C")
        return "C"
    return "F" """
        },
        {
            "id": "TC-REVIEW-04",
            "name": "No Input Validation",
            "code": """def create_user(name, age, email):
    user = {"name": name, "age": age, "email": email}
    return user"""
        },
        {
            "id": "TC-REVIEW-05",
            "name": "Hardcoded Credentials",
            "code": """def connect_database():
    host = "localhost"
    user = "admin"
    password = "admin123"
    return f"mysql://{user}:{password}@{host}/mydb" """
        },
    ],
    "code_explanation": [
        {
            "id": "TC-EXPLAIN-01",
            "name": "Fibonacci Memoization",
            "code": """def fibonacci(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)
    return memo[n]"""
        },
        {
            "id": "TC-EXPLAIN-02",
            "name": "Matrix Transpose",
            "code": """def matrix_transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))]
            for i in range(len(matrix[0]))]"""
        },
        {
            "id": "TC-EXPLAIN-03",
            "name": "Generator",
            "code": """def infinite_counter(start=0, step=1):
    current = start
    while True:
        yield current
        current += step"""
        },
        {
            "id": "TC-EXPLAIN-04",
            "name": "Retry Decorator",
            "code": """def retry(max_attempts=3):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for attempt in range(max_attempts):
                try:
                    return func(*args, **kwargs)
                except Exception as e:
                    if attempt == max_attempts - 1:
                        raise e
        return wrapper
    return decorator"""
        },
        {
            "id": "TC-EXPLAIN-05",
            "name": "Binary Search",
            "code": """def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1"""
        },
    ]
}

# ─── PROMPTS ─────────────────────────────────────────────────
def make_prompt(task, code, **kwargs):
    if task == "bug_detection":
        return f"""You are an expert bug detector. Analyze this Python code and find ALL bugs.
For each bug provide: (1) Line number, (2) Bug type, (3) Explanation, (4) Fixed code.
Be concise and precise.

Code:
```python
{code}
```"""
    elif task == "test_generation":
        return f"""You are a Python testing expert. Generate comprehensive pytest unit tests for this function.
Include: happy path, edge cases, and error cases.
Return only the test code, ready to run.

Code:
```python
{code}
```"""
    elif task == "code_review":
        return f"""You are a senior software engineer doing code review.
Review this code for: readability, performance, security, best practices.
Give specific improvement suggestions with example code.

Code:
```python
{code}
```"""
    elif task == "code_explanation":
        return f"""Explain this Python code to a junior programmer (beginner level).
Include: (1) Overview, (2) Step-by-step explanation, (3) Simple analogy, (4) Usage example.
Use simple language.

Code:
```python
{code}
```"""

# ─── MAIN EVALUATION ─────────────────────────────────────────
def run_evaluation():
    all_results = []
    
    tasks = [
        ("bug_detection", "Bug Detection"),
        ("test_generation", "Test Generation"),
        ("code_review", "Code Review"),
        ("code_explanation", "Code Explanation"),
    ]
    
    total = sum(len(test_cases[t]) for t, _ in tasks)
    current = 0
    
    print("=" * 60)
    print("  AUTO EVALUASI LLM CODE INTELLIGENCE")
    print(f"  Total test cases: {total}")
    print("=" * 60)
    
    for task_key, task_name in tasks:
        print(f"\n📋 {task_name}...")
        
        for tc in test_cases[task_key]:
            current += 1
            print(f"\n  [{current}/{total}] {tc['id']}: {tc['name']}")
            
            prompt = make_prompt(task_key, tc['code'])
            
            # Call 3 LLMs
            print(f"    → Groq...", end=" ", flush=True)
            groq_resp, groq_time = call_groq(prompt)
            print(f"✅ ({groq_time}s)")
            time.sleep(1)  # hindari rate limit
            
            print(f"    → Mistral...", end=" ", flush=True)
            mistral_resp, mistral_time = call_mistral(prompt)
            print(f"✅ ({mistral_time}s)")
            time.sleep(1)
            
            print(f"    → OpenRouter...", end=" ", flush=True)
            openrouter_resp, openrouter_time = call_openrouter(prompt)
            print(f"✅ ({openrouter_time}s)")
            time.sleep(1)
            
            # Simpan hasil
            all_results.append({
                "Test ID": tc['id'],
                "Task": task_name,
                "Test Name": tc['name'],
                "Code": tc['code'],
                "Groq Response": groq_resp,
                "Groq Time (s)": groq_time,
                "Mistral Response": mistral_resp,
                "Mistral Time (s)": mistral_time,
                "OpenRouter Response": openrouter_resp,
                "OpenRouter Time (s)": openrouter_time,
                # Kolom untuk diisi manual
                "Groq Score (1-5)": "",
                "Mistral Score (1-5)": "",
                "OpenRouter Score (1-5)": "",
                "Notes": "",
            })
    
    return all_results

# ─── SAVE TO EXCEL ───────────────────────────────────────────
def save_to_excel(results):
    df = pd.DataFrame(results)
    
    filename = f"hasil_evaluasi_{datetime.now().strftime('%Y%m%d_%H%M%S')}.xlsx"
    
    with pd.ExcelWriter(filename, engine='openpyxl') as writer:
        # Sheet 1: Semua hasil
        df.to_excel(writer, sheet_name='Semua Hasil', index=False)
        
        # Sheet 2-5: Per task
        for task in ["Bug Detection", "Test Generation", "Code Review", "Code Explanation"]:
            df_task = df[df['Task'] == task]
            sheet_name = task[:31]  # Excel max 31 char
            df_task.to_excel(writer, sheet_name=sheet_name, index=False)
        
        # Sheet 6: Summary template
        summary_data = {
            "Task": ["Bug Detection", "Test Generation", "Code Review", "Code Explanation"],
            "Jumlah TC": [8, 5, 5, 5],
            "Groq Avg Score": ["=AVERAGE('Bug Detection'!L2:L9)", "", "", ""],
            "Mistral Avg Score": ["", "", "", ""],
            "OpenRouter Avg Score": ["", "", "", ""],
            "Best LLM": ["", "", "", ""],
        }
        df_summary = pd.DataFrame(summary_data)
        df_summary.to_excel(writer, sheet_name='Summary', index=False)
        
        # Auto-fit kolom
        for sheet_name in writer.sheets:
            worksheet = writer.sheets[sheet_name]
            for column in worksheet.columns:
                max_length = 0
                for cell in column:
                    try:
                        if len(str(cell.value)) > max_length:
                            max_length = min(len(str(cell.value)), 50)
                    except:
                        pass
                worksheet.column_dimensions[column[0].column_letter].width = max_length + 2
    
    return filename

# ─── RUN ─────────────────────────────────────────────────────
if __name__ == "__main__":
    print("\n🚀 Memulai evaluasi otomatis...")
    print("⏱️  Estimasi waktu: 5-10 menit\n")
    
    results = run_evaluation()
    
    print("\n💾 Menyimpan ke Excel...")
    filename = save_to_excel(results)
    
    print("\n" + "=" * 60)
    print(f"  🎉 SELESAI!")
    print(f"  📊 Hasil tersimpan di: {filename}")
    print(f"  📋 Total: {len(results)} test cases")
    print(f"  🤖 3 LLM: Groq, Mistral, OpenRouter")
    print("=" * 60)
    print("\n  Selanjutnya:")
    print("  1. Buka file Excel")
    print("  2. Isi kolom 'Score (1-5)' secara manual")
    print("  3. Gunakan hasilnya untuk paper!")
EOF
