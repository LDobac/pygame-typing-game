class Event:

    callbacks = []

    def AddCallback(callback):
        if callback not in Event.callbacks:
            Event.callbacks.insert(0, callback)

    def RemoveCallback(callback):
        if callback in Event.callbacks:
            Event.callbacks.remove(callback)

    def ClearCallbacks():
        Event.callbacks.clear()

    def RaiseEvent(event):
        for callback in Event.callbacks:
            callback(event)
