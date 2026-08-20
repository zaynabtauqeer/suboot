import re
import json

DIAG_KEYWORDS = {
    "type_2_diabetes": ["type 2 diabetes", "type2 diabetes", "t2dm", "diabetes mellitus", "diabetes", "sugar", "zabiabetis", "ذیابیطس", "شاکر", "shakar"],
    "hypertension": ["hypertension", "high bp", "blood pressure", "bp", "lao bas", "ہائی بلڈ پریشر", "بلڈ پریشر"],
    "asthma": ["asthma", "wheezing", "damah", "saans ki bimari", "دمہ"],
    "ischemic_heart_disease": ["ihd", "ischemic heart", "angina", "chest pain", "dil ki bimari", "دل کی بیماری"],
    "chronic_kidney_disease": ["ckd", "chronic kidney", "kidney failure", "gurde ki bimari", "گردے"],
}

MED_KEYWORDS = [
    "metformin", "sitagliptin", "insulin", "amlodipine", "losartan", "enalapril",
    "salbutamol", "beclomethasone", "aspirin", "atorvastatin", "clopidogrel",
    "furosemide", "calcitriol",
]


def extract_diagnosis(note):
    low = note.lower()
    for dx, keys in DIAG_KEYWORDS.items():
        for k in keys:
            if k in low:
                return dx
    return "unknown"


def extract_medication(note):
    low = note.lower()
    for med in MED_KEYWORDS:
        if med in low:
            m = re.search(re.escape(med) + r"(\s+\d+\s*(?:mg|ug|u))?", low)
            dose = m.group(1).strip() if m and m.group(1) else ""
            return med, dose
    return "", ""


def extract_hba1c(note):
    m = re.search(r"hba1c\s*([0-9.]+)", note.lower())
    if m:
        return float(m.group(1))
    return None


def extract_bp(note):
    m = re.search(r"bp\s*([0-9]{2,3})/([0-9]{2,3})", note.lower())
    if m:
        return f"{m.group(1)}/{m.group(2)}"
    return None


def structurize(note):
    return {
        "diagnosis": extract_diagnosis(note),
        "medication": extract_medication(note)[0],
        "dose": extract_medication(note)[1],
        "hba1c": extract_hba1c(note),
        "bp": extract_bp(note),
    }


if __name__ == "__main__":
    import sys
    sample = sys.argv[1] if len(sys.argv) > 1 else "pt 45 saal ka M hai, type 2 dm ka mareez. metformin 850 mg bd leta hai. hba1c 8.9%. bp 140/90."
    print(json.dumps(structurize(sample), ensure_ascii=False, indent=2))
