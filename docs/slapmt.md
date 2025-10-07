# SLAPMT

## Function Signature

```fortran
SLAPMT(FORWRD, M, N, X, LDX, K)
```

## Description


 SLAPMT rearranges the columns of the M by N matrix X as specified
 by the permutation K(1),K(2),...,K(N) of the integers 1,...,N.
 If FORWRD = .TRUE.,  forward permutation:

      X(*,K(J)) is moved X(*,J) for J = 1,2,...,N.

 If FORWRD = .FALSE., backward permutation:

      X(*,J) is moved to X(*,K(J)) for J = 1,2,...,N.

## Parameters

### FORWRD (in)

FORWRD is LOGICAL = .TRUE., forward permutation = .FALSE., backward permutation

### M (in)

M is INTEGER The number of rows of the matrix X. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix X. N >= 0.

### X (in,out)

X is REAL array, dimension (LDX,N) On entry, the M by N matrix X. On exit, X contains the permuted matrix X.

### LDX (in)

LDX is INTEGER The leading dimension of the array X, LDX >= MAX(1,M).

### K (in,out)

K is INTEGER array, dimension (N) On entry, K contains the permutation vector. K is used as internal workspace, but reset to its original value on output.

