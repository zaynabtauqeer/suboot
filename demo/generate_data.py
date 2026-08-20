import json
import os
import random
import sqlite3
from datetime import datetime, timedelta

random.seed(42)

BASE = os.path.dirname(os.path.abspath(__file__))
HOSPITALS = {
    "Shifa Hospital": "hospital_a.db",
    "Civil Hospital": "hospital_b.db",
}

DIAGNOSES = {
    "type_2_diabetes": ["type 2 diabetes", "T2DM", "shakar ki bimari", "diabetes mellitus", "sugar"],
    "hypertension": ["hypertension", "high BP", "blood pressure", "lao bas", "bp"],
    "asthma": ["asthma", "saans ki bimari", "damah", "wheezing"],
    "ischemic_heart_disease": ["IHD", "ischemic heart disease", "dil ki bimari", "angina", "chest pain"],
    "chronic_kidney_disease": ["CKD", "chronic kidney disease", "gurde ki bimari", "kidney failure"],
}

MEDICATIONS = {
    "type_2_diabetes": [("metformin", "850mg bd"), ("insulin glargine", "20u od"), ("sitagliptin", "100mg od")],
    "hypertension": [("amlodipine", "5mg od"), ("losartan", "50mg od"), ("enalapril", "10mg bd")],
    "asthma": [("salbutamol", "inhaler prn"), ("beclomethasone", "inhaler bd")],
    "ischemic_heart_disease": [("aspirin", "75mg od"), ("atorvastatin", "20mg od"), ("clopidogrel", "75mg od")],
    "chronic_kidney_disease": [("furosemide", "40mg od"), ("calcitriol", "0.25ug od")],
}

TEMPLATES_EN = [
    "Pt is a {age}y {sex}, known case of {dx} for {years}y. On {med}. Recent HbA1c {hba1c}%. BP {sbp}/{dbp}. Advised {advice}. Follow up in {fu} weeks.",
    "{age}-year-old {sex} presents with {complaint}. History of {dx}. Currently on {med}. Blood sugar {glu} mg/dl, BP {sbp}/{dbp}. Plan: {advice}.",
    "Patient with {dx}, compliant on {med}. Last visit {last}. HbA1c improved to {hba1c}%. Continue same, review in {fu} weeks.",
]

TEMPLATES_RO = [
    "pt {age} saal ka {sex} hai, {dx} ka mareez. {med} leta hai. hba1c {hba1c}%. bp {sbp}/{dbp}. {advice}. {fu} haftay baad ayen.",
    "{age} saal ka {sex}, {dx} ka case. {med} par hai. sugar {glu}, bp {sbp}/{dbp}. masla {complaint}. ilaj: {advice}.",
    "{dx} ka mareez, {med} se theek chal raha hai. pichli dafa {last} aya tha. hba1c {hba1c}%. wohi ilaj jari rakhen, {fu} haftay baad.",
]

TEMPLATES_UR = [
    "{age} سال کا {sex} مریض، {dx} کا عرصہ {years} سال سے شکار ہے۔ {med} استعمال کرتا ہے۔ حالیہ ایچ بی اے ون سی {hba1c} فیصد، بلڈ پریشر {sbp}/{dbp}۔",
    "{sex} مریض {age} سال، شکایت {complaint}۔ تاریخ میں {dx}۔ اس وقت {med} زیر استعمال۔",
]

ADVICE_EN = ["Control diet, reduce salt", "Increase exercise to 30 min daily", "Monitor sugar twice daily"]
ADVICE_RO = ["diet control karein, namak kam", "roz 30 min walk karein", "sugar roza do martaba check karein"]
COMPLAINTS_EN = ["polyuria and weight loss", "headache and dizziness", "shortness of breath", "fatigue"]
COMPLAINTS_RO = ["bar bar peshab aana", "sar dard aur chakkar", "saans mein takleef", "kamzori"]
SEX = ["M", "F"]


def age_hba1c(dx):
    if dx == "type_2_diabetes":
        return round(random.uniform(7.1, 11.2), 1), random.randint(150, 320)
    return round(random.uniform(5.0, 6.9), 1), random.randint(90, 140)


