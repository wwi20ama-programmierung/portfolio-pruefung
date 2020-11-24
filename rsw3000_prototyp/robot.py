class Robot:
    def __init__(self):
        self.done = False

    def step(self, surroundingTiles):
        """ Liefert den naechsten Schritt als Paar (dx, dy) """

        # Beispiel: Geht solange nach rechts, falls dort keine Wand ist.
        # Wenn rechts eine Wand ist, bewegt sich der Roboter nicht mehr
        # und setzt sein done-Flag.
        if not self.done and surroundingTiles[1][2] != 'W':
            return 1,0
        else:
            self.done = True
            return 0,0
