# ZGBEQUB

## Function Signature

```fortran
ZGBEQUB(M, N, KL, KU, AB, LDAB, R, C, ROWCND, COLCND,
*                           AMAX, INFO)
```

## Description


 ZGBEQUB computes row and column scalings intended to equilibrate an
 M-by-N matrix A and reduce its condition number.  R returns the row
 scale factors and C the column scale factors, chosen to try to make
 the largest element in each row and column of the matrix B with
 elements B(i,j)=R(i)*A(i,j)*C(j) have an absolute value of at most
 the radix.

 R(i) and C(j) are restricted to be a power of the radix between
 SMLNUM = smallest safe number and BIGNUM = largest safe number.  Use
 of these scaling factors is not guaranteed to reduce the condition
 number of A but works well in practice.

 This routine differs from ZGEEQU by restricting the scaling factors
 to a power of the radix.  Barring over- and underflow, scaling by
 these factors introduces no additional rounding errors.  However, the
 scaled entries' magnitudes are no longer approximately 1 but lie
 between sqrt(radix) and 1/sqrt(radix).

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### KL (in)

KL is INTEGER The number of subdiagonals within the band of A. KL >= 0.

### KU (in)

KU is INTEGER The number of superdiagonals within the band of A. KU >= 0.

### AB (in)

AB is COMPLEX*16 array, dimension (LDAB,N) On entry, the matrix A in band storage, in rows 1 to KL+KU+1. The j-th column of A is stored in the j-th column of the array AB as follows: AB(KU+1+i-j,j) = A(i,j) for max(1,j-KU)<=i<=min(N,j+kl)

### LDAB (in)

LDAB is INTEGER The leading dimension of the array A. LDAB >= max(1,M).

### R (out)

R is DOUBLE PRECISION array, dimension (M) If INFO = 0 or INFO > M, R contains the row scale factors for A.

### C (out)

C is DOUBLE PRECISION array, dimension (N) If INFO = 0, C contains the column scale factors for A.

### ROWCND (out)

ROWCND is DOUBLE PRECISION If INFO = 0 or INFO > M, ROWCND contains the ratio of the smallest R(i) to the largest R(i). If ROWCND >= 0.1 and AMAX is neither too large nor too small, it is not worth scaling by R.

### COLCND (out)

COLCND is DOUBLE PRECISION If INFO = 0, COLCND contains the ratio of the smallest C(i) to the largest C(i). If COLCND >= 0.1, it is not worth scaling by C.

### AMAX (out)

AMAX is DOUBLE PRECISION Absolute value of largest matrix element. If AMAX is very close to overflow or very close to underflow, the matrix should be scaled.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, and i is <= M: the i-th row of A is exactly zero > M: the (i-M)-th column of A is exactly zero

