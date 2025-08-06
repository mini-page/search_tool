# 🔍 Search Tool (CLI)

A simple Python-based command-line tool to **search one or more IDs** from a text file.

---

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/mini-page/search_tool.git
```

### 2. Navigate to the Project Directory

```bash
cd search_tool
```

### 3. Run the Script with a Single ID

```bash
python search.py --file ids.txt --search 1773875622809418
```

#### ✅ Output (if found)

```
✅ Found: 1773875622809418
```

#### ❌ Output (if not found)

```
❌ Not found: 1773875622809418
```

![Single ID Search](search_tool/screenCaptures/single%20id%20search.png)

---

### 4. Replace `ids.txt` with Your Own Data

Edit the `ids.txt` file and paste the list of IDs you want to search from (one per line):

```
177811096730619200
OD334960656204375100
402-9894652-3522702
1773875622809418
1773875622809418..3
```

---

### 5. Run the Script with Multiple IDs

```bash
python search.py --file ids.txt --search 1773875622809418 1773875622809418..2 1773875622809418..3 1773875622809418..4
```

#### ✅ Output Example

```
✅ Found: 1773875622809418
✅ Found: 1773875622809418..2
✅ Found: 1773875622809418..3
✅ Found: 1773875622809418..4
```

![Multiple ID Search](search_tool/screenCaptures/multiple%20id%20search.png)

---

## 📂 Folder Structure

```
search_tool/
├── search.py        # Main CLI tool
├── ids.txt          # Sample file containing IDs
└── screenCaptures   # Folder containing screenshots of the tool in action
```

---

## ⚙️ Dependencies

* Python 3.x
* Works on Linux, macOS, and Windows
* No external libraries required

---

## 🛠️ Dev TODOs (Extend the Tool)

You can enhance this tool by adding:

* 🔍 Partial / fuzzy search support
* 🔡 Case-insensitive matching
* 📄 CSV or JSON file input support

* 💾 Exporting results to an output file
