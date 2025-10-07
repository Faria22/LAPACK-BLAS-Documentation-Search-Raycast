#!/usr/bin/env python3
"""
Parse LAPACK/BLAS Fortran source files and generate markdown documentation.
"""
import os
import re
from pathlib import Path
from typing import Dict, List, Optional

def extract_routine_name(filepath: Path) -> str:
    """Extract the routine name from the filepath."""
    return filepath.stem

def parse_fortran_file(filepath: Path) -> Optional[Dict]:
    """Parse a Fortran file and extract documentation."""
    try:
        with open(filepath, 'r', encoding='latin-1') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return None
    
    # Extract the brief description
    brief_match = re.search(r'\*>\s*\\brief\s*<b>(.*?)</b>', content, re.IGNORECASE)
    brief = brief_match.group(1).strip() if brief_match else ""
    
    # Extract the function signature
    signature_match = re.search(r'SUBROUTINE\s+(\w+)\s*\((.*?)\)', content, re.IGNORECASE | re.DOTALL)
    if not signature_match:
        # Try FUNCTION instead
        signature_match = re.search(r'FUNCTION\s+(\w+)\s*\((.*?)\)', content, re.IGNORECASE | re.DOTALL)
    
    if not signature_match:
        return None
    
    routine_name = signature_match.group(1).strip()
    params_str = signature_match.group(2).strip()
    
    # Extract purpose/description
    purpose_match = re.search(r'\*>\s*\\par\s+Purpose:.*?\*>\s*\\verbatim\s*(.*?)\*>\s*\\endverbatim', 
                             content, re.IGNORECASE | re.DOTALL)
    purpose = purpose_match.group(1).strip() if purpose_match else ""
    purpose = re.sub(r'\*>', '', purpose)  # Remove Doxygen markers
    purpose = re.sub(r'^\s*\*\s*', '', purpose, flags=re.MULTILINE)  # Remove leading * from lines
    
    # Extract arguments section
    args_section = re.search(r'\*\s*Arguments:\s*\*\s*=+\s*(.*?)(?=\*\s*Authors:|\*\s*  ={50,})', 
                            content, re.IGNORECASE | re.DOTALL)
    
    parameters = []
    if args_section:
        args_text = args_section.group(1)
        # Find all parameter blocks
        param_blocks = re.finditer(
            r'\*>\s*\\param\[(.*?)\]\s+(\w+)\s*\*>\s*\\verbatim\s*(.*?)\*>\s*\\endverbatim',
            args_text, re.DOTALL | re.IGNORECASE
        )
        
        for param_match in param_blocks:
            param_type = param_match.group(1).strip()  # in, out, in/out
            param_name = param_match.group(2).strip()
            param_desc = param_match.group(3).strip()
            param_desc = re.sub(r'\*>', '', param_desc)
            param_desc = re.sub(r'^\s*\*\s*', '', param_desc, flags=re.MULTILINE)
            param_desc = ' '.join(param_desc.split())
            
            parameters.append({
                'name': param_name,
                'type': param_type,
                'description': param_desc
            })
    
    return {
        'name': routine_name,
        'brief': brief,
        'signature': f"{routine_name}({params_str})",
        'purpose': purpose,
        'parameters': parameters
    }

def generate_markdown(routine_info: Dict) -> str:
    """Generate markdown documentation from parsed routine info."""
    md = f"# {routine_info['name']}\n\n"
    
    if routine_info['brief']:
        md += f"{routine_info['brief']}\n\n"
    
    md += f"## Function Signature\n\n"
    md += f"```fortran\n{routine_info['signature']}\n```\n\n"
    
    if routine_info['purpose']:
        md += f"## Description\n\n"
        md += f"{routine_info['purpose']}\n\n"
    
    if routine_info['parameters']:
        md += f"## Parameters\n\n"
        for param in routine_info['parameters']:
            md += f"### {param['name']} ({param['type']})\n\n"
            md += f"{param['description']}\n\n"
    
    return md

def process_lapack_sources(src_dir: Path, output_dir: Path):
    """Process all LAPACK source files and generate markdown documentation."""
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Find all Fortran files
    fortran_files = list(src_dir.glob('*.f'))
    
    print(f"Found {len(fortran_files)} Fortran files")
    
    processed = 0
    for filepath in fortran_files:
        routine_info = parse_fortran_file(filepath)
        
        if routine_info:
            md_content = generate_markdown(routine_info)
            output_file = output_dir / f"{routine_info['name'].lower()}.md"
            
            with open(output_file, 'w', encoding='utf-8') as f:
                f.write(md_content)
            
            processed += 1
            if processed % 100 == 0:
                print(f"Processed {processed} files...")
    
    print(f"\nSuccessfully processed {processed} routines")
    print(f"Generated markdown files in {output_dir}")

if __name__ == "__main__":
    base_dir = Path("/tmp/lapack-scraper/lapack")
    output_dir = Path("/home/runner/work/LAPACK-BLAS-Documentation-Search-Raycast/LAPACK-BLAS-Documentation-Search-Raycast/docs")
    
    # Process LAPACK routines
    lapack_src = base_dir / "SRC"
    if lapack_src.exists():
        print("Processing LAPACK routines...")
        process_lapack_sources(lapack_src, output_dir)
    else:
        print(f"Error: LAPACK source directory not found at {lapack_src}")
    
    # Process BLAS routines
    blas_src = base_dir / "BLAS" / "SRC"
    if blas_src.exists():
        print("\nProcessing BLAS routines...")
        process_lapack_sources(blas_src, output_dir)
    else:
        print(f"Warning: BLAS source directory not found at {blas_src}")
