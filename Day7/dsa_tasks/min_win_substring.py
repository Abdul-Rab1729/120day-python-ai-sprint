def min_win_substring(s,t):
    freq={}
    for ch in t:
        if ch in freq:
            freq[ch]+=1
        else:
            freq[ch]=1
            
    win_cnt = {}
    have = 0
    need = len(freq)

    res = ""
    min_len = float('inf')
    start = 0

    for end in range(len(s)):
        ch = s[end]
        if ch in freq:
            win_cnt[ch] = win_cnt.get(ch, 0) + 1
            if win_cnt[ch] == freq[ch]:
                have += 1

        # Try shrinking from the left while window is valid
        while have == need:
            window_len = end - start + 1
            if window_len < min_len:
                min_len = window_len
                res = s[start:end+1]

            left_ch = s[start]
            if left_ch in freq:
                win_cnt[left_ch] -= 1
                if win_cnt[left_ch] < freq[left_ch]:
                    have -= 1
            start += 1

    return res
s = "ADOBECODEBANC"
t = "ABC"

print(min_win_substring(s,t))
