dwarves = [int(input()) for _ in range(9)]

mod = sum(dwarves) - 100

def not_my_dwarf_index(dwarves):
	for i, dwarf in enumerate(dwarves):
		for j, d in enumerate(dwarves):
			if i != j and d < mod:
				if dwarf + d == mod:
					return dwarf, d

a, b = not_my_dwarf_index(dwarves)

dwarves.remove(a)
dwarves.remove(b)
dwarves.sort()

for dwarf in dwarves:
	print(dwarf)