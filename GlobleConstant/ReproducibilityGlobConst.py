import ClassBase.ObjectRef

class ReproducibilityGlobConst:
    always = ClassBase.ObjectRef(id=10, name='always')
    sometimes = ClassBase.ObjectRef(id=30, name='sometimes')
    random = ClassBase.ObjectRef(id=50, name='random')
    have_not_tried = ClassBase.ObjectRef(id=70, name='have not tried')
    unable_to_reproduce = ClassBase.ObjectRef(id=90, name='unable to reproduce')
    NA = ClassBase.ObjectRef(id=100, name='N/A')
