def mean(dataset):
    return round(sum(dataset) / len(dataset), 2)


def median(dataset):
    data = sorted(dataset)
    index = len(data) // 2

    # If the dataset is odd
    if len(dataset) % 2 != 0:
        return data[index]

    # If the dataset is even
    return round((data[index - 1] + data[index]) / 2, 2)


def compute_median_mean_diff(dataset):
    return round(mean(dataset) - median(dataset), 2)