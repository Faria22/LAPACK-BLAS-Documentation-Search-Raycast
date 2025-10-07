# ZLALSD

## Function Signature

```fortran
ZLALSD(UPLO, SMLSIZ, N, NRHS, D, E, B, LDB, RCOND,
*                          RANK, WORK, RWORK, IWORK, INFO)
```

## Description


 ZLALSD uses the singular value decomposition of A to solve the least
 squares problem of finding X to minimize the Euclidean norm of each
 column of A*X-B, where A is N-by-N upper bidiagonal, and X and B
 are N-by-NRHS. The solution X overwrites B.

 The singular values of A smaller than RCOND times the largest
 singular value are treated as zero in solving the least squares
 problem; in this case a minimum norm solution is returned.
 The actual singular values are returned in D in ascending order.


## Parameters

### UPLO (in)

UPLO is CHARACTER*1 = 'U': D and E define an upper bidiagonal matrix. = 'L': D and E define a lower bidiagonal matrix.

### SMLSIZ (in)

SMLSIZ is INTEGER The maximum size of the subproblems at the bottom of the computation tree.

### N (in)

N is INTEGER The dimension of the bidiagonal matrix. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of columns of B. NRHS must be at least 1.

### D (in,out)

D is DOUBLE PRECISION array, dimension (N) On entry D contains the main diagonal of the bidiagonal matrix. On exit, if INFO = 0, D contains its singular values.

### E (in,out)

E is DOUBLE PRECISION array, dimension (N-1) Contains the super-diagonal entries of the bidiagonal matrix. On exit, E has been destroyed.

### B (in,out)

B is COMPLEX*16 array, dimension (LDB,NRHS) On input, B contains the right hand sides of the least squares problem. On output, B contains the solution X.

### LDB (in)

LDB is INTEGER The leading dimension of B in the calling subprogram. LDB must be at least max(1,N).

### RCOND (in)

RCOND is DOUBLE PRECISION The singular values of A less than or equal to RCOND times the largest singular value are treated as zero in solving the least squares problem. If RCOND is negative, machine precision is used instead. For example, if diag(S)*X=B were the least squares problem, where diag(S) is a diagonal matrix of singular values, the solution would be X(i) = B(i) / S(i) if S(i) is greater than RCOND*max(S), and X(i) = 0 if S(i) is less than or equal to RCOND*max(S).

### RANK (out)

RANK is INTEGER The number of singular values of A greater than RCOND times the largest singular value.

### WORK (out)

WORK is COMPLEX*16 array, dimension (N * NRHS)

### RWORK (out)

RWORK is DOUBLE PRECISION array, dimension at least (9*N + 2*N*SMLSIZ + 8*N*NLVL + 3*SMLSIZ*NRHS + MAX( (SMLSIZ+1)**2, N*(1+NRHS) + 2*NRHS ), where NLVL = MAX( 0, INT( LOG_2( MIN( M,N )/(SMLSIZ+1) ) ) + 1 )

### IWORK (out)

IWORK is INTEGER array, dimension at least (3*N*NLVL + 11*N).

### INFO (out)

INFO is INTEGER = 0: successful exit. < 0: if INFO = -i, the i-th argument had an illegal value. > 0: The algorithm failed to compute a singular value while working on the submatrix lying in rows and columns INFO/(N+1) through MOD(INFO,N+1).

