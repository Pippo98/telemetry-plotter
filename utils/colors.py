class Color:
    r = 0
    g = 0
    b = 0
    def __init__(self, r=0, g=0, b=0, hex_="") -> None:
        if not hex_ == "":
            hex_ = hex_ if not hex_[0] == "#" else hex_[1:]
            r = int(hex_[1:2], 16)
            g = int(hex_[3:4], 16)
            b = int(hex_[5:6], 16)
        self.r = r
        self.g = g
        self.b = b

    def __str__(self) -> str:
        return self.rgb()
    
    def rgb(self) -> str:
        return f"{self.r}, {self.g}, {self.b}"

    def rgb_unit(self) -> str:
        return f"{self.r/255}, {self.g/255}, {self.b/255}"
    
    def hex(self) -> str:
        color = (hex(self.r) + hex(self.g) + hex(self.b)).replace("0x", "")
        return "#{color}"


BASE_COLOR = Color(hex_="#20224C")