# PRD: nusnetID2021

## Overview
A Python script that generates all mathematically valid NUS (National University of Singapore) matriculation ID numbers by applying the official checksum algorithm. Produces two exhaustive lists: one for A-prefix IDs and one for U-prefix IDs. Useful for research into ID format structure, not for any form of impersonation.

## Goals
- Implement the NUS matric number checksum algorithm in Python (ported from official JS)
- Generate all valid A-prefix IDs (A0000001 through A9999999)
- Generate all valid U-prefix IDs (U0000001 through U9999999)
- Write results to `nusnetidA.txt` and `nusnetidU.txt`

## Non-Goals
- Looking up or verifying real student records
- Any form of authentication bypass or impersonation
- Network requests or database access
- Web UI or API

## User Stories
- As a security researcher, I want to understand the NUS ID format and verify the checksum algorithm is implemented correctly.
- As a developer, I want a complete list of valid ID formats for testing an NUS-ID validation function.

## Tech Stack
- **Language**: Python 3.x
- **Libraries**: `js2py` (pip) — used to evaluate the original JavaScript checksum function

## Architecture
```
nusnetID2021/
├── generate.py       # main script
├── nusnetidA.txt     # output: all valid A-prefix IDs
└── nusnetidU.txt     # output: all valid U-prefix IDs
```

**Algorithm (embedded JS via js2py):**
- Match `A{7digits}` or `U{6-7digits}` prefix
- For U-prefix 8-char IDs: discard 3rd digit
- Apply weighted sum over last 6 digits
- Map `sum % 13` to checksum character from `'YXWURNMLJHEAB'`
- Append checksum to form full matric number (e.g., `A0171424M`)

## Features (detailed)

### A-prefix Generation
- Iterates `num` from 1 to 9,999,999
- Formats as `A{num:07d}` (zero-padded 7 digits)
- Computes checksum via `calculateNUSMatricNumber()`
- Appends result to `nusnetidA.txt`

### U-prefix Generation
- Same loop for `U{num:07d}`
- Algorithm discards 3rd digit for 8-char U IDs before checksum
- Appends to `nusnetidU.txt`

## Data / Config
| File | Description |
|------|-------------|
| `nusnetidA.txt` | ~10 million A-prefix IDs, one per line |
| `nusnetidU.txt` | ~10 million U-prefix IDs, one per line |

No config needed — all parameters hardcoded.

## Deployment / Run
```bash
pip install js2py
python generate.py
# WARNING: generates ~20 million lines across two files
# Each file will be several hundred MB
```

## Constraints & Notes
- **Output size**: ~10M lines × ~10 chars = ~100MB per file; ensure sufficient disk space
- **Runtime**: sequential generation; expect 10–30 minutes for full run
- **Legal**: generating the list itself is not illegal; using IDs to impersonate is
- **Accuracy**: checksum algorithm ported from official NUS JavaScript — output matches real ID format
- **Educational**: this demonstrates that sequential numeric ID schemes with simple checksums are enumerable
