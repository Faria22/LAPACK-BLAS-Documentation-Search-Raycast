# CSYEQUB

## Function Signature

```fortran
CSYEQUB(UPLO, N, A, LDA, S, SCOND, AMAX, WORK, INFO)
```

## Description


 CSYEQUB computes row and column scalings intended to equilibrate a
 symmetric matrix A (with respect to the Euclidean norm) and reduce
 its condition number. The scale factors S are computed by the BIN
 algorithm (see references) so that the scaled matrix B with elements
 B(i,j) = S(i)*A(i,j)*S(j) has a condition number within a factor N of
 the smallest possible condition number over all possible diagonal
 scalings.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### A (in)

A is COMPLEX array, dimension (LDA,N) The N-by-N symmetric matrix whose scaling factors are to be computed.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### S (out)

S is REAL array, dimension (N) If INFO = 0, S contains the scale factors for A.

### SCOND (out)

SCOND is REAL If INFO = 0, S contains the ratio of the smallest S(i) to the largest S(i). If SCOND >= 0.1 and AMAX is neither too large nor too small, it is not worth scaling by S.

### AMAX (out)

AMAX is REAL Largest absolute value of any matrix element. If AMAX is very close to overflow or very close to underflow, the matrix should be scaled.

### WORK (out)

WORK is COMPLEX array, dimension (2*N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, the i-th diagonal element is nonpositive.

