class RemoteControl:
    def __init__(self):
        self.max_volume = 20
        self.min_volume = 0
        self.current_volume = 10
        self.channel_list = [1, 2, 3, 4, 5, 6, 7, 8]
        self.current_channel = 0

    def volumeUp(self):
        if self.current_volume < self.max_volume:
            self.current_volume += 1

        print("volume:", self.current_volume)

    def volumeDown(self):
        if self.current_volume > self.min_volume:
            self.current_volume -= 1

        print("volume:", self.current_volume)

    def changeChannel(self, channel_up, channel_down):
        if channel_up == True:
            if self.current_channel < len(self.channel_list):
                self.current_channel += 1
            print("channel:", self.current_channel)

        if channel_down == True:
            if self.current_channel > 1:
                self.current_channel -= 1

                if self.current_channel<0:
                    raise StopIteration
            print("channel:", self.current_channel)



    def selectChannel(self, channel_number):
        self.current_channel= self.channel_list[channel_number-1]
        print("channel:", self.current_channel)





remote1 = RemoteControl()
"""
remote1.volumeUp()
remote1.volumeUp()
remote1.volumeUp()
remote1.volumeDown()
remote1.volumeDown()
print(remote1.current_channel)
remote1.changeChannel(True, False)
remote1.changeChannel(True, False)
remote1.changeChannel(True, False)
remote1.changeChannel(True, False)

remote1.changeChannel(False, True)
remote1.changeChannel(False, True)
remote1.changeChannel(False, True)
remote1.changeChannel(False, True)
remote1.changeChannel(False, True)

remote1.changeChannel(True, True)
"""
print(remote1.current_channel)

myit = iter(remote1.channel_list)
print(myit)
print(next(myit))
print(next(myit))
print(remote1.current_channel)

next(myit)
print(remote1.current_channel)
