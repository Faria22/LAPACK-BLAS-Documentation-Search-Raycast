```fortran  
subroutine dlarrf (  
n,  
d,  
l,  
ld,  
clstrt,  
clend,  
*                          w,  
wgap,  
werr,  
*                          spdiam,  
clgapl,  
clgapr,  
pivmin,  
sigma,  
*                          dplus,  
lplus,  
work,  
info  
)  
```  
  
Given the initial representation L D L^T and its cluster of close  
eigenvalues (in a relative measure), W( CLSTRT ), W( CLSTRT+1 ), ...  
W( CLEND ), DLARRF finds a new relatively robust representation  
L D L^T - SIGMA I = L(+) D(+) L(+)^T such that at least one of the  
eigenvalues of L(+) D(+) L(+)^T is relatively isolated.  
  
## Parameters  
N : Integer [in]  
> The order of the matrix (subblock, if the matrix split).  
  
D : Double Precision Array, Dimension (n) [in]  
> The N diagonal elements of the diagonal matrix D.  
  
L : Double Precision Array, Dimension (n-1) [in]  
> The (N-1) subdiagonal elements of the unit bidiagonal  
> matrix L.  
  
Ld : Double Precision Array, Dimension (n-1) [in]  
  
Clstrt : Integer [in]  
> The index of the first eigenvalue in the cluster.  
  
Clend : Integer [in]  
> The index of the last eigenvalue in the cluster.  
  
W : Double Precision Array, Dimension [in]  
> dimension is >=  (CLEND-CLSTRT+1)  
> The eigenvalue APPROXIMATIONS of L D L^T in ascending order.  
> W( CLSTRT ) through W( CLEND ) form the cluster of relatively  
> close eigenalues.  
  
Wgap : Double Precision Array, Dimension [in,out]  
> dimension is >=  (CLEND-CLSTRT+1)  
> The separation from the right neighbor eigenvalue in W.  
  
Werr : Double Precision Array, Dimension [in]  
> dimension is  >=  (CLEND-CLSTRT+1)  
> WERR contain the semiwidth of the uncertainty  
> interval of the corresponding eigenvalue APPROXIMATION in W  
  
Spdiam : Double Precision [in]  
> estimate of the spectral diameter obtained from the  
> Gerschgorin intervals  
  
Clgapl : Double Precision [in]  
  
Clgapr : Double Precision [in]  
> absolute gap on each end of the cluster.  
> Set by the calling routine to protect against shifts too close  
> to eigenvalues outside the cluster.  
  
Pivmin : Double Precision [in]  
> The minimum pivot allowed in the Sturm sequence.  
  
Sigma : Double Precision [out]  
> The shift used to form L(+) D(+) L(+)^T.  
  
Dplus : Double Precision Array, Dimension (n) [out]  
> The N diagonal elements of the diagonal matrix D(+).  
  
Lplus : Double Precision Array, Dimension (n-1) [out]  
> The first (N-1) elements of LPLUS contain the subdiagonal  
> elements of the unit bidiagonal matrix L(+).  
  
Work : Double Precision Array, Dimension (2*n) [out]  
> Workspace.  
  
Info : Integer [out]  
> Signals processing OK (=0) or failure (=1)  
  
