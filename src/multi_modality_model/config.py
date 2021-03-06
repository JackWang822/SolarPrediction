class Model_Config:
    """model configuration"""
    # regressor type
    # mse: mean square error
    # meef: information theoretic learning
    # msvr: multiple support vector regression
    # quantile: probabilistic regression (use the quantile regression algorithms)
    regressor = "mse"

    # msvr params
    epsilon = 60
    C  = 0.0

    # quantile regression params
    quantile_rate = 0.3

    # meef loss function params
    theta = 20
    gamma = 0.1

    # network params
    # the hidden size for three modalities, second level lstm and fully connected network
    n_first_hidden = 300
    n_second_hidden = 500
    n_third_hidden = 500
    cnn_feat_size = 200
    n_hidden_level2 = 400

    # learning rate
    lr = 0.0001

    #modal configuration
    modality = [1, 1, 1]

    # data reader configuration
    # data_step: the lag between the two input series
    # n_step: the length of the input time series
    # h_head: the lag between the input and output time series
    # n_target: the lenght of the output length if not equal one, use the msvr
    batch_size = 50
    data_step = 1

    n_step_1 = 24
    n_step_2 = 24
    n_step_3 = 24

    n_shift_1 = 24
    n_shift_2 = 24
    n_shift_3 = 24

    h_ahead = 6
    n_target = 1

    #train and test params
    epoch_size = 15000

    print_step = 100
    test_step = 5000
    evaluation_batch_size = 50

    n_input_ir = 3
    n_input_mete = 7
    width = 64
    height = 64
