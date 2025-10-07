# CLAQZ1

## Function Signature

```fortran
CLAQZ1(ILQ, ILZ, K, ISTARTM, ISTOPM, IHI, A, LDA, B,
*     $    LDB, NQ, QSTART, Q, LDQ, NZ, ZSTART, Z, LDZ)
```

## Description


      CLAQZ1 chases a 1x1 shift bulge in a matrix pencil down a single position

## Parameters

### ILQ (in)

ILQ is LOGICAL Determines whether or not to update the matrix Q

### ILZ (in)

ILZ is LOGICAL Determines whether or not to update the matrix Z

### K (in)

K is INTEGER Index indicating the position of the bulge. On entry, the bulge is located in (A(k+1,k),B(k+1,k)). On exit, the bulge is located in (A(k+2,k+1),B(k+2,k+1)).

### ISTARTM (in)

ISTARTM is INTEGER

### ISTOPM (in)

ISTOPM is INTEGER Updates to (A,B) are restricted to (istartm:k+2,k:istopm). It is assumed without checking that istartm <= k+1 and k+2 <= istopm

### IHI (in)

IHI is INTEGER

### A (inout)

A is COMPLEX array, dimension (LDA,N)

### LDA (in)

LDA is INTEGER The leading dimension of A as declared in the calling procedure.

### B (inout)

B is COMPLEX array, dimension (LDB,N)

### LDB (in)

LDB is INTEGER The leading dimension of B as declared in the calling procedure.

### NQ (in)

NQ is INTEGER The order of the matrix Q

### QSTART (in)

QSTART is INTEGER Start index of the matrix Q. Rotations are applied To columns k+2-qStart:k+3-qStart of Q.

### Q (inout)

Q is COMPLEX array, dimension (LDQ,NQ)

### LDQ (in)

LDQ is INTEGER The leading dimension of Q as declared in the calling procedure.

### NZ (in)

NZ is INTEGER The order of the matrix Z

### ZSTART (in)

ZSTART is INTEGER Start index of the matrix Z. Rotations are applied To columns k+1-qStart:k+2-qStart of Z.

### Z (inout)

Z is COMPLEX array, dimension (LDZ,NZ)

### LDZ (in)

LDZ is INTEGER The leading dimension of Q as declared in the calling procedure.

