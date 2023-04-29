from Database.Database import Database


def lambda_handler(event,context):
    db = Database()
    if(event['requestType']=="taxi-location-write"):
        taxi_location_data = event["payloadData"]
        id_result = db.insert_single_data("taxi_locations",taxi_location_data)
        if(id_result is not None):
            return taxi_location_data
        else:
            return None
        #pass
    if(event['requestType']=="taxi-location-read"):
        pass

    if(event['requestType']=="user-location-write"):
        user_location_data = event["payloadData"]
        id_result = db.insert_single_data("user_location",user_location_data)
        if(id_result is not None):
            return user_location_data
        else:
            return None
        #pass
    if(event['requestType']=="user-location-read"):
        pass
