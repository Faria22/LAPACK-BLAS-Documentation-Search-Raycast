```fortran  
subroutine dlarrd (  
range,  
order,  
n,  
vl,  
vu,  
il,  
iu,  
gers,  
*                           reltol,  
d,  
e,  
e2,  
pivmin,  
nsplit,  
isplit,  
*                           m,  
w,  
werr,  
wl,  
wu,  
iblock,  
indexw,  
*                           work,  
iwork,  
info  
)  
```  
  
DLARRD computes the eigenvalues of a symmetric tridiagonal  
matrix T to suitable accuracy. This is an auxiliary code to be  
called from DSTEMR.  
The user may ask for all eigenvalues, all eigenvalues  
in the half-open interval (VL, VU], or the IL-th through IU-th  
eigenvalues.  
  
To avoid overflow, the matrix must be scaled so that its  
largest element is no greater than overflow**(1/2) * underflow**(1/4) in absolute value, and for greatest  
accuracy, it should not be much smaller than that.  
  
See W. Kahan "Accurate Eigenvalues of a Symmetric Tridiagonal  
Matrix", Report CS41, Computer Science Dept., Stanford  
University, July 21, 1966.  
  
## Parameters  
Range : Character*1 [in]  
> = 'A': ("All")   all eigenvalues will be found.  
> = 'V': ("Value") all eigenvalues in the half-open interval  
> (VL, VU] will be found.  
> = 'I': ("Index") the IL-th through IU-th eigenvalues (of the  
> entire matrix) will be found.  
  
Order : Character*1 [in]  
> = 'B': ("By Block") the eigenvalues will be grouped by  
> split-off block (see IBLOCK, ISPLIT) and  
> ordered from smallest to largest within  
> the block.  
> = 'E': ("Entire matrix")  
> the eigenvalues for the entire matrix  
> will be ordered from smallest to  
> largest.  
  
N : Integer [in]  
> The order of the tridiagonal matrix T.  N >= 0.  
  
Vl : Double Precision [in]  
> If RANGE='V', the lower bound of the interval to  
> be searched for eigenvalues.  Eigenvalues less than or equal  
> to VL, or greater than VU, will not be returned.  VL < VU.  
> Not referenced if RANGE = 'A' or 'I'.  
  
Vu : Double Precision [in]  
> If RANGE='V', the upper bound of the interval to  
> be searched for eigenvalues.  Eigenvalues less than or equal  
> to VL, or greater than VU, will not be returned.  VL < VU.  
> Not referenced if RANGE = 'A' or 'I'.  
  
Il : Integer [in]  
> If RANGE='I', the index of the  
> smallest eigenvalue to be returned.  
> 1 <= IL <= IU <= N, if N > 0; IL = 1 and IU = 0 if N = 0.  
> Not referenced if RANGE = 'A' or 'V'.  
  
Iu : Integer [in]  
> If RANGE='I', the index of the  
> largest eigenvalue to be returned.  
> 1 <= IL <= IU <= N, if N > 0; IL = 1 and IU = 0 if N = 0.  
> Not referenced if RANGE = 'A' or 'V'.  
  
