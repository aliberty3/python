from television import Television

# Test the power method
def test_power():
    tv = Television()
    tv.power()
    assert tv._Television__status  # Check if the power is toggled on
    tv.power()
    assert not tv._Television__status  # Check if the power is toggled off again

# Test the mute method
def test_mute():
    tv = Television()
    # Turn on TV
    tv.power()
    # Mute TV
    tv.mute()
    assert tv._Television__muted  # Check if the TV is muted
    assert tv._Television__volume == 0  # Check if the volume is set to minimum when muted
    # Unmute TV
    tv.mute()
    assert not tv._Television__muted  # Check if the TV is unmuted
    assert tv._Television__volume == 0  # Check if the volume is restored to previous volume

# Test the channel_up method
def test_channel_up():
    tv = Television()
    # Turn on TV
    tv.power()
    # Change channel
    tv.channel_up()
    assert tv._Television__channel == 1  # Check if the channel is incremented

# Test the channel_down method
def test_channel_down():
    tv = Television()
    # Turn on TV
    tv.power()
    # Change channel
    tv.channel_down()
    assert tv._Television__channel == 3  # Check if the channel is decremented

# Test the volume_up method
def test_volume_up():
    tv = Television()
    # Turn on TV
    tv.power()
    # Increase volume
    tv.volume_up()
    assert tv._Television__volume == 1  # Check if the volume is incremented

# Test the volume_down method
def test_volume_down():
    tv = Television()
    # Turn on TV
    tv.power()
    # Decrease volume
    tv.volume_down()
    assert tv._Television__volume == 0  # Check if the volume is decremented

