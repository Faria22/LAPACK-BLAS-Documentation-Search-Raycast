```fortran
subroutine claic1	(	integer	job,
		integer	j,
		complex, dimension(j)	x,
		real	sest,
		complex, dimension(j)	w,
		complex	gamma,
		real	sestpr,
		complex	s,
		complex	c )
```

 CLAIC1 applies one step of incremental condition estimation in
 its simplest version:

 Let x, twonorm(x) = 1, be an approximate singular vector of an j-by-j
 lower triangular matrix L, such that
          twonorm(L*x) = sest
 Then CLAIC1 computes sestpr, s, c such that
 the vector
                 [ s*x ]
          xhat = [  c  ]
 is an approximate singular vector of
                 [ L      0  ]
          Lhat = [ w**H gamma ]
 in the sense that
          twonorm(Lhat*xhat) = sestpr.

 Depending on JOB, an estimate for the largest or smallest singular
 value is computed.

 Note that [s c]**H and sestpr**2 is an eigenpair of the system

     diag(sest*sest, 0) + [alpha  gamma] * [ conjg(alpha) ]
                                           [ conjg(gamma) ]

 where  alpha =  x**H*w.

## Parameters
Job : Integer [in]
> = 1: an estimate for the largest singular value is computed.
> = 2: an estimate for the smallest singular value is computed.

J : Integer [in]
> Length of X and W

X : Complex Array, Dimension (j) [in]
> The j-vector x.

Sest : Real [in]
> Estimated singular value of j by j matrix L

W : Complex Array, Dimension (j) [in]
> The j-vector w.

Gamma : Complex [in]
> The diagonal element gamma.

Sestpr : Real [out]
> Estimated singular value of (j+1) by (j+1) matrix Lhat.

S : Complex [out]
> Sine needed in forming xhat.

C : Complex [out]
> Cosine needed in forming xhat.

