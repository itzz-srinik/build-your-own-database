import json
import os


class MiniDB:
    """A tiny key-value database that saves every change to a log file."""

    def __init__(self, path="data.log"):
        self.path = path
        self.data = {}
        self._load()

    def _load(self):
        # Replay the log to rebuild the current state
        if not os.path.exists(self.path):
            return
        with open(self.path) as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                entry = json.loads(line)
                if entry["op"] == "set":
                    self.data[entry["key"]] = entry["value"]
                elif entry["op"] == "delete":
                    self.data.pop(entry["key"], None)

    def _write(self, entry):
        with open(self.path, "a") as f:
            f.write(json.dumps(entry) + "\n")

    def set(self, key, value):
        self._write({"op": "set", "key": key, "value": value})
        self.data[key] = value

    def get(self, key, default=None):
        return self.data.get(key, default)

    def delete(self, key):
        self._write({"op": "delete", "key": key})
        self.data.pop(key, None)

    def keys(self):
        return list(self.data.keys())
