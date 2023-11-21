class Serializable:
    def to_dict(self):
        dict_repr = {}
        for key, value in self.__dict__.items():
            print(key, value)
            if hasattr(value, "to_dict"):
                dict_repr[value.__class__.__name__] = value.to_dict()
            else:
                dict_repr[key] = value
        return dict_repr
    
    @classmethod
    def from_dict(cls, data: dict):
        new_data = {}
        for key, value in data.items():
            if isinstance(value, dict):
                class_ = globals().get(key)
                if class_ is not None and issubclass(class_, Serializable):
                    new_data[key.lower()] = class_.from_dict(value)
                else:
                    new_data[key] = value
            else:
                new_data[key] = value
        return cls(**new_data)