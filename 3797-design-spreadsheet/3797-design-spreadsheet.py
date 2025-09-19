class Spreadsheet:
    def __init__(self, rows: int) -> None:
        self.rows = rows
        self.sheet = {}

    def setCell(self, c: str, v: int) -> None:
        self.sheet[c] = v

    def resetCell(self, c: str) -> None:
        if c in self.sheet:
            del self.sheet[c]

    def getValue(self, f: str) -> int:
        if not f or f[0] != '=':
            return 0
        parts = f[1:].split('+')
        s = 0
        for p in parts:
            p = p.strip()
            s += self._val(p)
        return s

    def _val(self, t: str) -> int:
        return int(t) if t.isdigit() else self.sheet.get(t, 0)
