```fortran  
subroutine dsptrd (  
character uplo,  
integer n,  
double precision, dimension(*) ap,  
double precision, dimension(*) d,  
double precision, dimension(*) e,  
double precision, dimension(*) tau,  
integer info  
)  
```  
  
DSPTRD reduces a real symmetric matrix A stored in packed form to  
symmetric tridiagonal form T by an orthogonal similarity  
transformation: Q**T * A * Q = T.  
  
## Parameters  
Uplo : Character*1 [in]  
> = 'U':  Upper triangle of A is stored;  
> = 'L':  Lower triangle of A is stored.  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Ap : Double Precision Array, Dimension (n*(n+1)/2) [in,out]  
> On entry, the upper or lower triangle of the symmetric matrix  
> A, packed columnwise in a linear array.  The j-th column of A  
> is stored in the array AP as follows:  
> On exit, if UPLO = 'U', the diagonal and first superdiagonal  
> of A are overwritten by the corresponding elements of the  
> tridiagonal matrix T, and the elements above the first  
> superdiagonal, with the array TAU, represent the orthogonal  
> matrix Q as a product of elementary reflectors; if UPLO  
> = 'L', the diagonal and first subdiagonal of A are over-  
> written by the corresponding elements of the tridiagonal  
> matrix T, and the elements below the first subdiagonal, with  
> the array TAU, represent the orthogonal matrix Q as a product  
> of elementary reflectors. See Further Details.  
  
D : Double Precision Array, Dimension (n) [out]  
> The diagonal elements of the tridiagonal matrix T:  
> D(i) = A(i,i).  
  
E : Double Precision Array, Dimension (n-1) [out]  
> The off-diagonal elements of the tridiagonal matrix T:  
> E(i) = A(i,i+1) if UPLO = 'U', E(i) = A(i+1,i) if UPLO = 'L'.  
  
Tau : Double Precision Array, Dimension (n-1) [out]  
> The scalar factors of the elementary reflectors (see Further  
> Details).  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
