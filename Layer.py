from Enums.ELayer import ELayer

class Layer:

    """
    batches - array of size Elayer.values (globally declared and managed)
    """
    def __init__(self, batches):
        self.batches = batches
        self.layers = []
        for layer in [e.value for e in ELayer]:
            self.layers.append(None)


    def add_to_batch(self):
        for i in range(len(self.layers)):
            if self.layers[i] is not None:
                self.layers[i]

    def draw(self):
