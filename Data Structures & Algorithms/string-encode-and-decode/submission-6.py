class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == [""]:
            return "empty"
        return "xuegjut".join(strs)

    def decode(self, s: str) -> List[str]:
        if s == "empty":
            return [""]
        if not s:
            return []
        return s.split("xuegjut")
