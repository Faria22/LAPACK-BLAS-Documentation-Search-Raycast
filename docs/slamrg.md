# SLAMRG

## Function Signature

```fortran
SLAMRG(N1, N2, A, STRD1, STRD2, INDEX)
```

## Description


 SLAMRG will create a permutation list which will merge the elements
 of A (which is composed of two independently sorted sets) into a
 single set which is sorted in ascending order.

## Parameters

### N1 (in)

N1 is INTEGER

### N2 (in)

N2 is INTEGER These arguments contain the respective lengths of the two sorted lists to be merged.

### A (in)

A is REAL array, dimension (N1+N2) The first N1 elements of A contain a list of numbers which are sorted in either ascending or descending order. Likewise for the final N2 elements.

### STRD1 (in)

STRD1 is INTEGER

### STRD2 (in)

STRD2 is INTEGER These are the strides to be taken through the array A. Allowable strides are 1 and -1. They indicate whether a subset of A is sorted in ascending (STRDx = 1) or descending (STRDx = -1) order.

### INDEX (out)

INDEX is INTEGER array, dimension (N1+N2) On exit this array will contain a permutation such that if B( I ) = A( INDEX( I ) ) for I=1,N1+N2, then B will be sorted in ascending order.

