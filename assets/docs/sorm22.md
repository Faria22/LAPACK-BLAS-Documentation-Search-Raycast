```fortran  
subroutine sorm22 (  
side,  
trans,  
m,  
n,  
n1,  
n2,  
q,  
ldq,  
c,  
ldc,  
*    $                   work,  
lwork,  
info  
)  
```  
## Parameters  
Side : Character*1 [in]  
  
Trans : Character*1 [in]  
> = 'N':  apply Q (No transpose);  
  
M : Integer [in]  
> The number of rows of the matrix C. M >= 0.  
  
N : Integer [in]  
> The number of columns of the matrix C. N >= 0.  
  
N2 : Integer [in] N1  
*> \param[in]  
> N2 is INTEGER  
> The dimension of Q12 and Q21, respectively. N1, N2 >= 0.  
> The following requirement must be satisfied:  
> N1 + N2 = M if SIDE = 'L' and N1 + N2 = N if SIDE = 'R'.  
  
Q : Real Array, Dimension [in]  
> (LDQ,M) if SIDE = 'L'  
> (LDQ,N) if SIDE = 'R'  
  
Ldq : Integer [in]  
> The leading dimension of the array Q.  
> LDQ >= max(1,M) if SIDE = 'L'; LDQ >= max(1,N) if SIDE = 'R'.  
  
C : Real Array, Dimension (ldc,n) [in,out]  
> On entry, the M-by-N matrix C.  
  
Ldc : Integer [in]  
> The leading dimension of the array C. LDC >= max(1,M).  
  
Work : Real Array, Dimension (max(1,lwork)) [out]  
> On exit, if INFO = 0, WORK(1) returns the optimal LWORK.  
  
Lwork : Integer [in]  
> The dimension of the array WORK.  
> If SIDE = 'L', LWORK >= max(1,N);  
> if SIDE = 'R', LWORK >= max(1,M).  
> If LWORK = -1, then a workspace query is assumed; the routine  
> only calculates the optimal size of the WORK array, returns  
> this value as the first entry of the WORK array, and no error  
> message related to LWORK is issued by XERBLA.  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
  
