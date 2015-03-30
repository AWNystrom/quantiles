from random import randint

def swap(l, a, b):
	t = l[a]
	l[a] = l[b]
	l[b] = t
	
def partition(l, left, right, p_idx):
	"""
	Used by quicksort and quickselect.
	
	l: the entire list
	
	left: the smallest index to partition
	
	right: the largest index to partition
	
	p_idx: the pivit's initial index
	
	Returns the pivot's final index. The value in this position 
	will be in its sorted position.
	"""
	p_val = l[p_idx]
	store_idx = left
	swap(l, p_idx, right)
	for i in xrange(left, right):
		if l[i] <= p_val:
			swap(l, i, store_idx)
			store_idx += 1
	swap(l, store_idx, right)
	return store_idx
	
def sort(l, a, b):
	"""Quicksort. Sort's a list l in place. initialize with a=0 and b=len(l)-1"""
	if a < b:
		p_idx = randint(a,b)
		p_idx = partition(l, a, b, p_idx)
		sort(l, a, p_idx-1)
		sort(l, p_idx+1, b)

def select(l, a, b, i):
	"""Returns the ith smallest element in the list in linear time."""
	if a < b:
		p_idx = randint(a,b)
		p_idx = partition(l, a, b, p_idx)
		if p_idx == i:
			return l[p_idx]
		elif p_idx > i:
			#go into the left side
			return select(l, a, p_idx-1, i)
		else:
			#go into the right side
			return select(l, p_idx+1, b, i)
	elif a >= 0:
		return l[a]

class disk_quick_select(list_gen, i):
		from disk_dict import DiskDict
		from tempfile import mkdtemp
		location = mkdtemp()
		self.dd = DiskDict(location)
		for i, val in enumerate(list_gen):
			self.dd[i] = val
		self.n = i
		return select(self.dd, 0, self.n, 1.*self.n//2)

def quantile_via_bin_search(l, q, tol):
    low, high = None, None
    n = 0
    for item in l:
        n += 1
        if item < low or low is None:
            low = item
        if item > high or high is None:
            high = item
    
    #Now binary searh for the quantile
    guess = 1.*(high - low)/2 + low
    prev_guess = None
    while True:
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
