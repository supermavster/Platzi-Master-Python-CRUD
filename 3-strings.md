# Operaciones con strings: Slices en python

Los **slices** en Python nos permiten manejar secuencias de una manera poderosa.

**Slices** en español significa “rebanada”, si tenemos una secuencia de elementos y queremos una rebanada tenemos una sintaxis para definir qué pedazos queremos de esa secuencia.

```
secuencia[comienzo:final:pasos]
```

## Ejemplos:

```
string = "banana"

b a n a n a
0 1 2 3 4 5
```

---

Start in 1 and End in 3

```
string[1:3] # an
```

---

Start in 3 and End in N

```
string[3:] # ana
```

---

Start in 3 and End in 3

```
string[3:3] # No exist data or steps
```

---

Start in 0 and End in N

```
string[:] # banana
```

---

Start in 1 and End in the last one word and make a step in two

```
string[1:-1:2]

banana # Word
anan # 1:-1
aa # 2

Result: aa
```

---

Start in 1 and End in 4

```
string[1:4] # ana
```

---

Start in 4 and End in 8

```
string[4:8] # na
# No da error porque dice: Si no hay más indices muestre hasta el último posible
```

---

Reverse the string

```
string[::-1] # Start to end and the steps is the N to 0 (reverse) # ananab
```

---

Start in 0 and End in 8 by Step 3

```
string[:8:3] # ba

# Process
b a n a n a
0 1 2 3 4 5

0...8
banana

b..a..
ba
```

---

Start in 0 and End in N by Step 2

```
string[::2] # bnn

# Process
b a n a n a
0 1 2 3 4 5

0....n

b.n.n.
bnn
```

# Word Most Longer (Spanish)

**arroz (Comienza con la A y termina en la Z) :v**

La palabra más grande es el nombre completo de la proteina llamada titin
https://fullformdirectory.in/titin.html
