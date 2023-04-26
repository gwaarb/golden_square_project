class Runman():
    
    def __init__(self):
        self.track_list = []

    def add(self, track):
        if not isinstance(track, str) or not track.strip():
            raise Exception("Invalid string")
        self.track_list.append(track)
        return f"Track Added: {track}" 

    def review(self):
        track_string = ", ".join(self.track_list)
        return f"Listened Tracks: {track_string}"