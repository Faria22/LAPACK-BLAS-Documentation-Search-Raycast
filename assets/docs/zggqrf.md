```fortran  
subroutine zggqrf (  
n,  
m,  
p,  
a,  
lda,  
taua,  
b,  
ldb,  
taub,  
work,  
*                          lwork,  
info  
)  
```  
  
ZGGQRF computes a generalized QR factorization of an N-by-M matrix A  
and an N-by-P matrix B:  
  
A = Q*R,        B = Q*T*Z,  
  
where Q is an N-by-N unitary matrix, Z is a P-by-P unitary matrix,  
and R and T assume one of the forms:  
  
if N >= M,  R = ( R11 ) M  ,   or if N < M,  R = ( R11  R12 ) N,  
(  0  ) N-M                         N   M-N  
M  
  
where R11 is upper triangular, and  
  
if N <= P,  T = ( 0  T12 ) N,   or if N > P,  T = ( T11 ) N-P,  
P-N  N                           ( T21 ) P  
P  
  
where T12 or T21 is upper triangular.  
  
In particular, if B is square and nonsingular, the GQR factorization  
of A and B implicitly gives the QR factorization of inv(B)*A:  
  
inv(B)*A = Z**H * (inv(T)*R)  
  
where inv(B) denotes the inverse of the matrix B, and Z**H denotes the  
conjugate transpose of matrix Z.  
  
## Parameters  
N : Integer [in]  
> The number of rows of the matrices A and B. N >= 0.  
  
M : Integer [in]  
> The number of columns of the matrix A.  M >= 0.  
  
P : Integer [in]  
> The number of columns of the matrix B.  P >= 0.  
  
A : Complex*16 Array, Dimension (lda,m) [in,out]  
> On entry, the N-by-M matrix A.  
> On exit, the elements on and above the diagonal of the array  
> contain the min(N,M)-by-M upper trapezoidal matrix R (R is  
> upper triangular if N >= M); the elements below the diagonal,  
> with the array TAUA, represent the unitary matrix Q as a  
> product of min(N,M) elementary reflectors (see Further  
> Details).  
  
Lda : Integer [in]  
> The leading dimension of the array A. LDA >= max(1,N).  
  
Taua : Complex*16 Array, Dimension (min(n,m)) [out]  
> The scalar factors of the elementary reflectors which  
> represent the unitary matrix Q (see Further Details).  
  
B : Complex*16 Array, Dimension (ldb,p) [in,out]  
> On entry, the N-by-P matrix B.  
> On exit, if N <= P, the upper triangle of the subarray  
> B(1:N,P-N+1:P) contains the N-by-N upper triangular matrix T;  
> if N > P, the elements on and above the (N-P)-th subdiagonal  
> contain the N-by-P upper trapezoidal matrix T; the remaining  
> elements, with the array TAUB, represent the unitary  
> matrix Z as a product of elementary reflectors (see Further  
> Details).  
  
Ldb : Integer [in]  
> The leading dimension of the array B. LDB >= max(1,N).  
  
Taub : Complex*16 Array, Dimension (min(n,p)) [out]  
> The scalar factors of the elementary reflectors which  
> represent the unitary matrix Z (see Further Details).  
  
Work : Complex*16 Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> The dimension of the array WORK. LWORK >= max(1,N,M,P).  
> where NB1 is the optimal blocksize for the QR factorization  
> of an N-by-M matrix, NB2 is the optimal blocksize for the  
> RQ factorization of an N-by-P matrix, and NB3 is the optimal  
> blocksize for a call of ZUNMQR.  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value.  
  
