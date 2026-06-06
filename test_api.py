"""
=====================================================
TEST KONEKSI 3 API (FINAL VERSION)
Groq + Mistral + OpenRouter
=====================================================
"""

import os
from dotenv import load_dotenv

load_dotenv()

print("=" * 55)
print("  TEST KONEKSI 3 API (FINAL VERSION)")
print("  Groq | Mistral | OpenRouter")
print("=" * 55)

TEST_PROMPT = "Explain what is a bug in programming in one sentence."

results = {"Groq": False, "Mistral": False, "OpenRouter": False}

# ─────────────────────────────────────────────
# TEST 1: GROQ
# ─────────────────────────────────────────────
print("\n[1/3] Testing Groq API...")
try:
    from groq import Groq
    client = Groq(api_key=os.getenv("GROQ_API_KEY"))
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[{"role": "user", "content": TEST_PROMPT}],
        max_tokens=100
    )
    print(f"    ✅ GROQ OK! (model: llama-3.3-70b-versatile)")
    print(f"    Response: {response.choices[0].message.content[:120]}...")
    results["Groq"] = True
except Exception as e:
    print(f"    ❌ GROQ GAGAL: {e}")

# ─────────────────────────────────────────────
# TEST 2: MISTRAL
# ─────────────────────────────────────────────
print("\n[2/3] Testing Mistral API...")
try:
    from mistralai import Mistral
    client = Mistral(api_key=os.getenv("MISTRAL_API_KEY"))
    response = client.chat.complete(
        model="mistral-small-latest",
        messages=[{"role": "user", "content": TEST_PROMPT}],
        max_tokens=100
    )
    print(f"    ✅ MISTRAL OK! (model: mistral-small-latest)")
    print(f"    Response: {response.choices[0].message.content[:120]}...")
    results["Mistral"] = True
except Exception as e:
    print(f"    ❌ MISTRAL GAGAL: {e}")

# ─────────────────────────────────────────────
# TEST 3: OPENROUTER — model gratis terbaru
# ─────────────────────────────────────────────
print("\n[3/3] Testing OpenRouter API...")
try:
    from openai import OpenAI
    client = OpenAI(
        api_key=os.getenv("OPENROUTER_API_KEY"),
        base_url="https://openrouter.ai/api/v1"
    )

    # Model gratis terbaru dari OpenRouter (Juni 2026)
    free_models = [
        "nvidia/nemotron-super-49b-v1:free",
        "poolside/laguna-m-1:free",
        "openai/gpt-oss-120b:free",
    ]

    success = False
    for model_name in free_models:
        try:
            response = client.chat.completions.create(
                model=model_name,
                messages=[{"role": "user", "content": TEST_PROMPT}],
                max_tokens=100
            )
            print(f"    ✅ OPENROUTER OK! (model: {model_name})")
            print(f"    Response: {response.choices[0].message.content[:120]}...")
            results["OpenRouter"] = True
            success = True
            break
        except Exception as me:
            print(f"    ⚠️  {model_name} gagal, coba model lain...")
            continue

    if not success:
        print(f"    ❌ OPENROUTER GAGAL: semua model tidak tersedia")

except Exception as e:
    print(f"    ❌ OPENROUTER GAGAL: {e}")

# ─────────────────────────────────────────────
# RINGKASAN
# ─────────────────────────────────────────────
print("\n" + "=" * 55)
print("  RINGKASAN HASIL")
print("=" * 55)
for name, status in results.items():
    icon = "✅" if status else "❌"
    print(f"  {icon} {name}")

total_ok = sum(results.values())
print(f"\n  {total_ok}/3 API berhasil terhubung")

if total_ok == 3:
    print("\n  🎉 SEMUA OK! Siap lanjut build extension!")
elif total_ok >= 2:
    print("\n  ⚠️  Groq + Mistral sudah cukup untuk mulai!")
else:
    print("\n  ❌ Ada masalah. Screenshot & kirim ke Claude!")

print("=" * 55)