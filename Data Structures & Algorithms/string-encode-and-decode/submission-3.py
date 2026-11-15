class Solution:
    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)

    def decode(self, s: str) -> List[str]:
        ret = []
        i = 0
        while i < len(s):
            j = s.find('#', i)
            size = int(s[i:j])
            start = j + 1
            ret.append(s[start:start + size])
            i = start + size
        return ret