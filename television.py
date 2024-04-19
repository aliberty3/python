class Television:
    """A class representing a Television."""

    # Class variables
    MIN_VOLUME: int = 0
    MAX_VOLUME: int = 2
    MIN_CHANNEL: int = 0
    MAX_CHANNEL: int = 3

    def __init__(self) -> None:
        """Initialize the Television with default settings."""
        # Instance variables
        self.__status: bool = False
        self.__muted: bool = False
        self.__volume: int = self.MIN_VOLUME
        self.__channel: int = self.MIN_CHANNEL
        self.__previous_volume: int = self.MIN_VOLUME  # Initialize previous volume

    def power(self) -> None:
        """Toggle the power status of the Television."""
        self.__status = not self.__status

    def mute(self) -> None:
        """Mute or unmute the Television."""
        if self.__status:
            if not self.__muted:
                self.__previous_volume = self.__volume
            self.__muted = not self.__muted
            if self.__muted:
                self.__volume = self.MIN_VOLUME
            elif not self.__muted:
                self.__volume = self.__previous_volume

    def channel_up(self) -> None:
        """Increase the channel of the Television."""
        if self.__status:
            self.__channel = (self.__channel + 1) % (self.MAX_CHANNEL + 1)

    def channel_down(self) -> None:
        """Decrease the channel of the Television."""
        if self.__status:
            if self.__channel == self.MIN_CHANNEL:
                self.__channel = self.MAX_CHANNEL
            else:
                self.__channel -= 1

    def volume_up(self) -> None:
        """Increase the volume of the Television."""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume + 1 if self.__previous_volume < self.MAX_VOLUME else self.MAX_VOLUME
            elif self.__volume < self.MAX_VOLUME:
                self.__volume += 1

    def volume_down(self) -> None:
        """Decrease the volume of the Television."""
        if self.__status:
            if self.__muted:
                self.__muted = False
                self.__volume = self.__previous_volume + 1 if self.__previous_volume < self.MAX_VOLUME else self.MAX_VOLUME
            elif self.__volume > self.MIN_VOLUME:
                self.__volume -= 1

    def __str__(self) -> str:
        """Return the state of the Television."""
        return f"Power [{self.__status}], Channel [{self.__channel}], Volume [{self.__volume}]"
