# ZLAQHB

## Function Signature

```fortran
ZLAQHB(UPLO, N, KD, AB, LDAB, S, SCOND, AMAX, EQUED)
```

## Description


 ZLAQHB equilibrates a Hermitian band matrix A
 using the scaling factors in the vector S.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the upper or lower triangular part of the symmetric matrix A is stored. = 'U': Upper triangular = 'L': Lower triangular

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### KD (in)

KD is INTEGER The number of super-diagonals of the matrix A if UPLO = 'U', or the number of sub-diagonals if UPLO = 'L'. KD >= 0.

### AB (in,out)

AB is COMPLEX*16 array, dimension (LDAB,N) On entry, the upper or lower triangle of the symmetric band matrix A, stored in the first KD+1 rows of the array. The j-th column of A is stored in the j-th column of the array AB as follows: if UPLO = 'U', AB(kd+1+i-j,j) = A(i,j) for max(1,j-kd)<=i<=j; if UPLO = 'L', AB(1+i-j,j) = A(i,j) for j<=i<=min(n,j+kd). On exit, if INFO = 0, the triangular factor U or L from the Cholesky factorization A = U**H *U or A = L*L**H of the band matrix A, in the same storage format as A.

### LDAB (in)

LDAB is INTEGER The leading dimension of the array AB. LDAB >= KD+1.

### S (out)

S is DOUBLE PRECISION array, dimension (N) The scale factors for A.

### SCOND (in)

SCOND is DOUBLE PRECISION Ratio of the smallest S(i) to the largest S(i).

### AMAX (in)

AMAX is DOUBLE PRECISION Absolute value of largest matrix entry.

### EQUED (out)

EQUED is CHARACTER*1 Specifies whether or not equilibration was done. = 'N': No equilibration. = 'Y': Equilibration was done, i.e., A has been replaced by diag(S) * A * diag(S).

