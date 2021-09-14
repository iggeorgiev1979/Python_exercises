from collections import deque


def add(seq: set, new_seq: set):
    seq.update(new_seq)
    return seq


def remove(seq: set, new_seq: set):
    return seq - new_seq


def check_subset(first_seq, second_seq):
    if first_seq <= second_seq:
        return True
    if second_seq <= first_seq:
        return True
    return False


first_sequence = set(int(el) for el in input().split())
second_sequence = set(int(el) for el in input().split())
n = int(input())
for _ in range(n):
    command = deque(input().split())
    tmp = command.popleft()
    if tmp == 'Add':
        tmp = command.popleft()
        if tmp == 'First':
            first_sequence = add(first_sequence, set(int(el) for el in command))
        elif tmp == 'Second':
            second_sequence = add(second_sequence, set(int(el) for el in command))
    elif tmp == 'Remove':
        tmp = command.popleft()
        if tmp == 'First':
            first_sequence = remove(first_sequence, set(int(el) for el in command))
        elif tmp == 'Second':
            second_sequence = remove(second_sequence, set(int(el) for el in command))
    elif tmp == 'Check':
        print(check_subset(first_sequence, second_sequence))
print(*sorted(first_sequence), sep=', ')
print(*sorted(second_sequence), sep=', ')
