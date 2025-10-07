```fortran
subroutine dlags2 (
		upper,
		a1,
		a2,
		a3,
		b1,
		b2,
		b3,
		csu,
		snu,
		csv,
		*                          snv,
		csq,
		snq
)
```

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
Upper : Logical [in]
> = .TRUE.: the input matrices A and B are upper triangular.
> = .FALSE.: the input matrices A and B are lower triangular.

A1 : Double Precision [in]

A2 : Double Precision [in]

A3 : Double Precision [in]
> On entry, A1, A2 and A3 are elements of the input 2-by-2
> upper (lower) triangular matrix A.

B1 : Double Precision [in]

B2 : Double Precision [in]

B3 : Double Precision [in]
> On entry, B1, B2 and B3 are elements of the input 2-by-2
> upper (lower) triangular matrix B.

Csu : Double Precision [out]

Snu : Double Precision [out]
> The desired orthogonal matrix U.

Csv : Double Precision [out]

Snv : Double Precision [out]
> The desired orthogonal matrix V.

Csq : Double Precision [out]

Snq : Double Precision [out]
> The desired orthogonal matrix Q.

