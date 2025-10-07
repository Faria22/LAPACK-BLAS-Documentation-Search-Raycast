# SLARFB_GETT

## Function Signature

```fortran
SLARFB_GETT(IDENT, M, N, K, T, LDT, A, LDA, B, LDB,
*      $                        WORK, LDWORK)
```

## Description


 SLARFB_GETT applies a real Householder block reflector H from the
 left to a real (K+M)-by-N  "triangular-pentagonal" matrix
 composed of two block matrices: an upper trapezoidal K-by-N matrix A
 stored in the array A, and a rectangular M-by-(N-K) matrix B, stored
 in the array B. The block reflector H is stored in a compact
 WY-representation, where the elementary reflectors are in the
 arrays A, B and T. See Further Details section.

## Parameters

### IDENT (in)

IDENT is CHARACTER*1 If IDENT = not 'I', or not 'i', then V1 is unit lower-triangular and stored in the left K-by-K block of the input matrix A, If IDENT = 'I' or 'i', then V1 is an identity matrix and not stored. See Further Details section.

### M (in)

M is INTEGER The number of rows of the matrix B. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrices A and B. N >= 0.

### K (in)

K is INTEGER The number or rows of the matrix A. K is also order of the matrix T, i.e. the number of elementary reflectors whose product defines the block reflector. 0 <= K <= N.

### T (in)

T is REAL array, dimension (LDT,K) The upper-triangular K-by-K matrix T in the representation of the block reflector.

### LDT (in)

LDT is INTEGER The leading dimension of the array T. LDT >= K.

### A (in,out)

A is REAL array, dimension (LDA,N) On entry: a) In the K-by-N upper-trapezoidal part A: input matrix A. b) In the columns below the diagonal: columns of V1 (ones are not stored on the diagonal). On exit: A is overwritten by rectangular K-by-N product H*A. See Further Details section.

### LDA (in)

LDB is INTEGER The leading dimension of the array A. LDA >= max(1,K).

### B (in,out)

B is REAL array, dimension (LDB,N) On entry: a) In the M-by-(N-K) right block: input matrix B. b) In the M-by-N left block: columns of V2. On exit: B is overwritten by rectangular M-by-N product H*B. See Further Details section.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,M).

### WORK (out)

WORK is REAL array, dimension (LDWORK,max(K,N-K))

### LDWORK (in)

LDWORK is INTEGER The leading dimension of the array WORK. LDWORK>=max(1,K).