def gen_note(idx, hospital):
    dx = random.choice(list(DIAGNOSES))
    years = random.randint(1, 12)
    age = random.randint(35, 75)
    sex = random.choice(SEX)
    hba1c, glu = age_hba1c(dx)
    sbp = random.randint(115, 165)
    dbp = random.randint(70, 100)
    med, dose = random.choice(MEDICATIONS[dx])
    last = (datetime(2026, 1, 1) + timedelta(days=random.randint(0, 180))).strftime("%b %Y")
    fu = random.choice([2, 4, 6, 8])
    dxtxt = DIAGNOSES[dx][random.randint(0, len(DIAGNOSES[dx]) - 1)]
    complaint = random.choice(COMPLAINTS_EN) if random.random() < 0.5 else random.choice(COMPLAINTS_RO)
    advice = random.choice(ADVICE_EN) if random.random() < 0.5 else random.choice(ADVICE_RO)
    lang = random.choice(["en", "ro", "ur"])
    if lang == "en":
        note = random.choice(TEMPLATES_EN).format(age=age, sex=sex, dx=dxtxt, years=years, med=f"{med} {dose}", hba1c=hba1c, sbp=sbp, dbp=dbp, advice=advice, fu=fu, complaint=complaint, glu=glu, last=last)
    elif lang == "ro":
        note = random.choice(TEMPLATES_RO).format(age=age, sex=sex, dx=dxtxt, med=f"{med} {dose}", hba1c=hba1c, sbp=sbp, dbp=dbp, advice=advice, fu=fu, complaint=complaint, glu=glu, last=last)
    else:
        dxtxt_ur = {"type_2_diabetes": "ذیابیطس ٹائپ ۲", "hypertension": "ہائی بلڈ پریشر", "asthma": "دمہ", "ischemic_heart_disease": "دل کی بیماری", "chronic_kidney_disease": "گردے کی بیماری"}[dx]
        note = random.choice(TEMPLATES_UR).format(age=age, sex=sex, dx=dxtxt_ur, years=years, med=f"{med} {dose}", hba1c=hba1c, sbp=sbp, dbp=dbp, complaint=complaint)

    return {
        "patient_id": f"{hospital[:3].upper()}-{1000 + idx}",
        "hospital": hospital,
        "age": age,
        "sex": sex,
        "diagnosis": dx,
        "diagnosis_text": dxtxt,
        "medication": med,
        "dose": dose,
        "hba1c": hba1c,
        "glucose_mgdl": glu,
        "bp": f"{sbp}/{dbp}",
        "lang": lang,
        "note": note,
        "date": last,
    }


def main():
    notes_dir = os.path.join(BASE, "notes")
    hospitals_dir = os.path.join(BASE, "hospitals")
    for hospital, dbname in HOSPITALS.items():
        records = [gen_note(i, hospital) for i in range(300)]
        notes_file = os.path.join(notes_dir, hospital.replace(" ", "_").lower() + "_notes.jsonl")
        with open(notes_file, "w", encoding="utf-8") as f:
            for r in records:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        db = sqlite3.connect(os.path.join(hospitals_dir, dbname))
        db.execute("DROP TABLE IF EXISTS patients")
        db.execute(
            """CREATE TABLE patients (
                patient_id TEXT, hospital TEXT, age INT, sex TEXT,
                diagnosis TEXT, diagnosis_text TEXT, medication TEXT, dose TEXT,
                hba1c REAL, glucose_mgdl INT, bp TEXT, lang TEXT, note TEXT, date TEXT)"""
        )
        db.executemany(
            "INSERT INTO patients VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
            [tuple(r.values()) for r in records],
        )
        db.commit()
        db.close()
        print(f"[OK] {hospital}: 300 notes + db created ({dbname})")

    print("\nDone. Sample notes:")
    with open(os.path.join(notes_dir, "shifa_hospital_notes.jsonl"), encoding="utf-8") as f:
        for i in range(3):
            r = json.loads(f.readline())
            print(f"\n--- ({r['lang']}) ---\n{r['note']}")


if __name__ == "__main__":
    main()
