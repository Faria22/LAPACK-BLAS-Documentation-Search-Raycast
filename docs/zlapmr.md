# ZLAPMR

## Function Signature

```fortran
ZLAPMR(FORWRD, M, N, X, LDX, K)
```

## Description


 ZLAPMR rearranges the rows of the M by N matrix X as specified
 by the permutation K(1),K(2),...,K(M) of the integers 1,...,M.
 If FORWRD = .TRUE.,  forward permutation:

      X(K(I),*) is moved X(I,*) for I = 1,2,...,M.

 If FORWRD = .FALSE., backward permutation:

      X(I,*) is moved to X(K(I),*) for I = 1,2,...,M.

## Parameters

### FORWRD (in)

FORWRD is LOGICAL = .TRUE., forward permutation = .FALSE., backward permutation

### M (in)

M is INTEGER The number of rows of the matrix X. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix X. N >= 0.

### X (in,out)

X is COMPLEX*16 array, dimension (LDX,N) On entry, the M by N matrix X. On exit, X contains the permuted matrix X.

### LDX (in)

LDX is INTEGER The leading dimension of the array X, LDX >= MAX(1,M).

### K (in,out)

K is INTEGER array, dimension (M) On entry, K contains the permutation vector. K is used as internal workspace, but reset to its original value on output.

