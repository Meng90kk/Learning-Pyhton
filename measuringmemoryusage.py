import tracemalloc

tracemalloc.start()

x = 1
y = [4] * 100 ## peak memory here with large list
x = 4
y = x ## reassign variable that was large list, large list deleted
print(tracemalloc.get_traced_memory())
snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')
print(top_stats)

tracemalloc.stop()
