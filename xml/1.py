count = len(node.attrib)

    for child in node:
        count += get_attr_number(child)

    return count



#len(node.attrib) counts the attributes of the current XML tag.

#for child in node visits each tag inside it.

#get_attr_number(child) counts the attributes inside that child, including its nested tags.

#count += adds all those attributes together.

#return count gives the total.