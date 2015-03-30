def quantile_via_bin_search(l, q, tol):
    low, high = None, None
    n = 0
    for item in l:
        n += 1
        if item < low or low is None:
            low = item
        if item > high or high is None:
            high = item
    
    #Now binary searh for the median
    guess = 1.*(high - low)/2 + low
    prev_guess = None
    while True:#high > low and abs(high-low ) < tol:
        num_higher = 0
        for item in l:
            if item >= guess:
                num_higher += 1
        if abs(num_higher-1.*n*(1-q)) < tol:
            break #Found a good enough guess
        if num_higher > 1.*n*(1-q):
            #More than half of the elements are to the left, so increase guess
            low = guess
        else:
            high = guess
        prev_guess = guess
        guess = 1.*(high - low)/2 + low
        if prev_guess is not None and guess == prev_guess:
            #In case the median is in a run
            break
    
    #Now find the element closest to guess and return it as the median.
    closest_dist, closest_elem = inf, None
    for item in l:
        dist = abs(guess-item)
        if dist < closest_dist:
            closest_dist = dist
            closest_elem = item
    return closest_elem
