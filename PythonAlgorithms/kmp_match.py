def kmp_match(txt: str, pat: str) -> int:
    pt = 1
    pp = 0
    skip = [0]*(len(pat)+1)

    skip[pt] = 0
    while pt != len(pat):
        if pat[pt] == pat[pp]:
            pt += 1
            pp += 1
            skip[pt] = pp
        elif pp == 0:
            pt += 1
            skip[pt] = pp
        else:
            pp = skip[pp]

    pt = pp = 0
