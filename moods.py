class mood:
    min_danceability = 0.5
    max_danceability = 1.0
    min_energy = 0.5
    max_energy = 1.0

    def setMood(self,mood):
        if mood == '1':
            # Happy mode: High danceability, high energy
            self.min_danceability = 0.8
            self.max_danceability = 1.0
            self.min_energy = 0.8
            self.max_energy = 1.0
        elif mood == '2':
        # Sad mode: Low danceability, low energy
            self.min_danceability = 0.0
            self.max_danceability = 0.2
            self.min_energy = 0.0
            self.max_energy = 0.2
        elif mood == '3':
        # Energetic mode: High danceability, high energy
            self.min_danceability = 0.8
            self.max_danceability = 1.0
            self.min_energy = 0.8
            self.max_energy = 1.0
    
    def songMatchesMood(self,features):
        try:
            return (features[0]['danceability'] >= self.min_danceability and features[0]['danceability'] <= self.max_danceability) \
            and (features[0]['energy'] >= self.min_energy and features[0]['energy'] <= self.max_energy)
        except:
            return False

