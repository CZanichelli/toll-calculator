
# Walkthrough of the C# code

## GetTollFee(date, vehicle) - the fee schedule (lines 55-72) 

## Fee-table as it's written
| From | To | Fee |
|------|------|--------|
| 06:00 | 06:29 | 8 kr |
| 06:30 | 06:59 | 13 kr |
| 07:00 | 07:59 | 18 kr |
| 08:00 | 08:29 | 13 kr |
| minute 30-59 every hour 08-14 | | 8 kr |
| 15:00 | 15:29 | 13 kr |
| 15:30 | 16:59 | 18 kr |
| 17:00 | 17:59 | 13 kr |
| 18:00 | 18:29 | 8 kr  |
| All other times|  | 0 kr  |





# Issues to be fixed in my python implementation

## TollCalculator.cs -line 66
It only counts the second half of every hour between 8 and 14, that means 30-59. Because of this 09:15 becomes free, it falls outside of the interval 30-59, nothing else catches it. 
## How to Fix it: 
Rules are most expensive fees around rush hour, for the span 8:30-14:59 8 kr fee is reasonable. 

## TollCalculator.cs -lines 67-68
&& binds harder than ||, and minute >=0 is always true, the statement meaning is the whole hour 15 or whole hour 16, it still comes out right due to the line above catches 15:00 - 15:29 
if the line 67 is removed or being moved the timestamps 15:00 - 15:29 changes to 18kr instead of 13 kr 

## Vehicle types as strings
- the type is compared as text against enum-names.
- a small letter instead of a capital gives the wrong fee, with no warning
- two lists of vehicle types that need to be synced by hand.

## Time difference, TollCalculator.cs line 25
- .Millisecond is just thousandths, not the whole time difference.
- always becomes 0 
- therefore the code thinks every passage is within the same hour.
- the correct approach is date - intervalStart 














# Worked example: line 66
Condition  Is        Answer
hour >= 8  | 9 >= 8  | True
hour <= 14 | 9 <= 14 | True
minute >=30| 45 >=30 | True
minute <=59| 45 <=59 | True




