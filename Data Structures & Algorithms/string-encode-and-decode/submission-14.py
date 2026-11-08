class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for s in strs:
            l = len(s)
            res.append(str(len(s)) + "#" + s)
        return "".join(res)

    def decode(self, s: str) -> List[str]:
        i = 0
        res = []
        word_length = 0
        while i < len(s):
            j = i
            while s[i] != "#":
                i += 1

            word_length = int(s[j:i])
            res.append(s[i + 1:i + word_length + 1])
            i += word_length
            i += 1
        return res




# class Solution:

#     def encode(self, strs: List[str]) -> str:
#         if strs == [""]:
#             return "empty"
#         return "xuegjut".join(strs)

#     def decode(self, s: str) -> List[str]:
#         if s == "empty":
#             return [""]
#         if not s:
#             return []
#         return s.split("xuegjut")
