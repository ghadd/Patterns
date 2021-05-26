from .modellable import Modellable
from . import *


class ModelBuilder:
    """Builder"""

    def create_model(self, object_classname, model_classname=None, **kwargs):
        if model_classname is None:
            model_classname = object_classname + "Model"

        object_class = eval(object_classname)
        model_class = eval(model_classname)

        obj = object_class(**kwargs)
        return model_class.create(**obj.to_dict())
