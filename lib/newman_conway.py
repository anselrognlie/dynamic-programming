

# Time complexity: ?
# Space Complexity: ?
def newman_conway(num):
    """ Returns a list of the Newman Conway numbers for the given value.
        Time Complexity: O(n) where n is the number of terms
        Space Complexity: O(n) where n is the number of terms
                          a little wiggle since stringifying the ints will get
                          longer the larger the terms
    """
    if num < 1:
        raise ValueError

    if num == 1:
        nums = [1]
    else:        
        nums = [1] * num

    for i in range(3, num + 1):
        p_nm1 = nums[i - 1 - 1]
        p_p_nm1 = nums[p_nm1 - 1]
        p_nmp_nm1 = nums[i - p_nm1 - 1]
        nums[i - 1] = p_p_nm1 + p_nmp_nm1

    return " ".join(map(str, nums))
