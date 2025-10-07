# DTGEXC

## Function Signature

```fortran
DTGEXC(WANTQ, WANTZ, N, A, LDA, B, LDB, Q, LDQ, Z,
*                          LDZ, IFST, ILST, WORK, LWORK, INFO)
```

## Description


 DTGEXC reorders the generalized real Schur decomposition of a real
 matrix pair (A,B) using an orthogonal equivalence transformation

                (A, B) = Q * (A, B) * Z**T,

 so that the diagonal block of (A, B) with row index IFST is moved
 to row ILST.

 (A, B) must be in generalized real Schur canonical form (as returned
 by DGGES), i.e. A is block upper triangular with 1-by-1 and 2-by-2
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

A is DOUBLE PRECISION array, dimension (LDA,N) On entry, the matrix A in generalized real Schur canonical form. On exit, the updated matrix A, again in generalized real Schur canonical form.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### B (in,out)

B is DOUBLE PRECISION array, dimension (LDB,N) On entry, the matrix B in generalized real Schur canonical form (A,B). On exit, the updated matrix B, again in generalized real Schur canonical form (A,B).

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### Q (in,out)

Q is DOUBLE PRECISION array, dimension (LDQ,N) On entry, if WANTQ = .TRUE., the orthogonal matrix Q. On exit, the updated matrix Q. If WANTQ = .FALSE., Q is not referenced.

### LDQ (in)

LDQ is INTEGER The leading dimension of the array Q. LDQ >= 1. If WANTQ = .TRUE., LDQ >= N.

### Z (in,out)

Z is DOUBLE PRECISION array, dimension (LDZ,N) On entry, if WANTZ = .TRUE., the orthogonal matrix Z. On exit, the updated matrix Z. If WANTZ = .FALSE., Z is not referenced.

### LDZ (in)

LDZ is INTEGER The leading dimension of the array Z. LDZ >= 1. If WANTZ = .TRUE., LDZ >= N.

### IFST (in,out)

IFST is INTEGER

### ILST (in,out)

ILST is INTEGER Specify the reordering of the diagonal blocks of (A, B). The block with row index IFST is moved to row ILST, by a sequence of swapping between adjacent blocks. On exit, if IFST pointed on entry to the second row of a 2-by-2 block, it is changed to point to the first row; ILST always points to the first row of the block in its final position (which may differ from its input value by +1 or -1). 1 <= IFST, ILST <= N.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (MAX(1,LWORK)) On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

### LWORK (in)

LWORK is INTEGER The dimension of the array WORK. LWORK >= 1 when N <= 1, otherwise LWORK >= 4*N + 16. If LWORK = -1, then a workspace query is assumed; the routine only calculates the optimal size of the WORK array, returns this value as the first entry of the WORK array, and no error message related to LWORK is issued by XERBLA.

### INFO (out)

INFO is INTEGER =0: successful exit. <0: if INFO = -i, the i-th argument had an illegal value. =1: The transformed matrix pair (A, B) would be too far from generalized Schur form; the problem is ill- conditioned. (A, B) may have been partially reordered, and ILST points to the first row of the current position of the block being moved.

