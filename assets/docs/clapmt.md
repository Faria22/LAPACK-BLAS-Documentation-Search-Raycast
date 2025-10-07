```fortran  
subroutine clapmt (  
logical forwrd,  
integer m,  
integer n,  
complex, dimension(ldx, *) x,  
integer ldx,  
integer, dimension(*) k  
)  
```  
  
CLAPMT rearranges the columns of the M by N matrix X as specified  
by the permutation K(1),K(2),...,K(N) of the integers 1,...,N.  
If FORWRD = .TRUE.,  forward permutation:  
  
X(*,K(J)) is moved X(*,J) for J = 1,2,...,N.  
  
If FORWRD = .FALSE., backward permutation:  
  
X(*,J) is moved to X(*,K(J)) for J = 1,2,...,N.  
  
## Parameters  
Forwrd : Logical [in]  
> = .TRUE., forward permutation  
> = .FALSE., backward permutation  
  
M : Integer [in]  
> The number of rows of the matrix X. M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix X. N >= 0.  
  
X : Complex Array, Dimension (ldx,n) [in,out]  
> On entry, the M by N matrix X.  
> On exit, X contains the permuted matrix X.  
  
Ldx : Integer [in]  
> The leading dimension of the array X, LDX >= MAX(1,M).  
  
K : Integer Array, Dimension (n) [in,out]  
> On entry, K contains the permutation vector. K is used as  
> internal workspace, but reset to its original value on  
> output.  
  
