# CLARFY

## Function Signature

```fortran
CLARFY(UPLO, N, V, INCV, TAU, C, LDC, WORK)
```

## Description


 CLARFY applies an elementary reflector, or Householder matrix, H,
 to an n x n Hermitian matrix C, from both the left and the right.

 H is represented in the form

    H = I - tau * v * v'

 where  tau  is a scalar and  v  is a vector.

 If  tau  is  zero, then  H  is taken to be the unit matrix.

## Parameters

### UPLO (in)

UPLO is CHARACTER*1 Specifies whether the upper or lower triangular part of the Hermitian matrix C is stored. = 'U': Upper triangle = 'L': Lower triangle

### N (in)

N is INTEGER The number of rows and columns of the matrix C. N >= 0.

### V (in)

V is COMPLEX array, dimension (1 + (N-1)*abs(INCV)) The vector v as described above.

### INCV (in)

INCV is INTEGER The increment between successive elements of v. INCV must not be zero.

### TAU (in)

TAU is COMPLEX The value tau as described above.

### C (in,out)

C is COMPLEX array, dimension (LDC, N) On entry, the matrix C. On exit, C is overwritten by H * C * H'.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max( 1, N ).

### WORK (out)

WORK is COMPLEX array, dimension (N)

