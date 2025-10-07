```fortran  
subroutine sstebz (  
range,  
order,  
n,  
vl,  
vu,  
il,  
iu,  
abstol,  
d,  
e,  
*                          m,  
nsplit,  
w,  
iblock,  
isplit,  
work,  
iwork,  
*                          info  
)  
```  
  
SSTEBZ computes the eigenvalues of a symmetric tridiagonal  
matrix T.  The user may ask for all eigenvalues, all eigenvalues  
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
  
Vl : Real [in]  
> If RANGE='V', the lower bound of the interval to  
> be searched for eigenvalues.  Eigenvalues less than or equal  
> to VL, or greater than VU, will not be returned.  VL < VU.  
> Not referenced if RANGE = 'A' or 'I'.  
  
Vu : Real [in]  
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
  
Abstol : Real [in]  
> The absolute tolerance for the eigenvalues.  An eigenvalue  
> (or cluster) is considered to be located if it has been  
> determined to lie in an interval whose width is ABSTOL or  
> will be used, where |T| means the 1-norm of T.  
> Eigenvalues will be computed most accurately when ABSTOL is  
  
D : Real Array, Dimension (n) [in]  
> The n diagonal elements of the tridiagonal matrix T.  
  
E : Real Array, Dimension (n-1) [in]  
> The (n-1) off-diagonal elements of the tridiagonal matrix T.  
  
M : Integer [out]  
> The actual number of eigenvalues found. 0 <= M <= N.  
> (See also the description of INFO=2,3.)  
  
Nsplit : Integer [out]  
> The number of diagonal blocks in the matrix T.  
> 1 <= NSPLIT <= N.  
  
W : Real Array, Dimension (n) [out]  
> On exit, the first M elements of W will contain the  
> eigenvalues.  (SSTEBZ may use the remaining N-M elements as  
> workspace.)  
  
Iblock : Integer Array, Dimension (n) [out]  
> At each row/column j where E(j) is zero or small, the  
> matrix T is considered to split into a block diagonal  
> matrix.  On exit, if INFO = 0, IBLOCK(i) specifies to which  
> block (from 1 to the number of blocks) the eigenvalue W(i)  
> belongs.  (SSTEBZ may use the remaining N-M elements as  
> workspace.)  
  
Isplit : Integer Array, Dimension (n) [out]  
> The splitting points, at which T breaks up into submatrices.  
> The first submatrix consists of rows/columns 1 to ISPLIT(1),  
> the second of rows/columns ISPLIT(1)+1 through ISPLIT(2),  
> etc., and the NSPLIT-th consists of rows/columns  
> ISPLIT(NSPLIT-1)+1 through ISPLIT(NSPLIT)=N.  
> (Only the first NSPLIT elements will actually be used, but  
> since the user cannot know a priori what value NSPLIT will  
> have, N words must be reserved for ISPLIT.)  
  
Work : Real Array, Dimension (4*n) [out]  
  
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
  
