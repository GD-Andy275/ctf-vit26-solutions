Imaginarium (Misc)
Флаг: vit26{rgb_pix3ls_m4s73r}

Разбор
Файл Imaginarium.jpg — не картинка, а ASCII-текст с числами.
Всего 1 260 000 чисел = ровно 1000 × 1260 пикселей.
Собрал числа обратно в grayscale-картинку через Python/PIL:

python
from PIL import Image
import numpy as np
nums = np.array(open('Imaginarium.jpg').read().split(), dtype=np.uint8)
Image.fromarray(nums.reshape((1260, 1000)), mode='L').save('out.png')

На картинке виден текст флага.

Gamer (Misc)
Флаг: vit26{7h3_f457357_h4nd5_1n_7h3_w357}

Разбор
challenge_server — сервер на :1337, присылает задания в формате:
- Метод: AES / XOR / 3DES / ROT13 / BASE64
- Ключ: ...
- Шифртекс: base64

Нужно за 2 секунды расшифровать и ответить. Написан Python-клиент (см. s2.py)

Scater (OSINT)
Флаг: vit26{central_park}

Разбор
Фото скейтера — кадр из реконструкции Bas Jan Ader «Fall» (Elena Muti, 2014).
Через Yandex.Images нашли оригинал на Wikimedia Commons.
Место съёмки — Central Park, Нью-Йорк.

Distreverse (Reverse)
Флаг: vit26{vm_r3v3rs3_1s_fUn_2026}

interpreter — PyInstaller-сборка Python 3.13.
Распаковал через pyinstxtractor, дизассемблировал ".pyc" через pycdas.
Внутри — кастомная VM, интерпретирующая байткод core.bin.

Восстановил логику опкодов:
- 153 — push b[0]
- 34 — ADD
- 63 — READ input
- 162 — push byte from core.bin
- 116 — XOR
- 27 — ADD
- 233 — COMPARE

Написал симулятор VM и посимвольный брутфорс — нашел правильный ACCESS KEY = флаг.


