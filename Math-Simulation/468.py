"""
468. Validate IP Address  [Medium]

Approach (format-specific validation):
  - Decide which format to attempt from the delimiter present: '.' only ->
    IPv4, ':' only -> IPv6, otherwise neither.
  - IPv4: split on '.', require exactly 4 non-empty parts, each all digits,
    no leading zero (unless the part is just "0"), and in [0, 255].
  - IPv6: split on ':', require exactly 8 non-empty parts, each 1-4 hex
    digits (letters compared case-insensitively against 'f').

Complexity: O(n) time, O(n) space (n = len(queryIP))
"""

class Solution:
    def validIPAddress(self, queryIP: str) -> str:
        self.solution = "Neither"
        temp = set(queryIP)

        def IPv4_checker(ip: str):
            ip = ip.split(".")

            # check length
            if len(ip) != 4:
                return

            # check values
            for val in ip:
                if not val:
                    return
                if len(val) > 4:
                    return
                if not val.isdigit():
                    return
                if len(val) > 1 and val[0] == "0":
                    return
                if int(val) > 255 or int(val) < 0:
                    return

            self.solution = "IPv4"


        def IPv6_checker(ip: str):
            ip = ip.split(":")

            # check length
            if len(ip)!= 8:
                return

            # check values
            for val in ip:
                if not val:
                    return
                if len(val) > 4:
                    return
                for i in val:
                    if not i.isalnum():
                        return
                    if i.isalpha():
                        if i.lower() > "f":
                            return

            self.solution = "IPv6"

        if '.' in temp and ':' not in temp:
            IPv4_checker(queryIP)
        if '.' not in temp and ':' in temp:
            IPv6_checker(queryIP)

        return self.solution
