import streamlit as st
import json
import os
import sys
import random

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from structurize import structurize
from federated import federated_query, HOSPITALS
from ledger import AuditLedger

st.set_page_config(page_title="Suboot Demo — Clinical Evidence Network", layout="wide")

st.title("Suboot")
st.caption("Federated Clinical-Evidence Network — Live Demo")

TAB_NOTES, TAB_FEDERATED, TAB_LEDGER, TAB_PIPELINE = st.tabs([
    "1. Note Structurization",
    "2. Federated Query",
    "3. Audit Ledger",
    "4. Full Pipeline",
])

SAMPLE_NOTES = {
    "English (Diabetes)": "Patient is a 52-year-old male, type 2 diabetes mellitus. On metformin 850mg BD. HbA1c 9.2%. BP 138/88.",
    "Roman Urdu (Diabetes)": "pt 45 saal ka M hai, type 2 dm ka mareez. metformin 850 mg bd leta hai. hba1c 8.9%. bp 140/90.",
    "Urdu (Hypertension)": "مریض 60 سال کی خاتون ہے۔ ہائی بلڈ پریشر ہے۔ amlodipine 5 mg روزانہ۔ bp 160/100۔",
    "English (Asthma)": "34-year-old female with asthma. Uses salbutamol inhaler PRN, beclomethasone 200mcg BD. Recent FEV1 72%.",
    "Roman Urdu (CKD)": "pt 58 saal ka M, chronic kidney disease stage 3. creatinine 2.8. furosemide 40mg OD.",
}

# ── Tab 1: Note Structurization ──
with TAB_NOTES:
    st.subheader("Clinical Note → Structured Data")
    st.markdown("Paste a clinical note in **Urdu**, **Roman Urdu**, or **English**. The engine extracts diagnosis, medication, dose, HbA1c, and BP.")

    col1, col2 = st.columns([3, 2])
    with col1:
        note_choice = st.selectbox("Sample notes", list(SAMPLE_NOTES.keys()), key="note_choice")
        custom_note = st.text_area("Or paste your own note", value=SAMPLE_NOTES[note_choice], height=120, key="custom_note")

    with col2:
        if st.button("Extract", key="extract_btn", use_container_width=True):
            result = structurize(custom_note)
            st.markdown("**Extracted fields:**")
            for k, v in result.items():
                label = k.replace("_", " ").title()
                display = v if v is not None else "_not found_"
                st.markdown(f"**{label}:** `{display}`")

            st.json(result)

# ── Tab 2: Federated Query ──
with TAB_FEDERATED:
    st.subheader("Federated Query Across Hospitals")
    st.markdown("Query runs **on-prem at each hospital**. Only aggregated, differentially-private statistics leave. No patient data moves.")

    c1, c2, c3 = st.columns(3)
    with c1:
        diagnosis = st.selectbox("Diagnosis", ["type_2_diabetes", "hypertension", "asthma", "ischemic_heart_disease", "chronic_kidney_disease"], key="dx")
    with c2:
        min_age = st.number_input("Min age", min_value=0, max_value=120, value=30, key="min_age")
        hba1c_gt = st.number_input("HbA1c greater than", min_value=0.0, max_value=20.0, value=8.0, step=0.5, key="hba1c")
    with c3:
        max_age = st.number_input("Max age", min_value=0, max_value=120, value=70, key="max_age")
        privacy = st.checkbox("Differential privacy", value=True, key="privacy")

    if st.button("Run Federated Query", key="run_query", use_container_width=True):
        result = federated_query(
            diagnosis=diagnosis,
            min_age=min_age,
            max_age=max_age,
            hba1c_gt=hba1c_gt,
            privacy=privacy,
        )

        st.markdown(f"**Query:** `{result['query']}`")
        st.markdown(f"**Total patients across all hospitals:** `{result['total_patients']}`")

        for hosp_name, hosp_data in result["per_hospital"].items():
            with st.expander(hosp_name, expanded=True):
                cols = st.columns(3)
                cols[0].metric("Patients", hosp_data["count"])
                cols[1].metric("Avg HbA1c", hosp_data["avg_hba1c"] or "N/A")
                cols[2].metric("Avg Age", hosp_data["avg_age"] or "N/A")
                st.caption(hosp_data.get("privacy", ""))

