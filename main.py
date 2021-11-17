def medians(nums1, nums2):
    lst = []
    i=0
    j=0
    n=len(nums1)
    m=len(nums2)
    while i<n or j<m:
        if i<n and j<m:
            if nums1[i]<=nums2[j]:
                lst.append(nums1[i])
                i+=1
            else:
                lst.append(nums2[j])
                j+=1
        elif i<n:
            lst.append(nums1[i])
            i+=1
        else:
            lst.append(nums2[j])
            j+=1
    return (lst[(int)((n+m)/2)]+lst[(int)((n+m)/2)-1+(n+m)%2])/2

