from __future__ import annotations

import pandas as pd


def load_table_vi(path: str = "data/curated/e1020_table_vi_v0.csv") -> pd.DataFrame:
    """Load the curated Table VI dataset."""
    return pd.read_csv(path)


def add_log_ed50(df: pd.DataFrame) -> pd.DataFrame:
    """Add log10 ED50 column for rows with numeric ED50."""
    out = df.copy()
    out["log10_ed50_ug_per_kg"] = pd.to_numeric(out["ed50_ug_per_kg"], errors="coerce").map(
        lambda x: None if pd.isna(x) else __import__("math").log10(x)
    )
    return out


def ed50_ranking(df: pd.DataFrame) -> pd.DataFrame:
    """Return compounds ranked by numeric ED50 threshold/value."""
    cols = ["compound_id", "ed50_ug_per_kg", "ed50_relation", "ed50_censored", "iv_potency_class"]
    available = [c for c in cols if c in df.columns]
    return df[available].sort_values(["ed50_ug_per_kg", "compound_id"]).reset_index(drop=True)
