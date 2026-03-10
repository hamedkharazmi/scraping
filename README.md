# JoinSecret Activation Scraper

This Python script scrapes activation pages on [joinsecret.com](https://www.joinsecret.com) and saves deal info into a CSV.

---

## 📁 Project Structure

```
scraping/
├── main.py          # scraper script
├── auth.py          # auth script
├── auth.json        # saved login state (generated after first login)
├── requirements.txt # Python dependencies
└── README.md        # this file
```

---

## ⚡ Setup Instructions

### 1. Create a Virtual Environment

```bash
# On Windows
python -m venv .venv
.venv\Scripts\Activate.ps1

# On Linux/Mac
python3 -m venv .venv
source .venv/bin/activate
```

> Your terminal should now show `(.venv)` before the prompt.

### 2. Install Dependencies

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python -m playwright install
```

### 3. Login Manually and Save Auth State (You will need to run this once)

```bash
python auth.py
```
> Run this file and login manually once. It will generate `auth.json` with your login cookies. (It's better to use Login with Email method)

### 4. Run the Scraper

```bash
python main.py
```

* The script will loop over activation IDs (configured in `main.py`)
* Saves extracted data to `output/activation_data.csv`

---

## 📝 CSV Output

Columns:

* `activation_id`
* `deal_text` → e.g., "Save up to $237"
* `header_text` → e.g., "50% off for 3 months..."
* `link_text` → text inside the main `<a>`
* `link_href` → link URL
* `full_text` → full `<p>` content containing the link

---

## ⚙️ Notes

* Change `OPEN_BROWSER_UI=True` to `False` in `main.py` if you don't want it to open the browser.
* Adjust `START_ID` and `END_ID` in `main.py` to scrape a different range of activations.
* Always activate the virtual environment before running the scraper:

```bash
# Windows
.\.venv\Scripts\activate

# Linux/Mac
source .venv/bin/activate
```


* Deactivate the virtual environment when done:

```bash
deactivate
```
