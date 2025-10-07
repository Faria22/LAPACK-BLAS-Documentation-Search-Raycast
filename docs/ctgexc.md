# CTGEXC

## Function Signature

```fortran
CTGEXC(WANTQ, WANTZ, N, A, LDA, B, LDB, Q, LDQ, Z,
*                          LDZ, IFST, ILST, INFO)
```

## Description


 CTGEXC reorders the generalized Schur decomposition of a complex
 matrix pair (A,B), using an unitary equivalence transformation
 (A, B) := Q * (A, B) * Z**H, so that the diagonal block of (A, B) with
 row index IFST is moved to row ILST.

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

A is COMPLEX array, dimension (LDA,N) On entry, the upper triangular matrix A in the pair (A, B). On exit, the updated matrix A.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### B (in,out)

B is COMPLEX array, dimension (LDB,N) On entry, the upper triangular matrix B in the pair (A, B). On exit, the updated matrix B.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### Q (in,out)

Q is COMPLEX array, dimension (LDQ,N) On entry, if WANTQ = .TRUE., the unitary matrix Q. On exit, the updated matrix Q. If WANTQ = .FALSE., Q is not referenced.

### LDQ (in)

LDQ is INTEGER The leading dimension of the array Q. LDQ >= 1; If WANTQ = .TRUE., LDQ >= N.

### Z (in,out)

Z is COMPLEX array, dimension (LDZ,N) On entry, if WANTZ = .TRUE., the unitary matrix Z. On exit, the updated matrix Z. If WANTZ = .FALSE., Z is not referenced.

### LDZ (in)

LDZ is INTEGER The leading dimension of the array Z. LDZ >= 1; If WANTZ = .TRUE., LDZ >= N.

### IFST (in)

IFST is INTEGER

### ILST (in,out)

ILST is INTEGER Specify the reordering of the diagonal blocks of (A, B). The block with row index IFST is moved to row ILST, by a sequence of swapping between adjacent blocks.

### INFO (out)

INFO is INTEGER =0: Successful exit. <0: if INFO = -i, the i-th argument had an illegal value. =1: The transformed matrix pair (A, B) would be too far from generalized Schur form; the problem is ill- conditioned. (A, B) may have been partially reordered, and ILST points to the first row of the current position of the block being moved.

