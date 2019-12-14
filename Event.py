'''
    Event.py

    pygame evnet 값을 전달하는 CALLBACK 함수를 등록한다.
'''

# Static 클래스
class Event:

    # callback 함수들을 저장한다
    callbacks = []

    '''
        새로운 콜백 함수를 등록한다
        def callback(event) 형태를 갖는다
    ''' 
    def AddCallback(callback):
        if callback not in Event.callbacks:
            Event.callbacks.insert(0, callback)

    '''
        콜백 함수 삭제
    '''
    def RemoveCallback(callback):
        if callback in Event.callbacks:
            Event.callbacks.remove(callback)

    '''
        모든 콜백 함수를 제거한다
    '''
    def ClearCallbacks():
        Event.callbacks.clear()

    '''
        등록된 콜백 함수를 호출 해 이벤트를 전달한다
    '''
    def RaiseEvent(event):
        for callback in Event.callbacks:
            callback(event)
