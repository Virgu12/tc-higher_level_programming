#!/usr/bin/python3
abujanha = ["AbujJanha", "DaJanjaJarilanja", "J"]
abjh = "".join(abujanha)
pares = "".join([c for c in abjh if c.upper() != "J"])
print(pares)