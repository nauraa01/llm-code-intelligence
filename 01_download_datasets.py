"""
=====================================================
STEP 1: Download & Explore Dataset
Research: LLM-Powered Code Intelligence Extension
=====================================================

Cara pakai:
1. Install dulu: pip install datasets pandas numpy matplotlib seaborn
2. Jalankan: python 01_download_datasets.py
3. Semua dataset tersimpan di folder ./data/
"""

import os
import json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from datasets import load_dataset
from pathlib import Path

# ─── Setup folder ────────────────────────────────────────────
BASE_DIR = Path("./data")
(BASE_DIR / "humaneval").mkdir(parents=True, exist_ok=True)
(BASE_DIR / "codesearchnet").mkdir(parents=True, exist_ok=True)
(BASE_DIR / "bugsinpy").mkdir(parents=True, exist_ok=True)
(BASE_DIR / "eda_plots").mkdir(parents=True, exist_ok=True)

print("=" * 55)
print("  DATASET DOWNLOADER & EDA")
print("  Research: LLM Code Intelligence Extension")
print("=" * 55)


# ─────────────────────────────────────────────────────────────
# DATASET 1: HumanEval (untuk Test Generation)
# ─────────────────────────────────────────────────────────────
print("\n[1/3] Downloading HumanEval...")

try:
    ds_humaneval = load_dataset("openai/openai_humaneval", split="test")
    df_humaneval = ds_humaneval.to_pandas()
    df_humaneval.to_csv(BASE_DIR / "humaneval" / "humaneval.csv", index=False)
    print(f"    ✅ HumanEval: {len(df_humaneval)} soal")
    print(f"    Kolom: {list(df_humaneval.columns)}")

    # Preview
    print("\n    Contoh data:")
    print(f"    Task ID   : {df_humaneval['task_id'][0]}")
    print(f"    Fungsi    : {df_humaneval['entry_point'][0]}")
    print(f"    Prompt    :\n{df_humaneval['prompt'][0][:200]}...")

except Exception as e:
    print(f"    ❌ Error: {e}")
    print("    → Coba manual: pip install datasets --upgrade")


# ─────────────────────────────────────────────────────────────
# DATASET 2: CodeSearchNet Python (untuk Code Review & Explanation)
# ─────────────────────────────────────────────────────────────
print("\n[2/3] Downloading CodeSearchNet (Python subset)...")

try:
    # Ambil 5000 sample dulu — cukup untuk research
    ds_csn = load_dataset("code_search_net", "python", split="train[:5000]")
    df_csn = ds_csn.to_pandas()

    # Pilih kolom yang relevan
    cols = ["func_name", "whole_func_string", "docstring_tokens", "language"]
    df_csn_clean = df_csn[cols].copy()
    df_csn_clean.columns = ["function_name", "code", "docstring", "language"]

    # Buang yang kosong
    df_csn_clean = df_csn_clean.dropna(subset=["code", "docstring"])
    df_csn_clean = df_csn_clean[df_csn_clean["code"].str.len() > 50]

    df_csn_clean.to_csv(BASE_DIR / "codesearchnet" / "csn_python.csv", index=False)
    print(f"    ✅ CodeSearchNet: {len(df_csn_clean)} fungsi Python")
    print(f"    Kolom: {list(df_csn_clean.columns)}")

    print("\n    Contoh data:")
    print(f"    Nama fungsi : {df_csn_clean['function_name'].iloc[0]}")
    print(f"    Kode (50 char pertama): {df_csn_clean['code'].iloc[0][:100]}...")

except Exception as e:
    print(f"    ❌ Error: {e}")


# ─────────────────────────────────────────────────────────────
# DATASET 3: BugsInPy (untuk Bug Detection)
# Catatan: BugsInPy tidak ada di HuggingFace,
# kita pakai versi yang sudah diproses dari GitHub
# ─────────────────────────────────────────────────────────────
print("\n[3/3] Menyiapkan BugsInPy (versi preprocessed)...")

