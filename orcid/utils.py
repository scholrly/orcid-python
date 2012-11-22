def dictmapper(typename, mapping):
    """
    A factory to create `namedtuple`-like classes from a dict-path-to-field
    mapping::

        Person = dictmapper({'person':('person','name')})
        example_dict = {'person':{'name':'John'}}
        john = Person(example_dict)
        assert john.name == 'John'

    If a function is specified as a mapping value instead of a dict "path", it
    will be run with the backing dict as its first argument.
    """
    def init(self, d, *args, **kwargs):
        """
        Initialize `dictmapper` classes with a dict to back getters.
        """
        self._original_dict = d

    def getter_from_dict_path(path):
        if len(path) < 1:
            raise ValueError('Dict paths should be iterables with at least one'
                             ' key.')
        def getter(self):
            cur_dict = self._original_dict
            if callable(path):
                return path(cur_dict)
            for key in path[:-1]:
                cur_dict = cur_dict.get(key, {})
            return cur_dict.get(path[-1], None)
        return getter

    prop_mapping = dict((k, property(getter_from_dict_path(v))) 
                        for k, v in mapping.iteritems())
    prop_mapping['__init__'] = init
    return type(typename, tuple(), prop_mapping)
