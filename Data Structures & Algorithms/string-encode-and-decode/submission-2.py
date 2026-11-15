class Solution:
    def parse_header(self, s: str) -> [str, str]:
        i = 0
        while s[i] != '#':
            i += 1
        return [(s[:i]),s[i+1:]]


    def encode(self, strs: List[str]) -> str:
        return ''.join([str(len(s))+'#'+s for s in strs])

    def decode(self, s: str) -> List[str]:
        ret = []
        while s:
            size, s = self.parse_header(s)
            size = int(size)
            ret.append(s[:size])
            s = s[size:]
        return ret