try:
    # BugsInPy versi CSV yang sudah diproses komunitas
    ds_bugs = load_dataset("alexjercan/bugsinpy-dataset", split="train")
    df_bugs = ds_bugs.to_pandas()
    df_bugs.to_csv(BASE_DIR / "bugsinpy" / "bugsinpy.csv", index=False)
    print(f"    ✅ BugsInPy: {len(df_bugs)} bug samples")
    print(f"    Kolom: {list(df_bugs.columns)}")

except Exception as e:
    print(f"    ⚠️  Dataset alternatif tidak tersedia: {e}")
    print("    → Membuat synthetic BugsInPy sample untuk testing...")

    # Buat synthetic sample untuk testing sementara
    synthetic_bugs = []
    samples = [
        {
            "project": "pandas",
            "bug_id": "pandas-1",
            "buggy_code": "def get_mean(lst):\n    return sum(lst) / len(lst)",
            "fixed_code": "def get_mean(lst):\n    if not lst:\n        return 0\n    return sum(lst) / len(lst)",
            "bug_description": "Division by zero when list is empty",
            "label": 1
        },
        {
            "project": "requests",
            "bug_id": "requests-1",
            "buggy_code": "def parse_url(url):\n    return url.split('://')[1]",
            "fixed_code": "def parse_url(url):\n    parts = url.split('://')\n    return parts[1] if len(parts) > 1 else url",
            "bug_description": "Index error when URL has no protocol",
            "label": 1
        },
        {
            "project": "flask",
            "bug_id": "flask-1",
            "buggy_code": "def read_config(path):\n    with open(path) as f:\n        return json.load(f)",
            "fixed_code": "def read_config(path):\n    try:\n        with open(path) as f:\n            return json.load(f)\n    except FileNotFoundError:\n        return {}",
            "bug_description": "No exception handling for missing file",
            "label": 1
        },
    ]

    df_bugs = pd.DataFrame(samples)
    df_bugs.to_csv(BASE_DIR / "bugsinpy" / "bugsinpy_sample.csv", index=False)
    print(f"    ✅ Synthetic sample dibuat: {len(df_bugs)} contoh")
    print("    (Ganti dengan dataset asli saat research final)")


# ─────────────────────────────────────────────────────────────
# EDA: Exploratory Data Analysis
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  EDA - EXPLORATORY DATA ANALYSIS")
print("=" * 55)

sns.set_theme(style="darkgrid")
fig, axes = plt.subplots(2, 2, figsize=(14, 10))
fig.suptitle("EDA: Dataset Overview\nLLM Code Intelligence Research", 
             fontsize=14, fontweight="bold", y=1.02)

# Plot 1: HumanEval - distribusi panjang prompt
try:
    df_humaneval["prompt_length"] = df_humaneval["prompt"].str.len()
    axes[0, 0].hist(df_humaneval["prompt_length"], bins=20, color="#4F9CF9", edgecolor="white")
    axes[0, 0].set_title("HumanEval: Distribusi Panjang Prompt")
    axes[0, 0].set_xlabel("Jumlah Karakter")
    axes[0, 0].set_ylabel("Frekuensi")
    axes[0, 0].axvline(df_humaneval["prompt_length"].mean(), 
                        color="red", linestyle="--", label=f"Mean: {df_humaneval['prompt_length'].mean():.0f}")
    axes[0, 0].legend()
except:
    axes[0, 0].text(0.5, 0.5, "HumanEval\ndata not loaded", 
                    ha="center", va="center", transform=axes[0, 0].transAxes)

