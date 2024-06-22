from neo4j import GraphDatabase


class QueryDB:
    def __init__(self):
        self.driver = GraphDatabase.driver("bolt://localhost:7687")

    def close(self):
        self.driver.close()

    def query(self, query):
        result, summary, keys = self.driver.execute_query(query_=query)
        return result
