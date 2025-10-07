```fortran  
subroutine dopmtr (  
side,  
uplo,  
trans,  
m,  
n,  
ap,  
tau,  
c,  
ldc,  
work,  
*                          info  
)  
```  
  
DOPMTR overwrites the general real M-by-N matrix C with  
  
SIDE = 'L'     SIDE = 'R'  
TRANS = 'N':      Q * C          C * Q  
TRANS = 'T':      Q**T * C       C * Q**T  
  
where Q is a real orthogonal matrix of order nq, with nq = m if  
SIDE = 'L' and nq = n if SIDE = 'R'. Q is defined as the product of  
nq-1 elementary reflectors, as returned by DSPTRD using packed  
storage:  
  
if UPLO = 'U', Q = H(nq-1) . . . H(2) H(1);  
  
if UPLO = 'L', Q = H(1) H(2) . . . H(nq-1).  
  
## Parameters  
Side : Character*1 [in]  
  
Uplo : Character*1 [in]  
> = 'U': Upper triangular packed storage used in previous  
> call to DSPTRD;  
> = 'L': Lower triangular packed storage used in previous  
> call to DSPTRD.  
  
Trans : Character*1 [in]  
> = 'N':  No transpose, apply Q;  
  
M : Integer [in]  
> The number of rows of the matrix C. M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix C. N >= 0.  
  
Ap : Double Precision Array, Dimension [in]  
> The vectors which define the elementary reflectors, as  
> returned by DSPTRD.  AP is modified by the routine but  
> restored on exit.  
  
Tau : Double Precision Array, Dimension (m-1) If Side = 'l' [in]  
> or (N-1) if SIDE = 'R'  
> TAU(i) must contain the scalar factor of the elementary  
> reflector H(i), as returned by DSPTRD.  
  
C : Double Precision Array, Dimension (ldc,n) [in,out]  
> On entry, the M-by-N matrix C.  
  
Ldc : Integer [in]  
> The leading dimension of the array C. LDC >= max(1,M).  
  
Work : Double Precision Array, Dimension [out]  
> (N) if SIDE = 'L'  
> (M) if SIDE = 'R'  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
