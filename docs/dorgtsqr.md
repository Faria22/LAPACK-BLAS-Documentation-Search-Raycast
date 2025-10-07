```fortran
subroutine dorgtsqr (
		m,
		n,
		mb,
		nb,
		a,
		lda,
		t,
		ldt,
		work,
		lwork,
		*      $                     info
)
```

 DORGTSQR generates an M-by-N real matrix Q_out with orthonormal columns,
 which are the first N columns of a product of real orthogonal
 matrices of order M which are returned by DLATSQR

      Q_out = first_N_columns_of( Q(1)_in * Q(2)_in * ... * Q(k)_in ).

 See the documentation for DLATSQR.

## Parameters
M : Integer [in]
> The number of rows of the matrix A.  M >= 0.

N : Integer [in]
> The number of columns of the matrix A. M >= N >= 0.

Mb : Integer [in]
> The row block size used by DLATSQR to return
> arrays A and T. MB > N.
> (Note that if MB > M, then M is used instead of MB
> as the row block size).

Nb : Integer [in]
> The column block size used by DLATSQR to return
> arrays A and T. NB >= 1.
> (Note that if NB > N, then N is used instead of NB
> as the column block size).

A : Double Precision Array, Dimension (lda,n) [in,out]
> On entry:
> The elements on and above the diagonal are not accessed.
> The elements below the diagonal represent the unit
> lower-trapezoidal blocked matrix V computed by DLATSQR
> that defines the input matrices Q_in(k) (ones on the
> diagonal are not stored) (same format as the output A
> below the diagonal in DLATSQR).
> On exit:
> The array A contains an M-by-N orthonormal matrix Q_out,
> i.e the columns of A are orthogonal unit vectors.

Lda : Integer [in]
> The leading dimension of the array A.  LDA >= max(1,M).

T : Double Precision Array, [in]
> dimension (LDT, N * NIRB)
> where NIRB = Number_of_input_row_blocks
> = MAX( 1, CEIL((M-N)/(MB-N)) )
> Let NICB = Number_of_input_col_blocks
> = CEIL(N/NB)
> The upper-triangular block reflectors used to define the
> input matrices Q_in(k), k=(1:NIRB*NICB). The block
> reflectors are stored in compact form in NIRB block
> reflector sequences. Each of NIRB block reflector sequences
> is stored in a larger NB-by-N column block of T and consists
> of NICB smaller NB-by-NB upper-triangular column blocks.
> (same format as the output T in DLATSQR).

Ldt : Integer [in]
> The leading dimension of the array T.
> LDT >= max(1,min(NB1,N)).

Work : (workspace) Double Precision Array, Dimension (max(2,lwork)) [out]
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.

Lwork : Integer [in]
> The dimension of the array WORK.  LWORK >= (M+NB)*N.
> If LWORK = -1, then a workspace query is assumed.
> The routine only calculates the optimal size of the WORK
> array, returns this value as the first entry of the WORK
> array, and no error message related to LWORK is issued
> by XERBLA.

Info : Integer [out]
> = 0:  successful exit
> < 0:  if INFO = -i, the i-th argument had an illegal value

