# Binance Futures Testnet Trading Bot

## Features
- Binance Futures Testnet Integration
- Market Order Execution
- Input Validation
- Logging System
- Clean Architecture
- CLI Interface

---

## Setup Instructions

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Environment

Windows:
```bash
venv\Scripts\activate
```

Linux/Mac:
```bash
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Copy `.env.example` to `.env`

```bash
cp .env.example .env
```

Add your Binance Futures Testnet API credentials.

---

## Run Project

```bash
python run.py
```

---

## Future Improvements
- Stop Loss / Take Profit
- WebSocket Integration
- Risk Management
- Docker Support
- Telegram Alerts