# ZGGBAL

## Function Signature

```fortran
ZGGBAL(JOB, N, A, LDA, B, LDB, ILO, IHI, LSCALE,
*                          RSCALE, WORK, INFO)
```

## Description


 ZGGBAL balances a pair of general complex matrices (A,B).  This
 involves, first, permuting A and B by similarity transformations to
 isolate eigenvalues in the first 1 to ILO$-$1 and last IHI+1 to N
 elements on the diagonal; and second, applying a diagonal similarity
 transformation to rows and columns ILO to IHI to make the rows
 and columns as close in norm as possible. Both steps are optional.

 Balancing may reduce the 1-norm of the matrices, and improve the
 accuracy of the computed eigenvalues and/or eigenvectors in the
 generalized eigenvalue problem A*x = lambda*B*x.

## Parameters

### JOB (in)

JOB is CHARACTER*1 Specifies the operations to be performed on A and B: = 'N': none: simply set ILO = 1, IHI = N, LSCALE(I) = 1.0 and RSCALE(I) = 1.0 for i=1,...,N; = 'P': permute only; = 'S': scale only; = 'B': both permute and scale.

### N (in)

N is INTEGER The order of the matrices A and B. N >= 0.

### A (in,out)

A is COMPLEX*16 array, dimension (LDA,N) On entry, the input matrix A. On exit, A is overwritten by the balanced matrix. If JOB = 'N', A is not referenced.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,N).

### B (in,out)

B is COMPLEX*16 array, dimension (LDB,N) On entry, the input matrix B. On exit, B is overwritten by the balanced matrix. If JOB = 'N', B is not referenced.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### ILO (out)

ILO is INTEGER

### IHI (out)

IHI is INTEGER ILO and IHI are set to integers such that on exit A(i,j) = 0 and B(i,j) = 0 if i > j and j = 1,...,ILO-1 or i = IHI+1,...,N. If JOB = 'N' or 'S', ILO = 1 and IHI = N.

### LSCALE (out)

LSCALE is DOUBLE PRECISION array, dimension (N) Details of the permutations and scaling factors applied to the left side of A and B. If P(j) is the index of the row interchanged with row j, and D(j) is the scaling factor applied to row j, then LSCALE(j) = P(j) for J = 1,...,ILO-1 = D(j) for J = ILO,...,IHI = P(j) for J = IHI+1,...,N. The order in which the interchanges are made is N to IHI+1, then 1 to ILO-1.

### RSCALE (out)

RSCALE is DOUBLE PRECISION array, dimension (N) Details of the permutations and scaling factors applied to the right side of A and B. If P(j) is the index of the column interchanged with column j, and D(j) is the scaling factor applied to column j, then RSCALE(j) = P(j) for J = 1,...,ILO-1 = D(j) for J = ILO,...,IHI = P(j) for J = IHI+1,...,N. The order in which the interchanges are made is N to IHI+1, then 1 to ILO-1.

### WORK (out)

WORK is DOUBLE PRECISION array, dimension (lwork) lwork must be at least max(1,6*N) when JOB = 'S' or 'B', and at least 1 when JOB = 'N' or 'P'.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value.

