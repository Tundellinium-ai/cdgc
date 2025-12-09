from collections import defaultdict, Counter

patients = [
    ("P001", "Tolani", 29, "STRB", "6/6"),
    ("P002", "Adewunmi", 45, "GLC", "6/12"),
    ("P003", "Toluwalashe", 33, "STRB", "6/9"),
    ("P004", "Femi", 65, "GLC", "6/60"),
    ("P005", "Amarachi", 50, "CAT", "6/18"),
    ("P006", "God'sglory", 29, "NOA", "6/6"),
]

diagnosis_map = {
    "STRB": "Strabismus",
    "GLC": "Glaucoma",
    "CAT": "Cataract",
    "NOA": "Normal/Other Assessment",
}

#//
patient_dict = {
    pid: {"patient_name": name, "age": age, "diagnosis": code, "visual_acuity": va}
    for pid, name, age, code, va in patients
}

print("1. Patient_dictionary (showing their id and record): ")
for pid, rec in patient_dict.items():
    print(f"  {pid}: {rec}")
print()

#//
for pid, rec in patient_dict.items():
    code = rec["diagnosis"]
    rec["diagnosis_name"] = diagnosis_map.get(code, "Unknown")

print("2. Codes has been mapped to the diagnosis names, This is an example of a patient whose ID is 'P005':")
print(patient_dict["P005"])
print()

#//
unique_codes = {rec["diagnosis"] for rec in patient_dict.values()}
unique_names = {diagnosis_map.get(c, "Unknown") for c in unique_codes}
print("3. Unique diagnosis codes: ", unique_codes)
print("   Unique diagnosis names: ", unique_names)
print()

#//
grouped_by_diag = defaultdict(list)
for pid, rec in patient_dict.items():
    grouped_by_diag[rec["diagnosis_name"]].append(pid)

print("4. Grouped patient IDs by diagnosis name: ")
for diag_name, ids in grouped_by_diag.items():
    print(f"  {diag_name}: {ids}")
print()

#//
diag_counts = Counter(rec["diagnosis_name"] for rec in patient_dict.values())
print("5. Frequency of Diagnosis: ")
for diag, count in diag_counts.items():
    print(f"  {diag}: {count}")
print()

#//
screened = {"P001", "P002", "P003", "P005"}
follow_up = {"P002", "P004"}

def ids_to_idname_pairs(id_set):
    return [f"{pid} - {patient_dict[pid]["patient_name"]}" for pid in id_set if pid in patient_dict]

print("6. Assessment: ")
print("  These patients have been screened: ", ", ".join(ids_to_idname_pairs(screened)))
print("  This patient has been screened and needs follow-up: ", ", ".join(ids_to_idname_pairs(screened & follow_up)))
print("  These patients have been screened but do not need follow-up: ", ", ".join(ids_to_idname_pairs(screened - follow_up)))
print("  These patients are either screened or need follow-up: ", ", ".join(ids_to_idname_pairs(screened | follow_up)))
print()

#//
def advice_strabismus(patient):
    return f"Refer {patient['patient_name']} for orthoptic assessment."

def advice_glaucoma(patient):
    return f"Urgent glaucoma workup for {patient['patient_name']} (whose age is {patient['age']})."

def advice_cataract(patient):
    return f"Discuss cataract surgery options with {patient['patient_name']}."

def advice_default(patient):
    return f"Routine follow-up for {patient['patient_name']}."

advice_to_patients = {
    "Strabismus": advice_strabismus,
    "Glaucoma": advice_glaucoma,
    "Cataract": advice_cataract,
}

print("7. My advice to patients based on my assessment:")
for pid, rec in patient_dict.items():
    diag_name = rec["diagnosis_name"]
    fn = advice_to_patients.get(diag_name, advice_default)
    print(" ", fn(rec))
print()
