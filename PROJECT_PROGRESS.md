# PROJECT PROGRESS

## Phase

PHASE 0 — SETUP

## Status

IN PROGRESS

## Roadmap

### PHASE 0 — Setup
- [x] Folder
- [x] venv
- [x] .env
- [x] .gitignore
- [x] requirements.txt
- [ ] Git
- [x] PROJECT_PROGRESS.md

### PHASE 1 — Basic Bot
- [ ] /start
- [ ] /help
- [ ] whitelist user ID
- [ ] /status

### PHASE 2 — Token Config
- [ ] token address
- [ ] nama
- [ ] symbol
- [ ] creator wallet
- [ ] chain
- [ ] platform

### PHASE 3 — Market Data
- [ ] price
- [ ] market cap
- [ ] liquidity
- [ ] volume
- [ ] buy/sell
- [ ] holders
- [ ] source
- [ ] timestamp

### PHASE 4 — SQLite
- [ ] market snapshots
- [ ] konfigurasi
- [ ] data historis dasar

### PHASE 5 — Alert
- [ ] price alert
- [ ] liquidity alert
- [ ] volume alert
- [ ] market cap target
- [ ] cooldown

### PHASE 6 — Creator Wallet
- [ ] SOL balance
- [ ] token balance
- [ ] transaksi masuk
- [ ] transaksi keluar

### PHASE 7 — Creator Fee
- [ ] actual fee jika tersedia
- [ ] ESTIMASI jika tidak tersedia
- [ ] source + timestamp

### PHASE 8 — Report
- [ ] laporan harian
- [ ] perubahan vs hari sebelumnya
- [ ] WIB

### PHASE 9 — Sell Simulator
- [ ] jumlah token
- [ ] estimasi diterima
- [ ] price impact
- [ ] harga setelah simulasi
- [ ] sisa token

### PHASE 10 — Profit Calculator
- [ ] realized profit
- [ ] unrealized value
- [ ] creator fee
- [ ] total realized income

### PHASE 11 — AI Analyst
- [ ] analisis market
- [ ] analisis liquidity
- [ ] analisis holder
- [ ] analisis buy/sell pressure
- [ ] risk/probability

MVP SELESAI

## Completed

- Task 1: Cek Python (3.11.9) + buat folder `telegram_bot\bot`, `telegram_bot\data`
- Task 2: Buat virtual environment `telegram_bot\venv`
- Task 3: Simpan roadmap final ke `PROJECT_PROGRESS.md`
- Task 4: Buat `.env` (sudah diisi user), `.gitignore`, `requirements.txt`

## Files

- `ai_promt.md` — instruksi AI (sumber aturan project)
- `PROJECT_PROGRESS.md` — file ini
- `telegram_bot\.env` — secret (terisi user, tidak dicantumkan)
- `telegram_bot\.gitignore` — daftar file yang dilarang masuk Git
- `telegram_bot\requirements.txt` — dependensi (belum di-install)
- `telegram_bot\venv\` — virtual environment
- `telegram_bot\bot\` — (belum ada file)
- `telegram_bot\data\` — (belum ada file)

## Errors

Belum ada error.

## Decisions

- SQLite dipindah ke Phase 4 (sebelum Alert), supaya alert dan konfigurasi punya tempat penyimpanan sejak awal.
- `/status` ditambahkan ke Phase 1.
- Phase 6 = Creator Wallet, Phase 7 = Creator Fee (berbeda dengan urutan lama di `ai_promt.md`).
- Roadmap di file ini adalah versi FINAL dan menggantikan urutan lama di `ai_promt.md`.
- Versi dependensi diverifikasi dari PyPI (2026-10-08): python-telegram-bot 22.8, httpx 0.28.1, python-dotenv 1.2.4. Belum di-install.

## Architecture

Belum ada kode. Stack: Python 3.11+, python-telegram-bot, httpx, python-dotenv, SQLite.

## Next Step

Phase 0 — Task 5: Git init + commit pertama (pastikan `.env` tidak ikut ter-commit).
