import pandas as pd
import re
import csv
import os

directory = "SIT_controlGroup/SIT011.csv"


def actigraphy_data():
    target = re.compile(r"-------------------- Epoch-by-Epoch Data -------------------")
    row = 16

    with open(directory) as csv_file:
        csv_reader = csv.reader(csv_file)

        for item in csv_reader:
            if not re.search(target, str(item)):
                row += 1
            else:
                break
    df = pd.read_csv(
        directory,
        skiprows=row,
    )
    df = df.filter(["Line", "Date", "Time", "Activity"])
    df = df.rename(columns={"Activity": "Axis"})
    try:
        df.to_csv(
            "/SIT_ControlGroupFiltered/SIT001_allepoch.csv",
            index=False,
            encoding="utf-8",
        )
    except OSError:
        os.mkdir("SIT_ControlGroupFiltered")
        df.to_csv(
            "./SIT_ControlGroupFiltered/SIT001_all epoch.csv",
            index=False,
            encoding="utf-8",
        )

    return df.head(20)


actigraphy_data()
