import hashlib
import json
import time


class EvidenceReceipt:
    def __init__(self, query, hospital, result, prev_hash="0" * 64):
        self.timestamp = time.strftime("%Y-%m-%d %H:%M:%S")
        self.query = query
        self.hospital = hospital
        self.result = result
        self.prev_hash = prev_hash
        self.hash = self._compute_hash()

    def _compute_hash(self):
        data = json.dumps({
            "timestamp": self.timestamp,
            "query": self.query,
            "hospital": self.hospital,
            "result": self.result,
            "prev_hash": self.prev_hash,
        }, ensure_ascii=False, sort_keys=True)
        return hashlib.sha256(data.encode()).hexdigest()

    def to_dict(self):
        return {
            "timestamp": self.timestamp,
            "query": self.query,
            "hospital": self.hospital,
            "result": self.result,
            "prev_hash": self.prev_hash,
            "hash": self.hash,
        }


class AuditLedger:
    def __init__(self):
        self.chain = []

    def add_receipt(self, query, hospital, result):
        prev = self.chain[-1].hash if self.chain else "0" * 64
        receipt = EvidenceReceipt(query, hospital, result, prev)
        self.chain.append(receipt)
        return receipt

    def verify_chain(self):
        for i, r in enumerate(self.chain):
            if r.hash != r._compute_hash():
                return False, f"Receipt {i} hash mismatch — TAMPERED"
            if i > 0 and self.chain[i].prev_hash != self.chain[i - 1].hash:
                return False, f"Receipt {i} prev_hash broken — CHAIN BROKEN"
        return True, "All receipts verified — chain intact"

    def tamper_receipt(self, index, new_result):
        self.chain[index].result = new_result
        self.chain[index].hash = self.chain[index]._compute_hash()

    def to_list(self):
        return [r.to_dict() for r in self.chain]


if __name__ == "__main__":
    ledger = AuditLedger()
    ledger.add_receipt("diabetes patients > 8", "Shifa Hospital", {"count": 45})
    ledger.add_receipt("diabetes patients > 8", "Civil Hospital", {"count": 38})
    print("Valid:", ledger.verify_chain()[0])
    ledger.tamper_receipt(0, {"count": 999})
    print("After tamper:", ledger.verify_chain())
