from pathlib import Path
import pandas as pd


def test_table_vi_dataset_exists():
    assert Path("data/curated/e1020_table_vi_v0.csv").exists()


def test_table_vi_has_expected_rows():
    df = pd.read_csv("data/curated/e1020_table_vi_v0.csv")
    assert len(df) == 35


def test_11a_is_strong():
    df = pd.read_csv("data/curated/e1020_table_vi_v0.csv")
    row = df.loc[df["compound_id"] == "11a"].iloc[0]
    assert row["iv_potency_class"] == "strong"


def test_23_is_weak_and_right_censored():
    df = pd.read_csv("data/curated/e1020_table_vi_v0.csv")
    row = df.loc[df["compound_id"] == "23"].iloc[0]
    assert row["iv_potency_class"] == "weak"
    assert row["ed50_censored"] == "right"
