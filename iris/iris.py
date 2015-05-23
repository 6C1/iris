import csv
import math
import operator
import random

KNN_VERBOSE = True

def main():

    # Load, process data, and split it into training and testing subsets.
    training_set, test_set = split_data(format_data(get_data()))
    # Test predictions and display success rate.
    print "{0:.2f}% accuracy".format(ntests(training_set, test_set, 20))


def ntests(training_set, test_set, n):
    '''
        Run n tests and return average success rate.
    '''
    results = []
    for i in xrange(n):
        results.append(test(training_set, test_set))
    avg = float(sum([r[2] for r in results])) / len(results)
    return avg

def test(training_set, test_set, v = False):
    
    a = [(p, predict_label(p, training_set) == p[-1]) for p in test_set]
    successes = len([p for p in a if p[1]])
    success_rate = 1.0 * successes / len(test_set)
    if v:
        return "{} points tested.\n{} successes.\n{2:.2f}% success rate.".format(
            len(test_set),
            successes,
            success_rate)
    else:
        return (len(test_set), successes, success_rate)


def predict_label(p, t, k=4):
    '''
        Estimate label based on labels of k nearest neighbors.
    '''

    return _predict(knn(p, t, min(k,len(t)-1)))


def _predict(neighbors):
    '''
        Estimate label based on labels of neighbors.
    '''

    labels = {}

    for neighbor in neighbors:
        label = neighbor[-1]
        if label not in labels:
            labels[label] = 1
        else:
            labels[label] += 1
    sorted_labels = sorted(labels.iteritems(), key=operator.itemgetter(1))
    return sorted_labels[-1][0] if len(sorted_labels) > 0 else -1


def knn(p, t, k):
    '''
        Returns k nearest neighbors of point p in set t.
    '''

    neighbors, tset = [], [x for x in t]
    
    for i in xrange(k):
        compare = lambda a,b: a if dist(a,p) < dist(b,p) else b
        current_neighbor = reduce(compare,tset)
        neighbors.append(current_neighbor)
        tset.remove(current_neighbor)
    return neighbors


def dist(a, b, d=4):
    '''
        Calculates Euclidean distance between d-dimensional points a and b.
    '''

    return math.sqrt(sum([pow(a[i]-b[i], 2) for i in xrange(d)]))

def get_data():
    '''
        Returns iris data as 2d array.
    '''

    with open('data/iris.data', 'r') as f:
        return [
            map(
                lambda x: x.strip(), 
                row.split(",")) 
            for row in f 
            if len(row) > 5
            ]


def format_data(data):
    '''
        Reformats row entries as floats where appropriate.
    '''

    for row in data:
        for i in xrange(4):
            row[i] = float(row[i])
    return data


def split_data(data, ratio=0.5):
    '''
        Splits data into complementary training and test subsets.
    '''

    training, test = [], []
    f = lambda x, a, b: a.append(x) if random.random() < ratio else b.append(x)
    [f(row,training,test) for row in data]
    return training, test


if __name__ == "__main__":
    main()
