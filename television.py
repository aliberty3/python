class Television:
    # Class variables
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self):
        # Instance variables
        self.__status = False
        self.__muted = False
        self.__volume = self.MIN_VOLUME
        self.__channel = self.MIN_CHANNEL
        self.__previous_volume = self.MIN_VOLUME  # Initialize previous volume

    def power(self):
        # Method to turn the TV on and off
        self.__status = not self.__status

    def mute(self):
        # Method to mute and unmute the TV
        if self.__status:
            if not self.__muted:  # Only store previous volume if TV was not already muted
                self.__previous_volume = self.__volume
            self.__muted = not self.__muted
            if self.__muted:
                self.__volume = self.MIN_VOLUME  # Muting sets volume to minimum
            elif not self.__muted:
                self.__volume = self.__previous_volume  # Unmute sets volume to previous level

    def channel_up(self):
        # Method to increase TV channel
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self):
        # Method to decrease TV channel
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self):
        # Method to increase TV volume
        if self.__status:
            if self.__muted:
                self.__muted = False  # Unmute if volume is adjusted while muted
                self.__volume = self.__previous_volume + 1 if self.__previous_volume < self.MAX_VOLUME else self.MAX_VOLUME  # Set volume to minimum non-muted level
            elif self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self):
        # Method to decrease TV volume
        if self.__status:
            if self.__muted:
                self.__muted = False  # Unmute if volume is adjusted while muted
                self.__volume = self.__previous_volume + 1 if self.__previous_volume < self.MAX_VOLUME else self.MAX_VOLUME  # Set volume to minimum non-muted level
            elif self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self):
        # Method to return the state of the TV
        return f"Power [{self.__status}], Channel [{self.__channel}], Volume [{self.__volume}]"

