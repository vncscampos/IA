from schwefel import Schwefel
    
class SchwefelFactory:
    @staticmethod
    def factory(chromosome: list) -> Schwefel:
        return Schwefel(chromosome)
