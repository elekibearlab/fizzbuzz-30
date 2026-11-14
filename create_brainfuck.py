from pathlib import Path
import textwrap

root = Path(__file__).resolve().parent
code = []
pointer = 0
next_cell = 12

def emit(text):
    code.append(text)

def at(cell):
    global pointer
    delta = cell - pointer
    emit('>' * delta if delta >= 0 else '<' * -delta)
    pointer = cell

def clear(cell):
    at(cell)
    emit('[-]')

def add(cell, value):
    at(cell)
    emit('+' * value if value >= 0 else '-' * -value)

def set_value(cell, value):
    clear(cell)
    add(cell, value)

def allocate():
    global next_cell
    cell = next_cell
    next_cell += 1
    return cell

def copy(source, target):
    temporary = allocate()
    clear(target)
    at(source)
    emit('[')
    add(source, -1)
    add(target, 1)
    add(temporary, 1)
    at(source)
    emit(']')
    at(temporary)
    emit('[')
    add(temporary, -1)
    add(source, 1)
    at(temporary)
    emit(']')

def when_nonzero(cell, body):
    gate = allocate()
    copy(cell, gate)
    at(gate)
    emit('[')
    clear(gate)
    body()
    at(gate)
    emit(']')

def when_zero(cell, body):
    gate = allocate()
    set_value(gate, 1)
    when_nonzero(cell, lambda: clear(gate))
    at(gate)
    emit('[')
    add(gate, -1)
    body()
    at(gate)
    emit(']')

def print_text(text):
    clear(11)
    previous = 0
    for letter in text:
        add(11, ord(letter) - previous)
        emit('.')
        previous = ord(letter)
    clear(11)

def print_digit(cell):
    copy(cell, 11)
    add(11, 48)
    emit('.')
    clear(11)

def carry():
    clear(3)
    add(4, 1)

def fizz():
    print_text('Fizz')
    set_value(1, 3)
    clear(10)

def buzz():
    print_text('Buzz')
    set_value(2, 5)
    clear(10)

def number():
    when_nonzero(4, lambda: print_digit(4))
    print_digit(3)

set_value(0, 100)
set_value(1, 3)
set_value(2, 5)
at(0)
emit('[')
add(3, 1)
copy(3, 6)
add(6, -10)
when_zero(6, carry)
set_value(10, 1)
add(1, -1)
when_zero(1, fizz)
add(2, -1)
when_zero(2, buzz)
when_nonzero(10, number)
print_text('\n')
add(0, -1)
emit(']')

source = '\n'.join(textwrap.wrap(''.join(code), 60)) + '\n'
folder = root / 'brainfuck'
folder.mkdir(exist_ok=True)
for version in ('aligned', 'idiomatic'):
    (folder / f'{version}.bf').write_text(
        source, encoding='utf-8', newline='\n'
    )
