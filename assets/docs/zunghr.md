```fortran  
subroutine zunghr (  
integer n,  
integer ilo,  
integer ihi,  
complex*16, dimension(lda, *) a,  
integer lda,  
complex*16, dimension(*) tau,  
complex*16, dimension(*) work,  
integer lwork,  
integer info  
)  
```  
  
ZUNGHR generates a complex unitary matrix Q which is defined as the  
product of IHI-ILO elementary reflectors of order N, as returned by  
ZGEHRD:  
  
Q = H(ilo) H(ilo+1) . . . H(ihi-1).  
  
## Parameters  
N : Integer [in]  
> The order of the matrix Q. N >= 0.  
  
Ilo : Integer [in]  
  
Ihi : Integer [in]  
> ILO and IHI must have the same values as in the previous call  
> of ZGEHRD. Q is equal to the unit matrix except in the  
> submatrix Q(ilo+1:ihi,ilo+1:ihi).  
> 1 <= ILO <= IHI <= N, if N > 0; ILO=1 and IHI=0, if N=0.  
  
A : Complex*16 Array, Dimension (lda,n) [in,out]  
> On entry, the vectors which define the elementary reflectors,  
> as returned by ZGEHRD.  
> On exit, the N-by-N unitary matrix Q.  
  
Lda : Integer [in]  
> The leading dimension of the array A. LDA >= max(1,N).  
  
Tau : Complex*16 Array, Dimension (n-1) [in]  
> TAU(i) must contain the scalar factor of the elementary  
> reflector H(i), as returned by ZGEHRD.  
  
Work : Complex*16 Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> The dimension of the array WORK. LWORK >= IHI-ILO.  
> the optimal blocksize.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
