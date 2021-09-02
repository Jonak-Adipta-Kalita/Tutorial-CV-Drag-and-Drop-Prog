class DragRect():
    def __init__(self, posCenter, size=[200, 200]):
        self.posCenter = posCenter
        self.size = size

    def update(self, cursor):
        cx, cy = self.posCenter
        w, h = self.size
    
        if cx-w//2 < cursor[0] < cy+h//2 and cx-h//2 < cursor[1] < cy+h//2:
            self.posCenter = cursor
