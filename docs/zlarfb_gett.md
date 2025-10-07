```fortran
subroutine zlarfb_gett	(	ident,
		m,
		n,
		k,
		t,
		ldt,
		a,
		lda,
		b,
		ldb,
		*      $                        work,
		ldwork )
```

 ZLARFB_GETT applies a complex Householder block reflector H from the
 left to a complex (K+M)-by-N  "triangular-pentagonal" matrix
 composed of two block matrices: an upper trapezoidal K-by-N matrix A
 stored in the array A, and a rectangular M-by-(N-K) matrix B, stored
 in the array B. The block reflector H is stored in a compact
 WY-representation, where the elementary reflectors are in the
 arrays A, B and T. See Further Details section.

## Parameters
Ident : Character*1 [in]
> If IDENT = not 'I', or not 'i', then V1 is unit
> lower-triangular and stored in the left K-by-K block of
> the input matrix A,
> If IDENT = 'I' or 'i', then  V1 is an identity matrix and
> not stored.
> See Further Details section.

M : Integer [in]
> The number of rows of the matrix B.
> M >= 0.

N : Integer [in]
> The number of columns of the matrices A and B.
> N >= 0.

K : Integer [in]
> The number or rows of the matrix A.
> K is also order of the matrix T, i.e. the number of
> elementary reflectors whose product defines the block
> reflector. 0 <= K <= N.

T : Complex*16 Array, Dimension (ldt,k) [in]
> The upper-triangular K-by-K matrix T in the representation
> of the block reflector.

Ldt : Integer [in]
> The leading dimension of the array T. LDT >= K.

A : Complex*16 Array, Dimension (lda,n) [in,out]
> On entry:
> a) In the K-by-N upper-trapezoidal part A: input matrix A.
> b) In the columns below the diagonal: columns of V1
> (ones are not stored on the diagonal).
> On exit:
> A is overwritten by rectangular K-by-N product H*A.
> See Further Details section.

Lda : Integer [in]
> The leading dimension of the array A. LDA >= max(1,K).

B : Complex*16 Array, Dimension (ldb,n) [in,out]
> On entry:
> a) In the M-by-(N-K) right block: input matrix B.
> b) In the M-by-N left block: columns of V2.
> On exit:
> B is overwritten by rectangular M-by-N product H*B.
> See Further Details section.

Ldb : Integer [in]
> The leading dimension of the array B. LDB >= max(1,M).

Work : Complex*16 Array, [out]
> dimension (LDWORK,max(K,N-K))

Ldwork : Integer [in]
> The leading dimension of the array WORK. LDWORK>=max(1,K).

