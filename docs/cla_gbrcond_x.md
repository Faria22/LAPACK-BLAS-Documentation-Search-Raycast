# CLA_GBRCOND_X

## Function Signature

```fortran
CLA_GBRCOND_X(TRANS, N, KL, KU, AB, LDAB, AFB,
*                                    LDAFB, IPIV, X, INFO, WORK, RWORK)
```

## Description


    CLA_GBRCOND_X Computes the infinity norm condition number of
    op(A) * diag(X) where X is a COMPLEX vector.

## Parameters

### TRANS (in)

TRANS is CHARACTER*1 Specifies the form of the system of equations: = 'N': A * X = B (No transpose) = 'T': A**T * X = B (Transpose) = 'C': A**H * X = B (Conjugate Transpose = Transpose)

### N (in)

N is INTEGER The number of linear equations, i.e., the order of the matrix A. N >= 0.

### KL (in)

KL is INTEGER The number of subdiagonals within the band of A. KL >= 0.

### KU (in)

KU is INTEGER The number of superdiagonals within the band of A. KU >= 0.

### AB (in)

AB is COMPLEX array, dimension (LDAB,N) On entry, the matrix A in band storage, in rows 1 to KL+KU+1. The j-th column of A is stored in the j-th column of the array AB as follows: AB(KU+1+i-j,j) = A(i,j) for max(1,j-KU)<=i<=min(N,j+kl)

### LDAB (in)

LDAB is INTEGER The leading dimension of the array AB. LDAB >= KL+KU+1.

### AFB (in)

AFB is COMPLEX array, dimension (LDAFB,N) Details of the LU factorization of the band matrix A, as computed by CGBTRF. U is stored as an upper triangular band matrix with KL+KU superdiagonals in rows 1 to KL+KU+1, and the multipliers used during the factorization are stored in rows KL+KU+2 to 2*KL+KU+1.

### LDAFB (in)

LDAFB is INTEGER The leading dimension of the array AFB. LDAFB >= 2*KL+KU+1.

### IPIV (in)

IPIV is INTEGER array, dimension (N) The pivot indices from the factorization A = P*L*U as computed by CGBTRF; row i of the matrix was interchanged with row IPIV(i).

### X (in)

X is COMPLEX array, dimension (N) The vector X in the formula op(A) * diag(X).

### INFO (out)

INFO is INTEGER = 0: Successful exit. i > 0: The ith argument is invalid.

### WORK (out)

WORK is COMPLEX array, dimension (2*N). Workspace.

### RWORK (out)

RWORK is REAL array, dimension (N). Workspace.

