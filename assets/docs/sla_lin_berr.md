```fortran  
subroutine sla_lin_berr (  
integer n,  
integer nz,  
integer nrhs,  
real, dimension(n, nrhs) res,  
real, dimension(n, nrhs) ayb,  
real, dimension(nrhs) berr  
)  
```  
  
SLA_LIN_BERR computes componentwise relative backward error from  
the formula  
max(i) ( abs(R(i)) / ( abs(op(A_s))*abs(Y) + abs(B_s) )(i) )  
where abs(Z) is the componentwise absolute value of the matrix  
or vector Z.  
  
## Parameters  
N : Integer [in]  
> The number of linear equations, i.e., the order of the  
> matrix A.  N >= 0.  
  
Nz : Integer [in]  
> guard against spuriously zero residuals. Default value is N.  
  
Nrhs : Integer [in]  
> The number of right hand sides, i.e., the number of columns  
> of the matrices AYB, RES, and BERR.  NRHS >= 0.  
  
Res : Real Array, Dimension (n,nrhs) [in]  
> The residual matrix, i.e., the matrix R in the relative backward  
> error formula above.  
  
Ayb : Real Array, Dimension (n, Nrhs) [in]  
> The denominator in the relative backward error formula above, i.e.,  
> are from iterative refinement (see sla_gerfsx_extended.f).  
  
Berr : Real Array, Dimension (nrhs) [out]  
> The componentwise relative backward error from the formula above.  
  
