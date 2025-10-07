# LAPACK/BLAS Documentation Search

Quickly search through official LAPACK/BLAS documentation

## Documentation

This extension provides searchable markdown files for 2,185+ LAPACK and BLAS routines, including:
- Function signatures
- Detailed descriptions
- Parameter documentation

## Generating Documentation

The markdown documentation files are generated from the official LAPACK source code using the `scripts/parse_lapack.py` script:

```bash
# Install dependencies (requires Python 3)
pip install -r requirements.txt

# Run the scraper (requires cloning the LAPACK repository first)
cd /tmp
git clone --depth 1 https://github.com/Reference-LAPACK/lapack.git
cd /path/to/this/repo
python3 scripts/parse_lapack.py
```

The script extracts Doxygen-formatted documentation from Fortran source files and generates markdown files in the `docs/` directory.