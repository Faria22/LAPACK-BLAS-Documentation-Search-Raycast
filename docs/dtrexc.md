# DTREXC

## Function Signature

```fortran
DTREXC(COMPQ, N, T, LDT, Q, LDQ, IFST, ILST, WORK,
*                          INFO)
```

## Description


 DTREXC reorders the real Schur factorization of a real matrix
 A = Q*T*Q**T, so that the diagonal block of T with row index IFST is
 moved to row ILST.

 The real Schur form T is reordered by an orthogonal similarity
 transformation Z**T*T*Z, and optionally the matrix Q of Schur vectors
 is updated by postmultiplying it with Z.

 T must be in Schur canonical form (as returned by DHSEQR), that is,
 block upper triangular with 1-by-1 and 2-by-2 diagonal blocks; each
 2-by-2 diagonal block has its diagonal elements equal and its
 off-diagonal elements of opposite sign.

## Parameters

### COMPQ (in)

COMPQ is CHARACTER*1 = 'V': update the matrix Q of Schur vectors; = 'N': do not update Q.

### N (in)

N is INTEGER The order of the matrix T. N >= 0. If N == 0 arguments ILST and IFST may be any value.

### T (in,out)

T is DOUBLE PRECISION array, dimension (LDT,N) On entry, the upper quasi-triangular matrix T, in Schur Schur canonical form. On exit, the reordered upper quasi-triangular matrix, again in Schur canonical form.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= max(1,N).

### Q (in,out)

Q is DOUBLE PRECISION array, dimension (LDQ,N) On entry, if COMPQ = 'V', the matrix Q of Schur vectors. On exit, if COMPQ = 'V', Q has been postmultiplied by the orthogonal transformation matrix Z which reorders T. If COMPQ = 'N', Q is not referenced.

### LDQ (in)

LDQ is INTEGER The leading dimension of the array Q. LDQ >= 1, and if COMPQ = 'V', LDQ >= max(1,N).

### IFST (in,out)

IFST is INTEGER

### ILST (in,out)

ILST is INTEGER Specify the reordering of the diagonal blocks of T. The block with row index IFST is moved to row ILST, by a sequence of transpositions between adjacent blocks. On exit, if IFST pointed on entry to the second row of a 2-by-2 block, it is changed to point to the first row; ILST always points to the first row of the block in its final position (which may differ from its input value by +1 or -1). 1 <= IFST <= N; 1 <= ILST <= N.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value = 1: two adjacent blocks were too close to swap (the problem is very ill-conditioned); T may have been partially reordered, and ILST points to the first row of the current position of the block being moved.

