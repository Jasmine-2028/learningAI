
patients = [
    {"id": "P001", "label": 1},
    {"id": "P002", "label": 0},
    {"id": "P003", "label": 1},
    {"id": "P004", "label": 1},
    {"id": "P005", "label": 0},
    {"id": "P006", "label": 0}
]


def count_patients(patients):
    tumor_count = 0
    nontumor_count = 0

    for patient in patients:
        if patient["label"] == 1:
            tumor_count += 1
        elif patient["label"] == 0:
            nontumor_count += 1

    return tumor_count, nontumor_count


tumor, nontumor = count_patients(patients)

print("Tumor:", tumor)
print("Non-tumor:", nontumor)
