import pandas as pd
import re
import csv
import os
import platform

# --- User input ---
input_directory = "csv_file"  # Which folder contains the raw csv input?
output_directory = (
    "formatted_csv"  # Which folder do you want to export the formatted csv to?
)
date_format = "%d/%m/%Y"

# ------------------
os.chdir(input_directory)


def actigraphy_data():

    target = re.compile(r"-{20} Epoch-by-Epoch Data -{19}")
    for file in os.listdir():
        print(f"Now reading {file}...")

        row = 17
        if not os.path.isdir(file):

            with open(file) as csv_file:
                csv_reader = csv.reader(csv_file)

                for item in csv_reader:
                    if not re.search(target, str(item)):
                        row += 1
                    else:
                        break
            while True:
                df = pd.read_csv(file, skiprows=row)

                try:
                    df.iloc[0]["Line"]
                except KeyError:
                    row -= 1
                else:
                    break
            df = df.filter(["Date", "Time", "Activity"])
            df["Date"] = pd.to_datetime(df["Date"], format=date_format)
            df = df.rename(columns={"Activity": "Axis1"})

            if platform.system() == "Windows":
                df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%e/%#m/%y")
            else:
                df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%-d/%-m/%y")

            if (
                pd.to_datetime(df["Time"], format="%H:%M:%S", errors="coerce")
                .notnull()
                .all()
            ):
                df["Time"] = pd.to_datetime(df["Time"], format="%H:%M:%S")
                df["Time"] = pd.to_datetime(df["Time"]).dt.strftime("%H:%M")
            elif (
                pd.to_datetime(df["Time"], format="%I:%M:%S %p", errors="coerce")
                .notnull()
                .all()
            ):
                df["Time"] = pd.to_datetime(df["Time"], format="%I:%M:%S %p")
                df["Time"] = pd.to_datetime(df["Time"]).dt.strftime("%H:%M")
            output_filename = file.split("_")[0]

            try:
                print(f"Exporting as {output_filename}_all epoch.csv")
                df.to_csv(
                    f"./{output_directory}/{output_filename}_all epoch.csv",
                    index=False,
                    encoding="utf-8",
                )
            except OSError:
                os.mkdir(f"{output_directory}")
                df.to_csv(
                    f"./{output_directory}/{output_filename}_all epoch.csv",
                    index=False,
                    encoding="utf-8",
                )
    print("All done!")

    return None


actigraphy_data()
