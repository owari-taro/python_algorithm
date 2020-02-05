def bf_match(txt: str, pat: str) -> int:
    """brute force math for text searching"""
    pt = pp = 0
    while pt != len(txt) and pp != len(pp):
        if txt[pt] == pat[pp]:
            pt += 1
            pp += 1
        else:
            pt = pt-pp+1
            pp = 0
        # if pat contan in txt then return starting index 
        return pt-pp if pp == len(pat) else -1

abcdefg
abcz