previous_probability_all = input("Initial Probability Estimate (all cases): ")
probability_if_true_perc = input("Probability if Event is True (percent): ")
probability_if_false_all = input("Probability if Event is False (all cases): ")

# previous_probability = 1.0/previous_probability_all
previous_probability = previous_probability_all
probability_if_true = 100.0/probability_if_true_perc
probability_if_false = 1.0/probability_if_false_all

posterior_probability = previous_probability * probability_if_true/(previous_probability * probability_if_true + probability_if_false*(1-previous_probability))

print "Probability is %.2f %%" % (posterior_probability * 100)