class Colors:
    empty = (26, 31, 40)
    green = (47, 230, 23)
    orange = (226, 116, 17)
    red = (232, 18, 18)
    purple = (166, 0, 247)
    yellow = (237, 234, 4)
    cyan = (21, 204, 209)
    blue = (13, 64, 216)

    @classmethod
    def get_colors(cls):
        return [cls.empty, cls.green, cls.orange, cls.red, cls.purple, cls.yellow, cls.cyan, cls.blue]