# SLAQGE

## Function Signature

```fortran
SLAQGE(M, N, A, LDA, R, C, ROWCND, COLCND, AMAX,
*                          EQUED)
```

## Description


 SLAQGE equilibrates a general M by N matrix A using the row and
 column scaling factors in the vectors R and C.

## Parameters

### M (in)

M is INTEGER The number of rows of the matrix A. M >= 0.

### N (in)

N is INTEGER The number of columns of the matrix A. N >= 0.

### A (in,out)

A is REAL array, dimension (LDA,N) On entry, the M by N matrix A. On exit, the equilibrated matrix. See EQUED for the form of the equilibrated matrix.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(M,1).

### R (in)

R is REAL array, dimension (M) The row scale factors for A.

### C (in)

C is REAL array, dimension (N) The column scale factors for A.

### ROWCND (in)

ROWCND is REAL Ratio of the smallest R(i) to the largest R(i).

### COLCND (in)

COLCND is REAL Ratio of the smallest C(i) to the largest C(i).

### AMAX (in)

AMAX is REAL Absolute value of largest matrix entry.

### EQUED (out)

EQUED is CHARACTER*1 Specifies the form of equilibration that was done. = 'N': No equilibration = 'R': Row equilibration, i.e., A has been premultiplied by diag(R). = 'C': Column equilibration, i.e., A has been postmultiplied by diag(C). = 'B': Both row and column equilibration, i.e., A has been replaced by diag(R) * A * diag(C).

