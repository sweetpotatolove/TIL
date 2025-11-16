from pyflink.datastream import StreamExecutionEnvironment

env = StreamExecutionEnvironment.get_execution_environment()
env.set_parallelism(1)

data = env.from_collection([("apple", 1), ("banana", 1), ("apple", 1)])
data.print()

env.execute("PyFlink Docker Job")
