def selection_sort(items):
    """Sorts a list of items into ascending order using the
       selection sort algoright.
       """
    for step in range(len(items)):
        # Find the location of the smallest element in
        # items[step:].
        location_of_smallest = step

        for location in range(step, len(items)):
            # TODO: determine location of smallest
            if items[location]<items[location_of_smallest]:
                location_of_smallest = location
        
        # TODO: Exchange items[step] with items[location_of_smallest]
        items[step], items[location_of_smallest] = items[location_of_smallest], items[step]

    return items
items = [21,1,9,33,3]

print("The sorted array is: ", selection_sort(items))
        