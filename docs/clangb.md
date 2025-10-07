# CLANGB

## Function Signature

```fortran
CLANGB(NORM, N, KL, KU, AB, LDAB,
*                        WORK)
```

## Description


 CLANGB  returns the value of the one norm,  or the Frobenius norm, or
 the  infinity norm,  or the element of  largest absolute value  of an
 n by n band matrix  A,  with kl sub-diagonals and ku super-diagonals.

## Parameters

### NORM (in)

NORM is CHARACTER*1 Specifies the value to be returned in CLANGB as described above.

### N (in)

N is INTEGER The order of the matrix A. N >= 0. When N = 0, CLANGB is set to zero.

### KL (in)

KL is INTEGER The number of sub-diagonals of the matrix A. KL >= 0.

### KU (in)

KU is INTEGER The number of super-diagonals of the matrix A. KU >= 0.

### AB (in)

AB is COMPLEX array, dimension (LDAB,N) The band matrix A, stored in rows 1 to KL+KU+1. The j-th column of A is stored in the j-th column of the array AB as follows: AB(ku+1+i-j,j) = A(i,j) for max(1,j-ku)<=i<=min(n,j+kl).

### LDAB (in)

LDAB is INTEGER The leading dimension of the array AB. LDAB >= KL+KU+1.

### WORK (out)

WORK is REAL array, dimension (MAX(1,LWORK)), where LWORK >= N when NORM = 'I'; otherwise, WORK is not referenced.

