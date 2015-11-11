import mediacloud, json, datetime, ConfigParser


config = ConfigParser.ConfigParser()
config.read('config.cfg')

my_api_key = config.get('Media Cloud', 'my_api')
mc = mediacloud.api.MediaCloud(my_api_key)

# Has the conversation about bees increased between 2013 and 2014?
    
bees_2013 = mc.sentenceCount('bee OR bees', solr_filter=[mc.publish_date_query( datetime.date( 2013, 1, 1), datetime.date( 2014, 1, 1) ), 'media_sets_id:1' ])
bees_2014 = mc.sentenceCount('bee OR bees', solr_filter=[mc.publish_date_query( datetime.date( 2014, 1, 1), datetime.date( 2015, 1, 1) ), 'media_sets_id:1' ])

print "In 2013: %d " % bees_2013['count']
print "In 2014: %d " % bees_2014['count']


if (bees_2013['count'] > bees_2014['count']):
    print "Conversation about bees has decreased since 2013!"
else :
    print "Conversation about bees has increased since 2013!"