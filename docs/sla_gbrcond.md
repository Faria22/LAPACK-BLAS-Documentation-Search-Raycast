# SLA_GBRCOND

## Function Signature

```fortran
SLA_GBRCOND(TRANS, N, KL, KU, AB, LDAB, AFB, LDAFB,
*                                  IPIV, CMODE, C, INFO, WORK, IWORK)
```

## Description


    SLA_GBRCOND Estimates the Skeel condition number of  op(A) * op2(C)
    where op2 is determined by CMODE as follows
    CMODE =  1    op2(C) = C
    CMODE =  0    op2(C) = I
    CMODE = -1    op2(C) = inv(C)
    The Skeel condition number  cond(A) = norminf( |inv(A)||A| )
    is computed by computing scaling factors R such that
    diag(R)*A*op2(C) is row equilibrated and computing the standard
    infinity-norm condition number.

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

AB is REAL array, dimension (LDAB,N) On entry, the matrix A in band storage, in rows 1 to KL+KU+1. The j-th column of A is stored in the j-th column of the array AB as follows: AB(KU+1+i-j,j) = A(i,j) for max(1,j-KU)<=i<=min(N,j+kl)

### LDAB (in)

LDAB is INTEGER The leading dimension of the array AB. LDAB >= KL+KU+1.

### AFB (in)

AFB is REAL array, dimension (LDAFB,N) Details of the LU factorization of the band matrix A, as computed by SGBTRF. U is stored as an upper triangular band matrix with KL+KU superdiagonals in rows 1 to KL+KU+1, and the multipliers used during the factorization are stored in rows KL+KU+2 to 2*KL+KU+1.

### LDAFB (in)

LDAFB is INTEGER The leading dimension of the array AFB. LDAFB >= 2*KL+KU+1.

### IPIV (in)

IPIV is INTEGER array, dimension (N) The pivot indices from the factorization A = P*L*U as computed by SGBTRF; row i of the matrix was interchanged with row IPIV(i).

### CMODE (in)

CMODE is INTEGER Determines op2(C) in the formula op(A) * op2(C) as follows: CMODE = 1 op2(C) = C CMODE = 0 op2(C) = I CMODE = -1 op2(C) = inv(C)

### C (in)

C is REAL array, dimension (N) The vector C in the formula op(A) * op2(C).

### INFO (out)

INFO is INTEGER = 0: Successful exit. i > 0: The ith argument is invalid.

### WORK (out)

WORK is REAL array, dimension (5*N). Workspace.

### IWORK (out)

IWORK is INTEGER array, dimension (N). Workspace.

