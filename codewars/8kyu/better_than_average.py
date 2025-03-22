def better_than_average(class_points, your_points):
    classAverage = sum(class_points) / len(class_points)
    return your_points > classAverage