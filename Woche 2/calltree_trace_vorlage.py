"""Vorlage: Aufrufbaum mit einem Dekorator automatisch ausgeben.

Ergänzen Sie die Funktion wrapper() so, dass beim Aufruf von g(2, 3) folgende Ausgabe entsteht:

g(2, 3)
├─ f(2)
│  ├─ inc(2)
│  │  ├─ add(2, 1)
│  │  │  └─ → 3
│  │  └─ → 3
│  ├─ double(3)
│  │  ├─ add(3, 3)
│  │  │  └─ → 6
│  │  └─ → 6
│  └─ → 6
├─ f(3)
│  ├─ inc(3)
│  │  ├─ add(3, 1)
│  │  │  └─ → 4
│  │  └─ → 4
│  ├─ double(4)
│  │  ├─ add(4, 4)
│  │  │  └─ → 8
│  │  └─ → 8
│  └─ → 8
├─ add(6, 8)
│  └─ → 14
└─ → 14
"""

import functools

# Sonderzeichen für die Baumdarstellung
ZWEIG = "├─ "  # vor jedem Aufruf außer dem ersten
LINIE = "│  "  # einmal pro Ebene zum Einrücken
ENDE = "└─ "  # vor dem Ergebnis eines Aufrufs
PFEIL = "→ "  # vor dem Ergebnis

depth = 0  # aktuelle Aufruftiefe: 0 für g, 1 für f, ...


def trace(fn):
    @functools.wraps(fn)
    def wrapper(*args):
        global depth
        aufruf = f"{fn.__name__}({', '.join(map(repr, args))})"  # z.B. "add(2, 1)"

        # TODO 1: Aufrufzeile ausgeben, je nach depth mit LINIE und ZWEIG davor.
        prefix = LINIE * (depth - 1) + ZWEIG if depth > 0 else ""
        

        # TODO 2: depth vor dem Aufruf erhöhen und danach wieder verringern.
        result = fn(*args)

        # TODO 3: Ergebnis in einer eigenen Zeile ausgeben, eingerückt mit LINIE
        #         und mit ENDE und PFEIL davor.
        print(f"{args}")
        return result

    return wrapper


@trace
def add(a, b):
    return a + b


@trace
def double(x):
    return add(x, x)


@trace
def inc(x):
    return add(x, 1)


@trace
def f(x):
    return double(inc(x))


@trace
def g(x, y):
    return add(f(x), f(y))


print(g(2, 3))
