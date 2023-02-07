from Item import Item


# def max_val(to_consider: [Item], avail: float) -> ():
#     if to_consider == [] or avail == 0:
#         result = (0, ())
#     elif to_consider[0].get_weight() > avail:
#         # explore right branch only
#         result = max_val(to_consider[1:], avail)
#     else:
#         next_item = to_consider[0]
#         # explore left branch
#         with_val, with_to_take = max_val(to_consider[1:], avail - next_item.get_weight())
#         with_val += next_item.get_value()
#
#         # explore right branch
#         without_val, without_to_take = max_val(to_consider[1:], avail)
#
#         # choose better branch
#         if with_val > without_val:
#             result = (with_val, with_to_take + (next_item,))
#         else:
#             result = (without_val, without_to_take)
#
#     return result


def fast_max_val(to_consider: [Item], avail: float, memo: dict = None) -> ():
    if memo is None:
        memo = {}
    if (len(to_consider), avail) in memo:
        result = memo[(len(to_consider), avail)]
    elif to_consider == [] or avail == 0:
        result = (0, ())
    elif to_consider[0].get_weight() > avail:
        # explore right branch only
        result = fast_max_val(to_consider[1:], avail, memo)
    else:
        next_item = to_consider[0]
        # explore left branch
        with_val, with_to_take = fast_max_val(to_consider[1:], avail - next_item.get_weight(), memo)
        with_val += next_item.get_value()

        # explore right branch
        without_val, without_to_take = fast_max_val(to_consider[1:], avail, memo)

        # choose better branch
        if with_val > without_val:
            result = (with_val, with_to_take + (next_item,))
        else:
            result = (without_val, without_to_take)
    memo[(len(to_consider), avail)] = result
    return result
