# a = {"a":100, "b":200, "c":300}
# # for i in a:
# #     # print(i)
# #     print(i,a[i])

# for key, value in a.items():
#     print(f"key:{key} value:{value}")

# --------formskey----------------

# a = ["a", "b", "c"]
# default = 100
# b = dict.fromkeys(a, default)
# print(b)

# a = ["a", "b", "c"]
# # default = 100
# b = dict.fromkeys(a)
# print(b)

# ------------get--------------

# d = {"a":100, "b":200, "c":300}
# # print(d.get("a"))
# print(d.get("e",0))

# ----------------keys()--------------

# d = {"a":100, "b":200, "c":300}
# print(d.keys())

# ----------------values()------------
# d = {"a":100, "b":200, "c":300}

# print(d.values())

# ----------------pop()----------------


# d = {"a":100, "b":200, "c":300}
# print(d.pop("a"))
# print(d)

# d = {"a":100, "b":200, "c":300}
# print(d.pop("e",0))
# print(d)

# -----------popitems()----------
# d = {"a":100, "b":200, "c":300}

# print(d.popitem())
# print(d)

# -------------setdefault()-------
# d = {"a":100, "b":200, "c":300}

# print(d.setdefault("e",100))
# print(d)

# d = {"a":100, "b":200, "c":300}

# print(d.setdefault("a",1000))
# print(d)


# ----------update()---------

d = {"a":100, "b":200, "c":300}

d.update({"a":1000})
print(d)