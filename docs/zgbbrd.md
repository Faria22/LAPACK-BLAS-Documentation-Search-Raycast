# ZGBBRD

## Function Signature

```fortran
ZGBBRD(VECT, M, N, NCC, KL, KU, AB, LDAB, D, E, Q,
*                          LDQ, PT, LDPT, C, LDC, WORK, RWORK, INFO)
```

## Description


 ZGBBRD reduces a complex general m-by-n band matrix A to real upper
 bidiagonal form B by a unitary transformation: Q**H * A * P = B.

 The routine computes B, and optionally forms Q or P**H, or computes
 Q**H*C for a given matrix C.

## Parameters

### VECT (in)

VECT is CHARACTER*1 Specifies whether or not the matrices Q and P**H are to be formed. = 'N': do not form Q or P**H; = 'Q': form Q only; = 'P': form P**H only; = 'B': form both.

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### NCC (in)

NCC is INTEGER The number of columns of the matrix C. NCC >= 0.

### KL (in)

KL is INTEGER The number of subdiagonals of the matrix A. KL >= 0.

### KU (in)

KU is INTEGER The number of superdiagonals of the matrix A. KU >= 0.

### AB (in,out)

AB is COMPLEX*16 array, dimension (LDAB,N) On entry, the m-by-n band matrix A, stored in rows 1 to KL+KU+1. The j-th column of A is stored in the j-th column of the array AB as follows: AB(ku+1+i-j,j) = A(i,j) for max(1,j-ku)<=i<=min(m,j+kl). On exit, A is overwritten by values generated during the reduction.

### LDAB (in)

LDAB is INTEGER The leading dimension of the array A. LDAB >= KL+KU+1.

### D (out)

D is DOUBLE PRECISION array, dimension (min(M,N)) The diagonal elements of the bidiagonal matrix B.

### E (out)

E is DOUBLE PRECISION array, dimension (min(M,N)-1) The superdiagonal elements of the bidiagonal matrix B.

### Q (out)

Q is COMPLEX*16 array, dimension (LDQ,M) If VECT = 'Q' or 'B', the m-by-m unitary matrix Q. If VECT = 'N' or 'P', the array Q is not referenced.

### LDQ (in)

LDQ is INTEGER The leading dimension of the array Q. LDQ >= max(1,M) if VECT = 'Q' or 'B'; LDQ >= 1 otherwise.

### PT (out)

PT is COMPLEX*16 array, dimension (LDPT,N) If VECT = 'P' or 'B', the n-by-n unitary matrix P'. If VECT = 'N' or 'Q', the array PT is not referenced.

### LDPT (in)

LDPT is INTEGER The leading dimension of the array PT. LDPT >= max(1,N) if VECT = 'P' or 'B'; LDPT >= 1 otherwise.

### C (in,out)

C is COMPLEX*16 array, dimension (LDC,NCC) On entry, an m-by-ncc matrix C. On exit, C is overwritten by Q**H*C. C is not referenced if NCC = 0.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M) if NCC > 0; LDC >= 1 if NCC = 0.

### WORK (out)

WORK is COMPLEX*16 array, dimension (max(M,N))

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension (max(M,N))

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value.

