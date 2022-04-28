# Actigraphy Cleaner

## Table of Contents

- About Actigraphy Cleaner
- Requirements
  - Optional
- Setting up Python
- How to use

---

## About Actigraphy Cleaner

The Actigraphy Cleaner attempts to clean up the CSV file(s) taken from Philips Actiwatch, and extract only the relevant data needed for further analysis using the SleepAnnotate R script.

## Requirements

1) Python 3.6+
   - Pandas library is installed.
2) Actigraphy_Clean.py
3) CSV file(s) obtained from the Philips Actiwatch.

### Optional

1) Text Editor (e.g. VSCode, Sublime Text, Notepad++ etc.)

## Setting up Python

1) Ensure that the option "Add Python to PATH" is selected if you are installing Python for the first time.
2) Install the pandas library using the following command in the command prompt/powershell/terminal

```bash
pip install -U pandas
```

## How to use

1. Place the CSV file(s) in the same folder where the Actigraphy_Cleaner.py is located.
2. Open Actigraphy_Clean.py by using a text editor or Python's built-in IDE.
3. Modify the input and output directory if needed. By default, the input directory is the current working directory (i.e. the location where the Actigraphy_Clean.py is located). The python script will create a new subdirectory where all the modified CSV generated will be stored.
4. Run the Actigraphy_Clean.py script. This can be done by pressing "F5" on your keyboard if you are using the Python's built-in IDE.
