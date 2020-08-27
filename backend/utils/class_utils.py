from typing import List


def get_abstract_subclasses(sub_classes: List[type]):
    """
        For all classes provided, those that start with abstract will get all
        of their subclasses, and recursivly for any of the new ones, until no
        new subclasses begin with abstract
    """

    new_results = []
    result = []

    for sub_class in sub_classes:
        if sub_class.__name__.startswith("Abstract"):
            for sub in sub_class.__subclasses__():
                new_results.append(sub)
        else:
            result.append(sub_class)

    if len(new_results) > 0:
        result.extend(get_abstract_subclasses(new_results))

    return result
