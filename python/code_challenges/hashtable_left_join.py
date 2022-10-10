from data_structures.hashtable import Hashtable

def left_join(a_table, b_table):
    joined_list = []

    for key, value in a_table.items():
        if b_table.get(key):
            joined_list.append([key, value, b_table.get(key)])
        else:
            joined_list.append([key, value, 'NONE'])


    return joined_list
