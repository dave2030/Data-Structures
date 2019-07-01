'''
----------------------------------------------
[program description]
----------------------------------------------
Author: Shyam Dave
ID: 180332030
Email: dave2030@mylaurier.ca
__updated__="2019-02-01"
----------------------------------------------
'''
from copy import deepcopy


class List:

    def __init__(self):
        """
        -------------------------------------------------------
        Initializes an empty list.
        Use: target = List()
        -------------------------------------------------------
        Returns:
            a new List object (List)
        -------------------------------------------------------
        """
        self._values = []

    def __getitem__(self, i):
        """
        -------------------------------------------------------
        Returns a copy of the nth element of the list.
        Use: value = source[i]
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
        Returns:
            value - the i-th element of list (?)
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value' 
        value=deepcopy(self._values[i])
        

        return value
 
    def __len__(self):
        """
        -------------------------------------------------------
        Returns the number of values in the list.
        Use: n = len(source)
        -------------------------------------------------------
        Returns:
            the number of values in the list.
        -------------------------------------------------------
        """
        # Your code here

        return len(self._values)

    def __setitem__(self, i, value):
        """
        -------------------------------------------------------
        The i-th element of list contains a copy of value. The existing
        value at i is overwritten.
        Use: source[i] = value
        -------------------------------------------------------
        Parameters:
            i - index of the element to access (int)
            value - a data value (?)
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index value'
        self._values[i]=deepcopy(value)

        return
    def __contains__(self, key):
        """
        ---------------------------------------------------------
        Determines if the list contains key.
        Use: b = key in source
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            True if the list contains key, False otherwise. (boolean)
        -------------------------------------------------------
        """
        i=self._linear_search(key)
        return i>-1
    def _is_valid_index(self, i):
        """
        -------------------------------------------------------
        Private helper method to validate an index value.
        Python index values can be positive or negative and range from
          -len(list) to len(list) - 1
        Use: assert self._is_valid_index(i)
        -------------------------------------------------------
        Parameters:
            i - an index value (int)
        Returns:
            True if i is a valid index, False otherwise.
        -------------------------------------------------------
        """
        if i<len(self._values) or i>=-len(self._values):
            x=True
        else:
            x=False

        return x

    def _linear_search(self, key):
        """
        -------------------------------------------------------
        Searches for the first occurrence of key in the list.
        Private helper method - used only by other ADT methods.
        Use: i = self._linear_search(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of key in the list, -1 if key is not found (int)
        -------------------------------------------------------
        """
        i = -1
        check = 0
        found = False
        while check < len(self._values) and found == False:
            if self._values[check] == key:
                i = check
                found = True
            else:
                i = -1
            check += 1
        return i

    def _swap(self, i, j):
        """
        -------------------------------------------------------
        Swaps the position of two elements in the data list.
        The element originally at position i is now at position j,
        and visa versa.
        Private helper operations called only from within class.
        Use: self._swap(i, j)
        -------------------------------------------------------
        Parameters:
            i - index of one element to switch (int, 0 <= i < len(self._values))
            j - index of other element to switch (int, 0 <= j < len(self._values))
        Returns:
            None
        -------------------------------------------------------
        """
        assert self._is_valid_index(i), 'Invalid index i'
       

    def append(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the end of the List.
        Use: source.append(value)
        -------------------------------------------------------
        Parameters:
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.append(deepcopy(value))

        return

    def apply(self, func):
        """
        -------------------------------------------------------
        Applies an external function to every value in list.
        Use: source.apply(func)
        -------------------------------------------------------
        Parameters:
          func - a function that takes a single value as a parameter 
              and returns a value (function)
        Returns:
            None
        -------------------------------------------------------
        """
        # Your code here

        return

    def clean(self):
        """
        ---------------------------------------------------------
        The list contains one and only one of each value formerly present
        in the list. The first occurrence of each value is preserved.
        Use: source.clean()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
        x=0
        while x<len(self._values):
            if self._values[x] in self._values[:x]:
                self._values.pop(x)
            else:
                x+=1
        return

    def combine(self, source1, source2):
        """
        -------------------------------------------------------
        Combines two source lists into the current target list. 
        When finished, the contents of source1 and source2 are interlaced 
        into target and source1 and source2 are empty.
        Order of source values is preserved.
        Use: target.combine(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (List)
            source2 - an array-based list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        while not source1.is_empty() and not source2.is_empty():
            self._values.append(source1.pop(0))
            self._values.append(source2.pop(0))
        while not source1.is_empty():
            self._values.append(source1.pop(0))
        while not source2.is_empty():
            self._values.append(source2.pop(0))
        return

    def copy(self):
        """
        -------------------------------------------------------
        Duplicates the current list to a new list in the same order.
        Use: target = source.copy()
        -------------------------------------------------------
        Returns:
            target - a copy of self (List)
        -------------------------------------------------------
        """
       
    def count(self, key):
        """
        -------------------------------------------------------
        Finds the number of times key appears in list.
        Use: n = source.count(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            number - number of times key appears in list (int)
        -------------------------------------------------------
        """
        number=0
        for x in range(len(self._values)):
            if self._values[x]==key:
                number+=1
        return number

    def find(self, key):
        """
        -------------------------------------------------------
        Finds and returns a copy of the first value in list that matches key.
        Use: value = source.find(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - a copy of the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        value=None
        if len(self._values)>0:
            check = self._linear_search(key)
            if check==-1:
                value=None
            else:
                value=deepcopy(self._values[check])
        return value

        

    def index(self, key):
        """
        -------------------------------------------------------
        Finds location of a value by key in list.
        Use: n = source.index(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            i - the index of the location of key in the list, -1 if
              key is not in the list. (int)
        -------------------------------------------------------
        """
        i=self._linear_search(key)
        return i
    def insert(self, i, value):
        """
        -------------------------------------------------------
        A copy of value is added to index i, following values are pushed right.
        If i outside of range of -len(list) to len(list) - 1, the value is 
        prepended or appended as appropriate.
        Use: source.insert(i, value)
        -------------------------------------------------------
        Parameters:
            i - index value (int)
            value - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """   
        self._values[:] = self._values[:i] + [deepcopy(value)] + self._values[i:]
        

    def intersection(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with values that appear in both
        source1 and source2. Values do not repeat.
        Use: target.intersection(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (List)
            source2 - an array-based list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        for x in source1:
            if x in source2:
                if x not in self._values:
                    self._values.append(x)
        
        
        
        return

    def is_empty(self):
        """
        -------------------------------------------------------
        Determines if the list is empty.
        Use: b = source.is_empty()
        -------------------------------------------------------
        Returns:
            True if the list is empty, False otherwise.
        -------------------------------------------------------
        """
        return len(self._values)==0

        

    def is_identical(self, target):
        """
        ---------------------------------------------------------
        Determines whether two lists are is_identical, i.e. same values 
        appear in the same locations in both lists. 
        (iterative version)
        Use: b = source.is_identical(target)
        -------------------------------------------------------
        Parameters:
            target - another list (List)
        Returns:
            identical - True if this list contains the same values
                as target in the same order, otherwise False. (boolean)
        -------------------------------------------------------
        """
        identical=True
        x=0
        if len(self._values)==len(target._values):
            while x<len(self._values) and identical:
                if self._values[x]==target._values[x]:
                    x+=1
                else:
                    identical=False
        else:
            identical=False
        return identical

    def max(self):
        """
        -------------------------------------------------------
        Finds the maximum value in list.
        Use: value = source.max()
        -------------------------------------------------------
        Returns:
            value - a copy of the maximum value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find maximum of an empty list'

        value=self._values[0]
        for x in range(len(self._values)):
            if self._values[x]>value:
                value=deepcopy(self._values[x])
        return value

    def min(self):
        """
        -------------------------------------------------------
        Finds the minimum value in list.
        Use: value = source.min()
        -------------------------------------------------------
        Returns:
            value - a copy of the minimum value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot find minimum of an empty list'

        value=self._values[0]
        for x in range(len(self._values)):
            if self._values[x]<value:
                value=deepcopy(self._values[x])
        return value

        

    def peek(self):
        """
        -------------------------------------------------------
        Returns a copy of the first value in list.
        Use: value = source.peek()
        -------------------------------------------------------
        Returns:
            value - a copy of the first value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot peek at an empty list'

        value=deepcopy(self._values[0])

        return value

    def pop(self, *args):
        """
        -------------------------------------------------------
        Finds, removes, and returns the value in list whose index matches i.
        Use: value = source.pop()
        Use: value = source.pop(i)
        -------------------------------------------------------
        Parameters:
            args - an array of arguments (tuple of int)
            args[0], if it exists, is the index i
        Returns:
            value - if args exists, the value at position args[0], 
                otherwise the last value in the list, value is 
                removed from the list (?)
        -------------------------------------------------------
        """
        assert len(self._values) > 0, "Cannot pop from an empty list"
        assert len(args) <= 1, "No more than 1 argument allowed"

        if len(args) == 1:
            # pop the element at position i
            i = args[0]
            value = self._values.pop(i)
        else:
            # pop the last element
            value = self._values.pop()
        return value

    def prepend(self, value):
        """
        -------------------------------------------------------
        Adds a copy of value to the front of the List.
        Use: source.prepend(value)
        -------------------------------------------------------
        Parameters:
            value - a data element. (?)
        Returns:
            None
        -------------------------------------------------------
        """
        self._values.insert(0,deepcopy(value))

        return

    def remove(self, key):
        """
        -------------------------------------------------------
        Finds, removes, and returns the first value in list that matches key.
        Use: value = source.remove(key)
        -------------------------------------------------------
        Parameters:
            key - a partial data element (?)
        Returns:
            value - the full value matching key, otherwise None (?)
        -------------------------------------------------------
        """
        check = self._linear_search(key)
        if check > -1 and len(self._values)>0:
            value = self._values.pop(check)
        else:
            value = None
        return value

    def remove_front(self):
        """
        -------------------------------------------------------
        Removes the first node in the list.
        Use: value = source.remove_front()
        -------------------------------------------------------
        Returns:
            value - the first value in the list (?)
        -------------------------------------------------------
        """
        assert (len(self._values) > 0), 'Cannot remove from an empty list'
        
        value=self._values.pop(0)
        return value
        

        

    def remove_many(self, key):
        """
        -------------------------------------------------------
        Finds and removes all values in the list that match key.
        Use: source.remove_many(key)
        -------------------------------------------------------
        Parameters:
            key - a data element (?)
        Returns:
            None
        -------------------------------------------------------
        """
        x=0
        while key in self._values:
            if self._values[x]==key:
                self._values.pop(x)
            else:
                x+=1
        return

    def reverse(self):
        """
        -------------------------------------------------------
        The contents of list are reversed in order with respect
        to their order before the operation was called.
        Use: source.reverse()
        -------------------------------------------------------
        Returns:
            None
        -------------------------------------------------------
        """
    
        return

    def split(self):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains the first half,
        target2 the second half. Current list becomes empty.
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - a new List with >= 50% of the original List (List)
            target2 - a new List with <= 50% of the original List (List)
        -------------------------------------------------------
        """
      
        target1=List()
        target2=List()
        mid=int(len(self._values)/2)
        even=len(self._values)%2
        count=0
        while len(self._values)>0:
            if even==0:
                if count<mid:
                    target1.append(self._values.pop(0))
                else:
                    target2.append(self._values.pop(0))
            else:
                if count<=mid:
                    target1.append(self._values.pop(0))
                else:
                    target2.append(self._values.pop(0))
            count+=1
        return target1,target2

    def split_alt(self):
        """
        -------------------------------------------------------
        Splits the source list into separate target lists with values 
        alternating into the targets. At finish source list is empty.
        Order of source values is preserved.
        Use: target1, target2 = source.split()
        -------------------------------------------------------
        Returns:
            target1 - contains alternating values from source (List)
            target2 - contains other alternating values from source (List)
        -------------------------------------------------------
        """
        target1=List()
        target2=List()
        left = True
        while len(self._values) > 0:
            if left:
                target1._values.append(self._values.pop(0))
            else:
                target2._values.append(self._values.pop(0))
            left = not left
        return target1, target2

    def split_apply(self, func):
        """
        -------------------------------------------------------
        Splits list into two parts. target1 contains all the values 
        where the result of calling func(value) is True, target2 contains
        the remaining values. At finish, self is empty. Order of values 
        in targets is maintained.
        Use: target1, target2 = source.split_apply(func)
        -------------------------------------------------------
        Parameters:
            func - a function that given a value in the list returns
                True for some condition, otherwise returns False.
        Returns:
            target1 - a new List with values where func(value) is True (List)
            target2 - a new List with values where func(value) is False (List)
        -------------------------------------------------------
        """
        # Your code here

        return

    def split_key(self, key):
        """
        -------------------------------------------------------
        Splits list so that target1 contains all values < key,
        and target2 contains all values >= key.
        Use: target1, target2 = source.split_key()
        -------------------------------------------------------
        Returns:
            target1 - a new List of values <= key (List)
            target2 - a new List of values > key (List)
        -------------------------------------------------------
        """
        target1=List()
        target2=List()
        for x in range(len(self._values)):
            if self._values[x]<=key:
                target1.append(self._values[x])
            else:
                target2.append(self._values[x])

        return

    def union(self, source1, source2):
        """
        -------------------------------------------------------
        Update the current list with all values that appear in
        source1 and source2. Values do not repeat.
        Use: target.union(source1, source2)
        -------------------------------------------------------
        Parameters:
            source1 - an array-based list (List)
            source2 - an array-based list (List)
        Returns:
            None
        -------------------------------------------------------
        """
        for x in source1:
            if x not in self._values:
                self._values.append(x)
        for y in source2:
            if y not in self._values:
                self._values.append(y)
        return

    def __iter__(self):
        """
        USE FOR TESTING ONLY
        -------------------------------------------------------
        Generates a Python iterator. Iterates through the list
        from front to rear.
        Use: for v in source:
        -------------------------------------------------------
        Returns:
            value - the next value in the list (?)
        -------------------------------------------------------
        """
        for value in self._values:
            yield value

