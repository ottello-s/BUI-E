import math

def hochdrei(x):
    return x*x*x

querschnitte = [
[10, 20],
[80, 120],
[100, 160],
[200, 300]
]

def I(höhe=1,breite=1):
    # h**3
    return (breite*hochdrei(höhe))/12, (höhe*hochdrei(breite))/12 

for qs in querschnitte:
    I_x, I_y = I(*qs)
    print(I_x)


%scope glob
%score funk

def globallocal():
    global x
    print(x)
    x = 6

% scope funk
x = 5
globallocal()
print(x)
%scope glob

%%%%%
def decorator(func)
    def wrapper()
        %%%%%%%%%%%%%%%%%%%%%%
        func()
        %%%%%%%%%%%%%%%%%%%%%%
    return wrapper


%%%%


def decorator(func)
    def wrapper()
        print("Hello User")
        func()
    return wrapper


@decorator
def login():


@decorator
def logout():
