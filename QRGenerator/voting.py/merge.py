def merge_intervals(intervals):
    if not intervals:
        return []

    # Step 1: Sort the intervals based on the starting times
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]  # Start with the first interval

    # Step 2: Iterate through the sorted intervals
    for current in intervals[1:]:
        last_merged = merged[-1]

        # Step 3: Check if there is an overlap
        if current[0] <= last_merged[1]:
            # There is an overlap, merge the current interval
            last_merged[1] = max(last_merged[1], current[1])
        else:
            # No overlap, add the current interval
            merged.append(current)

    return merged

# Example Usage

intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
merged_intervals = merge_intervals(intervals)
print(merged_intervals)  # Output: [[1, 6], [8, 10], [15, 18]]
