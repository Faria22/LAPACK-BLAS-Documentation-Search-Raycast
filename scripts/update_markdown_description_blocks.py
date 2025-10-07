from pathlib import Path

root_dir = Path(__file__).parent.parent

docs_dir = root_dir / 'assets' / 'docs'

for md_file in docs_dir.iterdir():
    with md_file.open('r', encoding='utf-8') as f:
        lines = f.readlines()

    new_lines = []
    for line in lines:
        new_line = line.strip() + '  \n'
        if not line.startswith('>'):
            new_lines.append(new_line)
            continue
        if '*' not in line:
            new_lines.append(new_line)
            continue

        new_line = new_line.replace('*', r'\*')

    with md_file.open('w', encoding='utf-8') as f:
        f.writelines(new_lines)
