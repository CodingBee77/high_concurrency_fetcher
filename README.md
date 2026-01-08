# 🚀 High Concurrency Fetcher

A **mini, runnable script** that fetches data from a public API  
(e.g. **JSONPlaceholder**) using **safe, high-performance concurrency**.

Designed to demonstrate how to scale API requests **without getting banned** ⚡

---

## ✨ Features

- ⚡ **High-performance async fetching**
- 🧵 **Concurrency control** with semaphores
- 🔁 **Automatic retries** for flaky requests
- 🛡️ **Graceful error handling** — no fail-fast crashes
- 📦 **Clean, minimal, and runnable**

---

## 🛠️ Built With

- 🐍 **asyncio**  
  → Manages async tasks and event loop  

- 🚦 **Semaphores**  
  → Limits concurrency to avoid rate-limits & bans  

- 🌐 **httpx (Async Client)**  
  → Fast, modern HTTP requests  

- 🔁 **Custom `@retry` decorator**  
  → Retries failed requests automatically  

- 🧯 **Safe exception handling**  
  → Uses `asyncio.gather(..., return_exceptions=True)` so:
  - The program **never fails fast**
  - You get a mixed list of:
    - ✅ successful results  
    - ❌ exception objects  
  - Just filter the list to handle errors cleanly!

---

## 🧠 How It Works

```text
Requests → Semaphore Gate → Async Workers → Retry Logic → Results Collector
