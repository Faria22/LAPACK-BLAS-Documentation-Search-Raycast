# DTRSYL

## Function Signature

```fortran
DTRSYL(TRANA, TRANB, ISGN, M, N, A, LDA, B, LDB, C,
*                          LDC, SCALE, INFO)
```

## Description


 DTRSYL solves the real Sylvester matrix equation:

    op(A)*X + X*op(B) = scale*C or
    op(A)*X - X*op(B) = scale*C,

 where op(A) = A or A**T, and  A and B are both upper quasi-
 triangular. A is M-by-M and B is N-by-N; the right hand side C and
 the solution X are M-by-N; and scale is an output scale factor, set
 <= 1 to avoid overflow in X.

 A and B must be in Schur canonical form (as returned by DHSEQR), that
 is, block upper triangular with 1-by-1 and 2-by-2 diagonal blocks;
 each 2-by-2 diagonal block has its diagonal elements equal and its
 off-diagonal elements of opposite sign.

## Parameters

### TRANA (in)

TRANA is CHARACTER*1 Specifies the option op(A): = 'N': op(A) = A (No transpose) = 'T': op(A) = A**T (Transpose) = 'C': op(A) = A**H (Conjugate transpose = Transpose)

### TRANB (in)

TRANB is CHARACTER*1 Specifies the option op(B): = 'N': op(B) = B (No transpose) = 'T': op(B) = B**T (Transpose) = 'C': op(B) = B**H (Conjugate transpose = Transpose)

### ISGN (in)

ISGN is INTEGER Specifies the sign in the equation: = +1: solve op(A)*X + X*op(B) = scale*C = -1: solve op(A)*X - X*op(B) = scale*C

### M (in)

M is INTEGER The order of the matrix A, and the number of rows in the matrices X and C. M >= 0.

### N (in)

N is INTEGER The order of the matrix B, and the number of columns in the matrices X and C. N >= 0.

### A (in)

A is DOUBLE PRECISION array, dimension (LDA,M) The upper quasi-triangular matrix A, in Schur canonical form.

### LDA (in)

LDA is INTEGER The leading dimension of the array A. LDA >= max(1,M).

### B (in)

B is DOUBLE PRECISION array, dimension (LDB,N) The upper quasi-triangular matrix B, in Schur canonical form.

### LDB (in)

LDB is INTEGER The leading dimension of the array B. LDB >= max(1,N).

### C (in,out)

C is DOUBLE PRECISION array, dimension (LDC,N) On entry, the M-by-N right hand side matrix C. On exit, C is overwritten by the solution matrix X.

### LDC (in)

LDC is INTEGER The leading dimension of the array C. LDC >= max(1,M)

### SCALE (out)

SCALE is DOUBLE PRECISION The scale factor, scale, set <= 1 to avoid overflow in X.

### INFO (out)

INFO is INTEGER = 0: successful exit < 0: if INFO = -i, the i-th argument had an illegal value = 1: A and B have common or very close eigenvalues; perturbed values were used to solve the equation (but the matrices A and B are unchanged).

