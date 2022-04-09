import pandas as pd
import re
import csv
import os

input_directory = "SIT_controlGroup"
output_directory = "SIT_ControlGroup Filtered"
os.chdir(input_directory)


def actigraphy_data():

    target = re.compile(r"-------------------- Epoch-by-Epoch Data -------------------")
    problematic_file = []
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
        df = df.filter(["Line", "Date", "Time", "Activity"])
        df = df.rename(columns={"Activity": "Axis"})
        if df.iloc[0]["Line"] != 1:
            problematic_file.append(file)

        try:
            df.to_csv(
                f"./{output_directory}/{file}_allepoch.csv",
                index=False,
                encoding="utf-8",
            )
        except OSError:
            os.mkdir(f"{output_directory}")
            df.to_csv(
                f"./{output_directory}/{file}_all epoch.csv",
                index=False,
                encoding="utf-8",
            )
    print(problematic_file) if len(problematic_file) > 0 else print("All good!")

    return None


actigraphy_data()
