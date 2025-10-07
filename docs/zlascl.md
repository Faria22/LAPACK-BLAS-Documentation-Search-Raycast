# ZLASCL

## Function Signature

```fortran
ZLASCL(TYPE, KL, KU, CFROM, CTO, M, N, A, LDA, INFO)
```

## Description


 ZLASCL multiplies the M by N complex matrix A by the real scalar
 CTO/CFROM.  This is done without over/underflow as long as the final
 result CTO*A(I,J)/CFROM does not over/underflow. TYPE specifies that
 A may be full, upper triangular, lower triangular, upper Hessenberg,
 or banded.

## Parameters

### TYPE (in)

TYPE is CHARACTER*1 TYPE indices the storage type of the input matrix. = 'G': A is a full matrix. = 'L': A is a lower triangular matrix. = 'U': A is an upper triangular matrix. = 'H': A is an upper Hessenberg matrix. = 'B': A is a symmetric band matrix with lower bandwidth KL and upper bandwidth KU and with the only the lower half stored. = 'Q': A is a symmetric band matrix with lower bandwidth KL and upper bandwidth KU and with the only the upper half stored. = 'Z': A is a band matrix with lower bandwidth KL and upper bandwidth KU. See ZGBTRF for storage details.

### KL (in)

KL is INTEGER The lower bandwidth of A. Referenced only if TYPE = 'B', 'Q' or 'Z'.

### KU (in)

KU is INTEGER The upper bandwidth of A. Referenced only if TYPE = 'B', 'Q' or 'Z'.

### CFROM (in)

CFROM is DOUBLE PRECISION

### CTO (in)

CTO is DOUBLE PRECISION The matrix A is multiplied by CTO/CFROM. A(I,J) is computed without over/underflow if the final result CTO*A(I,J)/CFROM can be represented without over/underflow. CFROM must be nonzero.

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) The matrix to be multiplied by CTO/CFROM. See TYPE for the storage type.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. If TYPE = 'G', 'L', 'U', 'H', LDA >= max(1,M); TYPE = 'B', LDA >= KL+1; TYPE = 'Q', LDA >= KU+1; TYPE = 'Z', LDA >= 2*KL+KU+1.

### INFO (out)

INFO is INTEGER 0 - successful exit <0 - if INFO = -i, the i-th argument had an illegal value.

