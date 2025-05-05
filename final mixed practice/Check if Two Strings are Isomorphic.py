def is_isomorphic(s, t):
    mapping_s_t = {}
    mapping_t_s = {}
    for a, b in zip(s, t):
        if mapping_s_t.get(a, b) != b or mapping_t_s.get(b, a) != a:
            return False
        mapping_s_t[a] = b
        mapping_t_s[b] = a
    return True

print(is_isomorphic("egg", "add"))  # True
print(is_isomorphic("foo", "bar"))  # False
