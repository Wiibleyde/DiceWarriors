class Serializable:
    def to_dict(self):
        dict_repr = {}
        for key, value in self.__dict__.items():
            if hasattr(value, "to_dict"):
                dict_repr[key] = value.to_dict()
            else:
                dict_repr[key] = value
        return dict_repr
    
    @classmethod
    def from_dict(cls, data: dict):
        return cls(**data) 
    