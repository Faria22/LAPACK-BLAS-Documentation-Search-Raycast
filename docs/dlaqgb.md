# DLAQGB

## Function Signature

```fortran
DLAQGB(M, N, KL, KU, AB, LDAB, R, C, ROWCND, COLCND,
*                          AMAX, EQUED)
```

## Description


 DLAQGB equilibrates a general M by N band matrix A with KL
 subdiagonals and KU superdiagonals using the row and scaling factors
 in the vectors R and C.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### KL (in)

KL is INTEGER The number of subdiagonals within the band of A. KL >= 0.

### KU (in)

KU is INTEGER The number of superdiagonals within the band of A. KU >= 0.

### AB (in,out)

AB is DOUBLE PRECISION array, dimension (LDAB,N) On entry, the matrix A in band storage, in rows 1 to KL+KU+1. The j-th column of A is stored in the j-th column of the array AB as follows: AB(ku+1+i-j,j) = A(i,j) for max(1,j-ku)<=i<=min(m,j+kl) On exit, the equilibrated matrix, in the same storage format as A. See EQUED for the form of the equilibrated matrix.

### LDAB (in)

LDAB is INTEGER The leading dimension of the array AB. LDA >= KL+KU+1.

### R (in)

R is DOUBLE PRECISION array, dimension (M) The row scale factors for A.

### C (in)

C is DOUBLE PRECISION array, dimension (N) The column scale factors for A.

### ROWCND (in)

ROWCND is DOUBLE PRECISION Ratio of the smallest R(i) to the largest R(i).

### COLCND (in)

COLCND is DOUBLE PRECISION Ratio of the smallest C(i) to the largest C(i).

### AMAX (in)

AMAX is DOUBLE PRECISION Absolute value of largest matrix entry.

### EQUED (out)

EQUED is CHARACTER*1 Specifies the form of equilibration that was done. = 'N': No equilibration = 'R': Row equilibration, i.e., A has been premultiplied by diag(R). = 'C': Column equilibration, i.e., A has been postmultiplied by diag(C). = 'B': Both row and column equilibration, i.e., A has been replaced by diag(R) * A * diag(C).

