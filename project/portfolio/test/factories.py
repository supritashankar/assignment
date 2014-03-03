import factory

from portfolio.models import *

class PortfolioFactory(factory.Factory):
  FACTORY_FOR = Portfolio

  color = 'B'
  description = 'This is blue color'
