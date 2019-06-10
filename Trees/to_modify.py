def tree_print(t):
    def tree_print_helper(t):
        if t is None:
            return [], 0, 0
        # label = str(t.key)
        label = str(t)
        leftstr, leftpos, leftwidth = tree_print_helper(t.left)
        rightstr, rightpos, rightwidth = tree_print_helper(t.right)
        middle = max(rightpos+leftwidth - leftpos+1, len(label), 2)
        pos = leftpos + middle // 2
        width = leftpos + middle + rightwidth - rightpos
        while len(leftstr)<len(rightstr):
            leftstr.append(' '*leftwidth)
        while len(rightstr)<len(leftstr):
            rightstr.append(' '*rightwidth)
        if (middle-len(label))%2 == 1:
            label += '_'
        label = label.center(middle, '_')
        if label[0] == '_': label=' ' + label[1:]
        if label[-1] == '_': label = label[:-1]+' '
        lines = [' '*leftpos + label + ' '*(rightwidth-rightpos), ' '*leftpos + '/' + ' '*(middle-2) + '\\' + ' '*(rightwidth-rightpos)] + [leftline + ' '*(width-leftwidth-rightwidth) + rightline for leftline, rightline in zip(leftstr, rightstr)]
        return lines, pos, width
    print('\n'.join(tree_print_helper(t)[0]))
