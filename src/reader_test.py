import solar_prediction_reader
import solar_prediction_model

config = solar_prediction_model.Config()
reader = solar_prediction_reader.Reader(config.data_path, config)

# for i in range(5):
# 	batch = reader.next_batch()
# 	print batch[2][0]


pattern = reader.get_pattern(6)
for i in pattern:
	print i


#get_test function test
for i in range(1):
	test = reader.get_test_set(1)
	print test[0]
	print "*"*40
	print test[2]
