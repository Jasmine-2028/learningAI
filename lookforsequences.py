
#-*- coding : utf-8 -*-

from pathlib import Path
root = Path(r"E:\Test Data\standard_nii")
if not root.exists():
    print("The path does not exist.")
    exit()
patient_count = 0
for file in root.iterdir():
    if not file.is_dir():
        continue
    patient_id = file.name
    t1ce = file / "T1CE.nii.gz"
    flair = file / "FLAIR.nii.gz"
    if t1ce.is_file() and flair.is_file():
        patient_count += 1

print("Patients with both sequences:",patient_count)