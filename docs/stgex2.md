# STGEX2

## Function Signature

```fortran
STGEX2(WANTQ, WANTZ, N, A, LDA, B, LDB, Q, LDQ, Z,
*                          LDZ, J1, N1, N2, WORK, LWORK, INFO)
```

## Description


 STGEX2 swaps adjacent diagonal blocks (A11, B11) and (A22, B22)
 of size 1-by-1 or 2-by-2 in an upper (quasi) triangular matrix pair
 (A, B) by an orthogonal equivalence transformation.

 (A, B) must be in generalized real Schur canonical form (as returned
 by SGGES), i.e. A is block upper triangular with 1-by-1 and 2-by-2
 diagonal blocks. B is upper triangular.

 Optionally, the matrices Q and Z of generalized Schur vectors are
 updated.

        Q(in) * A(in) * Z(in)**T = Q(out) * A(out) * Z(out)**T
        Q(in) * B(in) * Z(in)**T = Q(out) * B(out) * Z(out)**T


## Parameters

### WANTQ (in)

WANTQ is LOGICAL .TRUE. : update the left transformation matrix Q; .FALSE.: do not update Q.

### WANTZ (in)

WANTZ is LOGICAL .TRUE. : update the right transformation matrix Z; .FALSE.: do not update Z.

### N (in)

N is INTEGER The order of the matrices A and B. N >= 0.

### A (in,out)

A is REAL array, dimension (LDA,N) On entry, the matrix A in the pair (A, B). On exit, the updated matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### B (in,out)

B is REAL array, dimension (LDB,N) On entry, the matrix B in the pair (A, B). On exit, the updated matrix B.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### Q (in,out)

Q is REAL array, dimension (LDQ,N) On entry, if WANTQ = .TRUE., the orthogonal matrix Q. On exit, the updated matrix Q. Not referenced if WANTQ = .FALSE..

### LDQ (in)

LDQ is INTEGER The leading dimension of the array Q. LDQ >= 1. If WANTQ = .TRUE., LDQ >= N.

### Z (in,out)

Z is REAL array, dimension (LDZ,N) On entry, if WANTZ =.TRUE., the orthogonal matrix Z. On exit, the updated matrix Z. Not referenced if WANTZ = .FALSE..

### LDZ (in)

LDZ is INTEGER The leading dimension of the array Z. LDZ >= 1. If WANTZ = .TRUE., LDZ >= N.

### J1 (in)

J1 is INTEGER The index to the first block (A11, B11). 1 <= J1 <= N.

### N1 (in)

N1 is INTEGER The order of the first block (A11, B11). N1 = 0, 1 or 2.

### N2 (in)

N2 is INTEGER The order of the second block (A22, B22). N2 = 0, 1 or 2.

### WORK (out)

WORK is REAL array, dimension (MAX(1,LWORK)).

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= MAX( N*(N2+N1), (N2+N1)*(N2+N1)*2 )

### INFO (out)

INFO is INTEGER =0: Successful exit >0: If INFO = 1, the transformed matrix (A, B) would be too far from generalized Schur form; the blocks are not swapped and (A, B) and (Q, Z) are unchanged. The problem of swapping is too ill-conditioned. <0: If INFO = -16: LWORK is too small. Appropriate value for LWORK is returned in WORK(1).

