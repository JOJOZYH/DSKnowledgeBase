def read_lines(path):
    with open(path, "r", encoding="utf-8") as f:
        return {line.rstrip() for line in f}

file1 = "./temp_1.txt"
file2 = "./temp_2.txt"

lines1 = read_lines(file1)
lines2 = read_lines(file2)

only_in_file1 = lines1 - lines2
only_in_file2 = lines2 - lines1

print("=== Lines in file1 but NOT in file2 ===")
for line in sorted(only_in_file1):
    print(line)

print("\n=== Lines in file2 but NOT in file1 ===")
for line in sorted(only_in_file2):
    print(line)