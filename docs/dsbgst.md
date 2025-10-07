# DSBGST

## Function Signature

```fortran
DSBGST(VECT, UPLO, N, KA, KB, AB, LDAB, BB, LDBB, X,
*                          LDX, WORK, INFO)
```

## Description


 DSBGST reduces a real symmetric-definite banded generalized
 eigenproblem  A*x = lambda*B*x  to standard form  C*y = lambda*y,
 such that C has the same bandwidth as A.

 B must have been previously factorized as S**T*S by DPBSTF, using a
 split Cholesky factorization. A is overwritten by C = X**T*A*X, where
 X = S**(-1)*Q and Q is an orthogonal matrix chosen to preserve the
 bandwidth of A.

## Parameters

### VECT (in)

VECT is CHARACTER*1 = 'N': do not form the transformation matrix X; = 'V': form X.

### UPLO (in)

UPLO is CHARACTER*1 = 'U': Upper triangle of A is stored; = 'L': Lower triangle of A is stored.

### N (in)

N is INTEGER The order of the matrices A and B. N >= 0.

### KA (in)

KA is INTEGER The number of superdiagonals of the matrix A if UPLO = 'U', or the number of subdiagonals if UPLO = 'L'. KA >= 0.

### KB (in)

KB is INTEGER The number of superdiagonals of the matrix B if UPLO = 'U', or the number of subdiagonals if UPLO = 'L'. KA >= KB >= 0.

### AB (in,out)

AB is DOUBLE PRECISION array, dimension (LDAB,N) On entry, the upper or lower triangle of the symmetric band matrix A, stored in the first ka+1 rows of the array. The j-th column of A is stored in the j-th column of the array AB as follows: if UPLO = 'U', AB(ka+1+i-j,j) = A(i,j) for max(1,j-ka)<=i<=j; if UPLO = 'L', AB(1+i-j,j) = A(i,j) for j<=i<=min(n,j+ka). On exit, the transformed matrix X**T*A*X, stored in the same format as A.

### LDAB (in)

LDAB is INTEGER The leading dimension of the array AB. LDAB >= KA+1.

### BB (in)

BB is DOUBLE PRECISION array, dimension (LDBB,N) The banded factor S from the split Cholesky factorization of B, as returned by DPBSTF, stored in the first KB+1 rows of the array.

### LDBB (in)

LDBB is INTEGER The leading dimension of the array BB. LDBB >= KB+1.

### X (out)

X is DOUBLE PRECISION array, dimension (LDX,N) If VECT = 'V', the n-by-n matrix X. If VECT = 'N', the array X is not referenced.

### LDX (in)

LDX is INTEGER The leading dimension of the array X. LDX >= max(1,N) if VECT = 'V'; LDX >= 1 otherwise.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (2*N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value.

