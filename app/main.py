import utils
import read_csv
import charts
import pandas as pd

def run():
  '''

  data = list(filter(lambda item : item['Continent'] == 'South America',data))

  countries = list(map(lambda x: x['Country'], data))
  percentages = list(map(lambda x: x['World Population Percentage'], data))
  

  '''
  
  data = read_csv.read_csv('data.csv')
  df = pd.read_csv('data.csv')

  #Filtrar en pandas
  df = df[df['Continent'] == 'Africa']

  # Hace lo mismo que hacía la primera linea comentaba arriba data = list(...)

  # Armo una lista de los paises de mi df. Simil hice en countries = list(...)
  countries = df['Country'].values

  # Armo otra lista para porcentajes...
  percentages = df['World Population Percentage'].values

  charts.generate_pie_chart(countries, percentages)

  country = input('Type Country => ')
  print(country)

  result = utils.population_by_country(data, country)

  if len(result) > 0:
    country = result[0]
    print(country)
    labels, values = utils.get_population(country)
    charts.generate_bar_chart(country['Country'], labels, values)

  print(type(data)) # <class 'list'>
  print(type(df)) # <class 'pandas.core.frame.DataFrame'>

if __name__ == '__main__':
  run()