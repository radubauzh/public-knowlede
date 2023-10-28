import rdflib
from rdflib import Graph, graph
from rdflib.namespace import RDF, RDFS, XSD, Namespace
QSTN_INTENT = ["person", "location", "time", "rating", "recommendations", "description", "crowdsourcing"]

linkErrorDict = {
  # award and ogranization not there because we need those in KG
  "film organization":rdflib.term.URIRef("http://www.wikidata.org/entity/Q104649845"), 
  "station building":rdflib.term.URIRef("http://www.wikidata.org/entity/Q1339195"), 
  "fictional princess":rdflib.term.URIRef("http://www.wikidata.org/entity/Q61928601"), 
  "comics":rdflib.term.URIRef("http://www.wikidata.org/entity/Q1004"),
  "children's book":rdflib.term.URIRef("http://www.wikidata.org/entity/Q8275050"), 
  "literary pentalogy":rdflib.term.URIRef("http://www.wikidata.org/entity/Q17710986"), 
  "supervillain team":rdflib.term.URIRef("http://www.wikidata.org/entity/Q16101952"), 
  "disputed territory":rdflib.term.URIRef("http://www.wikidata.org/entity/Q15239622"),
  "geographic entity":rdflib.term.URIRef("http://www.wikidata.org/entity/Q27096213"),
  "fictional character":rdflib.term.URIRef("http://www.wikidata.org/entity/Q95074"),
  "written work":rdflib.term.URIRef("http://www.wikidata.org/entity/Q47461344"),
  "series of creative works":rdflib.term.URIRef("http://www.wikidata.org/entity/Q7725310"),
} 


PREDICATES = {
 'IMDb ID': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P345'),
 'actor': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P161'),
 'cast member': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P161'),
 'country': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P17'),
 'country of origin': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P495'),
 'director': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P57'),
 'filming location': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P915'), 
 'genre': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P136'),
 'instance of': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P31'),
 'located in the administrative territorial entity': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P131'),
 'location': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P276'),
 'main subject': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P921'),
 'node description': rdflib.term.URIRef('http://schema.org/description'),
 'node label': rdflib.term.URIRef('http://www.w3.org/2000/01/rdf-schema#label'),
 'nominated for': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P1411'),
 'place of birth': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P19'),
 'place of death': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P20'),
 'place of burial': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P119'),
 'place of publication': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P291'),
 'publication date': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P577'),
 'screenwriter': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P58'),
 'voice actor': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P725'),
 'box office': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P2142'),
 'distributed by': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P750'),
 'director of photography': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P344'),
 'occupation': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P106'),
 'main subject': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P921'),
 'production designer': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P2554'),
 'JMK film rating': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P3650'),
 'film crew member': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P3092'),
 'original language of film or TV show': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P364'),
 'armament ': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P520'),
 'art director': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P3174'),
 'allegiance': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P945'),
 'country of citizenship': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P27'),
 'executive producer': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P1431'),
 'production company': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P272'),
 'languages spoken, written or signed': rdflib.term.URIRef('http://www.wikidata.org/prop/direct/P1412'),
 }

CLASSIFIED_PREDICATES = {"person":["actor", "cast member", "director", "screenwriter"],
                          "location":["country", 'country of origin', 'filming location', 'place of birth', 'place of death',  'place of publication'],
                          "time": ['publication date'],
                          "description":[],
                          "recommendations":[],
                          "rating":[],
                          "crowdsourcing":['languages spoken, written or signed', 'production company', 'executive producer', 'place of burial', 'allegiance', 'art director', 'armament', 'original language of film or TV show', 'film crew member', 'JMK film rating', 'production designer', 'main subject', 'occupation', 'director of photography', 'distributed by', 'box office', 'publication date',"actor", "voice actor", "cast member", "director", "screenwriter","country", 'country of origin', 'filming location', 'place of birth', 'place of death',  'place of publication']
                          }

CLASSIFIED_PREDICATES = {"person":["actor", "cast member", "director", "screenwriter"],
                          "location":["country", 'country of origin', 'filming location', 'place of birth', 'place of death',  'place of publication'],
                          "time": ['publication date'],
                          "description":[],
                          "recommendations":[],
                          "rating":[],
                          "crowdsourcing":['languages spoken, written or signed', 'production company', 'executive producer', 'place of burial', 'allegiance', 'art director', 'armament', 'original language of film or TV show', 'film crew member', 'JMK film rating', 'production designer', 'main subject', 'occupation', 'director of photography', 'distributed by', 'box office', 'publication date',"actor", "voice actor", "cast member", "director", "screenwriter","country", 'country of origin', 'filming location', 'place of birth', 'place of death',  'place of publication']
                          }


SPARQL_TEMPLATE_ENTITY = '''
PREFIX ddis: <http://ddis.ch/atai/> 
PREFIX wd: <http://www.wikidata.org/entity/> 
PREFIX wdt: <http://www.wikidata.org/prop/direct/> 
PREFIX schema: <http://schema.org/> 

SELECT DISTINCT ?uri WHERE{{
    ?uri rdfs:label ?entity .
    FILTER (regex(?entity, "{entity}"@en, "i")) .
}}
LIMIT 9
'''

SPARQL_TEMPLATE = '''
PREFIX ddis: <http://ddis.ch/atai/> 
PREFIX wd: <http://www.wikidata.org/entity/> 
PREFIX wdt: <http://www.wikidata.org/prop/direct/> 
PREFIX schema: <http://schema.org/> 

SELECT ?ans ?ans_uri WHERE{{
    {entity_uri} <{predicate_uri}> ?ans_uri .
    OPTIONAL {{ ?ans_uri rdfs:label ?ans   }} .
    FILTER( !bound(?ans) || LANG(?ans) = "en" ) .
}}
LIMIT 9
'''

SPARQL_TEMPLATE_RATINGS = """
    PREFIX ddis: <http://ddis.ch/atai/> 
    PREFIX wd: <http://www.wikidata.org/entity/> 
    PREFIX wdt: <http://www.wikidata.org/prop/direct/> 
    PREFIX schema: <http://schema.org/> 
    
    SELECT ?rating  WHERE {{
        OPTIONAL {{ {entity_uri} ddis:rating ?rating }} 
    }}
"""

SPARQL_TEMPLATE_DESCRIPTION = """
  PREFIX ddis: <http://ddis.ch/atai/> 
  PREFIX wd: <http://www.wikidata.org/entity/> 
  PREFIX wdt: <http://www.wikidata.org/prop/direct/> 
  PREFIX schema: <http://schema.org/>
  
  SELECT ?description WHERE {{
    {entity_uri} schema:description ?description
  }}
"""
# ----------------------------------------------------
