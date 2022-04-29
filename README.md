# Actigraphy Cleaner

## Table of Contents

- [Actigraphy Cleaner](#actigraphy-cleaner)
  - [Table of Contents](#table-of-contents)
  - [About Actigraphy Cleaner](#about-actigraphy-cleaner)
  - [Requirements](#requirements)
    - [Optional](#optional)
  - [Setting up Python](#setting-up-python)
  - [How to use](#how-to-use)

## About Actigraphy Cleaner

The Actigraphy Cleaner attempts to clean up the CSV file(s) taken from Philips Actiwatch, and extract only the relevant data needed for further analysis using the SleepAnnotate R script.

## Requirements

1) Python 3.6+
   - Pandas library is installed.
2) Actigraphy_Cleaner.py
3) CSV file(s) obtained from the Philips Actiwatch.

### Optional

1) Text Editor (e.g. VSCode, Sublime Text, Notepad++ etc.)

## Setting up Python

1) Ensure that the option "Add Python to PATH" is selected if you are installing Python for the first time.
2) Install the pandas library by entering the following command into the command prompt/powershell/terminal.

```bash
pip install -U pandas
```

## How to use

1. Place the CSV file(s) in the same folder where the Actigraphy_Cleaner.py is located.
2. Open Actigraphy_Cleaner.py by using a text editor or Python's built-in IDLE.
3. Modify the input and output directory if needed. By default, the input directory is the current working directory (i.e. the location where the Actigraphy_Cleaner.py is located). The python script will create a new subdirectory where all the modified CSV generated will be stored.
4. Run the Actigraphy_Cleaner.py script. This can be done by pressing "F5" on your keyboard if you are using the Python's built-in IDLE. If you are using a text editor mentioned in the [Optional](#optional) section, please check the editor's user guide.
