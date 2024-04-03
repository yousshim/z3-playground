from hypothesis import given, strategies as st

def binary_search(nums: list[int], target: int) -> int:
    """
    precondition:
        nums is sorted
    postcondition:
        binary_search(nums, target) = i where is is either the index
        of target in nums if it exists or -1 if target doesn't exist
    """
    l, r = 0, len(nums)
    i = -1
    # target should always be in the range [l, r[
    while l < r and i == -1:
        # 0 <= l <= mid < r <= len(nums)
        mid = (l + r) // 2
        if target < nums[mid]:
            # target not in range [mid, r[
            # [l', r'[ = [l, r[ - [mid, r[
            r = mid
        elif target > nums[mid]:
            # target not in range [l, mid]
            # [l', r'[ = [l, r[ - [l, mid]
            l = mid + 1
        else:
            i = mid
    return i



@given(nums = st.lists(st.integers()), target = st.integers())
def test_value_at_index_is_target(nums: list[int], target: int):
    nums.append(target)
    nums.sort()
    index = binary_search(nums, target)
    assert nums[index] == target


@given(nums = st.lists(st.integers()), target = st.integers())
def test_target_no_found(nums: list[int], target: int):
    if target in nums:
        nums.remove(target)
    nums.sort()
    index = binary_search(nums, target)
    assert index == -1


if __name__ == "__main__":
    test_value_at_index_is_target()
    test_target_no_found()
