from db import Query


def search_keywords(keywords):
	res = search_db(keywords)
	if res:
		return {'code':200,'data':res}
	else:
		return {'code':404,'msg':'No result found'}
	

def search_db(keywords, limit = 200):
	sql = (" SELECT * FROM `hindu` WHERE match(`title`, `link`) against('%s' IN BOOLEAN MODE) ORDER BY `id` desc LIMIT %d;" %(keywords,limit))
	query = Query()
	res = query.search(sql)
	query.close()
	return res