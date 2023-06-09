import feedparser
from sqlalchemy import create_engine
import pandas as pd


def newsfeeder(classe, url):
  if 'g1' in url:
    NewsFeed = feedparser.parse(url).entries
    engine = create_engine('sqlite:///db.db', echo=False)
    a = []
    for entry in NewsFeed:
      a.append(entry)
    if len(a) > 0:
      df = pd.DataFrame(a)
      df = df[['title', 'id', 'link', 'published_parsed', 'summary']]
      df['classe'] = classe
      df = df.astype(str)
      df = df.replace('"', '', regex=True)
      df = df.replace("'", '', regex=True)
      df = df.replace("“", '', regex=True)
      try:
        df.to_sql('news', con=engine, index=False)
      except:
        squery = f"""INSERT OR IGNORE INTO news VALUES {','.join([str(i) for i in list(df.to_records(index=False))])}"""
        engine.execute(squery)
    else:
      pass
  elif 'uol' in url:
    NewsFeed = feedparser.parse(url).entries
    engine = create_engine('sqlite:///db.db', echo=False)
    a = []
    for entry in NewsFeed:
      a.append(entry)
    if len(a) > 0:
      df = pd.DataFrame(a)
      df['id'] = df['link']
      df['published_parsed'] = df['published']
      df = df[['title', 'id', 'link', 'published_parsed', 'summary']]
      df['classe'] = classe
      df = df.astype(str)
      df = df.replace('"', '', regex=True)
      df = df.replace("'", '', regex=True)
      df = df.replace("“", '', regex=True)
      try:
        df.to_sql('news', con=engine, index=False)
      except:
        squery = f"""INSERT OR IGNORE INTO news VALUES {','.join([str(i) for i in list(df.to_records(index=False))])}"""
        engine.execute(squery)
    else:
      pass


newsfeeder('tecnologia', 'http://rss.uol.com.br/feed/tecnologia.xml')
newsfeeder('economia', 'http://rss.uol.com.br/feed/economia.xml')
newsfeeder('jogos', 'http://rss.uol.com.br/feed/jogos.xml')
newsfeeder('cinema', 'http://rss.uol.com.br/feed/cinema.xml')
newsfeeder('vestibular', 'http://rss.uol.com.br/feed/vestibular.xml')
newsfeeder('carros', 'http://rss.uol.com.br/feed/carros.xml')
newsfeeder('Carros', 'http://g1.globo.com/dynamo/carros/rss2.xml')
newsfeeder('Ciência e Saúde',
           'http://g1.globo.com/dynamo/ciencia-e-saude/rss2.xml')
newsfeeder('Concursos e Emprego',
           'http://g1.globo.com/dynamo/concursos-e-emprego/rss2.xml')
newsfeeder('Economia', 'http://g1.globo.com/dynamo/economia/rss2.xml')
newsfeeder('Educação', 'http://g1.globo.com/dynamo/educacao/rss2.xml')
newsfeeder('Loterias', 'http://g1.globo.com/dynamo/loterias/rss2.xml')
newsfeeder('Mundo', 'http://g1.globo.com/dynamo/mundo/rss2.xml')
newsfeeder('Música', 'http://g1.globo.com/dynamo/musica/rss2.xml')
newsfeeder('Natureza', 'http://g1.globo.com/dynamo/natureza/rss2.xml')
newsfeeder('Planeta Bizarro',
           'http://g1.globo.com/dynamo/planeta-bizarro/rss2.xml')
newsfeeder('Política', 'http://g1.globo.com/dynamo/politica/mensalao/rss2.xml')
newsfeeder('Pop & Arte', 'http://g1.globo.com/dynamo/pop-arte/rss2.xml')
newsfeeder('Tecnologia e Games',
           'http://g1.globo.com/dynamo/tecnologia/rss2.xml')
newsfeeder('Turismo e Viagem',
           'http://g1.globo.com/dynamo/turismo-e-viagem/rss2.xml')
