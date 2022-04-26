import pandas as pd
import re
import csv
import os

input_directory = "SIT_controlGroup"
output_directory = "SIT_control Group"
os.chdir(input_directory)


def actigraphy_data():

    target = re.compile(r"-{20} Epoch-by-Epoch Data -{19}")
    for file in os.listdir():
        print(f"Now reading {file}...")

        row = 17

        with open(file) as csv_file:
            csv_reader = csv.reader(csv_file)

            for item in csv_reader:
                if not re.search(target, str(item)):
                    row += 1
                else:
                    break
        while True:
            df = pd.read_csv(
                file,
                skiprows=row,
            )

            try:
                df.iloc[0]["Line"]
            except KeyError:
                row -= 1
                continue
            else:
                break
        df = df.filter(["Date", "Time", "Activity"])
        df = df.rename(columns={"Activity": "Axis1"})
        df["Axis1"].fillna(0, inplace=True)
        df["Date"].apply(pd.to_datetime, infer_datetime_format=True)
        df["Date"] = pd.to_datetime(df["Date"]).dt.strftime("%#d/%#m/%Y")
        df["Time"].apply(pd.to_datetime)
        df["Time"] = pd.to_datetime(df["Time"]).dt.strftime("%#H:%M")
        output_filename = file.split(".")[0]

        try:
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

    return None


actigraphy_data()
