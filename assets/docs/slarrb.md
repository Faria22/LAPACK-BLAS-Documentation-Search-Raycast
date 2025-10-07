```fortran  
subroutine slarrb (  
n,  
d,  
lld,  
ifirst,  
ilast,  
rtol1,  
*                          rtol2,  
offset,  
w,  
wgap,  
werr,  
work,  
iwork,  
*                          pivmin,  
spdiam,  
twist,  
info  
)  
```  
  
Given the relatively robust representation(RRR) L D L^T, SLARRB  
does "limited" bisection to refine the eigenvalues of L D L^T,  
W( IFIRST-OFFSET ) through W( ILAST-OFFSET ), to more accuracy. Initial  
guesses for these eigenvalues are input in W, the corresponding estimate  
of the error in these guesses and their gaps are input in WERR  
and WGAP, respectively. During bisection, intervals  
[left, right] are maintained by storing their mid-points and  
semi-widths in the arrays W and WERR respectively.  
  
## Parameters  
N : Integer [in]  
> The order of the matrix.  
  
D : Real Array, Dimension (n) [in]  
> The N diagonal elements of the diagonal matrix D.  
  
Lld : Real Array, Dimension (n-1) [in]  
  
Ifirst : Integer [in]  
> The index of the first eigenvalue to be computed.  
  
Ilast : Integer [in]  
> The index of the last eigenvalue to be computed.  
  
Rtol1 : Real [in]  
  
Rtol2 : Real [in]  
> Tolerance for the convergence of the bisection intervals.  
> An interval [LEFT,RIGHT] has converged if  
> where GAP is the (estimated) distance to the nearest  
> eigenvalue.  
  
Offset : Integer [in]  
> Offset for the arrays W, WGAP and WERR, i.e., the IFIRST-OFFSET  
> through ILAST-OFFSET elements of these arrays are to be used.  
  
W : Real Array, Dimension (n) [in,out]  
> On input, W( IFIRST-OFFSET ) through W( ILAST-OFFSET ) are  
> estimates of the eigenvalues of L D L^T indexed IFIRST through  
> ILAST.  
> On output, these estimates are refined.  
  
Wgap : Real Array, Dimension (n-1) [in,out]  
> On input, the (estimated) gaps between consecutive  
> eigenvalues of L D L^T, i.e., WGAP(I-OFFSET) is the gap between  
> eigenvalues I and I+1. Note that if IFIRST = ILAST  
> then WGAP(IFIRST-OFFSET) must be set to ZERO.  
> On output, these gaps are refined.  
  
Werr : Real Array, Dimension (n) [in,out]  
> On input, WERR( IFIRST-OFFSET ) through WERR( ILAST-OFFSET ) are  
> the errors in the estimates of the corresponding elements in W.  
> On output, these errors are refined.  
  
Work : Real Array, Dimension (2*n) [out]  
> Workspace.  
  
Iwork : Integer Array, Dimension (2*n) [out]  
> Workspace.  
  
Pivmin : Real [in]  
> The minimum pivot in the Sturm sequence.  
  
Spdiam : Real [in]  
> The spectral diameter of the matrix.  
  
Twist : Integer [in]  
> The twist index for the twisted factorization that is used  
> for the negcount.  
> TWIST = N: Compute negcount from L D L^T - LAMBDA I = L+ D+ L+^T  
> TWIST = 1: Compute negcount from L D L^T - LAMBDA I = U- D- U-^T  
> TWIST = R: Compute negcount from L D L^T - LAMBDA I = N(r) D(r) N(r)  
  
Info : Integer [out]  
> Error flag.  
  
