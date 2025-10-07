```fortran  
subroutine slaqsp (  
character uplo,  
integer n,  
real, dimension(*) ap,  
real, dimension(*) s,  
real scond,  
real amax,  
character equed  
)  
```  
  
SLAQSP equilibrates a symmetric matrix A using the scaling factors  
in the vector S.  
  
## Parameters  
Uplo : Character*1 [in]  
> Specifies whether the upper or lower triangular part of the  
> symmetric matrix A is stored.  
> = 'U':  Upper triangular  
> = 'L':  Lower triangular  
  
N : Integer [in]  
> The order of the matrix A.  N >= 0.  
  
Ap : Real Array, Dimension (n*(n+1)/2) [in,out]  
> On entry, the upper or lower triangle of the symmetric matrix  
> A, packed columnwise in a linear array.  The j-th column of A  
> is stored in the array AP as follows:  
> the same storage format as A.  
  
S : Real Array, Dimension (n) [in]  
> The scale factors for A.  
  
Scond : Real [in]  
> Ratio of the smallest S(i) to the largest S(i).  
  
Amax : Real [in]  
> Absolute value of largest matrix entry.  
  
Equed : Character*1 [out]  
> Specifies whether or not equilibration was done.  
> = 'N':  No equilibration.  
> = 'Y':  Equilibration was done, i.e., A has been replaced by  
  
