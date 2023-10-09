def get_response(user_message: str):
    p_message = user_message.lower()

    if p_message == 'play':
        return f'Resuming song'
    elif p_message[:4] == 'play':
        return f'Playing: {p_message[5:]}'
    elif p_message == 'pause':
        return 'Pausing...'
    elif p_message == 'skip':
        return 'Skipping'
    elif p_message == 'back':
        return 'Backing'
    elif p_message == 'clear':
        return 'Clearing queue'
    elif p_message == 'stop':
        return "I'm out of here"
    
    return 'Nothing'