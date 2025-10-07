# ZTGEX2

## Function Signature

```fortran
ZTGEX2(WANTQ, WANTZ, N, A, LDA, B, LDB, Q, LDQ, Z,
*                          LDZ, J1, INFO)
```

## Description


 ZTGEX2 swaps adjacent diagonal 1 by 1 blocks (A11,B11) and (A22,B22)
 in an upper triangular matrix pair (A, B) by an unitary equivalence
 transformation.

 (A, B) must be in generalized Schur canonical form, that is, A and
 B are both upper triangular.

 Optionally, the matrices Q and Z of generalized Schur vectors are
 updated.

        Q(in) * A(in) * Z(in)**H = Q(out) * A(out) * Z(out)**H
        Q(in) * B(in) * Z(in)**H = Q(out) * B(out) * Z(out)**H


## Parameters

### WANTQ (in)

WANTQ is LOGICAL .TRUE. : update the left transformation matrix Q; .FALSE.: do not update Q.

### WANTZ (in)

WANTZ is LOGICAL .TRUE. : update the right transformation matrix Z; .FALSE.: do not update Z.

### N (in)

N is INTEGER The order of the matrices A and B. N >= 0.

### A (in,out)

A is COMPLEX*16 array, dimensions (LDA,N) On entry, the matrix A in the pair (A, B). On exit, the updated matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### B (in,out)

B is COMPLEX*16 array, dimensions (LDB,N) On entry, the matrix B in the pair (A, B). On exit, the updated matrix B.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### Q (in,out)

Q is COMPLEX*16 array, dimension (LDQ,N) If WANTQ = .TRUE, on entry, the unitary matrix Q. On exit, the updated matrix Q. Not referenced if WANTQ = .FALSE..

### LDQ (in)

LDQ is INTEGER The leading dimension of the array Q. LDQ >= 1; If WANTQ = .TRUE., LDQ >= N.

### Z (in,out)

Z is COMPLEX*16 array, dimension (LDZ,N) If WANTZ = .TRUE, on entry, the unitary matrix Z. On exit, the updated matrix Z. Not referenced if WANTZ = .FALSE..

### LDZ (in)

LDZ is INTEGER The leading dimension of the array Z. LDZ >= 1; If WANTZ = .TRUE., LDZ >= N.

### J1 (in)

J1 is INTEGER The index to the first block (A11, B11).

### INFO (out)

INFO is INTEGER =0: Successful exit. =1: The transformed matrix pair (A, B) would be too far from generalized Schur form; the problem is ill- conditioned.

