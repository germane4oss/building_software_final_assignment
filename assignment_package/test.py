from assignment_package import Analysis

#create an Analysis class instance
analysis_1 = Analysis('configs/job_config.yml')

# load github repositories data
analysis_1.load_data()

# get the top 30 repositories based on the number of stars
analysis_1.compute_analysis()

# plot the data
analysis_1.plot_data()