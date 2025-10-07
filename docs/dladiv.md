```fortran
subroutine dladiv	(	double precision	a,
		double precision	b,
		double precision	c,
		double precision	d,
		double precision	p,
		double precision	q )
```

 DLADIV performs complex division in  real arithmetic

                       a + i*b
            p + i*q = ---------
                       c + i*d

 The algorithm is due to Michael Baudin and Robert L. Smith
 and can be found in the paper
 "A Robust Complex Division in Scilab"

## Parameters
A : Double Precision [in]

B : Double Precision [in]

C : Double Precision [in]

D : Double Precision [in]
> The scalars a, b, c, and d in the above expression.

P : Double Precision [out]

Q : Double Precision [out]
> The scalars p and q in the above expression.

