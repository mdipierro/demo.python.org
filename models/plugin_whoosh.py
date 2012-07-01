def whoosh(folder):
    from whoosh.index import create_in
    from whoosh.fields import ID,TEXT,Schema
    from whoosh.qparser import QueryParser
    from whoosh.query import And
    import os
    schema = Schema(title=TEXT(stored=True), 
                    content=TEXT,
                    id=ID(stored=True))
    indexdir = os.path.join(folder,'indexdir')
    if not os.path.exists(indexdir): os.mkdir(indexdir)    
    ix = create_in(indexdir, schema)
    def update(*items):
        writer = None
        for item in items:
            if len(item)==1 and 'id' in item:
                if writer:
                    writer.commit()
                    writer = None
                ix.delete_by_term('id',unicode(item['id']))
            else:
                if not writer: writer = ix.writer()
                for key in item:
                    item[key]=unicode(item[key])
                writer.update_document(**item)
        if writer: writer.commit()
    def search(**a):
        writer = ix.writer()
        with ix.searcher() as searcher:
            queries = [QueryParser(key, ix.schema).parse(unicode(value)) \
                           for key,value in a.items()]
            query = queries[0] if len(queries)==1 else And(*queries)
            results = searcher.search(query)
        return results
    return update, search

# whoosh_update, whoosh_search = whoosh(request.folder)
def test():
    whoosh_update(dict(id=1, title='test 1'),
                  dict(id=2, title='test 2'),
                  dict(id=3, title='test 3'))
    print whoosh_search(title='test')
    whoosh_update(dict(id=2))
    print whoosh_search(title='test')
              
