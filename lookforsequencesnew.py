from pathlib import Path
import csv

root = Path(r"E:\Test Data\standard_nii")
if not root.exists():
    raise FileNotFoundError(f"File do not exists:{ root }")

patient_count = 0
missing_flair_count = 0

with open("mri_qc.csv", "w", newline = "", encoding = "utf-8-sig") as f:
    writer = csv.writer(f)
    writer.writerow  (["patient_id", "T1CE", "FLAIR"])
    
    for patient in root.iterdir():
        if not patient.is_dir():
            continue
        patient_id = patient.name
        
        t1ce = patient / "T1CE.nii.gz"
        flair = patient / "FLAIR.nii.gz"
        t1ce_status = t1ce.is_file()
        flair_status = flair.is_file()
        if t1ce_status and flair_status:
            patient_count +=1
        if t1ce_status and not flair_status:
            missing_flair_count +=1
        
        writer.writerow  ([patient_id, t1ce_status,flair_status])
		
		
print("Patients with both sequnces:", patient_count)
print("Patients with T1CE but missing FLAIR:", missing_flair_count)
print("csv saved: mri_qc.csv")