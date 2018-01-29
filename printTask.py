# Create a queue of print tasks. Each task will be given a timestamp upon its arrival. The queue is empty to start.
# For each second (currentSecond):
# Does a new print task get created? If so, add it to the queue with the currentSecond as the timestamp.
# If the printer is not busy and if a task is waiting,
# Remove the next task from the print queue and assign it to the printer.
# Subtract the timestamp from the currentSecond to compute the waiting time for that task.
# Append the waiting time for that task to a list for later processing.
# Based on the number of pages in the print task, figure out how much time will be required.
# The printer now does one second of printing if necessary. It also subtracts one second from the time required for that task.
# If the task has been completed, in other words the time required has reached zero, the printer is no longer busy.
# After the simulation is complete, compute the average waiting time from the list of waiting times generated.