# ── Tab 3: Audit Ledger ──
with TAB_LEDGER:
    st.subheader("Cryptographic Audit Ledger")
    st.markdown("Every query + result is logged on an **append-only hash chain**. Regulators get ALCOA+ proof. Tamper the chain → verification fails instantly.")

    if "ledger" not in st.session_state:
        st.session_state.ledger = AuditLedger()

    ledger = st.session_state.ledger

    col_a, col_b = st.columns(2)
    with col_a:
        st.markdown("#### Add Receipt")
        receipt_query = st.text_input("Query ID", value="T2DM HbA1c>8", key="rq")
        receipt_hosp = st.selectbox("Hospital", list(HOSPITALS.keys()), key="rh")
        receipt_result = st.text_area("Result JSON", value='{"count": 42}', key="rr")
        if st.button("Add to Ledger", key="add_receipt"):
            try:
                result_obj = json.loads(receipt_result)
            except json.JSONDecodeError:
                result_obj = {"raw": receipt_result}
            ledger.add_receipt(receipt_query, receipt_hosp, result_obj)
            st.success(f"Receipt added. Total receipts: {len(ledger.chain)}")

    with col_b:
        st.markdown("#### Verify Chain")
        st.metric("Total receipts", len(ledger.chain))
        if st.button("Verify Integrity", key="verify"):
            ok, msg = ledger.verify_chain()
            if ok:
                st.success(msg)
            else:
                st.error(msg)

        if st.button("Simulate Tamper", key="tamper", disabled=len(ledger.chain) == 0):
            idx = random.randint(0, len(ledger.chain) - 1)
            ledger.tamper_receipt(idx, {"count": 99999, "TAMPERED": True})
            st.warning(f"Receipt {idx} tampered! Now verify again →")

    if ledger.chain:
        st.markdown("#### Ledger Chain")
        for i, r in enumerate(ledger.chain):
            with st.expander(f"Receipt {i}: {r.hospital} — {r.timestamp}"):
                st.json(r.to_dict())

# ── Tab 4: Full Pipeline ──
with TAB_PIPELINE:
    st.subheader("Full Pipeline: Note → Structure → Query → Ledger")
    st.markdown("End-to-end flow: paste a note, structurize it, run federated query, log to ledger.")

    pipeline_note = st.text_area(
        "Clinical note",
        value="Patient is a 55-year-old male, type 2 diabetes. On metformin 1000mg BD. HbA1c 9.5%. BP 145/92.",
        height=100,
        key="pipeline_note",
    )

    if st.button("Run Full Pipeline", key="run_pipeline", use_container_width=True):
        st.markdown("---")
        st.markdown("### Step 1: Structurize")
        structured = structurize(pipeline_note)
        st.json(structured)

        st.markdown("### Step 2: Federated Query")
        query_result = federated_query(
            diagnosis=structured.get("diagnosis"),
            hba1c_gt=structured.get("hba1c") or 8.0,
            privacy=True,
        )
        st.json(query_result)

        st.markdown("### Step 3: Ledger Receipt")
        pipeline_ledger = AuditLedger()
        for hosp_name, hosp_data in query_result["per_hospital"].items():
            pipeline_ledger.add_receipt(
                f"Pipeline: {structured.get('diagnosis')}",
                hosp_name,
                hosp_data,
            )
        ok, msg = pipeline_ledger.verify_chain()
        st.json({"chain_length": len(pipeline_ledger.chain), "integrity": msg})
        for i, r in enumerate(pipeline_ledger.chain):
            st.markdown(f"**Receipt {i}** — `{r.hospital}` — hash: `{r.hash[:16]}...`")

        st.success("Pipeline complete. No patient data left the hospital.")

st.markdown("---")
st.caption("Suboot Demo | Federated Clinical-Evidence Network | Built for NIC Islamabad Cohort 6")
