import numpy.random
import pandas


rng = numpy.random.default_rng(1234)

ratings = ['A', 'B', 'C']
ratings_weights = [0.35, 0.55, 0.10]
rates = [0.05, 0.06, 0.08, 0.10]
rates_weights = [0.20, 0.45, 0.30, 0.05]
n = 1000
total_principal = 100e6

loans = pandas.DataFrame()
loans['loan_id'] = list(map(lambda v: 'Loan-'+str(v), numpy.arange(0, n)))
loans['rating'] = rng.choice(ratings, size=n, replace=True, p=ratings_weights)
loans['yield'] = rng.choice(rates, size=n, replace=True, p=rates_weights)
loans['principal'] = rng.dirichlet(numpy.ones(n), size=1)[0]*total_principal
loans.to_json('collateral-base/data/loans.json', orient='records')

