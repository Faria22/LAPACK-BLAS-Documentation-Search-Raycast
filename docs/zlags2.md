# ZLAGS2

## Function Signature

```fortran
ZLAGS2(UPPER, A1, A2, A3, B1, B2, B3, CSU, SNU, CSV,
*                          SNV, CSQ, SNQ)
```

## Description


 ZLAGS2 computes 2-by-2 unitary matrices U, V and Q, such
 that if ( UPPER ) then

           U**H *A*Q = U**H *( A1 A2 )*Q = ( x  0  )
                             ( 0  A3 )     ( x  x  )
 and
           V**H*B*Q = V**H *( B1 B2 )*Q = ( x  0  )
                            ( 0  B3 )     ( x  x  )

 or if ( .NOT.UPPER ) then

           U**H *A*Q = U**H *( A1 0  )*Q = ( x  x  )
                             ( A2 A3 )     ( 0  x  )
 and
           V**H *B*Q = V**H *( B1 0  )*Q = ( x  x  )
                             ( B2 B3 )     ( 0  x  )
 where

   U = (   CSU    SNU ), V = (  CSV    SNV ),
       ( -SNU**H  CSU )      ( -SNV**H CSV )

   Q = (   CSQ    SNQ )
       ( -SNQ**H  CSQ )

 The rows of the transformed A and B are parallel. Moreover, if the
 input 2-by-2 matrix A is not zero, then the transformed (1,1) entry
 of A is not zero. If the input matrices A and B are both not zero,
 then the transformed (2,2) element of B is not zero, except when the
 first rows of input A and B are parallel and the second rows are
 zero.

## Parameters

### UPPER (in)

UPPER is LOGICAL = .TRUE.: the input matrices A and B are upper triangular. = .FALSE.: the input matrices A and B are lower triangular.

### A1 (in)

A1 is DOUBLE PRECISION

### A2 (in)

A2 is COMPLEX*16

### A3 (in)

A3 is DOUBLE PRECISION On entry, A1, A2 and A3 are elements of the input 2-by-2 upper (lower) triangular matrix A.

### B1 (in)

B1 is DOUBLE PRECISION

### B2 (in)

B2 is COMPLEX*16

### B3 (in)

B3 is DOUBLE PRECISION On entry, B1, B2 and B3 are elements of the input 2-by-2 upper (lower) triangular matrix B.

### CSU (out)

CSU is DOUBLE PRECISION

### SNU (out)

SNU is COMPLEX*16 The desired unitary matrix U.

### CSV (out)

CSV is DOUBLE PRECISION

### SNV (out)

SNV is COMPLEX*16 The desired unitary matrix V.

### CSQ (out)

CSQ is DOUBLE PRECISION

### SNQ (out)

SNQ is COMPLEX*16 The desired unitary matrix Q.

