from crossintray import CrossInTray
    
class CrossInTrayFactory:
    @staticmethod
    def factory(chromosome: list) -> CrossInTray:
        return CrossInTray(chromosome)
