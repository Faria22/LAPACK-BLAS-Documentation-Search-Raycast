# DLAGS2

## Function Signature

```fortran
DLAGS2(UPPER, A1, A2, A3, B1, B2, B3, CSU, SNU, CSV,
*                          SNV, CSQ, SNQ)
```

## Description


 DLAGS2 computes 2-by-2 orthogonal matrices U, V and Q, such
 that if ( UPPER ) then

           U**T *A*Q = U**T *( A1 A2 )*Q = ( x  0  )
                             ( 0  A3 )     ( x  x  )
 and
           V**T*B*Q = V**T *( B1 B2 )*Q = ( x  0  )
                            ( 0  B3 )     ( x  x  )

 or if ( .NOT.UPPER ) then

           U**T *A*Q = U**T *( A1 0  )*Q = ( x  x  )
                             ( A2 A3 )     ( 0  x  )
 and
           V**T*B*Q = V**T*( B1 0  )*Q = ( x  x  )
                           ( B2 B3 )     ( 0  x  )

 The rows of the transformed A and B are parallel, where

   U = (  CSU  SNU ), V = (  CSV SNV ), Q = (  CSQ   SNQ )
       ( -SNU  CSU )      ( -SNV CSV )      ( -SNQ   CSQ )

 Z**T denotes the transpose of Z.


## Parameters

### UPPER (in)

UPPER is LOGICAL = .TRUE.: the input matrices A and B are upper triangular. = .FALSE.: the input matrices A and B are lower triangular.

### A1 (in)

A1 is DOUBLE PRECISION

### A2 (in)

A2 is DOUBLE PRECISION

### A3 (in)

A3 is DOUBLE PRECISION On entry, A1, A2 and A3 are elements of the input 2-by-2 upper (lower) triangular matrix A.

### B1 (in)

B1 is DOUBLE PRECISION

### B2 (in)

B2 is DOUBLE PRECISION

### B3 (in)

B3 is DOUBLE PRECISION On entry, B1, B2 and B3 are elements of the input 2-by-2 upper (lower) triangular matrix B.

### CSU (out)

CSU is DOUBLE PRECISION

### SNU (out)

SNU is DOUBLE PRECISION The desired orthogonal matrix U.

### CSV (out)

CSV is DOUBLE PRECISION

### SNV (out)

SNV is DOUBLE PRECISION The desired orthogonal matrix V.

### CSQ (out)

CSQ is DOUBLE PRECISION

### SNQ (out)

SNQ is DOUBLE PRECISION The desired orthogonal matrix Q.

