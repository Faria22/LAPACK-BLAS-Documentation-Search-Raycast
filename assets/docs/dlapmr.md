```fortran  
subroutine dlapmr (  
logical forwrd,  
integer m,  
integer n,  
double precision, dimension(ldx, *) x,  
integer ldx,  
integer, dimension(*) k  
)  
```  
  
DLAPMR rearranges the rows of the M by N matrix X as specified  
by the permutation K(1),K(2),...,K(M) of the integers 1,...,M.  
If FORWRD = .TRUE.,  forward permutation:  
  
X(K(I),*) is moved X(I,*) for I = 1,2,...,M.  
  
If FORWRD = .FALSE., backward permutation:  
  
X(I,*) is moved to X(K(I),*) for I = 1,2,...,M.  
  
## Parameters  
Forwrd : Logical [in]  
> = .TRUE., forward permutation  
> = .FALSE., backward permutation  
  
M : Integer [in]  
> The number of rows of the matrix X. M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix X. N >= 0.  
  
X : Double Precision Array, Dimension (ldx,n) [in,out]  
> On entry, the M by N matrix X.  
> On exit, X contains the permuted matrix X.  
  
Ldx : Integer [in]  
> The leading dimension of the array X, LDX >= MAX(1,M).  
  
K : Integer Array, Dimension (m) [in,out]  
> On entry, K contains the permutation vector. K is used as  
> internal workspace, but reset to its original value on  
> output.  
  
