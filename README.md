
---

# 🌾 LLM Micro Challenge — Challenge 1

## **Domain-Specific Dataset Creation (Health)**

This repository contains the deliverables for **Challenge 1 of the LLM Micro Challenge Series**, where the objective was to design and prepare a clean, high-quality, domain-specific dataset to be used in later stages for **LLM training and fine-tuning**.

---

## 🚜 **Chosen Domain: Health**

We selected **Health** as the primary domain because:

*It has strong real-world impact and relevance
*It contains vast publicly available educational and research content
*It is widely used in AI applications such as medical chatbots, symptom checkers, and health recommendation systems
*It supports public awareness on wellness, nutrition, diseases, and preventive care
*It allows model training on non-sensitive, general-purpose health knowledge

The dataset covers topics such as:

*Human anatomy and physiology
*Nutrition & diet
*Common diseases and symptoms
*Public health information
*First aid
*Mental health basics
*Preventive healthcare
*Fitness & lifestyle
*Medical terminology

---

## 🧩 **Challenge Breakdown**

### ✅ **1. Data Collection**

General, non-sensitive, publicly available health information was gathered from trusted sources:

*Government health portals (CDC, WHO, NIH equivalents)
*Medical education websites
*Public scientific articles
*Health blogs & encyclopedic sources
*Open datasets

A total of **100+ entries of general health** were collected.

---

### ✅ **2. Data Cleaning**

To ensure high-quality input for model training, several cleaning steps were performed:

*Removed unnecessary symbols, noise, ads, and markup
*Eliminated duplicate entries
*Ensured valid UTF-8 formatting
*Normalized text for consistency
*Corrected structural errors in JSON
*Removed unwanted whitespace and spacing inconsistencies

A custom script **`clean_jsonl.py`** was used to automate this process.

---

### ✅ **3. Metadata Enrichment**

Each dataset entry was enriched with structured metadata fields:

*title – short label of the health topic
*domain – "health"
*source – where the information originally came from
*content – cleaned text of the health information

This improves dataset indexing, retrieval, searchability, and training consistency.

---

### ✅ **4. JSONL Conversion**

The dataset was converted to **JSON Lines (JSONL)** format, which is ideal for:

*LLM fine-tuning
*Embedding and vector search
*Large-scale data streaming
*Training pipelines

The conversion process was executed using **`create_jsonl.py`**.

---

## 📂 **Repository Structure**

| File Name                  | Description                                                |
| -------------------------- | ---------------------------------------------------------- |
| `health_dataset_100.jsonl`   | Original 100-entry dataset                                 |
| `health_dataset_clean.jsonl` | Cleaned & metadata-enriched dataset (final training-ready) |
| `health_dataset_pretty.json` | Pretty-printed JSON version for human readability          |
| `clean_jsonl.py`           | Script for cleaning JSONL data                             |
| `create_jsonl.py`          | Script for transforming raw text into JSONL format         |

---

## 🚀 **Outcome**

This challenge produced a **clean, structured, domain-specific Health dataset** enriched with metadata and formatted in JSONL — fully ready for:

*Model fine-tuning
*Prompt engineering
*Embeddings
*Health-aware generative AI applications

---
