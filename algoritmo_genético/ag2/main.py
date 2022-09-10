from different_power_factory import DifferentPowerFactory
from crossintray_factory import CrossInTrayFactory
from schewefel_factory import SchwefelFactory
from ag import Ag

MAX_INDIVIDUALS = 20
ELITE = 4
GENERATIONS = 1000

ag = Ag()

print("__________SUM DIFFERENT POWER__________")
ag.execute( GENERATIONS,
            MAX_INDIVIDUALS,
            ELITE,
            maximization=False,
            interval=(-1, 1),
            dimension=2,
            factory=DifferentPowerFactory.factory )

print("\n\n__________CROSS-IN-TRAY FUNCTION__________")
ag.execute( GENERATIONS,
            MAX_INDIVIDUALS,
            ELITE,
            maximization=False,
            interval=(-10, 10),
            dimension=2,
            factory=CrossInTrayFactory.factory )

print("\n\n__________SCHEWEFEL FUNCTION__________")
ag.execute( GENERATIONS,
            200,
            60,
            maximization=False,
            interval=(-500, 500),
            dimension=2,
            factory=SchwefelFactory.factory )
