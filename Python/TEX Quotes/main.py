import sys

def solve_uva272():
    quote_count = 0
    for line in sys.stdin:
        result_line = []
        for char in line:
            if char == '"':
                if quote_count % 2 == 0:
                    result_line.append("``")
                else:
                    result_line.append("''")
                quote_count += 1
            else:
                result_line.append(char)
        sys.stdout.write("".join(result_line))

if __name__ == '__main__':
    solve_uva272()