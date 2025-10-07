```fortran  
subroutine dsb2st_kernels (  
uplo,  
wantz,  
ttype,  
*                                   st,  
ed,  
sweep,  
n,  
nb,  
ib,  
*                                   a,  
lda,  
v,  
tau,  
ldvt,  
work  
)  
```  
  
DSB2ST_KERNELS is an internal routine used by the DSYTRD_SB2ST  
subroutine.  
  
## Parameters  
Uplo : Character*1 [in]  
  
Wantz : Logical Which Indicate If Eigenvalue Are Requested or Both [in]  
> Eigenvalue/Eigenvectors.  
  
Ttype : Integer [in]  
  
St : Integer [in]  
> internal parameter for indices.  
  
Ed : Integer [in]  
> internal parameter for indices.  
  
Sweep : Integer [in]  
> internal parameter for indices.  
  
N : Integer. The Order of the Matrix A. [in]  
  
Nb : Integer. The Size of the Band. [in]  
  
Ib : Integer. [in]  
  
A : Double Precision Array. A Pointer To the Matrix A. [in, out]  
  
Lda : Integer. The Leading Dimension of the Matrix A. [in]  
  
V : Double Precision Array, Dimension 2*n If Eigenvalues Only Are [out]  
> requested or to be queried for vectors.  
  
Tau : Double Precision Array, Dimension (2*n). [out]  
> The scalar factors of the Householder reflectors are stored  
> in this array.  
  
Ldvt : Integer. [in]  
  
Work : Double Precision Array. Workspace of Size Nb. [out]  
  
