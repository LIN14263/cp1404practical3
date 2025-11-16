class Monitor:
    def __init__(self,model,width,height):
        self.model=model
        self.width=width
        self.height=height
    def get_resolution(self):
        return (self.width,self.height)
    def get_total_pixels(self):
        return self.width*self.height

monitor1=Monitor(1920,1080)
monitor2=Monitor(1920,1080)
print(monitor1==monitor2)
monitor3=Monitor(2560,1440)
print(monitor1==monitor3)
montior4=Monitor(1920,2160)
print(monitor1==montior4)
print(monitor1=="not a monitor")