# Plot 2: CodeSearchNet - distribusi panjang kode
try:
    df_csn_clean["code_length"] = df_csn_clean["code"].str.len()
    axes[0, 1].hist(df_csn_clean["code_length"], bins=30, color="#10B981", edgecolor="white")
    axes[0, 1].set_title("CodeSearchNet: Distribusi Panjang Kode")
    axes[0, 1].set_xlabel("Jumlah Karakter")
    axes[0, 1].set_ylabel("Frekuensi")
    axes[0, 1].set_xlim(0, 2000)
    axes[0, 1].axvline(df_csn_clean["code_length"].mean(), 
                        color="red", linestyle="--", label=f"Mean: {df_csn_clean['code_length'].mean():.0f}")
    axes[0, 1].legend()
except:
    axes[0, 1].text(0.5, 0.5, "CodeSearchNet\ndata not loaded", 
                    ha="center", va="center", transform=axes[0, 1].transAxes)

# Plot 3: BugsInPy - distribusi per project
try:
    bug_counts = df_bugs["project"].value_counts().head(10)
    axes[1, 0].barh(bug_counts.index, bug_counts.values, color="#F59E0B")
    axes[1, 0].set_title("BugsInPy: Bug per Project (Top 10)")
    axes[1, 0].set_xlabel("Jumlah Bug")
except:
    axes[1, 0].text(0.5, 0.5, "BugsInPy\ndata not loaded", 
                    ha="center", va="center", transform=axes[1, 0].transAxes)

# Plot 4: Summary dataset stats
try:
    datasets_info = {
        "HumanEval\n(Test Gen)": len(df_humaneval) if "df_humaneval" in dir() else 0,
        "CodeSearchNet\n(Review/Explain)": len(df_csn_clean) if "df_csn_clean" in dir() else 0,
        "BugsInPy\n(Bug Detect)": len(df_bugs) if "df_bugs" in dir() else 0,
    }
    colors = ["#4F9CF9", "#10B981", "#F59E0B"]
    bars = axes[1, 1].bar(datasets_info.keys(), datasets_info.values(), color=colors, edgecolor="white")
    axes[1, 1].set_title("Ringkasan: Jumlah Data per Dataset")
    axes[1, 1].set_ylabel("Jumlah Sample")
    for bar, val in zip(bars, datasets_info.values()):
        axes[1, 1].text(bar.get_x() + bar.get_width()/2, bar.get_height() + 1,
                        str(val), ha="center", va="bottom", fontweight="bold")
except Exception as e:
    print(f"Plot 4 error: {e}")

plt.tight_layout()
plt.savefig(BASE_DIR / "eda_plots" / "eda_overview.png", dpi=150, bbox_inches="tight")
plt.show()
print("\n    ✅ Plot disimpan di: ./data/eda_plots/eda_overview.png")


# ─────────────────────────────────────────────────────────────
# RINGKASAN AKHIR
# ─────────────────────────────────────────────────────────────
print("\n" + "=" * 55)
print("  RINGKASAN DATASET")
print("=" * 55)

summary = {
    "HumanEval": {
        "Kegunaan": "Test Generation (Task 2)",
        "Jumlah": f"{len(df_humaneval) if 'df_humaneval' in dir() else 'N/A'} soal",
        "Format": "CSV",
        "Lokasi": "./data/humaneval/humaneval.csv"
    },
    "CodeSearchNet": {
        "Kegunaan": "Code Review & Explanation (Task 3 & 4)",
        "Jumlah": f"{len(df_csn_clean) if 'df_csn_clean' in dir() else 'N/A'} fungsi Python",
        "Format": "CSV",
        "Lokasi": "./data/codesearchnet/csn_python.csv"
    },
    "BugsInPy": {
        "Kegunaan": "Bug Detection (Task 1)",
        "Jumlah": f"{len(df_bugs) if 'df_bugs' in dir() else 'N/A'} bug samples",
        "Format": "CSV",
        "Lokasi": "./data/bugsinpy/bugsinpy.csv"
    },
}

for name, info in summary.items():
    print(f"\n  📦 {name}")
    for k, v in info.items():
        print(f"     {k:<12}: {v}")

print("\n" + "=" * 55)
print("  ✅ SELESAI! Lanjut ke script 02_preprocessing.py")
print("=" * 55)
