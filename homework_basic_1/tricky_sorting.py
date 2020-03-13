items = [('one', 'two'), ('three', 'four'), ('five', 'six'), ('string', 'a')]
# Мы хотим отсортировать этот список по последней букве второго элемента каждого tuple, т.е. получить такой список:
sorted_items = [ ('string', 'a'), ('one', 'two'), ('three', 'four'), ('five', 'six'),]
# Что нужно вставить вместо "<...>" в следующем выражении, чтобы получить верную сортировку?

sorted_items = sorted(items, key=lambda x: x[1][-1])
