from pathlib import Path
import pandas as pd

script_dir = Path(__file__).resolve().parent

eligibility = pd.read_csv(script_dir.parent / "SLB_ELG_SEC_05062026.csv")
open_pos = pd.read_csv(script_dir.parent / "slb_openpos_05062026.csv")
foreclosure = pd.read_csv(script_dir.parent / "Forclosure_SLB_20260605.CSV")

print("Eligibility:", eligibility.shape)
print("Open position:", open_pos.shape)
print("Foreclosure:", foreclosure.shape)


print("\n--- Foreclosure ---")
print(foreclosure)