class Solution:

    def encode(self, strs: List[str]) -> str:
        # concatenate
        # joe, bill, sally
        # joebillsally
        # separate by delimiter and scan until it hits one
        # joe$bill$sally$
        # but input can be any string
        # separate by number of characters and delimiter
        # 3$joe4$bill5$sally
        concatString = []
        for string in strs:
            concatString.append(f'{len(string)}')
            concatString.append("$")
            concatString.append(string)
        
        return "".join(concatString)

    def decode(self, s: str) -> List[str]:
        # increment through 1 character at a time
        # we know it starts with a number
        i = 0
        res = []
        while i < len(s):
            delimiterPos = s.find("$", i)

            length = int(s[i:delimiterPos])

            string = s[delimiterPos + 1 : delimiterPos + length + 1]

            res.append(string)

            i = delimiterPos + length + 1

        return res