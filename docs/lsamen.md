# LSAMEN

## Function Signature

```fortran
LSAMEN(N, CA, CB)
```

## Description


 LSAMEN  tests if the first N letters of CA are the same as the
 first N letters of CB, regardless of case.
 LSAMEN returns .TRUE. if CA and CB are equivalent except for case
 and .FALSE. otherwise.  LSAMEN also returns .FALSE. if LEN( CA )
 or LEN( CB ) is less than N.

## Parameters

### N (in)

N is INTEGER The number of characters in CA and CB to be compared.

### CA (in)

CA is CHARACTER*(*)

### CB (in)

CB is CHARACTER*(*) CA and CB specify two character strings of length at least N. Only the first N characters of each string will be accessed.

