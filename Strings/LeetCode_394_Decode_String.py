class Solution:
    def decodeString(self, s: str) -> str:
        # Shared pointer over the string. The recursive helper advances it.
        i = 0

        def decode() -> str:
            nonlocal i
            decoded_chars = []
            repeat = 0

            while i < len(s):
                ch = s[i]
                if ch.isdigit():
                    # Build a multi-digit repeat count.
                    repeat = repeat * 10 + int(ch)
                elif ch == "[":
                    # Enter a nested segment and decode it recursively.
                    i += 1
                    decoded_chars.append(decode() * repeat)
                    repeat = 0
                elif ch == "]":
                    # End of the current nested segment.
                    return "".join(decoded_chars)
                else:
                    # Regular character; append to current result.
                    decoded_chars.append(ch)
                i += 1

            # Return the top-level decoded string when the input is exhausted.
            return "".join(decoded_chars)

        return decode()