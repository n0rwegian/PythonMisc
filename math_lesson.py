(lambda s1, s2, s3: print(*sorted((s1 | s2 | s3) - (s1 & s2 & s3), key=int)))(*[set(input().split()) for _ in range(3)])

# [print(*sorted(f ^ s | s ^ t, key=int)) for f, s, t in [(set(input().split()) for _ in '012')]]