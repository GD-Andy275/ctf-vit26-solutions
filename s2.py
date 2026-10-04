#!/usr/bin/env python3
core = bytearray(open("core.bin", "rb").read())

def run(prefix):
    # ВАЖНО: b — это список из 256 значений, не число!
    b = [(x * 3) & 255 for x in range(256)]
    stack = []
    pos = 0
    inp_idx = 0

    while pos < len(core):
        op = core[pos]
        pos += 1

        if op == 153:
            stack.append(b[0])
            b[0] = (b[0] + 1) & 255
        elif op == 34:
            if len(stack) >= 2:
                stack.append((stack.pop() + stack.pop()) & 255)
        elif op == 63:
            if inp_idx >= len(prefix):
                return 'need_more'
            stack.append(prefix[inp_idx])
            inp_idx += 1
        elif op == 162:
            stack.append(core[pos])
            pos += 1
        elif op == 116:
            if len(stack) >= 2:
                a = stack.pop()
                b2 = stack.pop()
                stack.append((a ^ b2) & 255)
        elif op == 27:
            if len(stack) >= 2:
                a = stack.pop()
                b2 = stack.pop()
                stack.append((a + b2) & 255)
        elif op == 233:
            if len(stack) >= 2:
                a = stack.pop()
                b2 = stack.pop()
                if b2 != a:
                    return 'fail'
                stack.append(a)
        else:
            return 'unknown_opcode'

    return 'success'


key = []
for i in range(40):
    found = False
    for c in range(256):
        r = run(key + [c])
        if r in ('need_more', 'success'):
            key.append(c)
            ch = chr(c) if 32 <= c < 127 else '?'
            print(f"[{i:2d}] байт {c:3d} (0x{c:02x}) = {ch}")
            found = True
            break
    if not found:
        print(f"Не нашли байт на позиции {i}")
        break
    if r == 'success':
        print("\n=== ПОЛНЫЙ КЛЮЧ НАЙДЕН ===")
        break

result = bytes(key)
print(f"\nБайты: {result.hex()}")
print(f"Строка: {result.decode('latin1', errors='replace')}")
try:
    print(f"UTF-8: {result.decode('utf-8')}")
except:
    pass
