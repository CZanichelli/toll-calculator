from datetime import time

# Fee schedule per the city's requirements. Start inclusive, end exclusive.
# The schedule differs from the C# original, see README.

FEES = [
    (time(6, 0), time(6, 30), 8),
    (time(6, 30), time(7, 0), 13),
    (time(7, 0), time(8, 0), 18),
    (time(8, 0), time(8, 30), 13),
    (time(8, 30), time(15, 0), 8),
    (time(15, 0), time(15, 30), 13),
    (time(15, 30), time(17, 0), 18),
    (time(17, 0), time(18, 0), 13),
    (time(18, 0), time(18, 30), 8),   
]


def fee_for_time(passage):
    t = passage.time()
    for start, end, fee in FEES:
        if start <= t < end:
            return fee
    return 0