Gers : Double Precision Array, Dimension (2*n) [in]  
> The N Gerschgorin intervals (the i-th Gerschgorin interval  
  
Reltol : Double Precision [in]  
> The minimum relative width of an interval.  When an interval  
> is narrower than RELTOL times the larger (in  
> magnitude) endpoint, then it is considered to be  
> sufficiently small, i.e., converged.  Note: this should  
  
D : Double Precision Array, Dimension (n) [in]  
> The n diagonal elements of the tridiagonal matrix T.  
  
E : Double Precision Array, Dimension (n-1) [in]  
> The (n-1) off-diagonal elements of the tridiagonal matrix T.  
  
E2 : Double Precision Array, Dimension (n-1) [in]  
> The (n-1) squared off-diagonal elements of the tridiagonal matrix T.  
  
Pivmin : Double Precision [in]  
> The minimum pivot allowed in the Sturm sequence for T.  
  
Nsplit : Integer [in]  
> The number of diagonal blocks in the matrix T.  
> 1 <= NSPLIT <= N.  
  
Isplit : Integer Array, Dimension (n) [in]  
> The splitting points, at which T breaks up into submatrices.  
> The first submatrix consists of rows/columns 1 to ISPLIT(1),  
> the second of rows/columns ISPLIT(1)+1 through ISPLIT(2),  
> etc., and the NSPLIT-th consists of rows/columns  
> ISPLIT(NSPLIT-1)+1 through ISPLIT(NSPLIT)=N.  
> (Only the first NSPLIT elements will actually be used, but  
> since the user cannot know a priori what value NSPLIT will  
> have, N words must be reserved for ISPLIT.)  
  
M : Integer [out]  
> The actual number of eigenvalues found. 0 <= M <= N.  
> (See also the description of INFO=2,3.)  
  
W : Double Precision Array, Dimension (n) [out]  
> On exit, the first M elements of W will contain the  
> eigenvalue approximations. DLARRD computes an interval  
> I_j = (a_j, b_j] that includes eigenvalue j. The eigenvalue  
> approximation is given as the interval midpoint  
> W(j)= ( a_j + b_j)/2. The corresponding error is bounded by  
> WERR(j) = abs( a_j - b_j)/2  
  
Werr : Double Precision Array, Dimension (n) [out]  
> The error bound on the corresponding eigenvalue approximation  
> in W.  
  
Wl : Double Precision [out]  
  
Wu : Double Precision [out]  
> The interval (WL, WU] contains all the wanted eigenvalues.  
> If RANGE='V', then WL=VL and WU=VU.  
> If RANGE='A', then WL and WU are the global Gerschgorin bounds  
> on the spectrum.  
> If RANGE='I', then WL and WU are computed by DLAEBZ from the  
> index range specified.  
  
Iblock : Integer Array, Dimension (n) [out]  
> At each row/column j where E(j) is zero or small, the  
> matrix T is considered to split into a block diagonal  
> matrix.  On exit, if INFO = 0, IBLOCK(i) specifies to which  
> block (from 1 to the number of blocks) the eigenvalue W(i)  
> belongs.  (DLARRD may use the remaining N-M elements as  
> workspace.)  
  
Indexw : Integer Array, Dimension (n) [out]  
> The indices of the eigenvalues within each block (submatrix);  
> for example, INDEXW(i)= j and IBLOCK(i)=k imply that the  
> i-th eigenvalue W(i) is the j-th eigenvalue in block k.  
  
Work : Double Precision Array, Dimension (4*n) [out]  
  
Iwork : Integer Array, Dimension (3*n) [out]  
  
Info : Integer [out]  
> = 0:  successful exit  
> < 0:  if INFO = -i, the i-th argument had an illegal value  
> > 0:  some or all of the eigenvalues failed to converge or  
> were not computed:  
> =1 or 3: Bisection failed to converge for some  
> eigenvalues; these eigenvalues are flagged by a  
> negative block number.  The effect is that the  
> eigenvalues may not be as accurate as the  
> absolute and relative tolerances.  This is  
> generally caused by unexpectedly inaccurate  
> arithmetic.  
> =2 or 3: RANGE='I' only: Not all of the eigenvalues  
> IL:IU were found.  
> Effect: M < IU+1-IL  
> Cause:  non-monotonic arithmetic, causing the  
> Sturm sequence to be non-monotonic.  
> Cure:   recalculate, using RANGE='A', and pick  
> out eigenvalues IL:IU.  In some cases,  
> increasing the PARAMETER "FUDGE" may  
> make things work.  
> = 4:    RANGE='I', and the Gershgorin interval  
> initially used was too small.  No eigenvalues  
> were computed.  
> Probable cause: your machine has sloppy  
> floating-point arithmetic.  
> Cure: Increase the PARAMETER "FUDGE",  
> recompile, and try again.  
  
