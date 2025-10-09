class MedianFinder {
    vector<int> store; // resize-able container

public:
    // Adds a number into the data structure.
    void addNum(int num)
    {
        if (store.empty())
            store.push_back(num);
        else
            store.insert(lower_bound(store.begin(), store.end(), num), num);     // binary search and insertion combined
    }

    // Returns the median of current data stream
    double findMedian()
    {
        int n = store.size();
        return n & 1 ? store[n / 2] : ((double) store[n / 2 - 1] + store[n / 2]) * 0.5;
    }
};


// Time complexity: O(n)+O(logn)≈O(n).

// Binary Search takes O(logn) time to find correct insertion position.
// Insertion can take up to O(n) time since elements have to be shifted inside the container to make room for the new element.
// Pop quiz: Can we use a linear search instead of a binary search to find insertion position, without incurring any significant runtime penalty?

// Space complexity: O(n) linear space to hold input in a container.

// # Intuition

// Keeping our input container always sorted (i.e. maintaining the sorted nature of the container as an invariant).

// Algorithm

// Which algorithm allows a number to be added to a sorted list of numbers and yet keeps the entire list sorted? Well, for one, insertion sort!

// We assume that the current list is already sorted. When a new number comes, we have to add it to the list while maintaining the sorted nature of the list. This is achieved easily by finding the correct place to insert the incoming number, using a binary search (remember, the list is always sorted). Once the position is found, we need to shift all higher elements by one space to make room for the incoming number.

// This method would work well when the amount of insertion queries is lesser or about the same as the amount of median finding queries.