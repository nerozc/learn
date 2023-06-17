import time
def strcounter(s):
    for sym in set(s):
        count = 0
        for sub_sym in s:
            if sym == sub_sym:
                count+=1
        print(sym,count)
def strcounter_new(s):
    syms_counter = {}
    for sym in s:
        syms_counter[sym] = syms_counter.get(sym,0) + 1
    for sym, count in syms_counter.items():
        print(sym,count)
strcounter('abcc')
strcounter_new('abc')