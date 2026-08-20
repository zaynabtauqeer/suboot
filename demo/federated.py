import json
import os
import sqlite3
import random

BASE = os.path.dirname(os.path.abspath(__file__))
HOSPITALS = {
    "Shifa Hospital": os.path.join(BASE, "hospitals", "hospital_a.db"),
    "Civil Hospital": os.path.join(BASE, "hospitals", "hospital_b.db"),
}


def query_hospital(db_path, diagnosis=None, min_age=None, max_age=None, hba1c_gt=None):
    sql = "SELECT COUNT(*) AS n, AVG(hba1c) AS avg_hba1c, AVG(age) AS avg_age FROM patients WHERE 1=1"
    params = []
    if diagnosis:
        sql += " AND diagnosis = ?"
        params.append(diagnosis)
    if min_age:
        sql += " AND age >= ?"
        params.append(min_age)
    if max_age:
        sql += " AND age <= ?"
        params.append(max_age)
    if hba1c_gt:
        sql += " AND hba1c > ?"
        params.append(hba1c_gt)
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(sql, params)
    n, avg_hba1c, avg_age = cur.fetchone()
    conn.close()
    return {"count": n, "avg_hba1c": round(avg_hba1c, 2) if avg_hba1c else None, "avg_age": round(avg_age, 1) if avg_age else None}


def add_privacy_noise(result, epsilon=1.0):
    scale = 1.0 / max(epsilon, 0.1)
    noisy = dict(result)
    if noisy["count"] is not None:
        noisy["count"] = max(0, noisy["count"] + int(random.uniform(-scale * 3, scale * 3)))
    if noisy["avg_hba1c"] is not None:
        noisy["avg_hba1c"] = round(noisy["avg_hba1c"] + random.uniform(-scale / 5, scale / 5), 2)
    noisy["privacy"] = f"differential privacy noise applied (epsilon={epsilon})"
    return noisy


def federated_query(diagnosis=None, min_age=None, max_age=None, hba1c_gt=None, privacy=True):
    per_hospital = {}
    for name, db_path in HOSPITALS.items():
        raw = query_hospital(db_path, diagnosis, min_age, max_age, hba1c_gt)
        per_hospital[name] = add_privacy_noise(raw) if privacy else raw
    total = sum(h["count"] for h in per_hospital.values())
    return {
        "query": {"diagnosis": diagnosis, "min_age": min_age, "max_age": max_age, "hba1c_gt": hba1c_gt},
        "per_hospital": per_hospital,
        "total_patients": total,
    }


if __name__ == "__main__":
    print(json.dumps(federated_query(diagnosis="type_2_diabetes", hba1c_gt=8.0), ensure_ascii=False, indent=2))
