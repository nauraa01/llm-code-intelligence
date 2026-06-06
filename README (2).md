# 🤖 LLM Code Intelligence Extension

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![VS Code](https://img.shields.io/badge/VS%20Code-Extension-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![LLM](https://img.shields.io/badge/Powered%20by-Groq%20%7C%20Mistral%20%7C%20OpenRouter-orange)
![Cost](https://img.shields.io/badge/API%20Cost-Free-brightgreen)

> **Research Project** — A Unified VS Code Extension for Code Intelligence Using Free-Tier LLMs: A Comparative Study of Groq, Mistral, and OpenRouter

---

## 📌 About

This project implements a **unified VS Code extension** that integrates **four AI-powered code intelligence tasks** in a single tool, powered exclusively by **free-tier LLM APIs**:

| Feature | Description |
|---|---|
| 🐛 **Bug Detection** | Automatically detects bugs and suggests fixes |
| 🧪 **Test Generation** | Generates comprehensive pytest unit tests |
| 👁️ **Code Review** | Reviews code for readability, performance, and security |
| 📖 **Code Explanation** | Explains complex code in simple language |

All features are powered by **3 free LLMs simultaneously**:
- **Groq** (Llama 3.3 70B) — Fastest response
- **Mistral** (Mistral Small) — Balanced performance  
- **OpenRouter** (GPT-OSS 120B) — Most comprehensive output

---

## 📊 Key Results

| LLM | Avg Response Time | Best For |
|---|---|---|
| **Groq** | **1.71s** 🏆 | Speed-critical workflows |
| **Mistral** | **3.10s** | General purpose |
| **OpenRouter** | **26.90s** | Detailed analysis |

> All APIs are **100% free** — no credit card required.

---

## 🗂️ Repository Structure

```
llm-code-intelligence/
├── 📂 extension/              # VS Code Extension (TypeScript)
│   ├── src/
│   │   └── extension.ts       # Main extension with 4 AI features
│   └── package.json
├── 📂 evaluation/             # Python evaluation scripts
│   ├── auto_eval.py           # Auto-run all 23 test cases → Excel
│   ├── test_api.py            # Test API connections
│   ├── test_cases.py          # 23 benchmark test cases
│   ├── 01_download_datasets.py
│   └── 02_download_fix.py
├── 📂 results/
│   └── hasil_evaluasi_DIOLAH.xlsx  # Full evaluation results
├── .env.example               # API key template (copy to .env)
├── .gitignore
└── README.md
```

---

## 🚀 Quick Start

### 1. Clone the repo
```bash
git clone https://github.com/nauraa01/llm-code-intelligence.git
cd llm-code-intelligence
```

### 2. Get free API keys (no credit card needed)
| Provider | Sign Up | Free Limit |
|---|---|---|
| Groq | [console.groq.com](https://console.groq.com) | 14,400 req/day |
| Mistral | [console.mistral.ai](https://console.mistral.ai) | Free tier |
| OpenRouter | [openrouter.ai](https://openrouter.ai) | Free models |

### 3. Setup environment
```bash
cp .env.example .env
# Edit .env and fill in your API keys
```

### 4. Install Python dependencies
```bash
pip install groq mistralai openai python-dotenv pandas openpyxl matplotlib seaborn datasets
```

### 5. Test API connections
```bash
python test_api.py
```

### 6. Run full evaluation
```bash
python auto_eval.py
# Results saved to: hasil_evaluasi_TIMESTAMP.xlsx
```

---

## 💻 VS Code Extension

### Setup
```bash
cd extension
npm install
npm run compile
```

### Run (press F5 in VS Code)
The extension adds 4 commands to your right-click menu:
- `🐛 LLM: Detect Bugs`
- `🧪 LLM: Generate Tests`
- `👁️ LLM: Review Code`
- `📖 LLM: Explain Code`

---

## 📦 Datasets

All datasets used are **public and open-source**:

| Dataset | Task | Source | Size |
|---|---|---|---|
| **HumanEval** | Test Generation | [OpenAI/HumanEval](https://github.com/openai/human-eval) | 164 samples |
| **BugsInPy** | Bug Detection | [soarsmu/BugsInPy](https://github.com/soarsmu/BugsInPy) | Real Python bugs |
| **CodeSearchNet** | Review & Explanation | [github/CodeSearchNet](https://github.com/github/CodeSearchNet) | 2M+ functions |

> Custom benchmark: 23 hand-crafted Python test cases across 4 task categories.

---

## 🔑 Environment Variables

Copy `.env.example` to `.env` and fill in your keys:

```env
GROQ_API_KEY=your_groq_api_key_here
MISTRAL_API_KEY=your_mistral_api_key_here
OPENROUTER_API_KEY=your_openrouter_api_key_here
```

**Never commit your `.env` file!** It is already in `.gitignore`.

---

## 📄 Paper

This project is part of an ongoing research paper:

> **"A Unified VS Code Extension for Code Intelligence Using Free-Tier LLMs: A Comparative Study of Groq, Mistral, and OpenRouter on Bug Detection, Test Generation, Code Review, and Code Explanation"**
>
> Target Journal: *Information and Software Technology* (Elsevier, Q1 Scopus)

---

## 🛠️ Tech Stack

- **Extension**: TypeScript, Node.js, VS Code API
- **Evaluation**: Python 3.12, pandas, matplotlib, openpyxl
- **LLMs**: Groq API, Mistral API, OpenRouter API
- **Datasets**: HuggingFace Datasets library

---

## 📝 License

MIT License — free to use, modify, and distribute.

---

## 👤 Author

**Naura Anasya**  
Pradita University, Indonesia  

*Research assisted by Claude AI (Anthropic) for coding and writing support — declared in accordance with academic integrity guidelines.*
