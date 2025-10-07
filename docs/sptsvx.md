# SPTSVX

SPTSVX computes the solution to system of linear equations A * X = B for PT matrices

## Function Signature

```fortran
SPTSVX(FACT, N, NRHS, D, E, DF, EF, B, LDB, X, LDX,
*                          RCOND, FERR, BERR, WORK, INFO)
```

## Description


 SPTSVX uses the factorization A = L*D*L**T to compute the solution
 to a real system of linear equations A*X = B, where A is an N-by-N
 symmetric positive definite tridiagonal matrix and X and B are
 N-by-NRHS matrices.

 Error bounds on the solution and a condition estimate are also
 provided.

## Parameters

### FACT (in)

FACT is CHARACTER*1 Specifies whether or not the factored form of A has been supplied on entry. = 'F': On entry, DF and EF contain the factored form of A. D, E, DF, and EF will not be modified. = 'N': The matrix A will be copied to DF and EF and factored.

### N (in)

N is INTEGER The order of the matrix A. N >= 0.

### NRHS (in)

NRHS is INTEGER The number of right hand sides, i.e., the number of columns of the matrices B and X. NRHS >= 0.

### D (in)

D is REAL array, dimension (N) The n diagonal elements of the tridiagonal matrix A.

### E (in)

E is REAL array, dimension (N-1) The (n-1) subdiagonal elements of the tridiagonal matrix A.

### DF (in,out)

DF is REAL array, dimension (N) If FACT = 'F', then DF is an input argument and on entry contains the n diagonal elements of the diagonal matrix D from the L*D*L**T factorization of A. If FACT = 'N', then DF is an output argument and on exit contains the n diagonal elements of the diagonal matrix D from the L*D*L**T factorization of A.

### EF (in,out)

EF is REAL array, dimension (N-1) If FACT = 'F', then EF is an input argument and on entry contains the (n-1) subdiagonal elements of the unit bidiagonal factor L from the L*D*L**T factorization of A. If FACT = 'N', then EF is an output argument and on exit contains the (n-1) subdiagonal elements of the unit bidiagonal factor L from the L*D*L**T factorization of A.

### B (in)

B is REAL array, dimension (LDB,NRHS) The N-by-NRHS right hand side matrix B.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### X (out)

X is REAL array, dimension (LDX,NRHS) If INFO = 0 of INFO = N+1, the N-by-NRHS solution matrix X.

### LDX (in)

LDX is INTEGER The leading dimension of the array X. LDX >= max(1,N).

### RCOND (out)

RCOND is REAL The reciprocal condition number of the matrix A. If RCOND is less than the machine precision (in particular, if RCOND = 0), the matrix is singular to working precision. This condition is indicated by a return code of INFO > 0.

### FERR (out)

FERR is REAL array, dimension (NRHS) The forward error bound for each solution vector X(j) (the j-th column of the solution matrix X). If XTRUE is the true solution corresponding to X(j), FERR(j) is an estimated upper bound for the magnitude of the largest element in (X(j) - XTRUE) divided by the magnitude of the largest element in X(j).

### BERR (out)

BERR is REAL array, dimension (NRHS) The componentwise relative backward error of each solution vector X(j) (i.e., the smallest relative change in any element of A or B that makes X(j) an exact solution).

### WORK (out)

WORK is REAL array, dimension (2*N)

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value > 0: if INFO = i, and i is <= N: the leading principal minor of order i of A is not positive, so the factorization could not be completed, and the solution has not been computed. RCOND = 0 is returned. = N+1: U is nonsingular, but RCOND is less than machine precision, meaning that the matrix is singular to working precision. Nevertheless, the solution and error bounds are computed because there are a number of situations where the computed solution can be more accurate than the value of RCOND would suggest.

