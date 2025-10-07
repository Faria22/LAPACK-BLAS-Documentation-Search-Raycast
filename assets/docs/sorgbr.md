```fortran  
subroutine sorgbr (  
character vect,  
integer m,  
integer n,  
integer k,  
real, dimension(lda, *) a,  
integer lda,  
real, dimension(*) tau,  
real, dimension(*) work,  
integer lwork,  
integer info  
)  
```  
  
SORGBR generates one of the real orthogonal matrices Q or P**T  
determined by SGEBRD when reducing a real matrix A to bidiagonal  
form: A = Q * B * P**T.  Q and P**T are defined as products of  
elementary reflectors H(i) or G(i) respectively.  
  
If VECT = 'Q', A is assumed to have been an M-by-K matrix, and Q  
is of order M:  
if m >= k, Q = H(1) H(2) . . . H(k) and SORGBR returns the first n  
columns of Q, where m >= n >= k;  
if m < k, Q = H(1) H(2) . . . H(m-1) and SORGBR returns Q as an  
M-by-M matrix.  
  
If VECT = 'P', A is assumed to have been a K-by-N matrix, and P**T  
is of order N:  
if k < n, P**T = G(k) . . . G(2) G(1) and SORGBR returns the first m  
rows of P**T, where n >= m >= k;  
if k >= n, P**T = G(n-1) . . . G(2) G(1) and SORGBR returns P**T as  
an N-by-N matrix.  
  
## Parameters  
Vect : Character*1 [in]  
> required, as defined in the transformation applied by SGEBRD:  
> = 'Q':  generate Q;  
  
M : Integer [in]  
> M >= 0.  
  
N : Integer [in]  
> N >= 0.  
> If VECT = 'Q', M >= N >= min(M,K);  
> if VECT = 'P', N >= M >= min(N,K).  
  
K : Integer [in]  
> If VECT = 'Q', the number of columns in the original M-by-K  
> matrix reduced by SGEBRD.  
> If VECT = 'P', the number of rows in the original K-by-N  
> matrix reduced by SGEBRD.  
> K >= 0.  
  
A : Real Array, Dimension (lda,n) [in,out]  
> On entry, the vectors which define the elementary reflectors,  
> as returned by SGEBRD.  
  
Lda : Integer [in]  
> The leading dimension of the array A. LDA >= max(1,M).  
  
Tau : Real Array, Dimension [in]  
> (min(M,K)) if VECT = 'Q'  
> (min(N,K)) if VECT = 'P'  
> TAU(i) must contain the scalar factor of the elementary  
> returned by SGEBRD in its array argument TAUQ or TAUP.  
  
Work : Real Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> The dimension of the array WORK. LWORK >= max(1,min(M,N)).  
> is the optimal blocksize.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
