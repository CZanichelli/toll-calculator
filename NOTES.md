
# Walkthrough of the C# code

## GetTollFee(date, vehicle) - the fee schedule (lines 55-72) 

## Fee-table as it's written
| From | To | fee |
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

## TollCalculator.cs -Codeline:66
It only counts the second half of every hour between 8 - 14, that means 30-59. Because of this 09:15 becomes free, it falls outside of the interval 30-59, and nothing else is catching it. 
## How to Fix the issue: 
Rules are most expensive fees around rush hour, for the span 8:30-14:59 8 kr fee is reasonable. 

## TollCalculator.cs -Codeline:67-68
&& binds harder than ||, and minute >=0 is always true, the statement meaning is the whole hour 15 or whole hour 16, it still comes out right due to the line above catches 15:00 - 15:29 
if the line 67 is removed or being moved the timestamps 15:00 - 15:29 is being changed to 18kr instead of 13 kr 













# Playing around with values
Condition  Is        Answer
hour >= 8  | 9 >= 8  | True
hour <= 14 | 9 <= 14 | True
minute >=30| 45 >=30 | True
minute <=59| 45 <=59 | True




