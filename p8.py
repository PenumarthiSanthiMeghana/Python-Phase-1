class parent:
    def __init__(self):
        print("parent method")
class child(parent):
    def __init__(self):
        super(). __init__()
        print("child method")
c = child()
        
    
            