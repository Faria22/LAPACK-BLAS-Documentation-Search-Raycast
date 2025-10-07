# DLAQZ1

## Function Signature

```fortran
DLAQZ1(A, LDA, B, LDB, SR1, SR2, SI, BETA1, BETA2,
*     $    V)
```

## Description


      Given a 3-by-3 matrix pencil (A,B), DLAQZ1 sets v to a
      scalar multiple of the first column of the product

      (*)  K = (A - (beta2*sr2 - i*si)*B)*B^(-1)*(beta1*A - (sr2 + i*si2)*B)*B^(-1).

      It is assumed that either

              1) sr1 = sr2
          or
              2) si = 0.

      This is useful for starting double implicit shift bulges
      in the QZ algorithm.

## Parameters

### A (in)

A is DOUBLE PRECISION array, dimension (LDA,N) The 3-by-3 matrix A in (*).

### LDA (in)

LDA is INTEGER The leading dimension of A as declared in the calling procedure.

### B (in)

B is DOUBLE PRECISION array, dimension (LDB,N) The 3-by-3 matrix B in (*).

### LDB (in)

LDB is INTEGER The leading dimension of B as declared in the calling procedure.

### SR1 (in)

SR1 is DOUBLE PRECISION

### SR2 (in)

SR2 is DOUBLE PRECISION

### SI (in)

SI is DOUBLE PRECISION

### BETA1 (in)

BETA1 is DOUBLE PRECISION

### BETA2 (in)

BETA2 is DOUBLE PRECISION

### V (out)

V is DOUBLE PRECISION array, dimension (N) A scalar multiple of the first column of the matrix K in (*).

