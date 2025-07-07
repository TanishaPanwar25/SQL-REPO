def split_insert_file(input_file, output_file, bucket_size=5):
    with open(input_file, 'r') as infile:
        lines = infile.readlines()

    # Identify the insert header and value lines
    insert_header = ''
    value_lines = []

    for line in lines:
        stripped = line.strip()
        if stripped.upper().startswith('INSERT INTO'):
            insert_header = line.strip()
        elif stripped.endswith(',') or stripped.endswith(');') or stripped.endswith(')'):
            value_lines.append(stripped.rstrip(',;'))  # Remove ending comma or semicolon

    # Now write into output file in chunks
    with open(output_file, 'w') as outfile:
        for i in range(0, len(value_lines), bucket_size):
            chunk = value_lines[i:i+bucket_size]
            outfile.write(insert_header + "\nVALUES\n")
            for j, value in enumerate(chunk):
                ending = ',' if j < len(chunk) - 1 else ';'
                outfile.write(f"  {value}{ending}\n")
            outfile.write("\n")  # For separation between chunks

    print(f"✅ Done! Output written to {output_file}")

# Usage
split_insert_file("D:/QT/input.txt", "D:/QT/output.txt", bucket_size=900)

