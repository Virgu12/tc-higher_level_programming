#!/usr/bin/python3
def uppercase(str):
    texto_mudado = ""
    for c in str:
      if 97 <= ord(c) <= 122:
       texto_mudado += chr(ord(c) - 32)
      else:
        texto_mudado += c
    print("{}".format(texto_mudado), end="")
uppercase('')
