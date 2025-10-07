```fortran
subroutine zlaev2 (
		complex*16 a,
		complex*16 b,
		complex*16 c,
		double precision rt1,
		double precision rt2,
		double precision cs1,
		complex*16 sn1
)
```

 ZLAEV2 computes the eigendecomposition of a 2-by-2 Hermitian matrix
    [  A         B  ]
    [  CONJG(B)  C  ].
 On return, RT1 is the eigenvalue of larger absolute value, RT2 is the
 eigenvalue of smaller absolute value, and (CS1,SN1) is the unit right
 eigenvector for RT1, giving the decomposition

 [ CS1  CONJG(SN1) ] [    A     B ] [ CS1 -CONJG(SN1) ] = [ RT1  0  ]
 [-SN1     CS1     ] [ CONJG(B) C ] [ SN1     CS1     ]   [  0  RT2 ].

## Parameters
A : Complex*16 [in]
> The (1,1) element of the 2-by-2 matrix.

B : Complex*16 [in]
> The (1,2) element and the conjugate of the (2,1) element of
> the 2-by-2 matrix.

C : Complex*16 [in]
> The (2,2) element of the 2-by-2 matrix.

Rt1 : Double Precision [out]
> The eigenvalue of larger absolute value.

Rt2 : Double Precision [out]
> The eigenvalue of smaller absolute value.

Cs1 : Double Precision [out]

Sn1 : Complex*16 [out]
> The vector (CS1, SN1) is a unit right eigenvector for RT1.

