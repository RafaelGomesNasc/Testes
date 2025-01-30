from abc import ABC, abstractmethod

class Device:
    def __init__(self, id=0, channel=None, buffer =''):
        self.id = id
        if isinstance(channel, Media):
            self.channel = channel
        else:
            raise TypeError('channel must be a Media object')
        self.buffer = buffer
        

class Media(ABC):

    @abstractmethod
    def send(self, data):
        pass
    
    @abstractmethod
    def recv(self, data):
        pass

class Copper(Media):
    
    def convertToElectricPulse(self, data):
        print('Converting data to bits represented by electric pulse...')
        return data
    
    # Atribuição do método abstrato da classe abstrata Media
    def send(self, data):
        bits = self.convertToElectricPulse(data)
        print('Sending bits...')
        print(bits)

    def recv(self, data):
        bits = self.convertToElectricPulse(data)
        print('Receiving bits...')
        print(bits)

class Fiber(Media):

    def convertToLightPulse(self, data):
        print('Converting data to bits represented by light pulse...')
        return data
    
    # Atribuição do método abstrato da classe abstrata Media
    def send(self, data):
        bits = self.convertToLightPulse(data)
        print('Sending bits...')
        print(bits)

    def recv(self, data):
        bits = self.convertToLightPulse(data)
        print('Receiving bits...')
        print(bits)

class Wireless(Media):

    def convertToWavePulse(self, data):
        print('Converting data to bits represented by wave pulse...')
        return data
    
    # Atribuição do método abstrato da classe abstrata Media
    def send(self, data):
        bits = self.convertToWavePulse(data)
        print('Sending bits...')
        print(bits)

    def recv(self, data):
        bits = self.convertToWavePulse(data)
        print('Receiving bits...')
        print(bits)

class Switch(Device):
    def __init__(self, id = 0, channel = None, buffer = ''):
        Device.__init__(self, id, channel, buffer)
    
    def __str__(self):
        return f"Switch\nId: {self.id}\nChannel: {self.channel}\nBuffer: {self.buffer}"

class PC(Device):
    def __init__(self, id = 0, channel = None, buffer = ''):
        Device.__init__(self, id, channel, buffer)
    
    def __str__(self):
        return f"PC\nId: {self.id}\nChannel: {self.channel}\nBuffer: {self.buffer}"

class Cellphone(Device):
    def __init__(self, id = 0, channel = None, buffer = ''):
        Device.__init__(self, id, channel, buffer)
    
    def __str__(self):
        return f"Cellphone\nId: {self.id}\nChannel: {self.channel}\nBuffer: {self.buffer}"

if __name__ == '__main__':
    #--------------------------------#
    # Device
    #--------------------------------#
    try:
        d1 = Device(1, Copper(), 'Hello')
        d1.channel.send(d1.buffer)
        d1.channel.recv(d1.buffer)
        d2 = Device(2, Fiber(), 'Hello')
        d2.channel.send(d2.buffer)
        d2.channel.recv(d2.buffer)
        d3 = Device(3, Wireless(), 'Hello')
        d3.channel.send(d3.buffer)
        d3.channel.recv(d3.buffer)
    except Exception as e:
        print(e)
    #--------------------------------#
    # Media
    #--------------------------------#
    try:
        m = Media()
    except Exception as e:
        print(e)
    #--------------------------------#
    # Copper
    #--------------------------------#
    try:
        c = Copper()
        c.send('Hello')
        c.recv('Hello')
    except Exception as e:
        print(e)
    #--------------------------------#
    # Fiber
    #--------------------------------#
    try:
        f = Fiber()
        f.send('Hello')
        f.recv('Hello')
    except Exception as e:
        print(e)
    #--------------------------------#
    # Wireless
    #--------------------------------#
    try:
        w = Wireless()
        w.send('Hello')
        w.recv('Hello')
    except Exception as e:
        print(e)
    #--------------------------------#
    # Switch
    #--------------------------------#
    try:
        s = Switch(1, Copper(), 'Hello')
        print(s)
        s.channel.send(s.buffer)
        s.channel.recv(s.buffer)
    except Exception as e:
        print(e)
    #--------------------------------#
    # PC
    #--------------------------------#
    try:
        p = PC(2, Fiber(), 'Hello')
        print(p)
        p.channel.send(p.buffer)
        p.channel.recv(p.buffer)
    except Exception as e:
        print(e)
    #--------------------------------#
    # Cellphone
    #--------------------------------#
    try:
        c = Cellphone(3, Wireless(), 'Hello')
        print(c)
        c.channel.send(c.buffer)
        c.channel.recv(c.buffer)
    except Exception as e:
        print(e)

