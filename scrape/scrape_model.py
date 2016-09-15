import database as db
import json
from flask import Response

def create(uid, name):
    responseObj = {}
    
    try:
        db.Scrape.add(uid=uid, name=name)
    except:
        responseObj['error'] = 'failed to create_scrape' + name
    else:
        responseObj['success'] = 'created scrape ' + name
        
    return responseObj


def read(uid, scrape_id):
    responseObj = {}
    status = 200
    mimetype = 'application/json'
    
    try:
        scrape = db.Scrape.get(db.Scrape.id==scrape_id)
    except:
        responseObj['error'] = 'Could not find scrape: ' + scrape_id
        status = 404
        #need to build out 404 vs 500s
    else:
        if scrape.uid_id == uid:
            #return the information since user owns the scrape
            responseObj['name'] = scrape.name
            responseObj['success'] = 'found scrape ' + scrape.name
        else:
            responseObj['error'] = 'you don\'t own this, you turd'
            status = 403
        
    return Response(json.dumps(responseObj),status=status,mimetype=mimetype)

